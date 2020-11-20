import Data.repository.car_repository as cr


def get_all_customers():
    return cr.get_all_cars()


def get_all_reg_numbers():
    return cr.get_all_reg_numbers()


def get_customer_by_id(id):
    return cr.get_car_by_id(id)


def store_changes():
    cr.store_changes()


def store_new_first_name(customer, new_value):
    cr.store_new_first_name(customer, new_value)