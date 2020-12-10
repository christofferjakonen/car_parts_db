import Data.Repositories.store_repository as sr


def get_all_stores():
    return sr.get_all_stores()


def create_new_store(country, state, city, zip_code, street_address, phone_num, employee_list):
    sr.create_new_store(country, state, city, zip_code, street_address, phone_num, employee_list)


def add_new_employee():
    sr.add_new_employee()


def store_edited_store_address():
    sr.store_edited_address()


def store_edited_store_employee():
    sr.store_edited_store_employee()


def delete_store_address():
    sr.delete_store_address()


def delete_store_employee():
    sr.delete_store_employee()
