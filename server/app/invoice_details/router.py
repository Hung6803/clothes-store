from typing import List
from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.orm import Session
from app import database
from app.account.model import Account
from app.account.oauth2 import get_current_user
from app.invoice_details import schema, services

router = APIRouter(tags=['InvoiceDetail'], prefix='/invoice_details')


@router.get('/{invoice_id}', response_model=List[schema.DisplayProduct])
async def get_product_by_invoice(invoice_id: int, db: Session = Depends(database.get_db)):
    return services.get_product_by_invoice(invoice_id, db)


@router.post('/add', status_code=status.HTTP_201_CREATED)
async def add_product_to_invoice(request: schema.AddProduct, db: Session = Depends(database.get_db)):
    new_product = services.add_product_to_invoice(request=request, database=db)
    return new_product
