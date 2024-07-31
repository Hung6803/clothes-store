from typing import List
from fastapi import APIRouter, Depends, Response, status, HTTPException
from sqlalchemy.orm import Session
from app import database
from app.account import validator
from app.account.model import Account
from app.account.oauth2 import get_current_user
from app.employee import schema, services

router = APIRouter(tags=['Employee'], prefix='/employee')


@router.get('/', response_model=List[schema.DisplayEmployee])
async def get_all_employee(database: Session = Depends(database.get_db)):
    return services.get_all_employee(database)


@router.post('/create', status_code=status.HTTP_201_CREATED)
async def create_employee(request: schema.EmployeeCreate, database: Session = Depends(database.get_db)):
    account = validator.verify_email_exist(request.email, database)
    if account:
        raise HTTPException(
            status_code=400,
            detail='Email đã được sử dụng.'
        )
    new_employee = services.create_employee(request=request, database=database)
    return new_employee


@router.put('/edit/{employee_id}', response_class=Response)
async def edit_employee(employee_id: int, request: schema.EmployeeUpdate, database: Session = Depends(database.get_db)):
    services.edit_employee(employee_id, request, database)


@router.get('/{employee_id}', response_model=schema.DisplayEmployee)
async def get_employee_by_id(employee_id: int, database: Session = Depends(database.get_db)):
    return services.get_employee_by_id(employee_id, database)


@router.delete('/{employee_id}', response_class=Response)
async def delete_employee(employee_id: int, database: Session = Depends(database.get_db)):
    return services.delete_employee(employee_id, database)
