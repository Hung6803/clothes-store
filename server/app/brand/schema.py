from pydantic import BaseModel


class Brand(BaseModel):
    brand_name: str


class BrandDisplay(BaseModel):
    id: int
    brand_name: str

    class Config:
        from_attributes = True
