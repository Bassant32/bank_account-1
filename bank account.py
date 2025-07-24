import random
def check_account(name, balance):
    account = {"name": name, "balance": balance}
    print("User account:", account)

def deposite(balance):
    while True:
        try:
            amount = float(input("Enter amount to deposite: "))
            balance += amount
            break
        except ValueError:
            print("Invalid input. Please try again.")
    return balance

def withdraw(balance):
    while True:
        try:
            amount = float(input("Enter the amount to withdraw: "))
            if amount <= balance:
                balance -= amount
                break
            else:
                print("YOU EXCEEDED THE LIMIT OF YOUR BALANCE")
        except ValueError:
            print("INVALID INPUT.")
    return balance

def main():
    banks = ["bank MASR", "bank ESQUNDRIA", "bank alahly", "bank ALarabi_alefriki"]
    print("WELCOME TO", random.choice(banks))
    
    name = input("Enter your name: ")
    
    while True:
        try:
            balance = float(input("Enter your balance: "))
            break
        except ValueError:
            print("Invalid balance, try again.")
    
    while True:
        print("\nMAIN MENU")
        print("1: Check account")
        print("2: Deposite to balance")
        print("3: Withdraw from balance")
        print("4: Exit")
        
        try:
            entered_number = int(input("Enter a number from 1 to 4: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if entered_number == 1:
            check_account(name, balance)
        elif entered_number == 2:
            balance = deposite(balance)
            check_account(name, balance)
        elif entered_number == 3:
            balance = withdraw(balance)
            check_account(name, balance)
        elif entered_number == 4:
            check_account(name, balance)
            print("Thank you.")
            break
        else:
            print("Invalid number, try again.")

main()

