from typing import List

from pydantic import BaseModel
from app.product.schema import ProductName
from app.size.schema import DisplaySize


class Inventory(BaseModel):
    product_id: int
    size_id: int
    import_price: int
    quantity: int


class DisplayInventory(BaseModel):
    product: ProductName
    size: DisplaySize
    import_price: int
    quantity: int

    class Config:
        from_attributes = True


class DisplayProductSize(BaseModel):
    product: ProductName
    sizes: List[DisplaySize]
    quantity: List[int]

    class Config:
        from_attributes = True


class InventoryUpdate(BaseModel):
    import_price: int
    quantity: int


class InventorySchema(BaseModel):
    product: ProductName
    size: DisplaySize
