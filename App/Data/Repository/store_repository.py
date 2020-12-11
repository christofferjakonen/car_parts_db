from bson import ObjectId
from Data.models.models import *


def get_all_stores():
    return Store.all()


def create_new_store(country, state, city, zip_code, street_address, phone_num, employee_list):
    store = Store({
        'Address': {
            'Country': country,
            'State': state,
            'City': city,
            'ZipCode': zip_code,
            'StreetAddress': street_address,
            'PhoneNumber': phone_num
        },
        'Employees': employee_list
    })

    store.save()