from Controllers.supplier_controller import *


def suppliers_menu():
    while True:
        print("Suppliers Menu")
        print("--------------")
        print("1. View All Suppliers")
        print("2. Find Supplier By Name")
        print("3. Add New Supplier")
        print("4. Add A Part")
        print("5. Add An Address")
        print("6. Add A Contact Person")
        print("7. Edit A Supplier")
        print("8. Delete A Supplier")
        print("9. Delete A Part")
        print("10. Delete An Address")
        print("11. Delete A Contact Person")
        print("12. Exit Supplier Menu")

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
            supplier_name = input("Name Of Supplier: ")

            part_list = []

            while True:
                part = input("Part Id: ")
                part_list.append(part)
                print("Do you want to add another part?")
                add_part = input("Yes or No: ")
                if add_part.lower() == "n" or add_part.lower() == "no":
                    break

            address_list = []
            print("--Supplier Address--")
            while True:
                country = input("Country: ")
                state = input("State: ")
                city = input("City: ")
                zip_code = input("Zip Code: ")
                street_address = input("Street Address: ")
                phone_num = input("Phone Number: ")
                address = create_new_supplier_address(country, state, city, zip_code, street_address, phone_num)
                address_list.append(address)
                print("Do you want to add another address?")
                add_address = input("Yes or No: ")
                if add_address.lower() == "n" or add_address.lower() == "no":
                    break

            contact_list = []
            print("--Contact Person--")
            while True:
                contact_name = input("Name: ")
                phone_num = input("Phone Number: ")
                email = input("Email: ")
                contact = create_new_contact_person(contact_name, phone_num, email)
                contact_list.append(contact)
                print("Do you want to add another contact person?")
                add_contact = input("Yes or No: ")
                if add_contact.lower() == "n" or add_contact.lower() == "no":
                    break

            add_new_supplier(supplier_name, part_list, address_list, contact_list)

        elif choice == "4":
            suppliers = get_all_suppliers()
            for supplier in suppliers:
                print(supplier)
                print("------------------------------")

            supplier_name = input("Enter supplier you want to add a part for: ")

            new_part = input("Part Id: ")
            add_new_part(supplier_name, new_part)

            #print("Do you want to add another part?")
            #add_part = input("Yes or No: ")
            #if add_part.lower() == "n" or add_part.lower() == "no":
                #break

        elif choice == "5":
            suppliers = get_all_suppliers()
            for supplier in suppliers:
                print(supplier)
                print("------------------------------")

            supplier_name = input("Enter supplier you want to add an address for: ")

            while True:
                country = input("Country: ")
                state = input("State: ")
                city = input("City: ")
                zip_code = input("Zip Code: ")
                street_address = input("Street Address: ")
                phone_num = input("Phone Number: ")

                new_address = create_new_supplier_address(country, state, city, zip_code, street_address, phone_num)
                add_new_supplier_address(supplier_name, new_address)

                print("Do you want to add another address?")
                add_address = input("Yes or No: ")
                if add_address.lower() == "n" or add_address.lower() == "no":
                    break

        elif choice == "6":
            suppliers = get_all_suppliers()
            for supplier in suppliers:
                print(supplier)
                print("------------------------------")

            supplier_name = input("Enter supplier you want to add a contact person for: ")

            while True:
                contact_name = input("Name: ")
                phone_num = input("Phone Number: ")
                email = input("Email: ")

                new_contact = create_new_contact_person(contact_name, phone_num, email)
                add_new_contact_person(supplier_name, new_contact)

                print("Do you want to add another contact person?")
                add_contact = input("Yes or No: ")
                if add_contact.lower() == "n" or add_contact.lower() == "no":
                    break

        elif choice == "7":
            suppliers = get_all_suppliers()
            for supplier in suppliers:
                print(supplier)
                print("------------------------------")

            print("1. Supplier")
            print("2. Part")
            print("3. Address")
            print("4. Contact Person")

            field = input("Enter number of the field you want to edit: ")

            if field == "1":
                supplier_name = input("Enter name of supplier you want to edit: ")
                new_contact = input("Enter new supplier: ")
                store_edited_supplier_name(supplier_name, new_contact)

            elif field == "2":
                while True:
                    supplier_name = input("Enter supplier to edit: ")
                    supplier = get_supplier_by_name(supplier_name)
                    for i, part in enumerate(supplier.Parts, start=1):
                        print(f"{i}: {part}")

                    part_index = input("What part do you want to edit: ")
                    part_index = int(part_index) - 1

                    new_part = input("Enter new part: ")
                    store_edited_supplier_part(supplier_name, new_part, part_index)

                    print("Do you want to edit another part?")
                    edit_part = input("Yes or No: ")
                    if edit_part.lower() == "n" or edit_part.lower() == "no":
                        break

            elif field == "3":
                while True:
                    supplier_name = input("Enter supplier to edit: ")
                    supplier = get_supplier_by_name(supplier_name)
                    for i, address in enumerate(supplier.Address, start=1):
                        print(f"{i}: {address}")

                    manufacturer_index = input("What address do you want to edit: ")
                    manufacturer_index = int(manufacturer_index) - 1

                    new_country = input("Enter country: ")
                    new_state = input("Enter state: ")
                    new_city = input("Enter city: ")
                    new_zip_code = input("Enter zip code: ")
                    new_street_address = input("Enter street address: ")
                    new_phone_num = input("Enter phone number: ")

                    new_address = create_new_supplier_address(new_country, new_state, new_city, new_zip_code, new_street_address, new_phone_num)
                    store_edited_supplier_address(supplier_name, new_address, manufacturer_index)

                    print("Do you want to edit another address?")
                    edit_address = input("Yes or No: ")
                    if edit_address.lower() == "n" or edit_address.lower() == "no":
                        break

            elif field == "4":
                while True:
                    supplier_name = input("Enter supplier to edit: ")
                    supplier = get_supplier_by_name(supplier_name)
                    for i, contact in enumerate(supplier.ContactPerson, start=1):
                        print(f"{i}: {contact}")

                    contact_index = input("What contact person do you want to edit: ")
                    contact_index = int(contact_index) - 1

                    new_name = input("Enter contact person: ")
                    new_phone = input("Enter phone number: ")
                    new_email = input("Enter email: ")
                    new_contact = create_new_contact_person(new_name, new_phone, new_email)
                    store_edited_supplier_contact_person(supplier_name, new_contact, contact_index)

                    print("Do you want to edit another contact?")
                    edit_contact = input("Yes or No: ")
                    if edit_contact.lower() == "n" or edit_contact.lower() == "no":
                        break

        elif choice == "8":
            suppliers = get_all_suppliers()
            for supplier in suppliers:
                print(supplier)
                print("------------------------------")
            name = input("Enter The Id Of Supplier You Want To Delete: ")
            delete_supplier(name)

        elif choice == "9":
            suppliers = get_all_suppliers()
            for supplier in suppliers:
                print(supplier)
                print("------------------------------")

            supplier_name = input("Enter supplier you want to delete a part for: ")
            supplier = get_supplier_by_name(supplier_name)
            for i, part in enumerate(supplier.Parts, start=1):
                print(f"{i}: {part}")

            part_index = input("What part do you want to delete: ")
            part_index = int(part_index) - 1

            delete_part(supplier_name, part_index)

        elif choice == "10":
            suppliers = get_all_suppliers()
            for supplier in suppliers:
                print(supplier)
                print("------------------------------")

            supplier_name = input("Enter supplier you want to delete an address for: ")
            supplier = get_supplier_by_name(supplier_name)
            for i, address in enumerate(supplier.Address, start=1):
                print(f"{i}: {address}")

            address_index = input("What address do you want to delete: ")
            address_index = int(address_index) - 1

            delete_address(supplier_name, address_index)

        elif choice == "11":
            suppliers = get_all_suppliers()
            for supplier in suppliers:
                print(supplier)
                print("------------------------------")

            supplier_name = input("Enter supplier you want to delete a contact person for: ")
            supplier = get_supplier_by_name(supplier_name)
            for i, contact in enumerate(supplier.ContactPerson, start=1):
                print(f"{i}: {contact}")

            contact_index = input("What contact person do you want to delete: ")
            contact_index = int(contact_index) - 1

            delete_contact_person(supplier_name, contact_index)

        elif choice == "12":
            break
