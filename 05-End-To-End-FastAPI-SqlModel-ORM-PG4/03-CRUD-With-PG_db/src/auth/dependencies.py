from fastapi.security import HTTPBearer
from fastapi.security.http import HTTPAuthorizationCredentials
from fastapi import Request, status
from .utils import decode_token
from fastapi.exceptions import HTTPException

class TokenBearer(HTTPBearer):
    
    def __init__(self, auto_error= True):
        super().__init__(auto_error=auto_error)

    
    async def __call__(self, request: Request) -> HTTPAuthorizationCredentials | None:
        creds =  await super().__call__(request)

        # print("creds-schema--->", creds.schema,"<---creds-schema end")

        # print("--->",creds.credentials,"<----")
        token = creds.credentials

        token_data = decode_token(token)

        if not self.token_valid:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Invalid or Expired token."
            )
        
        self.verify_token_data(token_data)
        
        # print(token_data)
        return token_data
    
    def token_valid(self, token: str) -> bool:

        token_data = decode_token(token)

        return True if token_data is not None else False
    
    def verify_token_data(self, token_data) -> None:
        raise NotImplementedError("Please Override this method in the Child Class.")
    

class AccessTokenBearer(TokenBearer):

    def verify_token_data(self, token_data: dict) -> None:
        if token_data and  token_data["refresh"]:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Please provide the valid access token."
            )
        

class RefreshTokenBearer(TokenBearer):

    def verify_token_data(self, token_data: dict) -> None:
        if token_data and not token_data["refresh"]:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Please provide the refresh token."
            )