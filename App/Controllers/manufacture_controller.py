import Data.Repository.manufacture_repository as mr

def get_all_manufacturers():
    return mr.get_all_manufacturers()

def add_new_manufacturer(manufacturer, country="None", state="None", city="None", zipnum=1, address="None", phone="None"):
    return mr.add_new_manufacturer(manufacturer, country, state, city, zipnum, address, phone)

def update_manufacturer(searchId, searchColumn, newValue, index=None):
    if searchColumn == "1":
        searchColumn = "Manufacturer"
    elif searchColumn == "2":
        searchColumn = "Address"
    elif searchColumn == "3":
        searchColumn = "ContactNew"
    elif searchColumn == "4":
        searchColumn = "ContactEdit"
    return mr.update_manufacturer(searchId, searchColumn, newValue, index)

def get_manufacturer_by_name(search):
    return mr.get_manufacturer_by_name(search)

def get_manufacturer_by_id(search):
    manufacturer = mr.get_manufacturer_by_id(search)
    return manufacturer if manufacturer else ["No manufacturer was found"]

def delete_manufacturer_by_id(searchId):
    return mr.delete_manufacturer_by_id(searchId)