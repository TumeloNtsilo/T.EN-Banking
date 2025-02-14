from client import Client
import random


def greetings():
    print(f"Welcome to {bank_name}.\n")


def bank():
    client_details = {}

    choices = ["Open a bank account", "Use an existing bank account"]
    for index, choice in enumerate(choices):
        print(f"{index}: {choice}")
    print()

    while True:
        try:
            banking_options = int(input(f"How can we help you: {list(enumerate(choices))}: "))
            if 0 <= banking_options < len(choices):
                break
            else:
                print("Invalid input, try again.")
        except ValueError:
            print("Invalid input, please enter a number")
        
    user_choice = choices[banking_options]
    print()


    if user_choice == choices[0]:
        print("Please fill your information below")
        while True:
            try:
                name = input("Enter your full name: ")
                identity_num = int(input("Enter your ID number: "))
                if len(str(identity_num)) != 13:
                    print("Invalid ID number.")
                    break
                sex = input("Enter your gender: ")
            except:
                print("Invalid inputs")
            print()

            pin_num = random.randint(1000, 9999)
            print(f"Here is your account number: {client.account_num}")
            print(f"Here is your pin number, keep it safe and a secret: {pin_num}\n")

            client_details["name"] = name
            client_details["account number"] = client.account_num
            bank_clients.append(client_details)
            break

    elif user_choice == choices[1]:
        client.enter_pin()
        client.display_account_details()

        while True:
            client.action()
            if client.chosen_index == "quit.":
                print("Thank you for banking with us.")
                break
            client.bank(client.chosen_index)

if __name__ == "__main__":
    bank_name = "T.EN Bank"
    bank_clients = []
    client = Client()
    
    greetings()
    bank()
