from datetime import datetime
from sqlalchemy import Column, String, DateTime, Boolean, Integer
from sqlalchemy.orm import relationship
from app.database import Base
from app.account import hashing
from app.customer.model import Customer
from app.employee.model import Employee

class Account(Base):
    __tablename__ = 'account'

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(50), unique=True, nullable=False)
    password = Column(String(100))
    role = Column(Boolean, default=False)
    createDate = Column(DateTime, default=datetime.utcnow)

    customer = relationship('Customer', back_populates="account")
    employee = relationship("Employee", back_populates="account")

    def __init__(self, email, password, role, *args, **kwargs):
        self.email = email
        self.password = hashing.get_password_hash(password)
        self.role = role

    def check_password(self, password):
        return hashing.verify_password(self.password, password)

    def __str__(self):
        return f'{self.email} {self.password}'