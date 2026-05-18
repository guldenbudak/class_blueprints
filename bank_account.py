account_list = []


class BankAccount:
    def __init__(self, customer_no, password, balance=0):
        self.customer_no = customer_no
        self.password = password
        self.balance = balance

    def deposit(self, balance):
        self.balance += balance
        print(f"{self.customer_no} Deposit Made, balance: {self.balance} ")

    def withdraw(self, balance):
        if self.balance >= balance:
            self.balance -= balance
            print(f"{self.customer_no} Withdraw Made, balance: {self.balance} ")
        else:
            print("Insufficient balance, withdrawal transaction could not be processed.")

    def transfer(self, balance, receiver=None):
        receiver.balance += balance
        self.balance -= balance
        print(f"{self.customer_no} Transfer Made, balance: {self.balance} ")
        print(f"Receiver no : {receiver.customer_no},Receiver balance : {receiver.balance}")


while True:
    print("Welcome to Bank Account")
    print("1-Adding a User")
    print("2-Depositing Money")
    print("3-Withdrawing Money")
    print("4-Transferring to Account")
    print("5-Logging Out")
    option = int(input("Enter your choice: "))

    if option == 1:
        customer_no = int(input("Enter your customer number: "))
        password = int(input("Enter your password: "))
        balance = int(input("Enter your balance money: "))

        for item in account_list:
            if item.customer_no == customer_no:
                print(f"{customer_no} already exists.")
                break
        else:
            bank_account = BankAccount(customer_no=customer_no, password=password, balance=balance)
            account_list.append(bank_account)
            print(f"bank account balance, {bank_account.balance} ")

    elif option == 2:
        customer_no = int(input("Enter your customer number: "))
        password = int(input("Enter your password: "))
        for item in account_list:
            if item.customer_no == customer_no and item.password == password:
                balance = int(input("Enter your deposit money: "))
                item.deposit(balance)
                break
        else:
            print(f"{customer_no} User not found.")

    elif option == 3:
        customer_no = int(input("Enter your customer number: "))
        password = int(input("Enter your password: "))
        for item in account_list:
            if item.customer_no == customer_no and item.password == password:
                balance = int(input("Enter your deposit money: "))
                item.withdraw(balance)
                break
        else:
            print(f"{customer_no} User not found.")

    elif option == 4:
        customer_no = int(input("Enter your customer number: "))
        password = int(input("Enter your password: "))
        sender = None
        receiver = None
        for item in account_list:
            if item.customer_no == customer_no and item.password == password:
                sender = item
                break
        else:
            print(f"{customer_no} User not found.")
        receiver_no = int(input("Enter your receiver no: "))
        for item in account_list:
            if item.customer_no == receiver_no:
                receiver = item
                break
        else:
            print(f"{customer_no} User not found.")

        if receiver != None and sender != None:
            balance = int(input("Enter your deposit money: "))
            sender.transfer(balance, receiver)

    elif option == 5:
        print("Thank you for using Bank Account.")
        break
