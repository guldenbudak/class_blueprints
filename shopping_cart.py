shopping_list = []


class Shopping_cart:
    def __init__(self, items, price, customer_id, is_borrowed=False):
        self.items = items
        self.customer_id = customer_id
        self.is_borrowed = is_borrowed
        self.price = price

    def add_items(self):
        if self.is_borrowed == False:
            self.is_borrowed = True
            print(f"{self.items} added to cart.")

        elif self.is_borrowed == True:
            self.is_borrowed = True
            selected = shopping_list

            for shopping in shopping_list:
                if shopping.customer_id == self.customer_id:
                    selected = shopping
                    print(f"{self.items} added to cart.")
                    break

        else:
            print(f"{self.items} could not be added to the cart.")

    def remove_items(self):
        if self.is_borrowed == True:
            self.is_borrowed = False
            shopping_list.remove(shopping_cart)
            print(f"{self.items} removed from cart.")

        else:
            print(f"{self.items} could not be removed from the cart.")

    def show_cart(self):
        cart = "Available"
        if self.is_borrowed == True:
            cart = "Borrowed"
            print(
                f"items: {self.items} price: {self.price} customer id: {self.customer_id} the current situation: {cart}")

        elif self.is_borrowed == False:
            cart = "Borrowed"
            selected = shopping_list

            for shopping in shopping_list:
                if shopping.customer_id == self.customer_id:
                    selected = shopping
                    print(
                        f"items: {self.items} price: {self.price} customer id: {self.customer_id} the current situation: {cart}")
                    break
        else:
            print("No data was found to display.")

    def set_total_price(self):
        total = 0
        if self.is_borrowed == True:
            for item in shopping_list:
                if customer_id == item.customer_id:
                    total += item.price
        else:
            print("No data was found to display.")
        print(f"Customer id: {self.customer_id} Total:", total)


while True:
    print("Welcome to the Shopping Cart!")
    print("1-Add products to cart")
    print("2-Removing items from the cart")
    print("3-View items in the cart")
    print("4-Total price of the cart")
    print("5-Exit")

    option = int(input("Enter your choice: "))
    if option == 1:
        customer_id = int(input("Enter customer id: "))
        items = input("Enter product name: ")
        price = int(input("Enter product price: "))
        shopping_cart = Shopping_cart(customer_id=customer_id, items=items, price=price)
        shopping_list.append(shopping_cart)

        selected = shopping_list

        for shopping in shopping_list:
            if shopping.customer_id == customer_id:
                selected = shopping
                selected.add_items()
                break

        else:
            print("Customer ID did not match, please try again.")
            continue

    if option == 2:
        customer_id = int(input("Enter customer id: "))
        items = input("Enter the name of the item you wish to delete: ")
        selected = shopping_list

        for shopping in shopping_list:
            if shopping.items == items or shopping.customer_id == customer_id:
                selected = shopping
                selected.remove_items()
                break

            else:
                print("Customer ID did not match, please try again.")
                continue

    if option == 3:
        customer_id = int(input("Enter customer id: "))

        selected = shopping_list

        for shopping in shopping_list:
            if shopping.customer_id == customer_id:
                selected = shopping
                selected.show_cart()
                break

        else:
            print("Customer ID did not match, please try again.")
            continue

    if option == 4:
        customer_id = int(input("Enter customer id: "))
        selected = shopping_list

        for shopping in shopping_list:
            if shopping.customer_id == customer_id:
                selected = shopping
                selected.set_total_price()
                break
        else:
            print("Customer ID did not match, please try again.")

    if option == 5:
        print("Thank you for using our shopping cart system.")
        break
