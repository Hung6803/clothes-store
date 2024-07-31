from typing import List
from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.orm import Session
from app import database
from app.account.model import Account
from app.account.oauth2 import get_current_user
from app.inventory import schema, services

router = APIRouter(tags=['Inventory'], prefix='/inventory')


@router.get('/', response_model=List[schema.DisplayInventory])
async def get_all_inventory(database: Session = Depends(database.get_db)):
    return services.get_all_inventory(database)


@router.post('/create', status_code=status.HTTP_201_CREATED)
async def create_inventory(request: schema.Inventory, database: Session = Depends(database.get_db)):
    new_inventory = services.create_inventory(request=request, database=database)
    return new_inventory


@router.put('/edit/{inventory_id}', response_class=Response)
async def edit_inventory(inventory_id: int, request: schema.Inventory, database: Session = Depends(database.get_db)):
    return services.edit_inventory(inventory_id, request, database)


@router.get('/{inventory_id}', response_model=schema.DisplayInventory)
async def get_inventory_by_id(inventory_id, database: Session = Depends(database.get_db)):
    return services.get_inventory_by_id(inventory_id, database)


@router.delete('/{inventory_id}', response_class=Response)
async def delete_inventory(inventory_id: int, database: Session = Depends(database.get_db)):
    return services.delete_inventory(inventory_id, database)
