restaurant_list = []
total = 0


class RestaurantTable:
    def __init__(self, table_no, product, is_borrowed=False, price=0):
        self.table_no = table_no
        self.product = product
        self.is_borrowed = is_borrowed
        self.price = price
        self.total = 0

    def add_product(self,product):
        if product == "soup":
            self.price = 150
            self.total += self.price
        elif product == "meatball":
            self.price = 200
            self.total += self.price
        elif product == "water":
            self.price = 50
            self.total += self.price

        if self.is_borrowed == False:
            self.is_borrowed = True
            print(f"{product} added to restaurant.")

        elif self.is_borrowed == True:
            self.is_borrowed = True
            print(f"{product}  added to restaurant.")

        else:
            print(f"{product} not added to restaurant.")

    def make_payment(self):
        if self.is_borrowed == True:
            self.is_borrowed = False
            print(f" Table no: {self.table_no} total price: {self.total} makes payment.")
        else:
            print("Table empty, no payment received.")

    def total_price(self):
        if self.is_borrowed == True:
            print(f"Total price:  {self.total}")

        elif self.is_borrowed == False:
            print("The table is empty, total fee could not be found.")


while True:
    print("Welcome to our restaurant.")
    print("1- Add order")
    print("2- Total price")
    print("3- Make payment")
    print("4- Exit")

    option = int(input("Enter your option: "))
    if option == 1:
        table_no = int(input("Enter table no: "))
        product = input("Enter product name (Soup/ Meatball/ Water): ").lower()
        while product != "soup" and product != "meatball" and product != "water":
            print("Please select an item from the menu.")
            product = input("Enter product name: ").lower()

        for restaurant in restaurant_list:
            if restaurant.table_no == table_no:
                selected = restaurant
                selected.add_product(product)
                break
        else:
            restaurant_table = RestaurantTable(table_no=table_no, product=product)
            restaurant_list.append(restaurant_table)
            restaurant_table.add_product(product)

    if option == 2:
        table_no = int(input("Enter table no: "))
        selected = restaurant_list
        for restaurant in restaurant_list:
            if restaurant.table_no == table_no:
                selected = restaurant
                selected.total_price()
                break
        else:
            print("Table no did not match, please try again.")

    if option == 3:
        table_no = int(input("Enter table no: "))
        selected = restaurant_list
        for restaurant in restaurant_list:
            if restaurant.table_no == table_no:
                selected = restaurant
                selected.make_payment()
                break
        else:
            print("Table no did not match, please try again.")

    if option == 4:
        print("Thank you for using our restaurant.")
        break
