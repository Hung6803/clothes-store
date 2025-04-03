from datetime import datetime

from sqlalchemy import Column, String, ForeignKey, Integer, Text, DateTime
from sqlalchemy.orm import relationship
from app.database import Base
from app.employee.model import Employee
from app.invoice_details.model import InvoiceDetails

class Invoice(Base):
    __tablename__ = 'invoice'

    id = Column(Integer, primary_key=True, autoincrement=True)
    total_price = Column(Integer)
    payment_type = Column(String(50))
    address = Column(String(100))
    creation_date = Column(DateTime, default=datetime.utcnow)
    status = Column(Integer)
    employee_id = Column(Integer, ForeignKey('employee.id'))
    customer_id = Column(Integer, ForeignKey('customer.id'))

    employee = relationship('Employee', back_populates='invoices')
    customer = relationship('Customer', back_populates='invoices')
    invoice_details = relationship('InvoiceDetails', back_populates='invoice')

    def __init__(self, total_price, payment_type, address, status, employee_id, customer_id, *args, **kwargs):
        self.total_price = total_price
        self.payment_type = payment_type
        self.address = address
        self.status = status
        self.employee_id = employee_id
        self.customer_id = customer_id

    def __str__(self):
        return f'{self.total_price} {self.payment_type} {self.status} {self.customer_id}'