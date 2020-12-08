import Data.repository.car_repository as cr
import Data.repository.parts_repository as pr


def get_all_cars(): # View All Cars
    return cr.get_all_cars()


def get_car_by_brand(brand):  # View Car by brand
    return cr.get_car_by_brand(brand)


def store_new_car(brand, model, color, model_year):     # Add new Car
    cr.store_new_car(brand, model, color, model_year)


def delete_car(id): # Delete Car
    return cr.delete_car(id)


def view_parts_for_reg_num(reg):    # View All Parts for Registration number
    return cr.view_parts_for_reg_num(reg)


def get_car_for_car_id(car_id):     # View parts for reg number
    return cr.get_car_for_car_id(car_id)










