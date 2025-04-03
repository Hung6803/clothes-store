from typing import List

from fastapi import UploadFile, File
from pydantic import BaseModel


class ProductImage(BaseModel):
    image_path: str
    product_id: int


class DisplayImage(BaseModel):
    id: int
    image_path: str
    product_id: int

    class Config:
        from_attributes = True


class ProductImagePath(BaseModel):
    image_path: str

    class Config:
        from_attributes = True

