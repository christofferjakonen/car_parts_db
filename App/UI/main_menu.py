from UI.parts_menu import parts_menu
from UI.manufacture_menu import manufacture_menu
from UI.employee_menu import employee_menu


def main_menu():
    while True:
        print("\nMain Menu")
        print("=========")
        print("1. Parts")
        print("2. Manufacturers")
        print("3. Employees")

        selection = input("> ")
        if selection == "1":
            parts_menu()

        elif selection == "2":
            manufacture_menu()

        elif selection == "3":
            employee_menu()

        else:
            continue


if __name__ == '__main__':
    main_menu()