# Example 42 - Banking program

def show_balance(balance: float):
    print(f"Account balance: ${balance:.2f}")


def deposit(balance):
    amount = input("Enter your deposit: ")

    if amount.isdigit():
        amount = float(amount)

        if amount < 0:
            print("Amount can't be lower then zero")
            return 0
        else:
            return amount
    else:
        print("Invalid amount")


def withdraw(balance):

    amount = input("How much do you want to withdraw: ")

    try:
        amount = float(amount)
    except Exception as e:
        print(f"Invalid amount: {e}")
        return 0

    if amount > balance:
        print("Insufficient funds")
        return 0
    elif amount < 0:
        print(f"Amount can't be lower then zero")
        return 0
    else:
        return amount

def main():
    balance = 0
    choice = ""

    print("******************************")
    print("         Bank Account         ")
    print("******************************")
    print("Options:\n1 - Show account balance\n"
          "2 - Deposit\n3 - Withdraw\n4 - Exit")

    while choice != "4":
        choice = input("Choose one option: ")
        match choice:
            case "1":
                show_balance(balance)
            case "2":
                balance += deposit(balance)
            case "3":
                balance -= withdraw(balance)
            case "4":
                print("Good bye. Have a nice day!")
            case _:
                print("Invalid option")


if __name__ == "__main__":
    main()
    