from datetime import datetime

from pydantic import BaseModel, constr, EmailStr

from app.account.schema import AccountDisplay


class CustomerBase(BaseModel):
    name: str
    phone_number: str
    address: str | None = None
    date_of_birth: datetime

    def __str__(self):
        return f'{self.name}'


class CustomerCreate(CustomerBase):
    name: constr(min_length=1)
    phone_number: constr(min_length=10, max_length=10)
    address: str | None = None
    date_of_birth: datetime
    email: EmailStr
    password: str
    role: bool = False


class CustomerUpdate(CustomerBase):
    name: constr(min_length=1)
    phone_number: constr(min_length=10, max_length=10)
    address: str | None = None
    date_of_birth: datetime


class DisplayCustomer(CustomerBase):
    id: int
    account: AccountDisplay

    class Config:
        from_attributes = True

