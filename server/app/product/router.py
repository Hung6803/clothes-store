from typing import List
from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.orm import Session
from app import database
from app.account.model import Account
from app.account.oauth2 import get_current_user
from app.product import schema, services

router = APIRouter(tags=['Product'], prefix='/product')


@router.get('/', response_model=List[schema.DisplayProduct])
async def get_all_product(database: Session = Depends(database.get_db)):
    return services.get_all_product(database)


@router.get('/product_name', response_model=List[schema.ProductName])
async def get_product_name(database: Session = Depends(database.get_db)):
    return services.get_product_name(database)


@router.post('/create', status_code=status.HTTP_201_CREATED)
async def create_product(request: schema.Product, database: Session = Depends(database.get_db)):
    new_product = services.create_product(request=request, database=database)
    return new_product


@router.put('/edit/{product_id}', response_class=Response)
async def edit_product(product_id: int, request: schema.Product, database: Session = Depends(database.get_db)):
    return services.edit_product(product_id, request, database)


@router.get('/{product_id}', response_model=schema.ProductEdit)
async def get_product_by_id(product_id: int, database: Session = Depends(database.get_db)):
    return services.get_product_by_id(product_id, database)


@router.delete('/{product_id}', response_class=Response)
async def delete_product(product_id: int, database: Session = Depends(database.get_db)):
    return services.delete_product(product_id, database)
