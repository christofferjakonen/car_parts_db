import Data.Repository.employee_reposistory as er


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


def update_employee(searchId, columnName, newValue):
    pass