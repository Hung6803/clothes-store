from typing import Optional, List

from fastapi import Query
from pydantic import BaseModel
from app.brand.schema import BrandDisplay
from app.category.schema import DisplayCategory
from app.image.schema import ProductImagePath


class Product(BaseModel):
    product_name: str
    product_description: str | None = None
    price: int
    discount: int
    category_id: int
    brand_id: int


class ProductEdit(Product):
    class Config:
        from_attributes = True


class DisplayProduct(BaseModel):
    id: int
    product_name: str
    product_image: Optional[ProductImagePath]
    price: int
    discount: int
    category: DisplayCategory
    brand: BrandDisplay

    class Config:
        from_attributes = True


class ProductName(BaseModel):
    id: int
    product_name: str


class DisplayImage(BaseModel):
    image: str


class DisplayProductFull(DisplayProduct):
    product_description: str | None = None
    product_image: List[ProductImagePath]


class DisplayTopProduct(BaseModel):
    id: int
    product_name: str
    price: int
    discount: int
    total_sold: int
    product_image: Optional[ProductImagePath]

    class Config:
        from_attributes = True


class ProductOption(BaseModel):
    page: int = Query(1, ge=0)
    limit: int = Query(12, gt=0)
    category_id: int = None
    brand_id: int = None
    size_id: int = None
    price_min: int = None
    price_max: int = None
    search: Optional[str] = None
    sort_by: Optional[str] = "price"
    sort_order: str = Query("asc", regex="^(asc|desc)$")


