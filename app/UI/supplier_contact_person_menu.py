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
            pass

        elif choice == "8":
            contacts = get_all_supplier_contact_people()
            for contact in contacts:
                print(contact)
            contact_name = input("Enter the name of contact you want to delete: ")
            delete_supplier_contact_person(contact_name)

        elif choice == "9":
            break
