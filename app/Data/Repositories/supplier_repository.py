from bson import ObjectId
from app.Data.models.supplier_models import *


def get_all_suppliers():
    return Supplier.all()


def add_new_supplier(supplier, manufacturer_list, country, state, city, zip_code, street_address, contact_list):
    supplier = Supplier({
        'SupplierName': supplier,
        'Manufacturers': manufacturer_list,
        'Address': {'Country': country,
                    'State': state,
                    'City': city,
                    'ZipCode': zip_code,
                    'StreetAddress': street_address},
        'ContactPerson': contact_list
    })

    supplier.save()


def add_new_contact_person(contact_name, phone_num, email):
    contact_person = {'FullName': contact_name, 'PhoneNumber': phone_num, 'Email': email}
    return contact_person

def delete_supplier(supplier_id):
    Supplier.delete(_id=ObjectId(supplier_id))


def get_supplier_by_name(supplier_name):
    return Supplier.find(**{'SupplierName': supplier_name}).first_or_none()


def get_supplier_contact_person(contact_name):
    return Supplier.find(**{'ContactPerson': contact_name}).first_or_none()


def get_supplier_by_phone_number(phone_num):
    return Supplier.find(**{'PhoneNumber': phone_num}).first_or_none()


def get_supplier_by_email(email):
    return Supplier.find(**{'Email': email}).first_or_none()


def store_edited_supplier_name(supplier_name, new_value):
    old = Supplier.find(**{'SupplierName': supplier_name}).first_or_none()

    supplier = {
        '_id': old._id,
        'SupplierName': old.SupplierName,
        'Manufacturers': old.Manufacturers,
        'Address': old.Address,
        'ContactPerson': old.ContactPerson
    }


def store_edited_supplier_phone(supplier, new_value):
    pass


def store_edited_supplier_email(supplier, new_value):
    pass


def store_edited_supplier_contact_person(supplier_name, new_value, contact_index):
    old = Supplier.find(**{'SupplierName': supplier_name}).first_or_none()

    supplier = {
        '_id': old._id,
        'SupplierName': old.SupplierName,
        'Manufacturers': old.Manufacturers,
        'Address': old.Address,
        'ContactPerson': old.ContactPerson
    }

    supplier['ContactPerson'][contact_index] = new_value

    Supplier(supplier).save()
