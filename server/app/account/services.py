from typing import List, Optional
from app.account import model, schema, hashing, validator


def new_account_register(request: schema.Account, database) -> model.Account:
    new_account = model.Account(email=request.email, password=request.password, role=request.role)
    database.add(new_account)
    database.commit()
    database.refresh(new_account)
    return new_account


def verify_account(email, password, database) -> Optional[model.Account]:
    account_info = validator.verify_email_exist(email, database)
    if not account_info or not hashing.verify_password(password, account_info.password):
        return None
    else:
        return account_info


def get_account_by_email(email, database) -> Optional[model.Account]:
    user_info = database.query(model.Account).filter(model.Account.email == email).first()
    return user_info


async def authenticate_user(database, email, password):
    account = get_account_by_email(email, database)
    if not account:
        return False
    if not hashing.verify_password(password, account.hashed_password):
        return False
    return account


def edit_account(account_id, request, database):
    database.query(model.Account).filter(model.Account.id == account_id).update(request)
    database.commit()


def create_account(email, password, role, database):
    new_account = model.Account(email=email, password=password, role=role)
    database.add(new_account)
    database.commit()
    database.refresh(new_account)
    return database.query(model.Account.id).filter(model.Account.email == email).first()


def delete_account(account_id, database):
    database.query(model.Account).filter(model.Account.id == account_id).delete()
    database.commit()
