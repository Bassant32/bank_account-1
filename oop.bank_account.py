import random 
class bank_account :
    def __init__(self, name, balance):
       self.name=name
       self.balance=balance
    def check_account(self):
        account={"name":self.name,"balance":self.balance}
        print("user_account=",account)
    def deposite(self):
        while True:
            try :
                amount = float(input("enter the deposited amount :"))
                self.balance+=amount
                break
            except ValueError:
                 print("invalid input,try again")
    def withdraw(self):
        while True :
            try :
                amount=float(input("enter the withdrawed amount :"))
                if amount<=self.balance:
                    self.balance-=amount
                    break
                else:
                    print("you exceed the limit")
               
            except ValueError:
                print("invalid amount,try again")
    
def main ():
    bank = ["bank MASR", "bank ESQUNDRIA", "bank alahly", "bank ALarabi_alefriki"]
    print("WELCOME", random.choice(bank))
    name = input("Enter your name : ")
    while True :
        try :
            balance = float(input("enter your balance : "))
            break 
        except ValueError:
            print("invalid balance , try again ")
    account = bank_account(name,balance)
    while True :
        print("MAIN MENU")
        print("1: Check account")
        print("2: Deposit to balance")
        print("3: Withdraw from balance")
        print("4: Exit")
        entered_number = int(input("Enter a number from 1 to 4: "))

        if entered_number == 1:
            account.check_account()
        elif entered_number == 2:
            account.deposite()
            account.check_account()
        elif entered_number == 3:
            account.withdraw()
            account.check_account()
        elif entered_number == 4:
            account.check_account()
            print("Thank you.")

            break
        else:
            print("invalid number ,try again ")
main()           


