from bson import ObjectId
from ..models.models import *
import re


def get_all_manufacturers():
    return Manufacturer.all()

def get_manufacturer_by_name(search):
    everything = Manufacturer.all()
    search = search.lower()
    return [everything[i] for i in range(len(everything)) if re.search(f".*{search}.*", everything[i].Manufacturer.lower())]


def get_manufacturer_by_id(inputID):
    everything = Manufacturer.all()
    return [everything[i] for i in range(len(everything)) if re.search(f".*{inputID}.*", str(everything[i]._id))]


def add_new_manufacturer(manufacturer, country="None", state="None", city="None", zip="None", address="None", phone="None"):
    new_manufacturer = Manufacturer({
        "Manufacturer": manufacturer,
        "Contacts": [],
        "Address": {
            "Country": country,
            "State": state,
            "City": city,
            "Zipcode": zip,
            "StreetAddress": address,
            "PhoneNumber": phone
        }
    })
    new_manufacturer.save()
    return None


def update_manufacturer(searchId, searchColumn=None, newValue="None", index=None):
    old = Manufacturer.find(**{"_id": ObjectId(searchId)}).first_or_none()
    updated = {
        '_id': old._id,
        "Manufacturer": old.Manufacturer,
        "Contacts": old.Contacts,
        "Address": old.Address
    }
    if searchColumn == "Manufacturer":
        updated["Manufacturer"] = newValue
    if searchColumn == "Address":
        updated["Address"] = newValue
    if searchColumn == "ContactNew":
        updated["Contacts"].append(newValue)
    if searchColumn == "ContactEdit":
        updated["Contacts"][index] = newValue

    Manufacturer(updated).save()
    return None

def delete_manufacturer_by_id(searchId):
    Manufacturer.delete(_id=ObjectId(searchId))
    return None
