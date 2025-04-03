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
async def get_all_customer(db: Session = Depends(database.get_db)):
    return services.get_all_customer(db)


@router.post('/create', status_code=status.HTTP_201_CREATED)
async def create_customer(request: schema.CustomerCreate, db: Session = Depends(database.get_db)):
    account = validator.verify_email_exist(request.email, db)
    if account:
        raise HTTPException(
            status_code=400,
            detail='Email đã được sử dụng.'
        )
    new_customer = services.create_customer(request=request, database=db)
    return new_customer


@router.post('/createnoaccount', response_model=schema.DisplayCustomerCreateNoAccount)
async def create_customer_no_account(request: schema.CustomerCreateNoAccount, db: Session = Depends(database.get_db)):
    new_customer = services.create_customer_no_account(request=request, database=db)
    return new_customer


@router.put('/edit/{customer_id}', response_class=Response)
async def edit_customer(customer_id: int, request: schema.CustomerUpdate, db: Session = Depends(database.get_db)):
    services.edit_customer(customer_id, request, db)


@router.get('/{customer_id}', response_model=schema.DisplayCustomer)
async def get_customer_by_id(customer_id: int, db: Session = Depends(database.get_db)):
    return services.get_customer_by_id(customer_id, db)


@router.delete('/{customer_id}', response_class=Response)
async def delete_customer(customer_id: int, db: Session = Depends(database.get_db)):
    return services.delete_customer(customer_id, db)
