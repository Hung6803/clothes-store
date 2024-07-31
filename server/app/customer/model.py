from datetime import datetime
from sqlalchemy import Column, String, DateTime, Boolean, ForeignKey, Integer
from sqlalchemy.orm import relationship
from app.database import Base
from app.invoice.model import Invoice


class Customer(Base):
    __tablename__ = 'customer'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(60))
    phone_number = Column(String(10))
    address = Column(String(100))
    date_of_birth = Column(DateTime)
    account_id = Column(Integer, ForeignKey('account.id'))

    account = relationship("Account", back_populates="customer")
    invoices = relationship("Invoice", back_populates="customer")

    def __init__(self, name, phone_number, address, date_of_birth, account_id, *args, **kwargs):
        self.name = name
        self.phone_number = phone_number
        self.address = address
        self.date_of_birth = datetime.date(date_of_birth)
        self.account_id = account_id

    def __str__(self):
        return f'{self.name}'
