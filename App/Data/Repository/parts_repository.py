from bson import ObjectId
from ..models.models import *
import re

def get_all_parts():
    return Part.all()

def get_part_by_id(inputID):
    everything = Part.all()
    return [everything[i] for i in range(len(everything)) if re.search(f".*{inputID}.*", str(everything[i]._id))]


def get_part_by_name(partName):
    everything = Part.all()
    partName = partName.lower()
    return [everything[i] for i in range(len(everything)) if re.search(f".*{partName}.*", everything[i].Product_Name.lower())]

def get_part_by_product_number(productNumber):
    everything = Part.all()
    return [everything[i] for i in range(len(everything)) if re.search(f".*{productNumber}.*", everything[i].Product_Number)]


def add_new_part(partID, partName="None", partMaker="None", description="None", cost="None", sellPrice="None"):
    new_part = Part({
        "Product_Number": partID,
        "Product_Name": partName,
        "Manufacturer": partMaker,
        "Product_Description": description,
        "Warehouse": [],
        "Buy_Price": cost,
        "Sell_Price": sellPrice
    })
    new_part.save()
    return None


def update_part_by_id(partID, columnName=None, newValue="None", index=None):
    old = Part.find(**{"_id": ObjectId(partID)}).first_or_none()
    updated = {
        '_id': old._id,
        'Product_Number': old.Product_Number,
        'Product_Name': old.Product_Name,
        'Manufacturer': old.Manufacturer,
        'Product_Description': old.Product_Description,
        'Warehouse': old.Warehouse,
        'Buy_Price': old.Buy_Price,
        'Sell_Price': old.Sell_Price
    }
    if columnName == "ProductNum":
        updated["Product_Number"] = newValue
    if columnName == "ProductName":
        updated["Product_Name"] = newValue
    if columnName == "Manufacture":
        updated["Manufacturer"] = newValue
    if columnName == "PartDescription":
        updated["Product_Description"] = newValue
    if columnName == "PurchasePrice":
        updated["Buy_Price"] = newValue
    if columnName == "SellPrice":
        updated["Sell_Price"] = newValue
    if columnName == "Warehouse":
        updated["Warehouse"].append(newValue)
    if columnName == "WarehouseEdit":
        updated["Warehouse"][index] = newValue

    # todo reduce code size by using var directly as index

    Part(updated).save()
    return None


def delete_part_by_id(partID):
    Part.delete(_id=ObjectId(partID))
    return None


def get_cars_for_part_id(part_id):
    pass

