from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.orm import relationship
from app.database import Base


class ProductImage(Base):
    __tablename__ = 'product_image'

    id = Column(Integer, primary_key=True, autoincrement=True)
    image_path = Column(String(255))
    product_id = Column(Integer, ForeignKey('product.id'))

    product = relationship('Product', back_populates='images')

    def __init__(self, image_path, product_id, *args, **kwargs):
        self.image_path = image_path
        self.product_id = product_id

    def __str__(self):
        return f'{self.image_path}'
