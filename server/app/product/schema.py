from pydantic import BaseModel
from app.brand.schema import BrandDisplay
from app.category.schema import DisplayCategory


class Product(BaseModel):
    product_name: str
    product_description: str | None = None
    price: int
    category_id: int
    brand_id: int


class ProductEdit(Product):
    class Config:
        from_attributes = True


class DisplayProduct(BaseModel):
    id: int
    product_name: str
    product_description: str | None = None
    price: int
    category: DisplayCategory
    brand: BrandDisplay

    class Config:
        from_attributes = True


class ProductName(BaseModel):
    id: int
    product_name: str

# class DisplayProduct(BaseModel):
#     id: int
#     product_name: str
#     price: int
#     product_quantity: int
#
#     class Config:
#         from_attributes = True
