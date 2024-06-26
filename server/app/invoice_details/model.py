from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base


class InvoiceDetails(Base):
    __tablename__ = 'invoice_details'

    product_id = Column(Integer, ForeignKey('product.id'), primary_key=True)
    invoice_id = Column(Integer, ForeignKey('invoice.id'), primary_key=True)
    quantity = Column(Integer)
    discount = Column(Integer, default=0)
    price = Column(Integer)

    product = relationship("Product", back_populates="invoice_details")
    invoice = relationship("Invoice", back_populates="invoice_details")

    def __init__(self, product_id, size_id, import_price, quantity, *args, **kwargs):
        self.product_id = product_id
        self.size_id = size_id
        self.import_price = import_price
        self.quantity = quantity

    def __str__(self):
        return f'{self.product_id} - {self.size_id}: {self.quantity}, {self.import_price}'