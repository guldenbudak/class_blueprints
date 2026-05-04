class Order:
    def __init__(self, customer_name, coffe_type, size, change_material):
        self.customer_name = customer_name
        self.coffe_type = coffe_type
        self.price = None
        self.set_price()
        self.size = size
        self.set_size()
        self.change_material = change_material
        self.set_change_material()

    def set_price(self):
        if self.coffe_type == "Latte":
            self.price = 80
        elif self.coffe_type == "Cappuccino":
            self.price = 70
        elif self.coffe_type == "Espresso":
            self.price = 60

    def set_size(self):
        if self.size == "Small":
            self.price -= 5
        elif self.size == "Medium":
            self.price += 5
        elif self.size == "Large":
            self.price += 10

    def show_order(self):
        return ( f"show order: {self.customer_name}, {self.coffe_type}, {self.size}, Total price: {self.price}")

    def set_change_material(self):
        if self.change_material == "extra milk":
            self.price += 10
        elif self.change_material == "extra shot":
            self.price += 20
        else:
            self.price -= float(self.price * 0.10)

per_1 = Order("Alice", "Latte", "Small","extra milk")
print(per_1.show_order())
