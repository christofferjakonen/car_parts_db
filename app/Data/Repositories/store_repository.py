from bson import ObjectId
from app.Data.models.models import *


def get_all_stores():
    return Store.all()


def get_store_by_id(store_id):
    return Store.find(_id=ObjectId(store_id)).first_or_none()


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


def add_new_employee(store_id, employee):
    old = Store.find(_id=ObjectId(store_id)).first_or_none()
    store = {
        '_id': old._id,
        'Address': old.Address,
        'Employees': old.Employees
    }
    store['Employees'].append(employee)

    Store(store).save()


def store_edited_store_employee(store_id, employee_index, new_employee):
    old = Store.find(_id=ObjectId(store_id)).first_or_none()
    store = {
        '_id': old._id,
        'Address': old.Address,
        'Employees': old.Employees
    }

    store['Employees'][employee_index] = new_employee

    Store(store).save()

def store_edited_store_address(store_id, new_country, new_state, new_city, new_zip_code, new_street_address, new_phone_num):
    old = Store.find(_id=ObjectId(store_id)).first_or_none()
    store = {
        '_id': old._id,
        'Address': old.Address,
        'Employees': old.Employees
    }

    store['Address']['Country'] = new_country
    store['Address']['State'] = new_state
    store['Address']['City'] = new_city
    store['Address']['ZipCode'] = new_zip_code
    store['Address']['StreetAddress'] = new_street_address
    store['Address']['PhoneNumber'] = new_phone_num

    Store(store).save()


def delete_store(store_id):
    Store.delete(_id=ObjectId(store_id))


def delete_store_employee(store_id, employee_index):
    old = Store.find(_id=ObjectId(store_id)).first_or_none()
    store = {
        '_id': old._id,
        'Address': old.Address,
        'Employees': old.Employees
    }

    store['Employees'].pop(employee_index)
    Store(store).save()


