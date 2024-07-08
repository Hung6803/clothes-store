from pydantic import BaseModel


class Size(BaseModel):
    size_name: str


class DisplaySize(BaseModel):
    id: int
    size_name: str

    class Config:
        from_attributes = True
