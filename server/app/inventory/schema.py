from pydantic import BaseModel
from app.product.schema import ProductName
from app.size.schema import DisplaySize


class Inventory(BaseModel):
    product_id: int
    size_id: int
    import_price: int
    quantity: int


class DisplayInventory(BaseModel):
    id: int
    product: ProductName
    size: DisplaySize
    import_price: int
    quantity: int

    class Config:
        from_attributes = True