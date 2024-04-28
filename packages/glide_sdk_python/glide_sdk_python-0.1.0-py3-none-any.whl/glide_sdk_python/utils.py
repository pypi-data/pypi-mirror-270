import os
import string
import random
from typing import TypedDict

class GlideConfig(TypedDict):
    client_id: str
    client_secret: str
    redirect_uri: str
    internal_auth_base_url: str
    internal_api_base_url: str

def get_config() -> GlideConfig:
    client_id = os.environ.get("GLIDE_CLIENT_ID")
    if not client_id:
        raise ValueError("GLIDE_CLIENT_ID is not set")
    
    client_secret = os.environ.get("GLIDE_CLIENT_SECRET")
    if not client_secret:
        raise ValueError("GLIDE_CLIENT_SECRET is not set")
    
    redirect_uri = os.environ.get("GLIDE_REDIRECT_URI")
    if not redirect_uri:
        raise ValueError("GLIDE_REDIRECT_URI is not set")
    
    internal_auth_base_url = os.environ.get("GLIDE_INTERNAL_AUTH_BASE_URL", "https://oidc.gateway-x.io")
    internal_api_base_url = os.environ.get("GLIDE_INTERNAL_API_BASE_URL", "https://api.gateway-x.io")

    return GlideConfig(
        client_id=client_id,
        client_secret=client_secret,
        redirect_uri=redirect_uri,
        internal_auth_base_url=internal_auth_base_url,
        internal_api_base_url=internal_api_base_url
    )

def random_string(length: int) -> str:
    return "".join(random.choices(string.ascii_letters + string.digits, k=length))

def format_phone_number(phone_number: str) -> str:
    phone_number = phone_number.replace(" ", "")
    if not phone_number.startswith("+"):
        phone_number = "+" + phone_number
    return phone_number