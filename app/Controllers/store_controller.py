import Data.Repositories.store_repository as sr


def get_all_stores():
    return sr.get_all_stores()


def get_store_by_id(store_id):
    return sr.get_store_by_id(store_id)


def create_new_store(country, state, city, zip_code, street_address, phone_num, employee_list):
    sr.create_new_store(country, state, city, zip_code, street_address, phone_num, employee_list)


def add_new_employee(store_id, employee):
    sr.add_new_employee(store_id, employee)


def store_edited_store_address():
    sr.store_edited_store_address()


def store_edited_store_employee():
    sr.store_edited_store_employee()


def delete_store(store_id):
    sr.delete_store(store_id)


def delete_store_employee(store_id, employee_index):
    sr.delete_store_employee(store_id, employee_index)
