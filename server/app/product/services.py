from sqlalchemy import func, desc
from sqlalchemy.orm import joinedload

from app.invoice_details.model import InvoiceDetails
from app.product import model
from app.inventory.model import Inventory
from app.image.services import get_product_image_first


def format_product_list(products):
    product_list = []
    for product in products:
        product_response = {
            "id": product.id,
            "product_name": product.product_name,
            "price": product.price,
            "discount": product.discount,
            "category": {
                "id": product.category.id,
                "category_name": product.category.category_name
            },
            "brand": {
                "id": product.brand.id,
                "brand_name": product.brand.brand_name
            },
            "product_image": None
        }

        if product.images:
            product_response["product_image"] = {"image_path": product.images[0].image_path}

        product_list.append(product_response)

    return product_list


def get_all_product(database):
    products = database.query(model.Product).options(
        joinedload(model.Product.images),
    ).all()

    return format_product_list(products)


def get_product(options, database):
    query = database.query(model.Product).options(
        joinedload(model.Product.images),
    )

    if options.category_id:
        query = query.filter(model.Product.category_id == options.category_id)

    if options.brand_id:
        query = query.filter(model.Product.brand_id == options.brand_id)

    if options.price_min or options.price_max:
        query = query.filter(model.Product.price.between(options.price_min, options.price_max))

    # Tìm kiếm theo tên sản phẩm
    if options.search:
        query = query.filter(model.Product.product_name.ilike(f"%{options.search}%"))

    if options.size_id:
        query = (query.join(Inventory, model.Product.id == Inventory.product_id)
                 .filter(Inventory.size_id == options.size_id))

    # Sắp xếp
    if options.sort_by:
        sort_column = getattr(model.Product, options.sort_by, None)
        if sort_column is not None:
            if options.sort_order == "desc":
                query = query.order_by(sort_column.desc())
            else:
                query = query.order_by(sort_column.asc())

    total = query.count()

    # Phân trang
    skip = (options.page - 1) * options.limit
    products = query.offset(skip).limit(options.limit).all()
    product_list = format_product_list(products)

    return {"products": product_list, "total": total}


def create_product(request, database):
    new_product = model.Product(product_name=request.product_name, product_description=request.product_description,
                                price=request.price, discount=request.discount, category_id=request.category_id,
                                brand_id=request.brand_id)
    database.add(new_product)
    database.commit()
    database.refresh(new_product)
    return new_product


def edit_product(product_id, request, database):
    database.query(model.Product).filter(model.Product.id == product_id).update(request)
    database.commit()


def get_product_by_id(product_id, database):
    product_info = database.query(model.Product).filter(model.Product.id == product_id).first()
    return {
        "id": product_info.id,
        "product_name": product_info.product_name,
        "product_description": product_info.product_description,
        "price": product_info.price,
        "discount": product_info.discount,
        "category": product_info.category,
        "brand": product_info.brand,
        "product_image": [{"image_path": img.image_path} for img in product_info.images]
    }


def delete_product(product_id, database):
    database.query(model.Product).filter(model.Product.id == product_id).delete()
    database.commit()


def get_product_name(database):
    products = database.query(model.Product.id, model.Product.product_name).all()
    return products


def get_top_product(top_quantity, database):
    products = (
        database.query(
            model.Product.id.label("product_id"),
            model.Product.product_name.label("product_name"),
            model.Product.price.label("price"),
            model.Product.discount.label("discount"),
            func.sum(InvoiceDetails.quantity).label("total_sold")
        )
        .join(model.Product, model.Product.id == InvoiceDetails.product_id)
        .group_by(model.Product.id, model.Product.product_name, model.Product.price)
        .order_by(desc("total_sold"))
        .limit(top_quantity)
        .all()
    )
    product_top = []
    for product in products:
        product_response = {
            "id": product.product_id,
            "product_name": product.product_name,
            "price": product.price,
            "discount": product.discount,
            "total_sold": product.total_sold,
            "product_image": None
        }

        image = get_product_image_first(product.product_id, database)
        product_response["product_image"] = {"image_path": image.image_path}

        product_top.append(product_response)
    return product_top


def get_discount_product(quantity, database):
    products = (
        database.query(
            model.Product.id.label("product_id"),
            model.Product.product_name.label("product_name"),
            model.Product.price.label("price"),
            model.Product.discount.label("discount")
        )
        .filter(model.Product.discount > 0)
        .order_by(desc("discount"))
        .limit(quantity)
        .all()
    )
    product_discount = []
    for product in products:
        product_response = {
            "id": product.product_id,
            "product_name": product.product_name,
            "price": product.price,
            "discount": product.discount,
            "total_sold": 0,
            "product_image": None
        }

        image = get_product_image_first(product.product_id, database)
        product_response["product_image"] = {"image_path": image.image_path}

        product_discount.append(product_response)
    return product_discount


