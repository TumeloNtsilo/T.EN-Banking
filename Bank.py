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
            if len(str(identity_num)) != 13:
                print("Invalid ID number.")
                break
            tittle = input("Enter your tittle Mr, Miss, Ms, Mrs, or other: ")
        except:
            print("Invalid inputs")
        print()

        print(f"Here is your account number: {client.account_num}")
        print(f"Here is your pin number, keep it safe and a secret: {client.pin_number}\n")

        client_details["name"] = name
        client_details["account number"] = client.account_num
        client_details["pin number"] = client.pin_number
        bank_clients.append(client_details)
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
