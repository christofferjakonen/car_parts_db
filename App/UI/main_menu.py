from UI.parts_menu import parts_menu
from UI.manufacture_menu import manufacture_menu


def main_menu():
    while True:
        print("Main Menu")
        print("=========")
        print("1. Parts")
        print("2. Manufacturers")
        print("3. Exit")

        selection = input("> ")
        if selection == "1":
            parts_menu()

        if selection == "3":
            manufacture_menu()

        if selection == "3":
            break


if __name__ == '__main__':
    main_menu()