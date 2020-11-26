from UI.parts_menu import parts_menu
from UI.manufacture_menu import manufacture_menu


def main_menu():
    while True:
        print("\nMain Menu")
        print("=========")
        print("1. Parts")
        print("2. Manufacturers")
        print("3. Exit")

        selection = input("> ")
        if selection == "1":
            parts_menu()

        elif selection == "2":
            manufacture_menu()

        elif selection == "3":
            break

        else:
            continue


if __name__ == '__main__':
    main_menu()