from passlib.context import CryptContext
from datetime import timedelta, datetime
from src.config import Settings
import jwt
import uuid
import logging

ACCESS_TOKEN_EXPIRY = 3600

password_context = CryptContext(
    schemes=["bcrypt"]
)

def generate_password_hash(password: str) -> str:
    hash = password_context.hash(password)
    print(hash)

    return hash

setting = Settings()
def verify_password(password: str, hash: str) -> bool:
    return password_context.verify(password, hash)


def create_access_token(user_data: dict, expiry: timedelta = None, refresh: bool=False) -> bool:
    
    payload = {}

    payload["user"] = user_data
    payload["exp"] = datetime.now() + (expiry if expiry is not None else timedelta(seconds=ACCESS_TOKEN_EXPIRY))
    payload["jti"] = str(uuid.uuid4())
    payload["refresh"] = refresh

    token = jwt.encode(
        payload=payload,
        key=setting.JWT_SECRET,
        algorithm=setting.JWT_ALGORITHM
    )

    return token


def decode_token(token: str) -> dict:
    try:
        token_data = jwt.decode(
        jwt=token,
        key=setting.JWT_SECRET,
        algorithms=[setting.JWT_ALGORITHM]
        )
        
        return token_data
    
    except jwt.PyJWTError as e:
        logging.exception(e)
        return None


if __name__ == "__main__":
    generate_password_hash("alamin")