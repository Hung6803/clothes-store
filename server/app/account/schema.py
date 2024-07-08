from datetime import datetime

from pydantic import BaseModel, EmailStr


class Account(BaseModel):
    email: EmailStr
    password: str
    role: bool

class AccountDisplay(BaseModel):
    email: EmailStr
    createDate: datetime

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: EmailStr | None = None


class User:
    pass