import jwt
from datetime import datetime, timedelta, timezone
from app import config
from app.account import schema
from jwt.exceptions import InvalidTokenError


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=config.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, config.SECRET_KEY, algorithm=config.ALGORITHM)
    return encoded_jwt


def verify_token(token, credentials_exception):
    try:
        payload = jwt.decode(token, config.SECRET_KEY, algorithms=[config.ALGORITHM])
        email: str = payload.get("sub")
        role: bool = payload.get("role")
        if email is None:
            raise credentials_exception
        token_data = schema.TokenData(email=email, role=role)
        return token_data
    except InvalidTokenError:
        raise credentials_exception
