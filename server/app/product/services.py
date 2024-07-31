from sqlalchemy import func

from app.inventory.model import Inventory
from app.product import model


def get_all_product(database):
    products = database.query(model.Product).all()
    return products


def create_product(request, database):
    new_product = model.Product(product_name=request.product_name, product_description=request.product_description,
                                price=request.price, category_id=request.category_id, brand_id=request.brand_id)
    database.add(new_product)
    database.commit()
    database.refresh(new_product)
    return new_product


def edit_product(product_id, request, database):
    database.query(model.Product).filter(model.Product.id == product_id).update(request)
    database.commit()


def get_product_by_id(product_id, database):
    product_info = (database.query(model.Product.product_name, model.Product.product_description,
                                   model.Product.price, model.Product.category_id, model.Product.brand_id)
                    .filter(model.Product.id == product_id).first())
    return product_info


def delete_product(product_id, database):
    database.query(model.Product).filter(model.Product.id == product_id).delete()
    database.commit()


def get_product_name(database):
    products = database.query(model.Product.id, model.Product.product_name).all()
    return products
