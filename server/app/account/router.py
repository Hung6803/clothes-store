from fastapi import APIRouter, Depends, Response, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm

from app import database
from app.account import schema, services, validator, token
from app.account.model import Account
from app.account.oauth2 import get_current_user

router = APIRouter(tags=['Accounts'], prefix='/account')


@router.post('/login', status_code=status.HTTP_200_OK)
async def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    account = services.verify_account(request.username, request.password, db)

    if not account:
        raise HTTPException(
            status_code=400,
            detail='Email or password is incorrect'
        )
    access_token = token.create_access_token(data={"sub": account.email, "role": account.role})
    return schema.Token(access_token=access_token, token_type="bearer")


@router.post('/register', status_code=status.HTTP_201_CREATED)
async def create_user_registration(request: schema.Account, db: Session = Depends(database.get_db)):
    user = validator.verify_email_exist(request.email, db)

    if user:
        raise HTTPException(
            status_code=400,
            detail='Email đã được sử dụng.'
        )

    new_user = services.new_account_register(request, db)
    return new_user


@router.put("/edit/{account_id}", response_class=Response)
async def edit_account(account_id: int, request: schema.AccountUpdate, db: Session = Depends(database.get_db)):
    return services.edit_account(account_id, request, db)


@router.get('/me', response_model=schema.TokenData)
async def read_users_me(current_user: Account = Depends(get_current_user)):
    return current_user
