from typing import List
from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.orm import Session
from app import database
from app.account.model import Account
from app.account.oauth2 import get_current_user
from app.category import schema, services

router = APIRouter(tags=['Categories'], prefix='/category')


@router.get('/', response_model=List[schema.DisplayCategory])
async def get_all_category(database: Session = Depends(database.get_db)):
    return services.get_all_category(database)


@router.post('/create', status_code=status.HTTP_201_CREATED)
async def create_category(request: schema.Category, database: Session = Depends(database.get_db)):
    new_user = await services.create_category(request, database)
    return new_user


@router.put('/edit/{category_id}', response_class=Response)
async def edit_user(category_id: int, request: schema.Category, database: Session = Depends(database.get_db)):
    return services.edit_category(category_id, request, database)


@router.get('/{category_id}', response_model=schema.DisplayCategory)
async def get_category_by_id(category_id: int, database: Session = Depends(database.get_db)):
    return services.get_category_by_id(category_id, database)



@router.delete('/{category_id}', response_class=Response)
async def delete_user(category_id: int, database: Session = Depends(database.get_db)):
    return services.delete_category(category_id, database)
