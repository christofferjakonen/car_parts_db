from UI.customers_menu import customers_menu


def main_menu():
    while True:
        print("Main Menu")
        print("=========")
        print("1. Customers")
        print("2. Products")
        print("3. Orders")
        print("4. Quit")

        selection = input("> ")
        if selection == "1":
            customers_menu()

        else:
            break



def main():

    main_menu()



if __name__ == "__main__":
    main()

