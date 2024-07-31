from app.inventory import model


def get_all_inventory(database):
    inventories = database.query(model.Inventory).all()
    return inventories


def create_inventory(request, database):
    new_inventory = model.Inventory(product_id=request.product_id, size_id=request.size_id, import_price=request.import_price, quantity=request.quantity)
    database.add(new_inventory)
    database.commit()
    database.refresh(new_inventory)
    return new_inventory


def edit_inventory(inventory_id, request, database):
    database.query(model.Inventory).filter(model.Inventory.id == inventory_id).update(request)
    database.commit()


def get_inventory_by_id(inventory_id, database):
    inventory_info = database.query(model.Inventory).get(int(inventory_id))
    return inventory_info


def delete_inventory(inventory_id, database):
    database.query(model.Inventory).filter(model.Inventory.id == inventory_id).delete()
    database.commit()