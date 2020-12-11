
from UI.parts_menu import parts_menu
from UI.manufacture_menu import manufacture_menu
from UI.employee_menu import employee_menu
from UI.customer_menu import customers_menu
from UI.car_menu import car_menu
from UI.order_menu import order_menu



def main_menu():
    while True:

        print("\nMain Menu")
        print("=========")
        print("1. Parts")
        print("2. Manufacturers")
        print("3. Employees")
        print("4. Customers")
        print("5. Cars")
        print("6. Orders")

        selection = input("> ")
        if selection == "1":
            parts_menu()

        elif selection == "2":
            manufacture_menu()

        elif selection == "3":
            employee_menu()

        elif selection == "4":
            customers_menu()

        elif selection == "5":
            car_menu()

        elif selection == "6":
            order_menu()

        else:
            continue


def main():

    main_menu()



if __name__ == "__main__":
    main()

