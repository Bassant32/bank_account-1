import random 
bank = ["bank MASR", "bank ESQUNDRIA", "bank alahly", "bank ALarabi_alefriki"]
print("WELCOME", random.choice(bank))
def main():
   account = {}
   account["Name"] = input("ENTER YOUR NAME: ")
   while True:
    print("MAIN MENU")
    print("1: Check account")
    print("2: Deposit to balance")
    print("3: Withdraw from balance")
    print("4: Exit")
    entered_number = int(input("Enter a number from 1 to 4: "))

    if entered_number == 1:
        account=check_account(account)
    elif entered_number == 2:
        account["balance"] = deposit()
        check_account()
    elif entered_number == 3:
        account["balance"] = withdraw()
        check_account()
    elif entered_number == 4:
        print("Thank you.")
        break
    else:
        print("You entered a wrong digit1 that is not included in the list.")

main()

def check_account():
    account ={"name":name , "balance":balance}
    print(account)
def deposit():
    try:
        amount = float(input("Enter amount to deposit: "))
        account["balance"]+= amount
    except ValueError:
        print("INVALID. Please try again.")
    return account["balance"]
def withdraw():
    try:
        amount = float(input("Enter the amount to withdraw: "))
        if amount <= accout["balance"]:
           accout["balance"] -= amount
        else:
            print("YOU EXCEEDED THE LIMIT OF YOUR BALANCE")
    except ValueError:
        print("INVALID INPUT.")
    return accout["balance"]
    