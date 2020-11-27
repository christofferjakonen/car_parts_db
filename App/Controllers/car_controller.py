import Data.repository.car_repository as cr
import Data.repository.parts_repository as pr

def get_all_cars():
    return cr.get_all_cars()


def get_reg_number_for_car(id):
    reg_num = cr.get_reg_number_for_car(id)

    return reg_num


def view_parts_for_car_id(id):
    car_id_part = cr.view_parts_for_car_id(id)

    car_parts = []
    for i in range(len(car_id_part)):
        car_parts.append(pr.get_part_by_id(car_id_part[i][0]))

    return car_parts


def get_car_by_id(id):
    return cr.get_car_by_id(id)


def store_changes():
    cr.store_changes()


def store_new_car(brand, model, color, model_year):
    cr.store_new_car(brand, model, color, model_year)


def delete_car(id):
    return cr.delete_car(id)

