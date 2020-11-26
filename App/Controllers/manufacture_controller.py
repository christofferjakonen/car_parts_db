import Data.Repository.manufacture_repository as mr

def get_all_manufacturers():
    return mr.get_all_manufacturers()

def add_new_manufacturer(manufacturer, country="None", state="None", city="None", zipnum=1, address="None", phone="None"):
    return mr.add_new_manufacturer(manufacturer, country, state, city, zipnum, address, phone)

def update_manufacturer():
    return mr.update_