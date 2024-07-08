from typing import List
from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.orm import Session
from app import database
from app.account.model import Account
from app.account.oauth2 import get_current_user
from app.size import schema, services

router = APIRouter(tags=['Size'], prefix='/size')


@router.get('/', response_model=List[schema.DisplaySize])
async def get_all_size(database: Session = Depends(database.get_db)):
    return services.get_all_size(database)


@router.post('/create', status_code=status.HTTP_201_CREATED)
async def create_size(request: schema.Size, database: Session = Depends(database.get_db)):
    new_user = await services.create_size(request, database)
    return new_user


@router.put('/edit/{size_id}', response_class=Response)
async def edit_user(size_id: int, request: schema.Size, database: Session = Depends(database.get_db)):
    return services.edit_size(size_id, request, database)


@router.get('/{size_id}', response_model=schema.DisplaySize)
async def get_size_by_id(size_id: int, database: Session = Depends(database.get_db)):
    return services.get_size_by_id(size_id, database)


@router.delete('/{size_id}', response_class=Response)
async def delete_user(size_id: int, database: Session = Depends(database.get_db)):
    return services.delete_size(size_id, database)
