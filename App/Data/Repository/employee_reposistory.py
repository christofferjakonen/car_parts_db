from bson import ObjectId
from ..models.models import *
import re


def get_all_employees():
    return Employee.all()


def get_employee_by_name(searchName):
    everything = Employee.all()
    searchName = searchName.lower()
    return [everything[i] for i in range(len(everything)) if re.search(f".*{searchName}.*", everything[i].Full_Name.lower())]


def get_employee_by_id(searchId):
    everything = Employee.all()
    return [everything[i] for i in range(len(everything)) if re.search(f".*{searchId}.*", str(everything[i]._id))]


def add_new_employee(full_name, store, address, pay):
    new_employee = Employee({
        "Full_Name": full_name,
        "Store": store,
        "Address": address,
        "Pay": pay
    })
    new_employee.save()


def update_employee(searchId, columnName, newValue="None"):
    old = Employee.find(**{"_id": ObjectId(searchId)}).first_or_none()
    updated = {
        "_id": old._id,
        "Full_Name": old.Full_Name,
        "Store": old.Store,
        "Address": old.Address,
        "Pay": old.Pay
    }
    # changes
    Employee(updated).save()


def delete_employee_by_id(searchId):
    Employee.delete(_id=ObjectId(searchId))
    return None

