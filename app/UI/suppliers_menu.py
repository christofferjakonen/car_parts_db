from Controllers.supplier_controller import *
from UI.supplier_address_menu import supplier_address_menu
from UI.supplier_contact_person_menu import suppliers_contact_person_menu


def suppliers_menu():
    while True:
        print("Suppliers Menu")
        print("--------------")
        print("1. View All Suppliers")
        print("2. Find Supplier By Name")
        print("3. Find Supplier By Phone Number")
        print("4. Find Supplier By Name Email")
        print("5. Add New Supplier")
        print("6. Edit A Supplier")
        print("7. Delete A Supplier")
        print("8. View All Parts Suppliers Have")
        print("9. View All Manufacturers For Suppliers")
        print("10. View Supplier Addresses Menu")
        print("11. View Supplier Contact Person Menu")
        print("12. Exit Supplier Menu")

        choice = input("> ")

        if choice == "1":
            suppliers = get_all_suppliers()
            for supplier in suppliers:
                print(supplier)

        elif choice == "2":
            supplier_name = input("Enter name of supplier: ")
            suppliers = get_supplier_by_name(supplier_name)
            for supplier in suppliers:
                print(supplier)

        elif choice == "3":
            phone_num = input("Enter phone number of supplier: ")
            suppliers = get_supplier_by_phone_number(phone_num)
            for supplier in suppliers:
                print(supplier)

        elif choice == "4":
            email = input("Enter email of supplier: ")
            suppliers = get_supplier_by_email(email)
            for supplier in suppliers:
                print(supplier)

        elif choice == "5":
            supplier_name = input("Name Of Supplier: ")
            phone_num = input("Phone Number: ")
            email = input("Email: ")
            add_new_supplier(supplier_name, phone_num, email)

        elif choice == "6":
            supplier_names = get_all_suppliers()
            for supplier_name in supplier_names:
                print(supplier_name)

            name = input("Enter name of supplier: ")
            suppliers = get_supplier_by_name(name)
            for key, supplier in suppliers.items():
                print(f"{key}. {supplier}")

            edit = input("Enter number for supplier you want to edit: ")
            edit = int(edit)

            supplier = suppliers[edit]

            print("1. Supplier Name:", supplier.SupplierName)
            print("2. Phone Number:", supplier.PhoneNumber)
            print("3. Email:", supplier.Email)

            column = input("Enter number of the column you want to edit: ")
            if column == "1":
                new_value = input("Enter new supplier name: ")
                store_edited_supplier_name(supplier, new_value)
            elif column == "2":
                new_value = input("Enter new phone number: ")
                store_edited_supplier_phone(supplier, new_value)
            elif column == "3":
                new_value = input("Enter new email: ")
                store_edited_supplier_email(supplier, new_value)

        elif choice == "7":
            suppliers = get_all_suppliers()
            for supplier in suppliers:
                print(supplier)
            name = input("Enter The Name Of Supplier You Want To Delete: ")
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
            supplier_address_menu()

        elif choice == "11":
            suppliers_contact_person_menu()

        elif choice == "12":
            break





