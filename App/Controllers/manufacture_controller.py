import Data.Repository.manufacture_repository as mr

def get_all_manufacturers():
    return mr.get_all_manufacturers()

def add_new_manufacturer(manufacturer, country="None", state="None", city="None", zip=1, address="None", phone="None"):
    return mr.add_new_manufacturer(manufacturer, country, state, city, zip, address, phone)