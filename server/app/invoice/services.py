from fastapi import HTTPException

from app.invoice import model


def get_all_invoice(database):
    invoices = database.query(model.Invoice).all()
    return invoices


def create_invoice(request, database) -> model.Invoice:
    new_invoice = model.Invoice(total_price=request.total_price, payment_type=request.payment_type,
                                status=request.status, address=request.address, employee_id=request.employee_id,
                                customer_id=request.customer_id)
    database.add(new_invoice)
    database.commit()
    database.refresh(new_invoice)

    return new_invoice


def edit_status(request, database):
    for invoice in request:
        invoice_info = database.query(model.Invoice).filter(model.Invoice.id == invoice.id).first()
        if invoice_info:
            invoice_info.status = 2
            database.commit()
        else:
            raise HTTPException(status_code=404, detail="Don't query invoice ID")


def delete_invoice(invoice_id, database):
    database.query(model.Invoice).filter(model.Invoice.id == invoice_id).delete()
    database.commit()


def get_new_invoice(database):
    invoices = database.query(model.Invoice).filter(model.Invoice.status == 1).all()
    return invoices
