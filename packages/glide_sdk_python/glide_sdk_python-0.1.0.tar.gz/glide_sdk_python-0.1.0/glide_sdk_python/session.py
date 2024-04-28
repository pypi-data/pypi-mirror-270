from enum import Enum

class SessionType(Enum):
    Ciba = 0
    ThreeLeggedOAuth2 = 1

class Session:
    access_token: str
    session_type: SessionType

    def __init__(self, access_token: str, session_type: SessionType) -> None:
        self.access_token = access_token
        self.session_type = session_type
    
    def get_scopes(self) -> list[str]:
        if not self.access_token:
            return []
        
        # TODO: Implement this method
        return []

