from Controllers.supplier_controller import *
from UI.suppliers_menu import suppliers_menu


def suppliers_contact_person_menu():
    while True:
        print("Supplier Contact People Menu")
        print("--------------")
        print("1. View All Contact People For Suppliers")
        print("2. Find A Contact Person For A Supplier By Supplier")
        print("3. Find A Contact Person For A Supplier By Name")
        print("4. Find A Contact Person For A Supplier By Phone Number")
        print("5. Find A Contact Person For A Supplier By Email")
        print("6. Edit A Contact Person")
        print("7. Delete A Contact Person")
        print("8. Exit Supplier Contact People Menu")

        choice = input("> ")

        if choice == "1":
            contacts = get_all_supplier_contact_people()
            for contact in contacts:
                print(contact)
        elif choice == "2":
            supplier_name = input("Enter Supplier: ")
            contact = get_supplier_contact_person_by_supplier(supplier_name)
            for key, contact in contact.items():
                print(f"{key}. {contact}")
        elif choice == "3":
            name = input("Enter Name: ")
            contact = get_supplier_contact_person_by_name(name)
            for key, contact in contact.items():
                print(f"{key}. {contact}")
        elif choice == "4":
            state = input("Enter Phone Number: ")
            phone_num = get_supplier_contact_person_by_phone_number(state)
            for key, phone_num in phone_num.items():
                print(f"{key}. {phone_num}")
        elif choice == "5":
            email = input("Enter Email: ")
            contact = get_supplier_contact_person_by_email(email)
            for key, contact in contact.items():
                print(f"{key}. {contact}")
        elif choice == "7":
            pass

        elif choice == "8":
            suppliers_menu()
