from pydantic import BaseModel
from app.brand.schema import Brand
from app.category.schema import Category


class Product(BaseModel):
    product_name: str
    product_description: str | None = None
    price: int
    category_id: int
    brand_id: int


class DisplayProduct(BaseModel):
    id: int
    product_name: str
    product_description: str | None = None
    price: int
    category_name: Category
    brand_name: Brand

    class Config:
        from_attributes = True