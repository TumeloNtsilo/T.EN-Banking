import random

class Client:
    
    def __init__(self):
        self.account_type = "savings"
        self.account_num = random.randint(10000000, 99999999)
        self.pin_number = random.randint(1000, 9999)
        self.balance = 0.00

    def enter_pin(self):
        attempts = 3

        while attempts > 0:
            try:
                self.entered_pin = int(input("To access your account, enter four digit pin: "))
                if len(str(self.entered_pin)) == 4:
                    if int(self.entered_pin) == self.pin_number:
                        print("Pin number is correct.")
                        break
                    else:
                        attempts -= 1
                        print(f"Invalid pin, {attempts} attempts remaining.")
                    
                else:
                    attempts -=1
                    print(f"Invalid pin, {attempts} attempts remaining.")
                    break

            except:
                attempts -= 1
                print(f"Invalid pin, {attempts} attempts remaining.")
    
    
    
    def display_account_details(self):
        print(f"\nAccount number: {self.account_num}\nAccount type: {self.account_type}\n")
    
    def deposit(self):
        self.amount = float(input("Enter the amount to deposit: "))
        if 10 <= self.amount < 100:
            self.charges = 1.50

        elif 100 <= self.amount < 1000:
            self.charges = 2.0

        elif self.amount > 1000:
            self.charges = 3.0

        self.balance += (self.amount - self.charges)

        print(f"\nbalance: {self.balance}\n")
    

    def withdraw(self):
        self.amount = float(input("Enter the amount you want to withdraw: "))
        if self.amount > self.balance:
            print("Insuffient funds!")

        else:
            if 10 <= self.amount < 100:
                self.charges = 1.0

            elif 100 <= self.amount < 1000:
                self.charges = 4.00

            elif self.amount > 1000:
                self.charges = 8.00
                
                self.balance -= (self.amount - self.charges)

        print(f"\nBalance: {self.balance}\n")


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
            


    
