import matplotlib.pyplot as plt
import datetime


class Shop:
    def __init__(self, customers, flowers, orders, owners):
        self.customers = customers
        self.flowers = flowers
        self.orders = orders
        self.owners = owners

    def check_login(self, input_username, input_password):
        for item in owners:
            username = item[0]
            password = item[1]
            if input_username == username and input_password == password:
                print("Welcome back " + username)
                return True
        return False

    def login(self):
        successful_login = False
        while not successful_login:
            username = input("Please enter username: ")
            password = input("Please enter password: ")
            if shop.check_login(username, password):
                successful_login = True
                shop.main_menu()
            else:
                print("Invalid username and/or password. Try again")
        return username

    def load_list_of_customers(self):
        customers_file = open('customers.txt', "r")
        for line in customers_file:
            line = line.rstrip('\n')
            name, gender, number = line.split(",")
            customers[name] = (gender, number)
        customers_file.close()

    def save_list_of_customers(self):
        customers_file = open('customers.txt', "w")
        for k, v in customers.items():
            customers_file.write(k + "," + v[0] + "," + str(v[1]) + "\n")
        customers_file.close()

    def load_list_of_flowers(self):
        flowers_file = open('flowers.txt', "r")
        for line in flowers_file:
            line = line.rstrip('\n')
            name, price, quantity = line.split(",")
            flowers[name] = [price, quantity]
        flowers_file.close()

    def save_list_of_flowers(self):
        flowers_file = open('flowers.txt', "w")
        for k, v in flowers.items():
            flowers_file.write(k + "," + str(v[0]) + "," + str(v[1]) + "\n")
        flowers_file.close()

    def load_list_of_suppliers(self):
        suppliers_file = open('suppliers.txt', "r")
        for line in suppliers_file:
            line = line.rstrip('\n')
            name, type_of_supplier, number = line.split(",")
            suppliers[name] = (type_of_supplier, number)
        suppliers_file.close()

    def load_list_of_orders(self):
        orders_file = open('orders.txt', "r")
        for line in orders_file:
            line = line.rstrip('\n')
            order_number, customer, flower, quantity, day, month, year = line.split(",")
            orders[order_number] = (customer, flower, quantity, day, month, year)
        orders_file.close()

    def save_list_of_orders(self):
        orders_file = open('orders.txt', "w")
        for k, v in orders.items():
            orders_file.write(
                k + "," + v[0] + "," + v[1] + "," + str(v[2]) + "," + str(v[3]) + "," + str(v[4]) + "," + str(
                    v[5]) + "\n")
        orders_file.close()


    def show_customer_details(self):
        repeat_menu = True
        while repeat_menu:
            command = input("**********Customer Details********** \n"
                            "1. View all Customer Details \n"
                            "2. Search for a Customer \n"
                            "Please enter an option: ")
            if command == "1":
                self.load_list_of_customers()
                for k, v in customers.items():
                    print("Name =", k, ":", "Gender =", v[0], ":", "Contact Number:", v[1])
                repeat_menu = False
            elif command == "2":
                customer_name = input("Please enter name of customers: ")
                self.load_list_of_customers()
                for k, v in customers.items():
                    if customer_name == k:
                        print("Name =", k, ":", "Gender =", v[0], ":", "Contact Number =", v[1])
                repeat_menu = False
            else:
                print("Invalid Command")

    def show_flower_details(self):
        repeat_menu = True
        while repeat_menu:
            command = input("**********Flower Details********** \n"
                            "1.View all flower details \n "
                            "2.Search for a flower \n "
                            "Please enter option: ")
            if command == "1":
                self.load_list_of_flowers()
                for k, v in flowers.items():
                    print("Name =", k, ":", "Price =", v[0], ":", "Quantity in stock =", v[1])
                repeat_menu = False
            elif command == "2":
                flower_name = input("Please enter flower name: ")
                self.load_list_of_flowers()
                for k, v in flowers.items():
                    if flower_name == k:
                        print("Name =", k, ":", "Price = ", v[0], ":", "Quantity in Stock =", v[1])
                repeat_menu = False
            else:
                print("Invalid command")

    def show_supplier_details(self):
        repeat_menu = True
        while repeat_menu:
            command = input("*********Supplier Details********** \n"
                            "1. View all supplier details \n"
                            "2. Search for a supplier \n"
                            "Please enter option: ")
            if command == "1":
                self.load_list_of_suppliers()
                for k, v in suppliers.items():
                    print("Name =", k, ":", "Type =", v[0], ":", "Contact Number =", v[1])
                repeat_menu = False
            elif command == "2":
                supplier_name = input("Please enter name of supplier:")
                self.load_list_of_suppliers()
                for k, v in suppliers.items():
                    if supplier_name == k:
                        print("Name =", k, ":", "Type =", v[0], ":", "Contact Number =", v[1])
                repeat_menu = False
            else:
                print("Invalid Command")

    def add_customer(self):
        """
        Input: New customers.txt's name, their gender and their contact number
        Behaviour: 1) Searches through the 'customers.csv' dictionary's keys to check that the name of the new customers.txt
                    entered does not already exist within the system
                   2) If the name does not already exist in the 'customers.csv' dictionary, the new customers.txt's details will
                    be added to the dictionary and a message will be displayed to let the user know that the customers.txt
                    was added successfully
                   3) If the name already exists in the 'customers.csv' dictionary, a message will appear letting the user
                   know that the customers.txt already exists and therefore cannot be added to the dictionary
        Output: -
        Note: -
        """
        name = input("Please enter name of new customer: ")  # new customers name
        gender = input("Please enter the gender: ")  # new customers gender
        number = int(input("Please enter the contact number: "))  # new customers contact number
        self.load_list_of_customers()
        if name not in customers.keys():
            customers[name] = (gender, number)
            loyalty[name] = 0
            print("Customer added successfully.")  # new customers.txt added
            self.save_list_of_customers()
        else:
            print("Customer already exists.")  # new customers.txt NOT added

    def add_flower(self):
        """
        Input: New flower's name, its price and its quantity
        Behaviour: 1) Searches through the 'flowers' dictionary's keys to check that the name of the new flower
                    entered does not already exist within the system
                   2) If the name does not already exist in the 'flowers' dictionary, the new flower's details will
                    be added to the dictionary and a message will be displayed to let the user know that the flower
                    was added successfully
                   3) If the name already exists in the 'flowers' dictionary, a message will appear letting the user
                   know that the flower already exists and therefore cannot be added to the dictionary
        Output: -
        Note: -
        """
        name = input("Please enter name of new flower: ")  # new flower's name
        price = float(input("Please enter the price: "))  # new flower's price
        quantity = int(input("Please enter the quantity: "))  # new flower's quantity
        self.load_list_of_flowers()
        if name not in flowers.keys():
            flowers[name] = (price, quantity)
            print("Flower added successfully.")  # new flower added
            self.save_list_of_flowers()
        else:
            print("Flower already exists.")  # new flower NOT added

    def get_flower_quantity(self, name):
        """
        Input: Flower name
        Behaviour: Gets the quantity of whichever flower the customers.txt wishes to order by using the flower name
        Output: Quantity
        Note:     -
        """
        self.load_list_of_flowers()
        if name in flowers.keys():
            return self.flowers[name][1]
        else:
            print("Flower does not exist.")

    def check_flower_quantity(self, flower, quantity_ordered):
        """
        Input: Flower name
        Behaviour: Checks that there are enough quantity of flowers to create the order
        Output:   True or False
        Note:     -
        """
        self.load_list_of_flowers()
        if flower in flowers.keys():
            if int(self.get_flower_quantity(flower)) >= int(quantity_ordered):
                return True  # enough flowers - order can be placed
            else:
                return False  # not enough flowers - order can NOT be placed
        else:
            print("Flower does not exist.")

    def update_flower_quantity(self, flower):
        """
        Input: Flower name
        Behaviour: Updates the quantity of flowers, after they have been ordered by customers.csv
        Output: -
        Note: -
        """
        self.load_list_of_flowers()
        if flower in flowers.keys():
            current_quantity = int(self.get_flower_quantity(flower))
            self.load_list_of_orders()
            for item in self.orders.values():
                flower_name = item[1]
                quantity_ordered = item[2]
                if flower_name == flower:
                    new_quantity = current_quantity - int(quantity_ordered)
                    self.flowers[flower][1] = new_quantity
                    self.save_list_of_flowers()
        else:
            print("Flower does not exist.")

    def create_order(self):
        """
        Input:  1 or 2
                For option 2 - New order number, customers.txt's name, name of flower they wish to purchase and the quantity
        Behaviour: 1) A list of options will be displayed to the user of which they will need to choose an option
                   1.1) If the user chooses an option that does not exist, an error message will appear
                   2) If the user chooses option 1, the system will display a list of all orders recorded in the system
                   3) If the user chooses option 2, they will be asked to enter the new order number, the name of the
                   customers.txt, the flower the customers.txt wishes to order, as well as the quantity.
                        3.1) Then the system will check that there are enough flowers to process the order by calling
                            the 'check_flower_quantity' function.
                        3.2) It will also check that the new order number entered does not already exist within the
                            'orders' dictionary's keys, that the customers.txt's name entered already exists in the
                            'customers.csv' dictionary's keys and that the flower name entered already exists in the
                            'flowers' dictionary's keys.
                        3.3) If there are enough flowers to process the order, the order number does not exists and the
                            customers.txt and flower names exist, the order will be placed and added to the 'orders'
                            dictionary. A message will also appear to let the user know the order has been created
                            successfully and it will display the remaining quantity of the flower they ordered.
                        3.4) If one of the above requirements are not satisfied, the order will not be created and an
                            error message will be displayed indicating that there was error and that the user must
                            satisfy all the requirements stated above.
        Output: For option 1 - a list of all orders
        Note: -
        """
        repeat_menu = True
        while repeat_menu:
            command = input("**********Orders*********** \n"
                            "1. View all Orders \n"
                            "2. Create New Order \n"
                            "Please enter an option: ")
            if command == "1":
                self.load_list_of_orders()
                for k, v in orders.items():
                    print("Order Number =", k, ":", "Customer =", v[0], ":", "Flower =", v[1], ":", "Quantity =", v[2],
                          ":", "Date Ordered =", v[3], "/", v[4], "/", v[5])
                repeat_menu = False
            elif command == "2":
                now = datetime.datetime.now()
                order_number = input("Please enter the new order number (start with ORD): ")
                customer = input("Please enter the name of the customer wishing to order flowers: ")
                flower = input("Please enter the name of flower the customer wishes to order: ")
                quantity = int(input("Please enter the quantity of the customer wishes to order: "))
                day = now.day
                month = now.month
                year = now.year
                self.load_list_of_flowers()
                enough_flowers = self.check_flower_quantity(flower, quantity)
                # Checks if there are enough flowers to create the order
                self.load_list_of_orders()
                self.load_list_of_customers()
                if enough_flowers and order_number not in orders.keys() and customer in customers.keys() and flower \
                        in flowers.keys():
                    orders[order_number] = (customer, flower, quantity, day, month, year)
                    if self.qualify_dicount(customer):
                        print("This order is free! Thank you for your loyalty!")
                    else:
                        f_price = shop.get_flower_price(flower)
                        cost_order = float(f_price) * quantity
                        print("The cost of the order is: " + str(cost_order))
                    print("Order placed successfully.")
                    loyalty[customer] += 1
                    self.update_flower_quantity(flower)
                    print("Remaining Quantity:", self.get_flower_quantity(flower))
                    self.save_list_of_orders()
                    repeat_menu = False
                else:
                    print("ERROR - Order cannot be created. "
                          "Please ensure that the order number does not exist, there are enough flowers in stock to "
                          "order and that the customer and flower names exist.")
                    repeat_menu = False
            else:
                print("Invalid Command")

    def get_flower_price(self, name):
        """
        Input: Flower name
        Behaviour: Gets the price of a flower
        Output: Price
        Note: -
        """
        self.load_list_of_flowers()
        return self.flowers[name][0]

    def plot_flower_sales_for_year(self):
        """
        Input: Year
        Behaviour: 1) Asks the user to input a year
                   2) The system checks through the 'orders' dictionary and if the input year matches the year the
                    order was placed, it will add it into the bar chart
        Output: A bar chart of the flower sales for a specific year
        Note: If more than one person ordered the same flower in one year, it will combine both orders into
              a single bar on the chart
        """
        flower_sales = dict()
        input_year = int(input("Please enter a year: "))
        self.load_list_of_orders()
        for item in orders.values():
            name = item[1]
            quantity = int(item[2])
            price = int(self.get_flower_price(name))
            revenue = int(quantity) * int(price)
            year = int(item[5])
            if int(year) == int(input_year):
                if name in flower_sales:
                    flower_sales[name] += revenue
                else:
                    flower_sales[name] = revenue
        plt.bar(range(len(flower_sales)), flower_sales.values())
        plt.xticks(range(len(flower_sales)), flower_sales.keys())
        plt.xlabel("Flowers")
        plt.ylabel("Sales (£)")
        plt.title("Total Sales of Flowers in " + str(input_year))
        plt.show()

    def find_loyal_customers(self):
        from collections import Counter
        k = Counter(loyalty)
        high = k.most_common(3)
        print("Initial Dictionary:")
        print(loyalty, "\n")
        print("3 most loyal customers: ")
        print("Name: Amount of orders")
        for i in high:
            print(i[0], ":", i[1])

    def qualify_dicount(self, name):
        discount = False
        for k, v in loyalty.items():
            if k == name:
                if v > 10:
                    print("This purchase is free")
                    loyalty[name] = (v - 10)
                    discount = True
                else:
                    print("You need " + str(10 - v), "more purchases to get one free ")
        return discount

    def plot_total_sales_of_specific_flower(self):
        repeat_menu = True
        while repeat_menu:
            command = input("Please choose a flower to get total sales:\n"
                            "1-Lily\n"
                            "2-Rose\n"
                            "3-Tulip\n"
                            "4-Iris\n"
                            "5-Daisy\n"
                            "6-Orchid\n"
                            "7-Dahlia\n"
                            "8-Peony")
            if command.upper() == "1":
                # Lily
                total_sales = [15, 12, 8, 19, 20, 16, 21, 17, 18, 15, 13, 12]
                months = range(1, 13, 1)
                mnames = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
                plt.bar(months, total_sales)
                plt.xlabel("Months")
                plt.ylabel("Sales in £")
                plt.title("Flower: The Lily")
                plt.xticks(months, mnames)
                plt.show()
                repeat_menu = False
            elif command.upper() == "2":
                # Rose
                total_sales = [3, 2, 4, 3, 1, 5, 5, 5, 2, 4, 1, 3]
                months = range(1, 13, 1)
                mnames = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
                plt.bar(months, total_sales)
                plt.xlabel("Months")
                plt.ylabel("Sales in £")
                plt.title("Flower: The Rose")
                plt.xticks(months, mnames)
                plt.show()
                repeat_menu = False
            elif command == "3":
                # Tulip
                total_sales = [7, 1, 9, 14, 16, 19, 20, 17, 15, 12, 10, 8]
                months = range(1, 13, 1)
                mnames = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
                plt.bar(months, total_sales)
                plt.xlabel("Months")
                plt.ylabel("Sales in £")
                plt.title("Flower: The Tulip")
                plt.xticks(months, mnames)
                plt.show()
                repeat_menu = False
            elif command == "4":
                # Iris
                total_sales = [10, 13, 8, 12, 6, 16, 20, 25, 22, 13, 10, 12]
                months = range(1, 13, 1)
                mnames = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
                plt.bar(months, total_sales)
                plt.xlabel("Months")
                plt.ylabel("Sales in £")
                plt.title("Flower: The Iris")
                plt.xticks(months, mnames)
                plt.show()
                repeat_menu = False
            elif command == "5":
                # Daisy
                total_sales = [4, 6, 5, 8, 7, 6, 9, 9, 7, 5, 7, 3]
                months = range(1, 13, 1)
                mnames = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
                plt.bar(months, total_sales)
                plt.xlabel("Months")
                plt.ylabel("Sales in £")
                plt.title("Flower: The Daisy")
                plt.xticks(months, mnames)
                plt.show()
                repeat_menu = False
            elif command == "6":
                # Orchid
                total_sales = [180, 324, 216, 171, 225, 261, 252, 297, 162, 198, 180, 342]
                months = range(1, 13, 1)
                mnames = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
                plt.bar(months, total_sales)
                plt.xlabel("Months")
                plt.ylabel("Sales in £")
                plt.title("Flower: The Orchid")
                plt.xticks(months, mnames)
                plt.show()
                repeat_menu = False
            elif command == "7":
                # Dahlia
                total_sales = [11, 15, 8, 3, 15, 10, 12, 14, 9, 6, 8, 12]
                months = range(1, 13, 1)
                mnames = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
                plt.bar(months, total_sales)
                plt.xlabel("Months")
                plt.ylabel("Sales in £")
                plt.title("Flower: The Dahlia")
                plt.xticks(months, mnames)
                plt.show()
                repeat_menu = False
            elif command == "8":
                # Peony
                total_sales = [6, 3, 8, 7, 5, 2, 9, 10, 6, 4, 3, 1]
                months = range(1, 13, 1)
                mnames = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
                plt.bar(months, total_sales)
                plt.xlabel("Months")
                plt.ylabel("Sales in £")
                plt.title("Flower: The Peony")
                plt.xticks(months, mnames)
                plt.show()
                repeat_menu = False
            else:
                print("Error: Invalid command")

    def order_supplies(self):
        repeat_menu = True
        while repeat_menu:
            command = input("*********Order Supplies********** \n"
                            " 1.View stock \n "
                            "2.Search for a flower to restock \n "
                            "Please enter option: ")
            if command == "1":
                self.load_list_of_flowers()
                for k, v in flowers.items():
                    print("Name =", k, "--", "Quantity in stock=", v[1])
                repeat_menu = False
            elif command == "2":
                flower_name = input("Please enter flower name: ")
                self.load_list_of_flowers()
                for k, v in flowers.items():
                    if flower_name == k:
                        print("Name =", k, "--", "Price = ", v[0], "p", "--", "Quantity in stock=", v[1])
                        quantity = self.get_flower_quantity(k)
                        new_quantity = int(input("\nEnter quantity for the restocking of this flower: "))
                        totalprice = int(v[0]) * new_quantity
                        print("Total: £", totalprice)
                        self.flowers[k][1] = int(quantity) + new_quantity
                        print("Order has successfully been processed.")
                repeat_menu = False
            else:
                print("Invalid command")

    def main_menu(self):
        print("Please wait while flower system is loading")
        repeat_menu = True
        while repeat_menu:
            command = input("************ Main Menu ***********\n"
                            "1-View Customer Details\n"
                            "2-View Flower Details\n"
                            "3-View Supplier Details\n"
                            "4-Add New Customer\n"
                            "5-Add New Flower\n"
                            "6-Customer Orders\n"
                            "7-Order New Supplies\n"
                            "8-Compare flower sales for specific year\n"
                            "9-Find Loyal Customers\n"
                            "10-Total sales of specific flower\n"
                            "11- Log Out\n"
                            "Please select an option above: ")
            if command.upper() == "1":
                print(" ")
                shop.show_customer_details()
                print(" ")
            elif command.upper() == "2":
                print(" ")
                shop.show_flower_details()
                print(" ")
            elif command == "3":
                print(" ")
                shop.show_supplier_details()
                print(" ")
            elif command == "4":
                print(" ")
                shop.add_customer()
                print(" ")
            elif command == "5":
                print(" ")
                shop.add_flower()
                print(" ")
            elif command == "6":
                print(" ")
                shop.create_order()
                print(" ")
            elif command == "7":
                print(" ")
                shop.order_supplies()
                print(" ")
            elif command == "8":
                print(" ")
                shop.plot_flower_sales_for_year()
                print(" ")
            elif command == "9":
                print(" ")
                shop.find_loyal_customers()
                print(" ")
            elif command == "10":
                print(" ")
                shop.plot_total_sales_of_specific_flower()
                print(" ")
            elif command == "11":
                print(" ")
                print("Logout was successful.")
                quit()
                print(" ")
            else:
                print("Error: Invalid command")


if __name__ == "__main__":
    # name, gender, number
    customers = {}

    # name, price, quantity
    flowers = {}

    # order number, customers.txt, flower, quantity, day, month, year
    orders = {}

    # supplier name, type of supplier, number
    suppliers = {}

    #customer name, number of orders
    loyalty = {"Butch": 2, "Scrooge": 0, "Donald": 1, "Marie": 1,
               "Dewey": 1, "Tom": 0, "Jerry": 3, "Spike": 1}

    #username, password
    owners = [["Daisy", "1234"], ["Guest", "2222"]]

    shop = Shop(customers, flowers, orders, owners)
    shop.login()

