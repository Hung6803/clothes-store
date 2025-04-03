import os
from typing import List, Optional

from pathlib import Path
from starlette.responses import FileResponse

from app import config
from app.image import model, schema


def get_image(name: str):
    file_path = "image/" + name
    return FileResponse(file_path, media_type="image/png")


def get_all_product_image(product_id, database) -> List[model.ProductImage]:
    image = database.query(model.ProductImage).filter(model.ProductImage.product_id == product_id).all()
    return image


async def edit_image(product_id, request, old_image, database):
    images = database.query(model.ProductImage).filter(model.ProductImage.product_id == product_id).all()
    base_dir = os.path.dirname(os.path.abspath(__file__))
    image_folder = os.path.join(base_dir, '..', '..', config.UPLOAD_DIRECTORY)
    for image in images:
        if image.image_path not in old_image:
            file_path = os.path.join(image_folder, image.image_path)
            os.remove(file_path)
            delete_image(image.image_path, database)

    await upload_image(request, product_id, database)


async def upload_image(list_image, product_id, database):
    for image in list_image:
        new_image = model.ProductImage(image_path=image.filename, product_id=product_id)
        database.add(new_image)
        database.commit()
        database.refresh(new_image)
        file_location = os.path.join(config.UPLOAD_DIRECTORY, image.filename)
        with open(file_location, "wb") as buffer:
            buffer.write(await image.read())


def get_product_image_first(product_id, database) -> Optional[model.ProductImage]:
    image_info = database.query(model.ProductImage).filter(model.ProductImage.product_id == product_id).first()
    return image_info


def delete_image(file_name, database):
    database.query(model.ProductImage).filter(model.ProductImage.image_path == file_name).delete()
    database.commit()
