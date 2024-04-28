import time
import requests
from enum import Enum
from urllib.parse import urlencode
from glide_sdk_python.logger import logger
from glide_sdk_python.utils import random_string, get_config, GlideConfig, format_phone_number
from glide_sdk_python.session import Session, SessionType
from typing import List, TypedDict, Optional
from base64 import b64encode

class BaseAuthConfig(TypedDict):
    scopes: List[str]
    login_hint: str

class AuthConfig(BaseAuthConfig):
    provider: SessionType

class AuthenticationResponse(TypedDict):
    session: Optional[Session]
    redirect_url: Optional[str]

class CibaAuthResponse(TypedDict):
    auth_req_id: str
    expires_in: int
    interval: int

class NumberVerificationResponse(TypedDict):
    devicePhoneNumberVerified: bool

class GetPhoneNumberResponse(TypedDict):
    devicePhoneNumber: str

class LastSimChangeResponse(TypedDict):
    lastSimChange: str

class SimSwapResponse(TypedDict):
    swapped: bool

class DeviceIDType(Enum):
    IPV4 = "ipv4Address",
    IPV6 = "ipv6Address",
    PHONE_NUMBER = "phoneNumber",
    NAI = "networkAccessIdentifier",

class LocationBody(TypedDict):
    latitude: float
    longitude: float
    radius: int
    device_id: str
    device_id_type: DeviceIDType
    max_age: int

class LocationResponse(TypedDict):
    verificationResult: str

class GlideClient:
    config: GlideConfig
    session: Optional[Session]

    def __init__(self):
        self.config = get_config()
        self.session = None

    # auth functions
    def __get_basic_auth_header(self) -> str:
        return f"Basic {b64encode(f'{self.config['client_id']}:{self.config['client_secret']}'.encode())}"

    def __get_ciba_auth_login_hint(self, auth_config: AuthConfig) -> CibaAuthResponse:
        logger.debug("Sending CIBA auth request")

        data = {
            "scope": auth_config.get('scopes', ["openid"]),
        }

        if auth_config.get('login_hint'):
            data['login_hint'] = auth_config['login_hint']

        try:
            response = requests.post(
                f"{self.config['internal_auth_base_url']}/oauth2/backchannel-authentication",
                headers={
                    "Authorization": self.__get_basic_auth_header(),
                    "Content-Type": "application/x-www-form-urlencoded"
                },
                data=data,
            )

            response.raise_for_status()
            res_data: CibaAuthResponse = response.json()
            logger.debug(f"Received CIBA auth response: {res_data}")
            return res_data
        except Exception as e:
            logger.error(f"Failed to get CIBA auth login hint: {e}")
            raise e

    def __fetch_ciba_token(self, auth_req_id: str) -> Session:
        logger.debug("Polling CIBA token")

        try:
            response = requests.post(
                f"{self.config['internal_auth_base_url']}/oauth2/token",
                headers={
                    "Authorization": self.__get_basic_auth_header(),
                    "Content-Type": "application/x-www-form-urlencoded"
                },
                data={
                    "grant_type": "urn:openid:params:grant-type:ciba",
                    "auth_req_id": auth_req_id
                }
            )

            response.raise_for_status()
            res_data = response.json()
            logger.debug(f"Received CIBA token response: {res_data}")
            return Session(
                access_token=res_data['access_token'],
                session_type=SessionType.Ciba
            )
        except Exception as e:
            logger.error(f"Failed to fetch CIBA token: {e}")
            raise e

    def __poll_ciba_token(self, auth_req_id: str, interval: int) -> Session:
        if interval < 1:
            raise ValueError("Interval must be greater than 1")

        logger.debug("Polling CIBA token")

        retries = 0
        MAX_RETRIES = 10

        while retries < MAX_RETRIES:
            try:
                session = self.__fetch_ciba_token(auth_req_id)
                if session.access_token:
                    return session
            except Exception as e:
                logger.error(f"Failed to fetch CIBA token: {e}")
                raise e
            finally:
                retries += 1
                time.sleep(interval)

        logger.error("Failed to fetch CIBA token")
        raise ValueError("Failed to fetch CIBA token")

    def __get_ciba_session(self, auth_config: BaseAuthConfig) -> Session:
        logger.debug("Getting CIBA session")

        try:
            auth_res = self.__get_ciba_auth_login_hint(auth_config)
            session = self.__poll_ciba_token(auth_res['auth_req_id'], auth_res['interval'])
            logger.debug("Received CIBA session")
            return session
        except Exception as e:
            logger.error(f"Failed to get CIBA session: {e}")
            raise e

    def __get_3legged_auth_redirect_url(self, auth_config: BaseAuthConfig) -> str:
        logger.debug("Getting 3-legged OAuth2 redirect URL")

        nonce = random_string(16)
        state = random_string(10)

        data = {
            "client_id": self.config['client_id'],
            "redirect_uri": self.config['redirect_uri'],
            "state": state,
            "response_type": "code",
            "scope": " ".join(auth_config.get('scopes', ["openid"])),
            "nonce": nonce,
            "max_age": "0",
            "purpose": "",
            "audience": self.config['client_id'],
        }

        if auth_config.get('login_hint'):
            data['login_hint'] = auth_config['login_hint']

        base_url = f"{self.config['internal_auth_base_url']}/oauth2/auth?"
        params = urlencode(data)

        logger.debug(f"Generated 3-legged OAuth2 redirect URL: {base_url}{params}")
        return f"{base_url}{params}"

    def exchange_code_for_session(self, code: str) -> Session:
        logger.debug("Exchanging code for session")

        try:
            response = requests.post(
                f"{self.config['internal_auth_base_url']}/oauth2/token",
                headers={
                    "Authorization": self.__get_basic_auth_header(),
                    "Content-Type": "application/x-www-form-urlencoded"
                },
                data={
                    "grant_type": "authorization_code",
                    "code": code,
                    "redirect_uri": self.config['redirect_uri']
                }
            )

            response.raise_for_status()
            res_data = response.json()
            logger.debug(f"Received session response: {res_data}")
            self.session = Session(
                access_token=res_data['access_token'],
                session_type=SessionType.ThreeLeggedOAuth2
            )

            return self.session
        except Exception as e:
            logger.error(f"Failed to exchange code for session: {e}")
            raise e

    def authenticate(self, auth_config: AuthConfig) -> AuthenticationResponse:
        # only run auth flow if session type is higher
        if (self.session and self.session.session_type.value >= auth_config['provider'].value):
            logger.debug("Session type is higher than requested provider")
            return AuthenticationResponse(session=self.session, redirect_url=None)

        if not auth_config.get('scopes'):
            auth_config['scopes'] = ["openid"]

        try:
            if auth_config['provider'] == SessionType.Ciba:
                self.session = self.__get_ciba_session(auth_config)
                return AuthenticationResponse(session=self.session, redirect_url=None)
            elif auth_config['provider'] == SessionType.ThreeLeggedOAuth2:
                redirect_url = self.__get_3legged_auth_redirect_url(auth_config)
                return AuthenticationResponse(session=None, redirect_url=redirect_url)
            else:
                raise ValueError("Invalid provider")
        except Exception as e:
            logger.error(f"Failed to authenticate: {e}")
            raise e

    # number verification
    def __base_verify_number(self, phone_number: Optional[str] = None, hashed_phone_number: Optional[str] = None) -> bool:
        try:
            auth_res = self.authenticate(
                AuthConfig(
                    provider=SessionType.ThreeLeggedOAuth2,
                    scopes=["openid", "dpv:FraudDetectionAndPrevention:number-verification"],
                    login_hint=f"tel:{format_phone_number(phone_number)}" if phone_number else None
                )
            )

            if auth_res['redirect_url']:
                raise PermissionError("Number verification requires ThreeLeggedOAuth2 session - please call authenticate() flow first")

            response = requests.post(
                f"{self.config['internal_api_base_url']}/number-verification/verify",
                headers={
                    "Authorization": f"Bearer {auth_res['session'].access_token}",
                    "Content-Type": "application/json"
                },
                json={
                    "phoneNumber": format_phone_number(phone_number) if phone_number else None,
                    "hashedPhoneNumber": hashed_phone_number
                }
            )

            response.raise_for_status()
            res_data: NumberVerificationResponse = response.json()
            return res_data['devicePhoneNumberVerified']
        except Exception as e:
            logger.error(f"Failed to verify number: {e}")
            raise e

    def verify_by_number(self, phone_number: str) -> bool:
        logger.debug(f"Verifying number by phone number: {phone_number}")
        return self.__base_verify_number(phone_number=phone_number)

    def verify_by_hashed_number(self, hashed_phone_number: str) -> bool:
        logger.debug(f"Verifying number by hashed phone number: {hashed_phone_number}")
        return self.__base_verify_number(hashed_phone_number=hashed_phone_number)

    def get_phone_number(self) -> str:
        logger.debug("Getting phone number")

        try:
            auth_res = self.authenticate(
                AuthConfig(
                    provider=SessionType.ThreeLeggedOAuth2,
                    scopes=["openid", "dpv:FraudDetectionAndPrevention:number-verification"],
                    login_hint=None
                )
            )

            if auth_res['redirect_url']:
                raise PermissionError("Get phone number requires ThreeLeggedOAuth2 session - please call authenticate() flow first")

            response = requests.get(
                f"{self.config['internal_api_base_url']}/number-verification/device-phone-number",
                headers={
                    "Authorization": f"Bearer {auth_res['session'].access_token}"
                }
            )

            response.raise_for_status()
            res_data: GetPhoneNumberResponse = response.json()
            return res_data['devicePhoneNumber']
        except Exception as e:
            logger.error(f"Failed to get phone number: {e}")
            raise e

    # sim swap
    def retrieve_date(self, phone_number: str) -> str:
        logger.debug(f"Retrieving last SIM change date for phone number: {phone_number}")

        try:
            auth_res = self.authenticate(
                AuthConfig(
                    provider=SessionType.Ciba,
                    scopes=["openid", "dpv:FraudDetectionAndPrevention:sim-swap"],
                    login_hint=f"tel:{format_phone_number(phone_number)}"
                )
            )

            response = requests.post(
                f"{self.config['internal_api_base_url']}/sim-swap/retrieve-date",
                headers={
                    "Authorization": f"Bearer {auth_res['session'].access_token}",
                    "Content-Type": "application/json"
                },
                json={
                    "phoneNumber": format_phone_number(phone_number)
                }
            )

            response.raise_for_status()
            res_data: LastSimChangeResponse = response.json()
            return res_data['lastSimChange']
        except Exception as e:
            logger.error(f"Failed to retrieve last SIM change date: {e}")
            raise e

    def check_sim_swap(self, phone_number: str, max_age: int) -> bool:
        logger.debug(f"Checking SIM swap for phone number: {phone_number}")

        try:
            auth_res = self.authenticate(
                AuthConfig(
                    provider=SessionType.Ciba,
                    scopes=["openid", "dpv:FraudDetectionAndPrevention:sim-swap"],
                    login_hint=f"tel:{format_phone_number(phone_number)}"
                )
            )

            response = requests.post(
                f"{self.config['internal_api_base_url']}/sim-swap/check",
                headers={
                    "Authorization": f"Bearer {auth_res['session'].access_token}",
                    "Content-Type": "application/json"
                },
                json={
                    "phoneNumber": format_phone_number(phone_number),
                    "maxAge": max_age
                }
            )

            response.raise_for_status()
            res_data: SimSwapResponse = response.json()
            return res_data['swapped']
        except Exception as e:
            logger.error(f"Failed to check SIM swap: {e}")
            raise e

    # verify location
    def verify_location(self, location_body: LocationBody) -> str:
        logger.debug(f"Verifying location: {location_body}")

        if not location_body.get('latitude') or not location_body.get('longitude') or not location_body.get('device_id'):
            raise ValueError("Latitude, longitude, and device_id are required")

        try:
            auth_res = self.authenticate(
                AuthConfig(
                    provider=SessionType.Ciba,
                    scopes=["openid", "dpv:FraudPreventionAndDetection:device-location"],
                    login_hint=None
                )
            )

            response = requests.post(
                f"{self.config['internal_api_base_url']}/device-location/verify",
                headers={
                    "Authorization": f"Bearer {auth_res['session'].access_token}",
                    "Content-Type": "application/json"
                },
                json={
                    "device": {
                        location_body.get('device_id_type', DeviceIDType.PHONE_NUMBER): location_body['device_id'],
                    },
                    "area": {
                        "areaType": "CIRCLE",
                        "center": {
                            "latitude": location_body['latitude'],
                            "longitude": location_body['longitude']
                        },
                        "radius": location_body['radius']
                    },
                    "maxAge": location_body['max_age']
                }
            )

            response.raise_for_status()
            res_data: LocationResponse = response.json()

            if res_data["verificationResult"] == "FALSE":
                return False

            return True
        except Exception as e:
            logger.error(f"Failed to verify location: {e}")
            raise e
