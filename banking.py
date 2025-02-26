from bank import Bank

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
                print("Invalid ID number.\nPlease start over.")
                continue

            tittle = input("Enter your tittle Mr, Miss, Ms, Mrs, or other: ")
            address = input("Enter address in one line with spaces in between: ")

            
            print(f"\n{tittle} {name}\n{identity_num}")
            for x in address.split(" "):
                print(x)
            confirmation = input(f"\nAre your details correct (yes/no)?: ").lower()
            if confirmation == "yes":
                break
                

            elif confirmation == "no":
                print(f"Please start over!\n")
            
        except:
            print("Invalid inputs")
        

    client_details["name"] = f"{tittle} {name}"
    client_details["account number"] = client.account_num
    client_details["pin number"] = client.pin_number
    bank_clients.append(client_details)

    print(f"\nHere is your account number: {client.account_num}")
    print(f"Here is your pin number, keep it safe and a secret: {client.pin_number}\n")


def use_account():
    print(f"\nNow, you can use your account")

    if not client.enter_pin(): 
        return

    client.display_account_details()

    while True:
        option = client.action()
        if option == "quit":
            print("\nThank you for banking with us.")
            break
        client.bank(option)

if __name__ == "__main__":
    bank_name = "T.EN Bank"
    bank_clients = []
    client = Client()

    greetings()
    new_account()
    use_account()

