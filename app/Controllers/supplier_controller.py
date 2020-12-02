import Data.Repositories.supplier_repository as sr

# suppliers


def get_all_suppliers():
    return sr.get_all_suppliers()


def add_new_supplier(supplier_name, phone_num, email):
    return sr.add_new_supplier(supplier_name, phone_num, email)


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


# supplier contacts


def get_all_supplier_contact_people():
    return sr.get_all_supplier_contact_people()


def get_supplier_contact_person_by_name(name):
    people = sr.get_supplier_contact_person_by_name(name)
    return {i+1: person for i, person in enumerate(people)}


def get_supplier_contact_person_by_supplier(supplier):
    return sr.get_supplier_contact_person_by_supplier(supplier)



def get_supplier_contact_person_by_phone_number(phone_num):
    return sr.get_supplier_contact_person_by_phone_number(phone_num)



def get_supplier_contact_person_by_email(email):
    return sr.get_supplier_contact_person_by_email(email)


def add_new_supplier_contact(supplier_name, contact_name, phone_num, email):
    return sr.add_new_supplier_contact(supplier_name, contact_name, phone_num, email)


def delete_supplier_contact_person(contact_name):
    return sr.delete_supplier_contact_person(contact_name)


# supplier addresses


def get_all_supplier_addresses():
    return sr.get_all_supplier_addresses()


def get_supplier_address_by_id(address_id):
    return sr.get_supplier_address_by_id(address_id)


def get_supplier_address_by_name(supplier_name):
    addresses = sr.get_supplier_address_by_name(supplier_name)
    return {i+1: address for i, address in enumerate(addresses)}


def get_supplier_address_by_country(country):
    return sr.get_supplier_address_by_country(country)



def get_supplier_address_by_city(city):
    return sr.get_supplier_address_by_city(city)



def get_supplier_address_by_state(state):
    return sr.get_supplier_address_by_state(state)



def get_supplier_address_by_zip_code(zip_code):
    return sr.get_supplier_address_by_zip_code(zip_code)



def get_supplier_address_by_street_address(street_address):
    return sr.get_supplier_address_by_street_address(street_address)



def store_edited_supplier_address_name(supplier_name, new_value):
    sr.store_edited_supplier_address_name(supplier_name, new_value)


def store_edited_supplier_address_country(supplier_address, new_value):
    sr.store_edited_supplier_address_country(supplier_address, new_value)


def store_edited_supplier_address_state(supplier_address, new_value):
    sr.store_edited_supplier_address_state(supplier_address, new_value)


def store_edited_supplier_address_city(supplier_address, new_value):
    sr.store_edited_supplier_address_city(supplier_address, new_value)


def store_edited_supplier_address_zip_code(supplier_address, new_value):
    sr.store_edited_supplier_address_zip_code(supplier_address, new_value)


def store_edited_supplier_address_street_address(supplier_address, new_value):
    sr.store_edited_supplier_address_street_address(supplier_address, new_value)


def delete_supplier_address(supplier_name):
    sr.delete_supplier_address(supplier_name)



# manufacturers


def get_all_supplier_manufacturers():
    return sr.get_all_supplier_manufacturers()


# parts


def get_all_supplier_parts():
    return sr.get_all_supplier_parts()


def delete_supplier_parts():
    return sr.delete_supplier_parts()
