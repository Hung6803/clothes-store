from typing import List, Optional
from app.category import model, schema


def get_all_category(database) -> List[model.Category]:
    categories = database.query(model.Category).all()
    return categories


def edit_category(category_id, request, database):
    database.query(model.Category).filter(model.Category.id == category_id).update(request)
    database.commit()


async def create_category(request: schema.Category, database) -> model.Category:
    new_category = model.Category(category_name=request.category_name)
    database.add(new_category)
    database.commit()
    database.refresh(new_category)
    return new_category


def get_category_by_id(category_id, database) -> Optional[model.Category]:
    category_info = database.query(model.Category).get(int(category_id))
    return category_info


def delete_category(category_id, database):
    database.query(model.Category).filter(model.Category.id == category_id).delete()
    database.commit()