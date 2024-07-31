from datetime import date, datetime

from pydantic import BaseModel, EmailStr


class Account(BaseModel):
    email: EmailStr
    password: str
    role: bool


class AccountUpdate(BaseModel):
    email: EmailStr
    password: str


class AccountDisplay(BaseModel):
    id: int
    email: EmailStr
    createDate: datetime

    class Config:
        from_attributes = True


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: EmailStr | None = None
