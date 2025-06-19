from typing import List
from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.orm import Session
from app import database
from app.account.oauth2 import admin_required
from app.size import schema, services

router = APIRouter(tags=['Size'], prefix='/size')


@router.get('/', response_model=List[schema.DisplaySize])
async def get_all_size(db: Session = Depends(database.get_db)):
    return services.get_all_size(db)


@router.post('/create', status_code=status.HTTP_201_CREATED, dependencies=[Depends(admin_required)])
async def create_size(request: schema.Size, db: Session = Depends(database.get_db)):
    new_user = await services.create_size(request, db)
    return new_user


@router.put('/edit/{size_id}', response_class=Response, dependencies=[Depends(admin_required)])
async def edit_size(size_id: int, request: schema.Size, db: Session = Depends(database.get_db)):
    return services.edit_size(size_id, request, db)


@router.get('/{size_id}', response_model=schema.DisplaySize)
async def get_size_by_id(size_id: int, db: Session = Depends(database.get_db)):
    return services.get_size_by_id(size_id, db)


@router.delete('/{size_id}', response_class=Response, dependencies=[Depends(admin_required)])
async def delete_size(size_id: int, db: Session = Depends(database.get_db)):
    return services.delete_size(size_id, db)
