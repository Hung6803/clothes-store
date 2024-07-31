from typing import List
from fastapi import APIRouter, Depends, Response, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from app import database
from app.account import schema, services, validator, token
from app.account.model import Account
from app.account.oauth2 import get_current_user

router = APIRouter(tags=['Accounts'], prefix='/account')


@router.post('/login', status_code=status.HTTP_200_OK)
async def login(request: OAuth2PasswordRequestForm = Depends(), database: Session = Depends(database.get_db)):
    account = services.verify_account(request.username, request.password, database)

    if not account:
        raise HTTPException(
            status_code=400,
            detail='Email or password is incorrect'
        )
    if account.role:
        access_token = token.create_access_token(data={"sub": account.email})
        return schema.Token(access_token=access_token, token_type="bearer")
    else:
        return schema.AccountDisplay(email=account.email, createDate=account.createDate)


@router.post('/register', status_code=status.HTTP_201_CREATED)
async def create_user_registration(request: schema.Account, database: Session = Depends(database.get_db)):
    user = validator.verify_email_exist(request.email, database)

    if user:
        raise HTTPException(
            status_code=400,
            detail='Email đã được sử dụng.'
        )

    new_user = services.new_account_register(request, database)
    return new_user


@router.put("/edit/{account_id}", response_class=Response)
async def edit_account(account_id: int, request: schema.AccountUpdate, database: Session = Depends(database.get_db)):
    return services.edit_account(account_id, request, database)
