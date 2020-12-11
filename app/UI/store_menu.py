from Controllers.store_controller import *


def store_menu():
    while True:
        print("1. Get All Stores")
        print("2. Add New Store")
        print("3. Add New Employees To A Store")
        print("4. Edit An Address")
        print("5. Edit An Employee")
        print("6. Delete A Store")
        print("7. Delete An Employee")
        print("8. Quit Store Menu")

        choice = input("> ")

        if choice == "1":
            stores = get_all_stores()
            for store in stores:
                print(store)

        elif choice == "2":
            print("--Address--")
            country = input("Country: ")
            state = input("State: ")
            city = input("City: ")
            zip_code = input("Zip Code: ")
            street_address = input("Street Address: ")
            phone_num = input("Phone Number: ")

            print("--Employees--")
            employee_list = []
            while True:
                employee_name = input("Employee Name: ")
                employee_list.append(employee_name)
                print("Do you want to add another employee?")
                add_employee = input("Yes or No: ")

                if add_employee.lower() == "n" or add_employee.lower() == "no":
                    break

            create_new_store(country, state, city, zip_code, street_address, phone_num, employee_list)

        elif choice == "3":
            stores = get_all_stores()
            for store in stores:
                print(store)
            store_id = input("Enter the id of the store: ")
            employee = input("Enter name of new employee: ")

            add_new_employee(store_id, employee)

        elif choice == "4":
            stores = get_all_stores()
            for store in stores:
                print(store)

            store_id = input("Enter the id of the store you want to delete employee for: ")

            store = get_store_by_id(store_id)
            for i, address in enumerate(store.Address, start=1):
                print(f"{i}: {address}")

            address_index = input("What address do you want to edit: ")
            address_index = int(address_index) - 1

            new_name = input("Enter contact person: ")
            new_phone = input("Enter phone number: ")
            new_email = input("Enter email: ")
            new_contact = create_new_contact_person(new_name, new_phone, new_email)
            store_edited_supplier_contact_person(supplier_name, new_contact, address_index)

            print("Do you want to edit another contact?")
            edit_contact = input("Yes or No: ")
            if edit_contact.lower() == "n" or edit_contact.lower() == "no":
                break

        elif choice == "6":
            stores = get_all_stores()
            for store in stores:
                print(store)

            store_id = input("Enter id of store to delete: ")

            delete_store(store_id)

        elif choice == "7":
            stores = get_all_stores()
            for store in stores:
                print(store)

            store_id = input("Enter the id of the store you want to delete employee for: ")

            store = get_store_by_id(store_id)
            for i, employee in enumerate(store.Employees, start=1):
                print(f"{i}: {employee}")

            address_index = input("Which employee do you want to delete: ")
            address_index = int(address_index) - 1

            delete_store_employee(store_id, address_index)

        elif choice == "8":
            break
