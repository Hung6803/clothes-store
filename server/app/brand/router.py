from typing import List
from fastapi import APIRouter, Depends, Response, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from app import database
from app.account.model import Account
from app.account.oauth2 import get_current_user
from app.brand import schema, services

router = APIRouter(tags=['Brands'], prefix='/brand')


@router.get('/', response_model=List[schema.BrandDisplay])
async def get_all_brand(database: Session = Depends(database.get_db)):
    return services.get_all_brand(database)


@router.get('/limit', response_model=List[schema.BrandDisplay])
async def get_limit_brand(skip: int = 0, limit: int = 10, database: Session = Depends(database.get_db)):
    return services.get_limit_brand(limit, skip, database)


@router.post('/create', status_code=status.HTTP_201_CREATED)
async def create_brand(request: schema.Brand, database: Session = Depends(database.get_db)):
    new_user = await services.create_brand(request, database)
    return new_user


@router.put('/edit/{brand_id}', response_class=Response)
async def edit_user(brand_id: int, request: schema.Brand, database: Session = Depends(database.get_db)):
    return services.edit_brand(brand_id, request, database)


@router.get('/{brand_id}', response_model=schema.BrandDisplay)
async def get_brand_by_id(brand_id: int, database: Session = Depends(database.get_db)):
    return services.get_brand_by_id(brand_id, database)


@router.delete('/{brand_id}', response_class=Response)
async def delete_user(brand_id: int, database: Session = Depends(database.get_db)):
    return services.delete_brand(brand_id, database)
