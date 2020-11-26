from Controllers.supplier_controller import *


def supplier_address_menu():
    while True:
        print("Supplier Addresses Menu")
        print("--------------")
        print("1. View All Supplier Addresses")
        print("2. Find Supplier Address By Name")
        print("3. Find Supplier Address By Country")
        print("4. Find Supplier Address By City")
        print("5. Find Supplier Address By State")
        print("6. Find Supplier Address By Zip Code")
        print("7. Find Supplier Address By Street Address")
        print("8. Add New Address")
        print("9. Edit An Address")
        print("10. Delete An Address")
        print("11. Exit Supplier Addresses Menu")

        choice = input("> ")

        if choice == "1":
            addresses = get_all_supplier_addresses()
            for address in addresses:
                print(address)

        elif choice == "3":
            country = input("Enter Country: ")
            supplier_country = get_supplier_address_by_country(country)
            for key, supplier_country in supplier_country.items():
                print(f"{key}. {supplier_country}")

        elif choice == "4":
            city = input("Enter City: ")
            supplier_address = get_supplier_address_by_city(city)
            for key, supplier_address in supplier_address.items():
                print(f"{key}. {supplier_address}")

        elif choice == "5":
            state = input("Enter State: ")
            supplier_address = get_supplier_address_by_state(state)
            for key, supplier_address in supplier_address.items():
                print(f"{key}. {supplier_address}")

        elif choice == "6":
            zip_code = input("Enter Zip Code: ")
            zip_code = int(zip_code)
            supplier_address = get_supplier_address_by_zip_code(zip_code)
            print(supplier_address)
            for key, supplier_address in supplier_address.items():
                print(f"{key}. {supplier_address}")

        elif choice == "7":
            street_address = input("Enter Street Address: ")
            supplier_address = get_supplier_address_by_street_address(street_address)
            for key, supplier_address in supplier_address.items():
                print(f"{key}. {supplier_address}")

        elif choice == "8":
            pass

        elif choice == "9":
            supplier_addresses = get_all_supplier_addresses()
            for supplier_address in supplier_addresses:
                print(supplier_address)

            name = input("Enter Supplier You Want To Edit Address For: ")
            supplier_addresses = get_supplier_address_by_name(name)

            for key, supplier_address in supplier_addresses.items():
                print(f"{key}. {supplier_address}")

            edit = input("Enter number for address you want to edit: ")
            edit = int(edit)

            supplier_address = supplier_addresses[edit]

            print("1. Supplier Name:", supplier_address.Supplier)
            print("2. Country:", supplier_address.Country)
            print("3. State:", supplier_address.State)
            print("4. City:", supplier_address.City)
            print("5. Zip Code:", supplier_address.ZipCode)
            print("6. Street Address:", supplier_address.StreetAddress)
            column = input("Enter number of the column you want to edit: ")
            if column == "1":
                new_value = input("Enter new supplier name: ")
                store_edited_supplier_address_name(supplier_address, new_value)
            elif column == "2":
                new_value = input("Enter new country: ")
                store_edited_supplier_address_country(supplier_address, new_value)
            elif column == "3":
                new_value = input("Enter new state: ")
                store_edited_supplier_address_state(supplier_address, new_value)
            elif column == "4":
                new_value = input("Enter new city: ")
                store_edited_supplier_address_city(supplier_address, new_value)
            elif column == "5":
                new_value = input("Enter new zip code: ")
                store_edited_supplier_address_zip_code(supplier_address, new_value)
            elif column == "6":
                new_value = input("Enter new street address: ")
                store_edited_supplier_address_street_address(supplier_address, new_value)

        elif choice == "10":
            addresses = get_all_supplier_addresses()
            for address in addresses:
                print(address)
            supplier_name = input("Enter Supplier You Want To Delete An Address For: ")
            delete_supplier_address(supplier_name)

        elif choice == "11":
            break
