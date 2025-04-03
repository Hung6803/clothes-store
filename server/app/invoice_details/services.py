from fastapi import HTTPException

from app.invoice_details import model


def get_product_by_invoice(invoice_id, database):
    products = database.query(model.InvoiceDetails).filter(model.InvoiceDetails.invoice_id == invoice_id).all()
    return products


def add_product_to_invoice(request, database):
    new_product = model.InvoiceDetails(invoice_id=request.invoice_id, product_id=request.product_id,
                                       size_id=request.size_id, quantity=request.quantity, discount=request.discount,
                                       price=request.price)
    database.add(new_product)
    database.commit()
    database.refresh(new_product)

    return {'msg': 'success'}


def delete_product_from_invoice(invoice_id, database):
    database.query(model.InvoiceDetails).filter(model.InvoiceDetails.invoice_id == invoice_id).delete()
    database.commit()

