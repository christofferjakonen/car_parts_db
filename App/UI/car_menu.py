from Controllers.car_controller import get_all_cars, get_car_by_brand, \
    store_new_car, delete_car, get_car_for_car_id
from Controllers.customers_controller import get_all_customers, get_customer_by_id


def car_menu():

    while True:
        print("Car Menu")
        print("==============")
        print("1. View All Cars")
        print("2. View Cars by Brand")
        print("3. View Car by CarID")
        print("4. Add new Car")
        print("5. Delete Car")
        print("6. View All Parts for Registration number")
        print("7. Quit Car Menu")

        selection = input("> ")

        if selection == "1":    #View all cars
            cars = get_all_cars()
            for car in cars:
                print(car)
                print('-------------------')

        elif selection == "2":  #View Cars by brand

            brand = input("Enter full or partial Car Brand: ")

            cars = get_car_by_brand(brand)
            if cars:
                for car in cars:
                    print('-------------------')
                    print(car)
            else:
                print("Could not find car with brand: ", brand)

        elif selection == "3":  #View Car by CarID
            cars = get_all_cars()
            for car in cars:
                print(car)
                print('-------------------')

            car_ids = input("Enter full or partial Car Id: ")
            car_by_ids = get_car_for_car_id(car_ids)

            if car_by_ids:
                for car_by_id in car_by_ids:
                    print(car_by_id)
            else:
                print("Found no car with that ID")


        elif selection == "4":  #Add new Car


            brand = input("Enter the brand of the car: ")
            model = input("Enter the model of the car: ")
            color = input("Enter the color of the car: ")
            modelYear = input("Enter the model_year of the car: ")
            store_new_car(brand, model, color, modelYear)

        elif selection == "5":  #Delete Car

            cars = get_all_cars()
            for car in cars:
                print(car)
                print('-------------------')
            car_id = input("Enter Registration number to be removed: ")
            delete_car(car_id)

        elif selection == "6":   #View All Parts for Registration number

            customers = get_all_customers()
            for customer in customers:
                print('-------------------')
                print(f' Customer Name: {customer.fullName} \n Customer ID: {customer._id}')

            cust_id = input("Enter whole or part of Customer ID of whose Registration number you want to use: ")
            one_customer = get_customer_by_id(cust_id)
            if one_customer:
                for i in one_customer:
                    for j in i.regNumbers:
                        print('-------------------')
                        print("\n".join("{}\t{}".format(k, v) for k, v in j.items()))

            else:
                print("Could not find customer with id ", cust_id)

            car_id = input("Enter whole or part of Car ID for Registration Number you want to se parts for: ")

            car = get_car_for_car_id(car_id)
            if car:
                for i in car:
                    if i.parts:
                        for j in i.parts:
                            print('-------------------')
                            print("\n".join("{}\t{}".format(k, v) for k, v in j.items()))
                    else:
                        print('-------------------')
                        print('No parts found for that car')
                        print('-------------------')

            else:
                print("Could not find Car with id: ", cust_id)

            #id = input(" for Car to view compatible parts: ")



            #parts = view_parts_for_reg_num(reg)

            #for i in range(len(parts)):
                #print(parts[i])

        elif selection == "7":  #Quit Car Menu
            break




