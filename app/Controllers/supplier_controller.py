import Data.Repositories.supplier_repository as sr

# suppliers


def get_all_suppliers():
    return sr.get_all_suppliers()


def add_new_supplier(supplier_name, manufacturer_list, country, state, city, zip_code, street_address, contact_list):
    return sr.add_new_supplier(supplier_name, manufacturer_list, country, state, city, zip_code, street_address, contact_list)


def add_new_contact_person(contact_name, phone_num, email):
    return sr.add_new_contact_person(contact_name, phone_num, email)


def delete_supplier(supplier_name):
    sr.delete_supplier(supplier_name)


def get_supplier_by_name(supplier_name):
    return sr.get_supplier_by_name(supplier_name)


def get_supplier_by_phone_number(phone_num):
    return sr.get_supplier_by_phone_number(phone_num)


def get_supplier_by_email(email):
    return sr.get_supplier_by_email(email)


def store_edited_supplier_name(supplier, new_value):
    sr.store_edited_supplier_name(supplier, new_value)


def store_edited_supplier_phone(supplier, new_value):
    sr.store_edited_supplier_phone(supplier, new_value)


def store_edited_supplier_email(supplier, new_value):
    sr.store_edited_supplier_email(supplier, new_value)


def store_edited_supplier_contact_person(supplier_name, new_value, contact_index):
    return sr.store_edited_supplier_contact_person(supplier_name, new_value, contact_index)

