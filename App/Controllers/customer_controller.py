import Data.repository.customer_repository as cr

def simple_customer_find(cust_id):
    return cr.simple_customer_find(cust_id)

def get_all_customers():
    return cr.get_all_customers()


def get_customer_by_id(cust_id):
    return cr.get_customer_by_id(cust_id)


def get_customer_by_name(pattern):
    customers = cr.get_customer_by_name(pattern)
    return customers


def store_new_customer(name, phone_number, email, contact_person):
    cr.store_new_customer(name, phone_number, email, contact_person)


def delete_customer(cust_id):
    return cr.delete_customer(cust_id)


def add_car_to_customer(cust_id, reg_num, car_id):
    return cr.add_car_to_customer(cust_id, reg_num, car_id)


def delete_reg_num(cust_nr, reg_nr):
    return cr.delete_reg_num(cust_nr, reg_nr)


def get_reg_number_for_customer(cust_id):
    return cr.get_reg_number_for_customer(cust_id)
