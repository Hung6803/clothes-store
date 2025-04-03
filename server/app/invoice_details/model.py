from sqlalchemy import Column, Integer, ForeignKey, PrimaryKeyConstraint, ForeignKeyConstraint
from sqlalchemy.orm import relationship
from app.database import Base
from app.inventory.model import Inventory


class InvoiceDetails(Base):
    __tablename__ = 'invoice_details'

    product_id = Column(Integer, nullable=False)
    size_id = Column(Integer, nullable=False)
    invoice_id = Column(Integer, ForeignKey('invoice.id'), nullable=False)
    quantity = Column(Integer)
    discount = Column(Integer, default=0)
    price = Column(Integer)

    __table_args__ = (
        PrimaryKeyConstraint('product_id', 'size_id', 'invoice_id'),
        ForeignKeyConstraint(
            ['product_id', 'size_id'],
            ['inventory.product_id', 'inventory.size_id']
        ),
    )

    inventory = relationship("Inventory", back_populates="invoice_details")
    invoice = relationship("Invoice", back_populates="invoice_details")

    def __init__(self, product_id, size_id, invoice_id, quantity, discount, price, *args, **kwargs):
        self.product_id = product_id
        self.size_id = size_id
        self.invoice_id = invoice_id
        self.price = price
        self.discount = discount
        self.quantity = quantity

    def __str__(self):
        return f'{self.product_id} - {self.size_id} - {self.invoice_id}: {self.quantity}, {self.price}, {self.discount}'