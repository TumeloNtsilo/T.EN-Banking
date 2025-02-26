import random

class Client:
    def __init__(self):
        self.account_type = "savings"
        self.account_num = random.randint(10000000, 99999999)
        self.pin_number = random.randint(1000, 9999)
        self.balance = 0.00
        self.pin_verified = False

    def enter_pin(self):
        attempts = 3
        while attempts > 0:
            try:
                entered_pin = int(input("To access your account, enter four-digit PIN: "))
                if len(str(entered_pin)) == 4:
                    if entered_pin == self.pin_number:
                        print("PIN number is correct.")
                        self.pin_verified = True
                        return True
                    else:
                        attempts -= 1
                        print(f"Invalid PIN, {attempts} attempts remaining.")
                else:
                    print("PIN must be four digits.")
            except ValueError:
                print("Invalid input. Please enter numbers only.")

        print("Too many failed attempts. Access denied.")
        return False 

    def display_account_details(self):
        print(f"\nAccount number: {self.account_num}\nAccount type: {self.account_type}\n")

    def deposit(self):
        try:
            amount = float(input("Enter the amount to deposit: "))
            if amount < 10:
                print("Minimum deposit is 10.")
                return
            
            charges = 1.50 if amount < 100 else 2.5 if amount < 1000 else 7.5
            self.balance += (amount - charges)
            print(f"\nNew balance: {self.balance:.2f}\n")
        except ValueError:
            print("Invalid amount. Please enter a number.")

    def withdraw(self):
        try:
            amount = float(input("Enter the amount you want to withdraw: "))
            if amount > self.balance:
                print("Insufficient funds!")
                return

            charges = 1.0 if amount < 100 else 2.0 if amount < 1000 else 8.0
            self.balance -= (amount + charges)
            print(f"\nNew balance: {self.balance:.2f}\n")
        except ValueError:
            print("Invalid amount. Please enter a number.")

    def action(self):
        options = ["view balance", "withdraw", "deposit", "quit"]
        while True:
            try:
                print("\nOptions:")
                for index, option in enumerate(options):
                    print(f"{index}: {option}")

                choice = int(input("Choose an option: "))
                if 0 <= choice < len(options):
                    return options[choice]
                else:
                    print("Invalid choice, try again.")
            except ValueError:
                print("Invalid input. Enter a number.")

    def bank(self, option):
        if option == "view balance":
            print(f"Balance: {self.balance:.2f}\n")
        elif option == "withdraw":
            self.withdraw()
        elif option == "deposit":
            self.deposit()

            


    
