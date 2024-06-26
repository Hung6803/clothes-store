from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from app.database import Base


class Size(Base):
    __tablename__ = 'size'

    id = Column(Integer, primary_key=True, autoincrement=True)
    size_name = Column(String(5))

    inventory = relationship("Inventory", back_populates="size")

    def __init__(self, size_name, *args, **kwargs):
        self.size_name = size_name

    def __str__(self):
        return f'{self.size_name}'