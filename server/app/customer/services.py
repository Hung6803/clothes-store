from app.customer import model
from app.account import services as account_services


def get_all_customer(database):
    customers = database.query(model.Customer).all()
    return customers


def create_customer(request, database):
    account_id = account_services.create_account(request.email, request.password, request.role, database)
    new_customer = model.Customer(name=request.name, account_id=account_id,
                                  phone_number=request.phone_number, date_of_birth=request.date_of_birth,
                                  address=request.address)
    database.add(new_customer)
    database.commit()
    database.refresh(new_customer)

    return {'msg': 'success'}


def create_customer_no_account(request, database):
    new_customer = model.Customer(name=request.name, phone_number=request.phone_number, address=request.address)
    database.add(new_customer)
    database.commit()
    database.refresh(new_customer)

    return new_customer


def edit_customer(customer_id, request, database):
    database.query(model.Customer).filter(model.Customer.id == customer_id).update(request)
    database.commit()


def get_customer_by_id(customer_id, database):
    customer_info = database.query(model.Customer).get(int(customer_id))
    return customer_info


def delete_customer(customer_id, database):
    account_id = database.query(model.Customer.account_id).filter(model.Customer.id == customer_id).first()
    database.query(model.Customer).filter(model.Customer.id == customer_id).delete()
    account_services.delete_account(account_id, database)
    database.commit()