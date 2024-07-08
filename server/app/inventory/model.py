from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base
from app.size.model import Size

class Inventory(Base):
    __tablename__ = 'inventory'

    product_id = Column(Integer, ForeignKey('product.id'), primary_key=True)
    size_id = Column(Integer, ForeignKey('size.id'), primary_key=True)
    import_price = Column(Integer, primary_key=True)
    quantity = Column(Integer)

    product = relationship("Product", back_populates="inventory")
    size = relationship("Size", back_populates="inventory")

    def __init__(self, product_id, size_id, import_price, quantity, *args, **kwargs):
        self.product_id = product_id
        self.size_id = size_id
        self.import_price = import_price
        self.quantity = quantity

    def __str__(self):
        return f'{self.product_id} - {self.size_id}: {self.quantity}, {self.import_price}'