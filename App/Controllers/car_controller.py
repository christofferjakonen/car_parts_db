import Data.repository.car_repository as cr
import Data.repository.part_repository as pr


def get_all_cars():     # View All Cars
    return cr.get_all_cars()


def get_car_by_brand(brand):  # View Car by brand
    return cr.get_car_by_brand(brand)


def store_new_car(brand, model, color, model_year):     # Add new Car
    cr.store_new_car(brand, model, color, model_year)


def delete_car(car_id):     # Delete Car
    return cr.delete_car(car_id)


def get_car_for_car_id(car_id):     # View parts for reg number
    return cr.get_car_for_car_id(car_id)


def add_part_to_car(car_id, part_id):   # Add par to car
    return cr.add_part_to_car(car_id, part_id)


def simple_car_find(car_id):    # a simpler car find
    return cr.simple_car_find(car_id)


def simple_car_by_reg_num(reg_num):     # a simpler find car by registration number
    return cr.simple_car_by_reg_num(reg_num)



