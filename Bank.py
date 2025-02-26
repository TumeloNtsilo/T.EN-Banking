from client import Client

def greetings():
    print(f"Good day and welcome to {bank_name}.\n")

def new_account():
    print(f"Let us open a new account for you.\n")
    client_details = {} 

    while True:
        try:
            name = input("Enter your full name: ")
            identity_num = input("Enter your ID number (13 digits): ")
            address = input("Enter your address in one line with spaces: ")

            if len(identity_num) != 13 or not identity_num.isdigit():
                print("Invalid ID number. It must be 13 digits.\n")
                continue  # Restart loop instead of recursive call

            title = input("Enter your title (Mr, Miss, Ms, Mrs, or other): ")
            print(f"\n{title} {name}\nID: {identity_num}")
            print("\n".join(address.split(" ")))  # Print address parts

            confirmation = input("\nAre your details correct (yes/no)?: ").strip().lower()
            if confirmation == "yes":
                break
            else:
                print("Please start over.\n")

        except Exception:
            print("Invalid inputs, please try again.")

    client_details["name"] = f"{title} {name}"
    client_details["account number"] = client.account_num
    client_details["pin number"] = client.pin_number
    bank_clients.append(client_details)

    print(f"\nHere is your account number: {client.account_num}")
    print(f"Here is your PIN number. Keep it safe and secret: {client.pin_number}\n")

def use_account():
    print(f"\nNow, you can use your account")

    if not client.enter_pin():  # Stop if PIN verification fails
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

