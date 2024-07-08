from datetime import datetime
from pydantic import BaseModel, constr, EmailStr


class CustomerBase(BaseModel):
    first_name: str
    last_name: str
    phone_number: str
    address: str | None = None
    date_of_birth: datetime

    def __str__(self):
        return f'{self.last_name} {self.first_name}: {self.email}'

class CustomerCreate(CustomerBase):
    first_name: constr(min_length=1)
    last_name: constr(min_length=1)
    phone_number: constr(min_length=10, max_length=10)
    address: str | None = None
    date_of_birth: datetime
    email: EmailStr

class Customer(CustomerBase):

    class Config:
        orm_mode = True

class DisplayCustomer(BaseModel):
    id : int
    first_name : str
    last_name : str
    phone_number : str
    email : EmailStr

    class Config:
        from_attributes = True