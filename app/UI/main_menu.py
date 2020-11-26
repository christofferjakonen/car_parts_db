from UI.suppliers_menu import suppliers_menu


def main_menu():
    while True:
        print("Main Menu")
        print("---------")
        print("1. Suppliers")
        print("2. Quit")

        choice = input("> ")

        if choice == "1":
            suppliers_menu()
        elif choice == "2":
            break
