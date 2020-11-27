from Controllers.car_controller import get_reg_number_for_car, get_all_cars, get_car_by_id, store_changes, \
    store_new_car, delete_car, view_parts_for_car_id
from Controllers.customers_controller import get_customer_by_id


def car_menu():

    while True:
        print("Car Menu")
        print("==============")
        print("1. View All Cars")
        print("2. View Attributes of Car ID")
        print("3. View Registration number and Customer for CarID")
        print("4. Add new Car")
        print("5. Delete Car")
        print("6. View All Parts for CarID")
        print("7. Quit Car Menu")

        selection = input("> ")

        if selection == "1":
            cars = get_all_cars()
            for car in cars:
                print(car)

        elif selection == "2":
            id = input("Enter Car Id: ")
            cars = get_car_by_id(id)
            if cars:
                for car in cars:
                    print(car)
            else:
                print("Could not find car with id: ", id)


        elif selection == "3":
            id = input("Enter Car Id: ")
            reg_number = get_reg_number_for_car(id)

            for i in range(len(reg_number[0])):
                print(f"Registration number: {reg_number[0][i][0]}, Customer ID: {reg_number[1][i][0]}\n")

        elif selection == "4":


            brand = input("Enter the brand of the car: ")
            model = input("Enter the model of the car: ")
            color = input("Enter the color of the car: ")
            model_year = input("Enter the model_year of the car: ")
            store_new_car(model, brand, color, model_year)

        elif selection == "5":

            id = int(input("Enter Car Id to be removed: "))
            delete_car(id)

        elif selection == "6":

            id = int(input("Enter ID for Car to view compatible parts"))
            parts = view_parts_for_car_id(id)

            for i in range(len(parts)):
                print(parts[i])

        elif selection == "7":
            break




