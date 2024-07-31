from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base
from app.inventory.model import Inventory


class InvoiceDetails(Base):
    __tablename__ = 'invoice_details'

    id = Column(Integer, primary_key=True, autoincrement=True)
    inventory_id = Column(Integer, ForeignKey('inventory.id'))
    invoice_id = Column(Integer, ForeignKey('invoice.id'))
    quantity = Column(Integer)
    discount = Column(Integer, default=0)
    price = Column(Integer)

    inventory = relationship("Inventory", back_populates="invoice_details")
    invoice = relationship("Invoice", back_populates="invoice_details")

    def __init__(self, product_id, size_id, import_price, quantity, *args, **kwargs):
        self.product_id = product_id
        self.size_id = size_id
        self.import_price = import_price
        self.quantity = quantity

    def __str__(self):
        return f'{self.product_id} - {self.size_id}: {self.quantity}, {self.import_price}'