import Data.Repository.employee_reposistory as er
from bson import ObjectId


def get_all_employees():
    return er.get_all_employees()



def get_employee_by_name(searchName):
    return er.get_employee_by_name(searchName)


def get_employee_by_id(searchId):
    return er.get_employee_by_id(searchId)


def add_new_employee(full_name, country, state, city, zipnum, street, phone, store, pay):
    address = {
        "Country": country,
        "State": state,
        "City": city,
        "Zip_Number": zipnum,
        "Street_Address": street,
        "Phone_Number": phone
    }
    return er.add_new_employee(full_name, store, address, pay)


def update_employee(searchId, columnName, newValue, index=None):
    if columnName == "1":
        columnName = "Full_Name"
    elif columnName == "2":
        newValue = ObjectId(newValue)
        columnName = "Store"
    elif columnName == "3":
        columnName = "Address"
    elif columnName == "4":
        columnName = "Pay"
    return er.update_employee(searchId, columnName, newValue, index)


def delete_employee_by_id(searchId):
    return er.delete_employee_by_id(searchId)

