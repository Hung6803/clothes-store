from typing import List
from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.orm import Session
from app import database
from app.account.oauth2 import admin_required
from app.brand import schema, services

router = APIRouter(tags=['Brands'], prefix='/brand')


@router.get('/', response_model=List[schema.BrandDisplay])
async def get_all_brand(db: Session = Depends(database.get_db)):
    return services.get_all_brand(db)


@router.post('/create', status_code=status.HTTP_201_CREATED, dependencies=[Depends(admin_required)])
async def create_brand(request: schema.Brand, db: Session = Depends(database.get_db)):
    new_user = await services.create_brand(request, db)
    return new_user


@router.put('/edit/{brand_id}', response_class=Response, dependencies=[Depends(admin_required)])
async def edit_brand(brand_id: int, request: schema.Brand, db: Session = Depends(database.get_db)):
    return services.edit_brand(brand_id, request, db)


@router.get('/{brand_id}', response_model=schema.BrandDisplay)
async def get_brand_by_id(brand_id: int, db: Session = Depends(database.get_db)):
    return services.get_brand_by_id(brand_id, db)


@router.delete('/{brand_id}', response_class=Response, dependencies=[Depends(admin_required)])
async def delete_brand(brand_id: int, db: Session = Depends(database.get_db)):
    return services.delete_brand(brand_id, db)
