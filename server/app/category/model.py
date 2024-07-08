from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from app.database import Base



class Category(Base):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True, autoincrement=True)
    category_name = Column(String(30))

    products = relationship("Product", back_populates="category")

    def __init__(self, category_name, *args, **kwargs):
        self.category_name = category_name

    def __str__(self):
        return f'{self.category_name}'