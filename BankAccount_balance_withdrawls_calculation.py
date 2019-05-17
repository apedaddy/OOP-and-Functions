class Account():
    def __init__(self, owner, balance = 0):
    # Assign initial balance as 0
        self.owner = owner
        self.balance = balance

    def depost(self, deposit_amount):
        # Get existing balance and add new funds in it.
        self.balance += deposit_amount
        print (f"Added {deposit_amount} to the balance")
        print (f"Current balance is: {self.balance}")

    def withdrawls(self, withdrawl_amount=0):
        if self.balance >= withdrawl_amount:
            self.balance -= withdrawl_amount
            print (f"{withdrawl_amount} withdrawl is accepted")
            print (f"Remaining balance is: {self.balance}")
        else:
            print ("Sorry! Not enough funds in the account")

    def __str__(self):
        return f"Owner: {self.owner} \nBalance: {self.balance}"


print ("PROGRAM TO ACCEPT OWNER NAME AND BALANCE OF THE ACCOUNT")
print ("TAKES DEPOSIT, WITHDRAW, CALCULATE REMAINING BALANCE, CHECK IF WITHDRAW POSSIBLE?")

owner_name = str(input("\nEnter owner's name: "))
initial_balance = int(input("Enter initial balance: "))
account = Account(owner_name, initial_balance)

option = int(input("SELECT FROM FOLLOWING OPTION: \nDeposit Amount (1)\nWithdraw Money(2)\nQuit...(3)"))
if option ==1:
    dep_amount = int(input("\nEnter deposit amount"))
    account.depost(dep_amount)
elif option ==2:
    wtd_amount = int(input("\nEnter how much you wish to withdraw?"))
    account.withdrawls(wtd_amount)
elif option ==3:
    pass
else:
    print("\nInvalid input! Hence program quit")
    pass



