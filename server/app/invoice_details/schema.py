from datetime import datetime

from pydantic import BaseModel, conint, constr
from app.inventory.schema import InventorySchema


class InvoiceDetails(BaseModel):
    product_id: int
    size_id: int
    invoice_id: int
    quantity: int
    discount: int
    price: int


class DisplayProduct(InvoiceDetails):
    inventory: InventorySchema

    class Config:
        from_attributes = True


class AddProduct(InvoiceDetails):
    quantity: conint(gt=0)
