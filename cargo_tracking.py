import copy

cargo_list = []
history_list = []


class CargoPackage:
    def __init__(self, tracking_no, receiver, status):
        self.tracking_no = tracking_no
        self.receiver = receiver
        self.status = status

    def __repr__(self):
        return f" All history list: {self.tracking_no}, receiver: {self.receiver}, status: {self.status}"


while True:
    print("Welcome to the Cargo Tracking App")
    print("1- Creating a shipment")
    print("2- Change shipment status")
    print("3- Shipment history")
    print("4- All shipment statuses")
    print("5- Exit")
    option = int(input("Enter your option: "))

    if option == 1:
        tracking_no = int(input("Enter your tracking number: "))
        receiver = int(input("Enter your receiver number: "))
        status = input("Enter your shipment status:(preparation / distribution / delivered) ").lower()
        while status != "preparation" and status != "distribution" and status != "delivered":
            print("Please enter a valid status.")
            status = input("Enter your shipment status:(preparation / distribution / delivered) ").lower()
        for item in cargo_list:
            if item.tracking_no == tracking_no and item.receiver == receiver and item.status == status:
                print(f"{item.receiver} already added .")
                break
        else:
            cargo_added = CargoPackage(tracking_no=tracking_no, receiver=receiver, status=status)
            cargo_list.append(cargo_added)
            copy.copy(cargo_added)
            history_list.append(copy.copy(cargo_added))
            print(
                f"{cargo_added.receiver} added to cargo list, status: {cargo_added.status}, sender: {cargo_added.tracking_no}.")

    elif option == 2:
        tracking_no = int(input("Enter your tracking number: "))
        receiver = int(input("Enter your receiver number: "))
        for item in cargo_list:
            if item.receiver == receiver and item.tracking_no == tracking_no:
                status = input("Enter your shipment status: (preparation / distribution / delivered) ").lower()
                print(f" Receiver: {item.receiver}, New shipment status: {item.status} ")
                cargo_added = CargoPackage(tracking_no=tracking_no, receiver=receiver, status=status)
                history_list.append(cargo_added)
                item.status = status
                print(f" Receiver: {item.receiver}, New shipment status: {item.status} ")
                break
        else:
            print("The user value you entered are incorrect.")

    elif option == 3:
        tracking_no = int(input("Enter your tracking number: "))
        for item in cargo_list:
            if item.tracking_no == tracking_no:
                print("Cargo list :", list.__repr__(cargo_list))
                break
        else:
            print("The user you entered could not be found.")

    elif option == 4:
        tracking_no = int(input("Enter your tracking number: "))
        for item in history_list:
            if item.tracking_no == tracking_no:
                print("All shipment History List: ", list.__repr__(history_list))
                break
        else:
            print("The user you entered could not be found.")

    elif option == 5:
        print("Thank you for using our Shipping Tracking App. We look forward to seeing you again.")
        break
