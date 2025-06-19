from typing import List
from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.orm import Session
from app import database
from app.account.oauth2 import admin_required
from app.category import schema, services

router = APIRouter(tags=['Categories'], prefix='/category')


@router.get('/', response_model=List[schema.DisplayCategory])
async def get_all_category(db: Session = Depends(database.get_db)):
    return services.get_all_category(db)


@router.post('/create', status_code=status.HTTP_201_CREATED, dependencies=[Depends(admin_required)])
async def create_category(request: schema.Category, db: Session = Depends(database.get_db)):
    new_user = await services.create_category(request, db)
    return new_user


@router.put('/edit/{category_id}', response_class=Response, dependencies=[Depends(admin_required)])
async def edit_category(category_id: int, request: schema.Category, db: Session = Depends(database.get_db)):
    return services.edit_category(category_id, request, db)


@router.get('/{category_id}', response_model=schema.DisplayCategory)
async def get_category_by_id(category_id: int, db: Session = Depends(database.get_db)):
    return services.get_category_by_id(category_id, db)


@router.delete('/{category_id}', response_class=Response, dependencies=[Depends(admin_required)])
async def delete_category(category_id: int, db: Session = Depends(database.get_db)):
    return services.delete_category(category_id, db)
