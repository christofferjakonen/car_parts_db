from bson import ObjectId
from app.Data.models.supplier_models import *


# supplier


def get_all_suppliers():
    return Supplier.all()


def add_new_supplier(supplier, phone_num, email):
    supplier = Supplier({
        'SupplierName': supplier,
        'PhoneNumber': phone_num,
        'Email': email
    })

    supplier.save()


def delete_supplier(supplier_id):
    Supplier.delete(_id=ObjectId(supplier_id))


def get_supplier_by_name(supplier_name):
    return Supplier.find(**{'SupplierName': supplier_name}).first_or_none()


def get_supplier_by_phone_number(phone_num):
    return Supplier.find(**{'PhoneNumber': phone_num}).first_or_none()


def get_supplier_by_email(email):
    return Supplier.find(**{'Email': email}).first_or_none()


def store_edited_supplier_name(supplier, new_value):
    pass


def store_edited_supplier_phone(supplier, new_value):
    pass


def store_edited_supplier_email(supplier, new_value):
    pass


# contacts


def get_all_supplier_contact_people():
    return SupplierContactPerson.all()


def get_supplier_contact_person_by_name(contact_person):
    return SupplierContactPerson.find(**{'FullName': contact_person}).first_or_none()


def get_supplier_contact_person_by_phone_number(phone_num):
    return SupplierContactPerson.find(**{'PhoneNumber': phone_num}).first_or_none()


def get_supplier_contact_person_by_email(email):
    return SupplierContactPerson.find(**{'Email': email}).first_or_none()


def get_supplier_contact_person_by_supplier(supplier):
    return SupplierContactPerson.find(**{'Supplier': supplier}).first_or_none()


def add_new_supplier_contact(supplier, contact_name, phone_num, email):
    contact = SupplierContactPerson({
        'Supplier': supplier,
        'FullName': contact_name,
        'PhoneNumber': phone_num,
        'Email': email
    })

    contact.save()
    print("Done")


def delete_supplier_contact_person(contact_id):
    SupplierContactPerson.delete(_id=ObjectId(contact_id))


def store_edited_supplier_contact_supplier(supplier_name, new_value):
    supplier = {"Supplier": supplier_name}
    new_supplier = {"$set": {"Supplier": new_value}}

    mdb.SupplierContactPerson.update(supplier, new_supplier)


def store_edited_supplier_contact_person(contact_name, new_value):
    pass


def store_edited_supplier_contact_phone_number(phone_num, new_value):
    pass


def store_edited_supplier_contact_email(email, new_value):
    pass


# addresses


def get_all_supplier_addresses():
    return SupplierAddress.all()


def get_supplier_address_by_name(supplier_name):
    supplier = Supplier.find(**{'SupplierName': supplier_name}).first_or_none()
    return supplier


def get_supplier_address_by_id(address_id):
    supplier = Supplier.find(**{'SupplierName': address_id}).first_or_none()
    return supplier


def get_supplier_address_by_country(country):
    supplier = Supplier.find(**{'SupplierName': country}).first_or_none()
    return supplier


def get_supplier_address_by_city(city):
    supplier = Supplier.find(**{'SupplierName': city}).first_or_none()
    return supplier


def get_supplier_address_by_state(state):
    supplier = Supplier.find(**{'SupplierName': state}).first_or_none()
    return supplier


def get_supplier_address_by_zip_code(zip_code):
    supplier = Supplier.find(**{'SupplierName': zip_code}).first_or_none()
    return supplier


def get_supplier_address_by_street_address(street_address):
    supplier = Supplier.find(**{'SupplierName': street_address}).first_or_none()
    return supplier


def add_new_supplier_address(supplier, country, state, city, zip_code, street_address):
    address = SupplierAddress({
        'Supplier': supplier,
        'Country': country,
        'State': state,
        'City': city,
        'ZipCode': zip_code,
        'StreetAddress': street_address
    })

    address.save()
    print("Done")


def store_edited_supplier_address_name(supplier_address, new_value):
    pass


def store_edited_supplier_address_country(supplier_address, new_value):
    pass


def store_edited_supplier_address_state(supplier_address, new_value):
    pass


def store_edited_supplier_address_city(supplier_address, new_value):
    pass


def store_edited_supplier_address_zip_code(supplier_address, new_value):
    pass


def store_edited_supplier_address_street_address(supplier_address, new_value):
    pass


def delete_supplier_address(address_id):
    SupplierAddress.delete(_id=ObjectId(address_id))


# manufacturers


def get_all_supplier_manufacturers():
    return SupplierHasManufacturer.all()


# parts


def get_all_supplier_parts():
    return SupplierHasPart.all()
