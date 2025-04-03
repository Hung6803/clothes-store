from typing import List
from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.orm import Session
from app import database
from app.account.model import Account
from app.account.oauth2 import get_current_user
from app.invoice import schema, services

router = APIRouter(tags=['Invoice'], prefix='/invoice')


@router.get('/', response_model=List[schema.DisplayInvoice])
async def get_all_invoice(db: Session = Depends(database.get_db)):
    return services.get_all_invoice(db)


@router.post('/create', status_code=status.HTTP_201_CREATED)
async def create_invoice(request: schema.InvoiceCreate, db: Session = Depends(database.get_db)):
    new_invoice = services.create_invoice(request=request, database=db)
    return new_invoice


@router.put('/edit/status', response_class=Response)
async def edit_status(request: List[schema.InvoiceUpdate], db: Session = Depends(database.get_db)):
    return services.edit_status(request, db)


@router.get('/new', response_model=List[schema.DisplayInvoice])
async def get_new_invoice(db: Session = Depends(database.get_db)):
    return services.get_new_invoice(db)


@router.delete('/{invoice_id}', response_class=Response)
async def delete_invoice(invoice_id: int, db: Session = Depends(database.get_db)):
    return services.delete_invoice(invoice_id, db)
