from pydantic import BaseModel


class Category(BaseModel):
    category_name: str


class DisplayCategory(BaseModel):
    id: int
    category_name: str

    class Config:
        from_attributes = True
