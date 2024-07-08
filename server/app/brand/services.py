from typing import List, Optional
from app.brand import model, schema


def get_all_brand(database) -> List[model.Brand]:
    brands = database.query(model.Brand).all()
    return brands


def edit_brand(brand_id, request, database):
    database.query(model.Brand).filter(model.Brand.id == brand_id).update(request)
    database.commit()


async def create_brand(request: schema.Brand, database) -> model.Brand:
    new_brand = model.Brand(brand_name=request.brand_name)
    database.add(new_brand)
    database.commit()
    database.refresh(new_brand)
    return new_brand


def get_brand_by_id(brand_id, database) -> Optional[model.Brand]:
    brand_info = database.query(model.Brand).get(int(brand_id))
    return brand_info


def delete_brand(brand_id, database):
    database.query(model.Brand).filter(model.Brand.id == brand_id).delete()
    database.commit()


def get_limit_brand(limit, database):
    brands = database.query(model.Brand).limit(limit).all()
    return brands