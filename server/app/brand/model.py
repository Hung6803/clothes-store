from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from app.database import Base


class Brand(Base):
    __tablename__ = 'brand'

    id = Column(Integer, primary_key=True, autoincrement=True)
    brand_name = Column(String(30))

    products = relationship("Product", back_populates="brand")

    def __init__(self, brand_name, *args, **kwargs):
        self.brand_name = brand_name

    def __str__(self):
        return f'{self.brand_name}'