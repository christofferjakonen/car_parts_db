import Data.Repository.parts_repository as pr


def get_all_parts():
    return pr.get_all_parts()


def get_part_by_id(inputID):
    part = pr.get_part_by_id(inputID)
    return part if part else ["No part was found"]


def get_part_by_name(partName):
    part = pr.get_part_by_name(partName)
    return part if part else ["No part was found"]


def get_part_by_product_number(partNumber):
    part = pr.get_part_by_product_number(partNumber)
    return part if part else ["No part was found"]


def add_new_part(partId, partName=None, manufacturer=None, partDescription=None, purchasePrice=None, sellPrice=None):
    return pr.add_new_part(partId, partName, manufacturer, partDescription, purchasePrice, sellPrice)


def delete_part_by_id(command):
    return pr.delete_part_by_id(command)


def update_part_by_id(partID, columnNr, newValue, index=None):

    if columnNr == 1:
        columnName = "ProductNum"
    elif columnNr == 2:
        columnName = "ProductName"
    elif columnNr == 3:
        columnName = "Manufacture"
    elif columnNr == 4:
        columnName = "PartDescription"
    elif columnNr == 5:
        columnName = "PurchasePrice"
    elif columnNr == 6:
        columnName = "SellPrice"
    elif columnNr == 8:
        columnName = "WarehouseEdit"
    else:
        columnName = None

    return pr.update_part_by_id(partID, columnName, newValue, index)


def get_cars_for_part(id):
    car_id_list = pr.get_cars_for_part_id(id)
    car_list = []
    for i in range(len(car_id_list)):
        car_list.append(car_id_list[i][0])
    return car_list

