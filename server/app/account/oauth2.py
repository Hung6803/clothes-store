from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from app.account import token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="account/login")


def get_current_user(data: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    return token.verify_token(data, credentials_exception)


def admin_required(current_user=Depends(get_current_user)):
    if not current_user.role:
        raise HTTPException(status_code=403, detail="Not authorized as admin")
    return current_user
