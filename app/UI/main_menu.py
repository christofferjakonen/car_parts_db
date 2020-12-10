from UI.suppliers_menu import suppliers_menu
from UI.store_menu import store_menu


def main_menu():
    while True:
        print("Main Menu")
        print("---------")
        print("1. Suppliers Menu")
        print("2. Store Menu")
        print("3. Quit")

        choice = input("> ")

        if choice == "1":
            suppliers_menu()
        elif choice == "2":
            store_menu()
        elif choice == "3":
            break
