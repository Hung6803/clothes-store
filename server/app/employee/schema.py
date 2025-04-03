from datetime import datetime

from pydantic import BaseModel, constr, EmailStr, conint

from app.account.schema import AccountDisplay


class EmployeeBase(BaseModel):
    name: str
    phone_number: str
    address: str | None = None
    date_of_birth: datetime
    salary: int
    start_date: datetime


class EmployeeCreate(EmployeeBase):
    name: constr(min_length=1)
    phone_number: constr(min_length=10, max_length=10)
    address: str | None = None
    date_of_birth: datetime
    salary: conint(gt=1000)
    start_date: datetime
    email: EmailStr
    password: str
    role: bool = True


class EmployeeUpdate(EmployeeBase):
    name: constr(min_length=1)
    phone_number: constr(min_length=10, max_length=10)
    address: str | None = None
    date_of_birth: datetime
    salary: conint(gt=1000)
    start_date: datetime


class DisplayEmployee(EmployeeBase):
    id: int
    account: AccountDisplay

    class Config:
        from_attributes = True


class EmployeeInvoice(BaseModel):
    id: int
    name: str
