import random

class Client:
    
    def __init__(self):
        self.account_type = "savings"
        self.account_num = random.randint(10000000, 99999999)
        self.balance = 0.00

    def enter_pin(self):
        attempts  = 3

        while attempts > 0:
            try:
                self.pin = int(input("To access your account, enter four digit pin: "))
                if len(str(self.pin)) != 4:
                    print(f"Invalid pin, {attempts -1} remaining.")
                else:
                    break
            except:
                print("Invalid pin.")
    
    def display_account_details(self):
        print(f"Account number: {self.account_num}\nAccount type: {self.account_type}\n")
    
    def deposit(self):
        self.amount = float(input("Enter the amount to deposit: "))
        if 10 <= self.amount < 100:
            self.charges = 1.50

        elif 100 <= self.amount < 1000:
            self.charges = 2.5

        elif self.amount > 1000:
            self.charges = 7.5

        self.balance += (self.amount - self.charges)

        print(f"balance: {self.balance}\n")
    

    def withdraw(self):
        self.amount = float(input("Enter the amount you want to withdraw: "))
        if self.amount > self.balance:
            print("Insuffient funds!")

        else:
            if 10 <= self.amount < 100:
                self.charges = 1.0

            elif 100 <= self.amount < 1000:
                self.charges = 2.00

            elif self.amount > 1000:
                self.charges = 8.00
                
                self.balance -= (self.amount - self.charges)

        print(f"Balance: {self.balance}\n")


    def action(self):
        self.options = ["view balance", "withdraw", "deposit", "quit"]
        for index, option in enumerate(self.options):
            print(f"{index}: {option}\n")

        while True:
            try:
                self.choose_option = int(input(f"How can we help you? {list(enumerate(self.options))}: "))
                if 0 <= self.choose_option < len(self.options):
                    self.chosen_index = self.options[self.choose_option]  
                    break
                else:
                    print("Invalid choice, try again.")
            except ValueError:
                print("Invalid option, enter a number.")


    def bank(self, option):
        if option == "view balance":
            print(f"Balance: {self.balance}\n")

        elif option == "withdraw":
            self.withdraw()

        elif option == "deposit":
            self.deposit()
        



    
