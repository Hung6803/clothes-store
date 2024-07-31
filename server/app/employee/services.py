from app.employee import model
from app.account import services as account_services


def get_all_employee(database):
    employees = database.query(model.Employee).all()
    return employees


def create_employee(request, database):
    account_id = account_services.create_account(request.email, request.password, request.role, database)
    new_employee = model.Employee(name=request.name, account_id=account_id,
                                  phone_number=request.phone_number, date_of_birth=request.date_of_birth,
                                  address=request.address, start_date=request.start_date, salary=request.salary)
    database.add(new_employee)
    database.commit()
    database.refresh(new_employee)

    return {'msg': 'success'}


def edit_employee(employee_id, request, database):
    database.query(model.Employee).filter(model.Employee.id == employee_id).update(request)
    database.commit()


def get_employee_by_id(employee_id, database):
    employee_info = database.query(model.Employee).get(int(employee_id))
    return employee_info


def delete_employee(employee_id, database):
    account_id = database.query(model.Employee.account_id).filter(model.Employee.id == employee_id).first()
    database.query(model.Employee).filter(model.Employee.id == employee_id).delete()
    account_services.delete_account(account_id, database)
    database.commit()
