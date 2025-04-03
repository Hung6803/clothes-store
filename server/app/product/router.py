import os
from typing import List
from fastapi import APIRouter, Depends, Response, status, UploadFile, File
from sqlalchemy.orm import Session
from starlette import schemas
from starlette.responses import FileResponse

from app import database, config
from app.account.model import Account
from app.account.oauth2 import get_current_user
from app.product import schema, services

router = APIRouter(tags=['Product'], prefix='/product')


@router.get('/', response_model=List[schema.DisplayProduct])
async def get_all_product(db: Session = Depends(database.get_db)):
    return services.get_all_product(db)


@router.get('/top/{top_quantity}', response_model=List[schema.DisplayTopProduct])
async def get_top_product(top_quantity: int, db: Session = Depends(database.get_db)):
    return services.get_top_product(top_quantity, db)


@router.get('/discount/{quantity}', response_model=List[schema.DisplayTopProduct])
async def get_discount_product(quantity: int, db: Session = Depends(database.get_db)):
    return services.get_discount_product(quantity, db)


@router.post("/")
async def get_products(request: schema.ProductOption, db: Session = Depends(database.get_db)):
    return services.get_product(options=request, database=db)


@router.get('/product_name', response_model=List[schema.ProductName])
async def get_product_name(db: Session = Depends(database.get_db)):
    return services.get_product_name(db)


@router.post('/create', status_code=status.HTTP_201_CREATED)
async def create_product(request: schema.Product, db: Session = Depends(database.get_db)):
    new_product = services.create_product(request=request, database=db)
    return new_product


@router.put('/edit/{product_id}', response_class=Response)
async def edit_product(product_id: int, request: schema.Product, db: Session = Depends(database.get_db)):
    return services.edit_product(product_id, request, db)


@router.get('/{product_id}', response_model=schema.DisplayProductFull)
async def get_product_by_id(product_id: int, db: Session = Depends(database.get_db)):
    return services.get_product_by_id(product_id, db)


@router.delete('/{product_id}', response_class=Response)
async def delete_product(product_id: int, db: Session = Depends(database.get_db)):
    return services.delete_product(product_id, db)
