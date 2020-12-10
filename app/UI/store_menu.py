from Controllers.store_controller import *


def store_menu():
    print("1. Get All Store Info")
    print("2. Add New Store")

    choice = input("> ")

    if choice == "1":
        stores = get_all_stores()
        for store in stores:
            print(store)
            print("------------------------------")

    elif choice == "2":
        print("--Address--")
        country = input("Country: ")
        state = input("State: ")
        city = input("City: ")
        zip_code = input("Zip Code: ")
        street_address = input("Street Address: ")
        phone_num = input("Phone Number: ")

        employee_list = []
        while True:
            employee_name = input("Employee Name: ")
            employee_list.append(employee_name)
            print("Do you want to add another employee?")
            add_employee = input("Yes or No: ")

            if add_employee.lower() == "n" or add_employee.lower() == "no":
                break
        
        create_new_store(country, state, city, zip_code, street_address, phone_num, employee_list)
