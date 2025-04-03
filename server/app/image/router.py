import os
from typing import List
from fastapi import APIRouter, Depends, Response, status, UploadFile, File, Form
from sqlalchemy.orm import Session
from starlette.responses import FileResponse

from app import database, config
from app.account.model import Account
from app.account.oauth2 import get_current_user
from app.image import schema, services

router = APIRouter(tags=['Product Image'], prefix='/image')


@router.post("/upload", status_code=status.HTTP_201_CREATED)
async def upload_image(list_image: List[UploadFile] = File(...), product_id: int = Form(...),
                       db: Session = Depends(database.get_db)):
    image = await services.upload_image(list_image, product_id, db)
    return image


@router.get("/{name}", responses={200: {"content": {"image/png": {}}}}, response_class=Response)
def get_image(name: str):
    file_path = "image/" + name
    return FileResponse(file_path, media_type="image/png")


@router.get('/{product_id}', response_model=List[schema.DisplayImage])
async def get_all_product_image(product_id: int, db: Session = Depends(database.get_db)):
    return services.get_all_product_image(product_id, db)


@router.put('/edit/{product_id}', response_class=Response)
async def edit_image(product_id: int, request: List[UploadFile] = File(...), old_image: List[str] = Form(...), db: Session = Depends(database.get_db)):
    return await services.edit_image(product_id, request, old_image, db)


@router.get('/{product_id}', response_model=schema.DisplayImage)
async def get_product_image_first(product_id: int, db: Session = Depends(database.get_db)):
    return services.get_product_image_first(product_id, db)


@router.delete('/{product_id}', response_class=Response)
async def delete_image(product_id: int, db: Session = Depends(database.get_db)):
    return services.delete_image(product_id, db)
