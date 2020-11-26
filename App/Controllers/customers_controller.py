import Data.repository.customer_repository as cr


def get_all_customers():
    return cr.get_all_customers()


def get_all_reg_numbers():
    return cr.get_all_reg_numbers()


def get_customer_by_id(id):
    return cr.get_customer_by_id(id)


def get_customer_by_name(pattern):
    customers = cr.get_customer_by_name(pattern)
    return {i+1: customer for i, customer in enumerate(customers)}


def store_changes():
    cr.store_changes()


def store_new_customer(new_name):
    cr.store_new_customer(new_name)


def delete_customer(id):
    return cr.delete_customer(id)


def change_name(old_name, name):
    return cr.change_name(old_name, name)


def add_car_to_customer(cust_id, reg_num, car_id):
    return cr.add_car_to_customer(cust_id, reg_num, car_id)


def delete_reg_num(reg_num):
    return cr.delete_reg_num(reg_num)


def get_reg_number_for_customer(id):
    return cr.get_reg_number_for_customer(id)
