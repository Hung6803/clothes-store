from app.inventory import model


def get_all_inventory(database):
    inventories = database.query(model.Inventory).all()
    return inventories


def create_inventory(request, database):
    new_inventory = model.Inventory(product_id=request.product_id, size_id=request.size_id,
                                    import_price=request.import_price, quantity=request.quantity)
    database.add(new_inventory)
    database.commit()
    database.refresh(new_inventory)
    return new_inventory


def edit_inventory(product_id, size_id, request, database):
    database.query(model.Inventory).filter(model.Inventory.product_id == product_id
                                           and model.Inventory.size_id == size_id).update(request)
    database.commit()


def get_inventory_by_id(product_id, size_id, database):
    inventory_info = (database.query(model.Inventory).filter(model.Inventory.product_id == product_id
                                                             and model.Inventory.size_id == size_id).first())
    return inventory_info


def delete_inventory(product_id, size_id, database):
    database.query(model.Inventory).filter(model.Inventory.product_id == product_id
                                           and model.Inventory.size_id == size_id).delete()
    database.commit()


def get_inventory_by_product_id(product_id, database):
    product_size_db = (database.query(model.Inventory).filter(model.Inventory.product_id == product_id).all())
    product_sizes = {
        "product": {
            "id": product_size_db[0].product.id,
            "product_name": product_size_db[0].product.product_name,
        },
        "quantity": product_size_db[0].quantity,
        "sizes": [],
    }
    for product_size in product_size_db:
        product_sizes["sizes"].append(product_size.size)

    return product_sizes
