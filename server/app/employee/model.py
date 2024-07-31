from datetime import datetime
from sqlalchemy import Column, String, DateTime, ForeignKey, Integer
from sqlalchemy.orm import relationship
from app.database import Base


class Employee(Base):
    __tablename__ = 'employee'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30))
    phone_number = Column(String(10))
    address = Column(String(100))
    date_of_birth = Column(DateTime)
    salary = Column(Integer)
    start_date = Column(DateTime, default=datetime.utcnow)
    account_id = Column(Integer, ForeignKey('account.id'))

    account = relationship("Account", back_populates="employee")
    invoices = relationship("Invoice", back_populates="employee")

    def __init__(self, name, phone_number, address, date_of_birth, salary, start_date, account_id, *args, **kwargs):
        self.name = name
        self.phone_number = phone_number
        self.address = address
        self.date_of_birth = datetime.date(date_of_birth)
        self.salary = salary
        self.start_date = datetime.date(start_date)
        self.account_id = account_id

    def __str__(self):
        return f'{self.name}'