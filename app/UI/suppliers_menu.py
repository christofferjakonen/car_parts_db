from Controllers.supplier_controller import *


def suppliers_menu():
    while True:
        print("Suppliers Menu")
        print("--------------")
        print("1. View All Suppliers")
        print("2. Find Supplier By Name")
        print("3. Find Supplier By Phone Number")
        print("4. Find Supplier By Email")
        print("5. Add New Supplier")
        print("6. Edit A Supplier")
        print("7. Delete A Supplier")
        print("8. View All Parts Suppliers Have")
        print("9. View All Manufacturers For Suppliers")
        print("10. Exit Supplier Menu")

        choice = input("> ")

        if choice == "1":
            suppliers = get_all_suppliers()
            for supplier in suppliers:
                print(supplier)
                print("------------------------------")

        elif choice == "2":
            supplier_name = input("Enter name of supplier: ")
            supplier = get_supplier_by_name(supplier_name)
            print(supplier)

        elif choice == "3":
            phone_num = input("Enter phone number of supplier: ")
            suppliers = get_supplier_by_phone_number(phone_num)
            print(suppliers)

        elif choice == "4":
            email = input("Enter email of supplier: ")
            suppliers = get_supplier_by_email(email)
            print(suppliers)

        elif choice == "5":
            supplier_name = input("Name Of Supplier: ")

            manufacturer_list = []

            while True:
                manufacture = input("Manufacturer: ")
                manufacturer_list.append(manufacture)
                print("Do you want to add another manufacturer?")
                add_manufacturer = input("Yes or No: ")
                if add_manufacturer.lower() == "n" or add_manufacturer.lower() == "no":
                    break

            print("--Supplier Address--")
            country = input("Country: ")
            state = input("State: ")
            city = input("City: ")
            zip_code = input("Zip Code: ")
            street_address = input("Street Address: ")

            contact_list = []

            while True:
                print("--Contact Person--")
                contact_name = input("Name: ")
                phone_num = input("Phone Number: ")
                email = input("Email: ")
                contact = {"ContactPerson": contact_name, "Phone Number": phone_num, "Email": email}
                contact_list.append(contact)
                print("Do you want to add another contact person?")
                add_contact = input("Yes or No: ")
                if add_contact.lower() == "n" or add_contact.lower() == "no":
                    break

            add_new_supplier(supplier_name, manufacturer_list, country, state, city, zip_code, street_address, contact_list)

        elif choice == "6":
            suppliers = get_all_suppliers()
            for supplier in suppliers:
                print(supplier)
                print("------------------------------")

            print("1. Supplier")
            print("2. Manufacturer")
            print("3. Address")
            print("4. Contact Person")

            field = input("Enter number of the field you want to edit: ")

            if field == "1":
                new_value = input("Enter new supplier: ")
                store_edited_supplier_name(supplier, new_value)

            elif field == "2":
                while True:
                    new_value = input("Enter new manufacturer: ")
                    store_edited_supplier_manufacturer(supplier, new_value)
                    print("Do you want to edit another manufacturer?")
                    edit_manufacturer = input("Yes or No: ")
                    if edit_manufacturer.lower() == "n" or edit_manufacturer.lower() == "no":
                        break

            elif field == "3":
                print("What do you want to edit?")
                print("1. Country")
                print("2. State")
                print("3. City")
                print("4. Zip Code")
                print("5. Street Address")
                field_to_edit = input("> ")

                if field_to_edit == "1":
                    new_value = input("Enter new country: ")
                elif field_to_edit == "2":
                    new_value = input("Enter new state: ")
                elif field_to_edit == "3":
                    new_value = input("Enter new city: ")
                elif field_to_edit == "4":
                    new_value = input("Enter new zip code: ")
                elif field_to_edit == "5":
                    new_value = input("Enter new street address: ")

            elif field == "4":
                supplier_name = input("Enter supplier name: ")
                supplier = get_supplier_by_name(supplier_name)
                for i, contact in enumerate(supplier.ContactPerson, start=1):
                    print(f"{i}: {contact}")

                contact_index = input("What contact person do you want to edit: ")
                contact_index = int(contact_index) - 1
                contact_to_edit = supplier.ContactPerson[contact_index]

                new_name = input("Enter new contact person: ")
                new_phone = input("Enter new phone number: ")
                new_email = input("Enter new email: ")
                new_value = add_new_contact_person(new_name, new_phone, new_email)
                store_edited_supplier_contact_person(supplier_name, new_value, contact_index)

        elif choice == "7":
            suppliers = get_all_suppliers()
            for supplier in suppliers:
                print(supplier)
                print("------------------------------")
            name = input("Enter The Id Of Supplier You Want To Delete: ")
            delete_supplier(name)

        elif choice == "8":
            supplier_parts = get_all_supplier_parts()
            for part in supplier_parts:
                print(part)

        elif choice == "9":
            supplier_manufacturers = get_all_supplier_manufacturers()
            for manufacture in supplier_manufacturers:
                print(manufacture)

        elif choice == "10":
            break





