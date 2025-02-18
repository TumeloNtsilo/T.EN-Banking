from client import Client
import random


def greetings():
    print(f"Good day and welcome to {bank_name}.\n")

def new_account():
    print(f"Let us open a new account for you.\n")
    client_details = {} 
    print("Please fill in your information below")
    while True:
        try:
            name = input("Enter your full name: ")
            identity_num = int(input("Enter your ID number: "))
            address = input("Enter address in one line with spaces in between: ")
            tittle = input("Enter your tittle Mr, Miss, Ms, Mrs, or other: ")
            if len(str(identity_num)) != 13 or not identity_num.isdigit():
                print("Invalid ID number.")
                break   
        except:
            print("Invalid inputs")
        print()

        print(f"{tittle} {name}\n{identity_num}")
        for x in address.split(" "):
            print(x)
        confirmation = input(f"Are your details correct (yes/no)?: ").lower()
        if confirmation == "yes":
            global client
            client = Client

            print(f"\nHere is your account number: {client.account_num}")
            print(f"Here is your pin number, keep it safe and a secret: {client.pin_number}\n")
            client_details["name"] = f"{tittle} {name}"
            client_details["account number"] = client.account_num
            client_details["pin number"] = client.pin_number
            bank_clients.append(client_details)

        elif confirmation == "no":
            print("Please start over!")
            new_account()
        
        break

def use_account():
    print(f"Now, you can use your account")
    client.enter_pin()

    while True:
        client.action()
        if client.chosen_index == "quit":
            print("Thank you for banking with us.")
            break
        client.bank(client.chosen_index)


if __name__ == "__main__":
    bank_name = "T.EN Bank"
    bank_clients = []
    client = Client()

    greetings()
    new_account()
    use_account()
    client = Client()

    greetings()
    new_account()
    use_account()
