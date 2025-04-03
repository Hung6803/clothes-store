from datetime import datetime

from pydantic import BaseModel, conint, constr

from app.employee.schema import EmployeeInvoice
from app.customer.schema import CustomerInvoice


class InvoiceBase(BaseModel):
    total_price: int
    payment_type: str
    address: str
    status: int


class InvoiceCreate(InvoiceBase):
    payment_type: constr(min_length=1)
    status: conint(gt=0, lt=10)
    address: constr(min_length=1)
    total_price: int
    employee_id: int
    customer_id: int


class InvoiceUpdate(BaseModel):
    id: int


class DisplayInvoice(InvoiceBase):
    id: int
    creation_date: datetime
    employee: EmployeeInvoice
    customer: CustomerInvoice

    class Config:
        from_attributes = True

