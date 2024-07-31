from typing import List
from fastapi import APIRouter, Depends, Response, status, HTTPException
from sqlalchemy.orm import Session
from app import database
from app.account import validator
from app.account.model import Account
from app.account.oauth2 import get_current_user
from app.customer import schema, services

router = APIRouter(tags=['Customer'], prefix='/customer')


@router.get('/', response_model=List[schema.DisplayCustomer])
async def get_all_customer(database: Session = Depends(database.get_db)):
    return services.get_all_customer(database)


@router.post('/create', status_code=status.HTTP_201_CREATED)
async def create_customer(request: schema.CustomerCreate, database: Session = Depends(database.get_db)):
    account = validator.verify_email_exist(request.email, database)
    if account:
        raise HTTPException(
            status_code=400,
            detail='Email đã được sử dụng.'
        )
    new_customer = services.create_customer(request=request, database=database)
    return new_customer


@router.put('/edit/{customer_id}', response_class=Response)
async def edit_customer(customer_id: int, request: schema.CustomerUpdate, database: Session = Depends(database.get_db)):
    services.edit_customer(customer_id, request, database)


@router.get('/{customer_id}', response_model=schema.DisplayCustomer)
async def get_customer_by_id(customer_id: int, database: Session = Depends(database.get_db)):
    return services.get_customer_by_id(customer_id, database)


@router.delete('/{customer_id}', response_class=Response)
async def delete_customer(customer_id: int, database: Session = Depends(database.get_db)):
    return services.delete_customer(customer_id, database)
