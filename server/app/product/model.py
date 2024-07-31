from sqlalchemy import Column, String, ForeignKey, Integer, Text
from sqlalchemy.orm import relationship
from app.database import Base
from app.category.model import Category
from app.inventory.model import Inventory
from app.brand.model import Brand

class Product(Base):
    __tablename__ = 'product'

    id = Column(Integer, primary_key=True, autoincrement=True)
    product_name = Column(String(50))
    product_description = Column(Text)
    price = Column(Integer)
    category_id = Column(Integer, ForeignKey('category.id'))
    brand_id = Column(Integer, ForeignKey('brand.id'))

    category = relationship('Category', back_populates='products')
    brand = relationship('Brand', back_populates='products')
    inventory = relationship('Inventory', back_populates='product')

    def __init__(self, product_name, product_description, price, category_id, brand_id, *args, **kwargs):
        self.product_name = product_name
        self.product_description = product_description
        self.price = price
        self.category_id = category_id
        self.brand_id = brand_id

    def __str__(self):
        return f'{self.product_name}'