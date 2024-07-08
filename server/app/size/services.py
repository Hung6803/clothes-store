from typing import List, Optional
from app.size import model, schema


def get_all_size(database) -> List[model.Size]:
    size = database.query(model.Size).all()
    return size


def edit_size(size_id, request, database):
    database.query(model.Size).filter(model.Size.id == size_id).update(request)
    database.commit()


async def create_size(request: schema.Size, database) -> model.Size:
    new_size = model.Size(size_name=request.size_name)
    database.add(new_size)
    database.commit()
    database.refresh(new_size)
    return new_size


def get_size_by_id(size_id, database) -> Optional[model.Size]:
    size_info = database.query(model.Size).get(int(size_id))
    return size_info


def delete_size(size_id, database):
    database.query(model.Size).filter(model.Size.id == size_id).delete()
    database.commit()