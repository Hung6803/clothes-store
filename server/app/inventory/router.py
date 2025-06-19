from typing import List
from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.orm import Session
from app import database
from app.account.oauth2 import admin_required
from app.inventory import schema, services

router = APIRouter(tags=['Inventory'], prefix='/inventory')


@router.get('/', response_model=List[schema.DisplayInventory])
async def get_all_inventory(db: Session = Depends(database.get_db)):
    return services.get_all_inventory(db)


@router.post('/create', status_code=status.HTTP_201_CREATED, dependencies=[Depends(admin_required)])
async def create_inventory(request: schema.Inventory, db: Session = Depends(database.get_db)):
    new_inventory = services.create_inventory(request=request, database=db)
    return new_inventory


@router.put('/edit/{product_id}/{size_id}', response_class=Response, dependencies=[Depends(admin_required)])
async def edit_inventory(product_id: int, size_id: int, request: schema.InventoryUpdate, db: Session = Depends(database.get_db)):
    return services.edit_inventory(product_id, size_id, request, db)


@router.get('/{product_id}/{size_id}', response_model=schema.DisplayInventory)
async def get_inventory_by_id(product_id: int, size_id: int, db: Session = Depends(database.get_db)):
    return services.get_inventory_by_id(product_id, size_id, db)


@router.get('/{product_id}', response_model=schema.DisplayProductSize)
async def get_inventory_by_product_id(product_id: int, db: Session = Depends(database.get_db)):
    return services.get_inventory_by_product_id(product_id, db)


@router.delete('/{product_id}/{size_id}', response_class=Response, dependencies=[Depends(admin_required)])
async def delete_inventory(product_id: int, size_id: int, db: Session = Depends(database.get_db)):
    return services.delete_inventory(product_id, size_id, db)
