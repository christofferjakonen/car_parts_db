import Data.Repository.parts_repository as pr


def get_all_parts():
    return pr.get_all_parts()


def get_part_by_id(inputID):
    part = pr.get_part_by_id(inputID)
    result = part if part else "No part was found"
    return result

def get_part_by_name(partName):
    parts = pr.get_part_by_name(partName)
    return {i+1: part for i, part in enumerate(parts)}

def add_new_part(partId, partName=None, manufacturer="None", partDescription=None, purchasePrice=None, sellPrice=None):
    return pr.add_new_part(partId, partName, manufacturer, partDescription, purchasePrice, sellPrice)


def delete_part_by_ID(command):
    return pr.delete_part_by_ID(command)

def update_part_by_ID(partID, columnNr):
    if columnNr == 1:
        columnName = "ProductName"
    elif columnNr == 2:
        columnName = "ProductNum"
    elif columnNr == 3:
        columnName = "PartDescription"
    elif columnNr == 4:
        columnName = "Manufacture"
    elif columnNr == 5:
        columnName = "PurchasePrice"
    elif columnNr == 6:
        columnName = "SellPrice"
    else:
        print("column does not exist")
        return None

    newValue = input("new value: ")
    return pr.update_part_by_ID(partID, columnName, newValue)
