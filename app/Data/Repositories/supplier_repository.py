from bson import ObjectId
from app.Data.models.supplier_models import *


def get_all_suppliers():
    return Supplier.all()


def get_supplier_by_name(supplier_name):
    return Supplier.find(**{'SupplierName': supplier_name}).first_or_none()


def add_new_supplier(supplier, manufacturer_list, address_list, contact_list):
    supplier = Supplier({
        'SupplierName': supplier,
        'Parts': manufacturer_list,
        'Address': address_list,
        'ContactPerson': contact_list
    })

    supplier.save()


def create_new_contact_person(contact_name, phone_num, email):
    contact_person = {'FullName': contact_name, 'PhoneNumber': phone_num, 'Email': email}
    return contact_person


def add_new_contact_person(supplier_name, new_contact):
    old = Supplier.find(**{'SupplierName': supplier_name}).first_or_none()

    supplier = {
        '_id': old._id,
        'SupplierName': old.SupplierName,
        'Parts': old.Manufacturers,
        'Address': old.Address,
        'ContactPerson': old.ContactPerson
    }

    supplier['ContactPerson'].append(new_contact)
    Supplier(supplier).save()


def add_new_part(supplier_name, new_part):
    old = Supplier.find(**{'SupplierName': supplier_name}).first_or_none()

    supplier = {
        '_id': old._id,
        'SupplierName': old.SupplierName,
        'Parts': old.Manufacturers,
        'Address': old.Address,
        'ContactPerson': old.ContactPerson
    }

    supplier['Parts'].append(new_part)
    Supplier(supplier).save()


def create_new_supplier_address(country, state, city, zip_code, street_address, phone_num):
    address = {'Country': country, 'State': state, 'City': city, 'ZipCode': zip_code, 'StreetAddress': street_address, 'PhoneNumber': phone_num}
    return address


def add_new_supplier_address(supplier_name, new_address):
    old = Supplier.find(**{'SupplierName': supplier_name}).first_or_none()

    supplier = {
        '_id': old._id,
        'SupplierName': old.SupplierName,
        'Parts': old.Manufacturers,
        'Address': old.Address,
        'ContactPerson': old.ContactPerson
    }

    supplier['Address'].append(new_address)
    Supplier(supplier).save()


def store_edited_supplier_name(supplier_name, new_value):
    old = Supplier.find(**{'SupplierName': supplier_name}).first_or_none()

    supplier = {
        '_id': old._id,
        'SupplierName': old.SupplierName,
        'Parts': old.Manufacturers,
        'Address': old.Address,
        'ContactPerson': old.ContactPerson
    }

    supplier['SupplierName'] = new_value
    Supplier(supplier).save()


def store_edited_supplier_contact_person(supplier_name, new_contact, contact_index):
    old = Supplier.find(**{'SupplierName': supplier_name}).first_or_none()

    supplier = {
        '_id': old._id,
        'SupplierName': old.SupplierName,
        'Parts': old.Manufacturers,
        'Address': old.Address,
        'ContactPerson': old.ContactPerson
    }

    supplier['ContactPerson'][contact_index] = new_contact

    Supplier(supplier).save()


def store_edited_supplier_address(supplier_name, new_address, address_index):
    old = Supplier.find(**{'SupplierName': supplier_name}).first_or_none()

    supplier = {
        '_id': old._id,
        'SupplierName': old.SupplierName,
        'Parts': old.Manufacturers,
        'Address': old.Address,
        'ContactPerson': old.ContactPerson
    }

    supplier['Address'][address_index] = new_address

    Supplier(supplier).save()


def store_edited_supplier_part(supplier_name, new_part, part_index):
    old = Supplier.find(**{'SupplierName': supplier_name}).first_or_none()

    supplier = {
        '_id': old._id,
        'SupplierName': old.SupplierName,
        'Parts': old.Manufacturers,
        'Address': old.Address,
        'ContactPerson': old.ContactPerson
    }

    supplier['Manufacturers'][part_index] = new_part

    Supplier(supplier).save()


def delete_supplier(supplier_id):
    Supplier.delete(_id=ObjectId(supplier_id))


def delete_address(supplier_name, address_index):
    old = Supplier.find(**{'SupplierName': supplier_name}).first_or_none()

    supplier = {
        '_id': old._id,
        'SupplierName': old.SupplierName,
        'Parts': old.Manufacturers,
        'Address': old.Address,
        'ContactPerson': old.ContactPerson
    }

    supplier['Address'].pop(address_index)

    Supplier(supplier).save()


def delete_part(supplier_name, part_index):
    old = Supplier.find(**{'SupplierName': supplier_name}).first_or_none()

    supplier = {
        '_id': old._id,
        'SupplierName': old.SupplierName,
        'Parts': old.Manufacturers,
        'Address': old.Address,
        'ContactPerson': old.ContactPerson
    }

    supplier['Parts'].pop(part_index)

    Supplier(supplier).save()


def delete_contact_person(supplier_name, contact_index):
    old = Supplier.find(**{'SupplierName': supplier_name}).first_or_none()

    supplier = {
        '_id': old._id,
        'SupplierName': old.SupplierName,
        'Parts': old.Manufacturers,
        'Address': old.Address,
        'ContactPerson': old.ContactPerson
    }

    supplier['ContactPerson'].pop(contact_index)

    Supplier(supplier).save()
