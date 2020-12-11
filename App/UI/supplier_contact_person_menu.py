from Controllers.supplier_controller import *


def suppliers_contact_person_menu():
    while True:
        print("Supplier Contact People Menu")
        print("--------------")
        print("1. View All Contact People For Suppliers")
        print("2. Find A Contact Person For A Supplier By Supplier")
        print("3. Find A Contact Person For A Supplier By Name")
        print("4. Find A Contact Person For A Supplier By Phone Number")
        print("5. Find A Contact Person For A Supplier By Email")
        print("6. Add A Contact Person")
        print("7. Edit A Contact Person")
        print("8. Delete A Contact Person")
        print("9. Exit Supplier Contact People Menu")

        choice = input("> ")

        if choice == "1":
            contacts = get_all_supplier_contact_people()
            for contact in contacts:
                print(contact)

        elif choice == "2":
            supplier_name = input("Enter Supplier: ")
            contacts = get_supplier_contact_person_by_supplier(supplier_name)
            for contact in contacts:
                print(contact)

        elif choice == "3":
            name = input("Enter Name: ")
            contacts = get_supplier_contact_person_by_name(name)
            for contact in contacts:
                print(contact)

        elif choice == "4":
            state = input("Enter Phone Number: ")
            contacts = get_supplier_contact_person_by_phone_number(state)
            for contact in contacts:
                print(contact)

        elif choice == "5":
            email = input("Enter Email: ")
            contacts = get_supplier_contact_person_by_email(email)
            for contact in contacts:
                print(contact)

        elif choice == "6":
            supplier_name = input("Name Of Supplier: ")
            contact_name = input("Fist And Last Name Of Contact: ")
            phone_num = input("Phone Number: ")
            email = input("Email: ")
            add_new_supplier_contact(supplier_name, contact_name, phone_num, email)

        elif choice == "7":
            supplier_contacts = get_all_supplier_contact_people()
            for supplier_contact in supplier_contacts:
                print(supplier_contact)

            name = input("Enter Supplier You Want To Edit A Contact For: ")
            supplier_contacts = get_supplier_contact_person_by_supplier(name)

            for key, supplier_contact in supplier_contacts.items():
                print(f"{key}. {supplier_contact}")

            edit = input("Enter number for contact you want to edit: ")
            edit = int(edit)

            supplier_contact = supplier_contacts[edit]

            print("1. Supplier Name:", supplier_contact.Supplier)
            print("2. Country:", supplier_contact.FullName)
            print("3. State:", supplier_contact.PhoneNumber)
            print("4. City:", supplier_contact.Email)

            column = input("Enter number of the column you want to edit: ")
            if column == "1":
                new_value = input("Enter new supplier name: ")
                store_edited_supplier_contact_supplier(supplier_contact, new_value)
            elif column == "2":
                new_value = input("Enter new contact name: ")
                store_edited_supplier_contact_name(supplier_contact, new_value)
            elif column == "3":
                new_value = input("Enter new phone number: ")
                store_edited_supplier_contact_phone_num(supplier_contact, new_value)
            elif column == "4":
                new_value = input("Enter new email: ")
                store_edited_supplier_contact_email(supplier_contact, new_value)

        elif choice == "8":
            contacts = get_all_supplier_contact_people()
            for contact in contacts:
                print(contact)
            contact_name = input("Enter the name of contact you want to delete: ")
            delete_supplier_contact_person(contact_name)

        elif choice == "9":
            break
