from datetime import datetime
from sqlalchemy import Column, String, DateTime, Boolean, ForeignKey, Integer
from sqlalchemy.orm import relationship
from app.database import Base

class Customer(Base):
    __tablename__ = 'customer'

    id = Column(Integer, primary_key=True, autoincrement=True)
    last_name = Column(String(30))
    first_name = Column(String(30))
    phone_number = Column(String(10))
    address = Column(String(100))
    date_of_birth = Column(DateTime)
    email = Column(String(50), ForeignKey('account.email'))

    account = relationship("Account", back_populates="customer")
    invoices = relationship("Invoice", back_populates="customer")

    def __init__(self, last_name, first_name, phone_number, address, date_of_birth, email, *args, **kwargs):
        self.last_name = last_name
        self.first_name = first_name
        self.phone_number = phone_number
        self.address = address
        self.date_of_birth = datetime.date(date_of_birth)
        self.email = email

    def __str__(self):
        return f'{self.last_name} {self.first_name}: {self.email}'