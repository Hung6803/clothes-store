from datetime import datetime
from sqlalchemy import Column, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base
from app.account import hashing

class Account(Base):
    __tablename__ = 'account'

    email = Column(String(50), primary_key=True)
    password = Column(String(20))
    role = Column(Boolean, default=False)
    createDate = Column(DateTime, default=datetime.utcnow)

    customer = relationship("Customer", back_populates="account")
    employee = relationship("Employee", back_populates="account")

    def __init__(self, email, password, role, *args, **kwargs):
        self.email = email
        self.password = hashing.get_password_hash(password)
        self.role = role

    def check_password(self, password):
        return hashing.verify_password(self.password, password)

    def __str__(self):
        return f'{self.email} {self.password}'