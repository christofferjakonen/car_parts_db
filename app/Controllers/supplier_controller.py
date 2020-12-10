import Data.Repositories.supplier_repository as sr


def get_all_suppliers():
    return sr.get_all_suppliers()


def get_supplier_by_name(supplier_name):
    return sr.get_supplier_by_name(supplier_name)


def add_new_supplier(supplier_name, manufacturer_list, address_list, contact_list):
    sr.add_new_supplier(supplier_name, manufacturer_list, address_list, contact_list)


def add_new_contact_person(supplier_name, new_contact):
    sr.add_new_contact_person(supplier_name, new_contact)


def create_new_contact_person(contact_name, phone_num, email):
    return sr.create_new_contact_person(contact_name, phone_num, email)


def create_new_supplier_address(country, state, city, zip_code, street_address, phone_num):
    return sr.create_new_supplier_address(country, state, city, zip_code, street_address, phone_num)


def add_new_supplier_address(supplier_name, new_address):
    sr.add_new_supplier_address(supplier_name, new_address)


def add_new_part(supplier_name, new_part):
    sr.add_new_part(supplier_name, new_part)


def delete_supplier(supplier_name):
    sr.delete_supplier(supplier_name)


def store_edited_supplier_name(supplier_name, new_value):
    sr.store_edited_supplier_name(supplier_name, new_value)


def store_edited_supplier_contact_person(supplier_name, new_contact, contact_index):
    sr.store_edited_supplier_contact_person(supplier_name, new_contact, contact_index)


def store_edited_supplier_address(supplier_name, new_address, address_index):
    sr.store_edited_supplier_address(supplier_name, new_address, address_index)


def store_edited_supplier_part(supplier_name, new_part, part_index):
    sr.store_edited_supplier_part(supplier_name, new_part, part_index)


def delete_address(supplier_name, address_index):
    sr.delete_address(supplier_name, address_index)


def delete_part(supplier_name, part_index):
    sr.delete_part(supplier_name, part_index)


def delete_contact_person(supplier_name, contact_index):
    sr.delete_contact_person(supplier_name, contact_index)
