teller = raw_input("Do you want to withdraw or deposit money?")
# # account = raw_input("To/From which Account?")

withdraw_amount = 0
deposit_amount = 0

if (teller == "withdraw"):
    withdraw_amount = int(raw_input("How much do you want to withdraw from your account?"))

if (teller = "deposit"):
    deposit_amount = raw_input("How much do you want to put in your account?")

# funds = int(raw_input("How much do you want to withdraw?"))

class BankAccount(object):
    def __init__(self, name, accountbalance):
            self.name = name
            self.accountbalance = accountbalance
    def withdraw(self, accountbalance):
            self.accountbalance -= withdraw_amount
            return self.accountbalance
    def deposit(self, accountbalance):
            self.accountbalance += deposit_amount
            return self.accountbalance

Checking = BankAccount("business account", 778)
Savings = BankAccount("Rainy Day Fund", 2000)

print Checking.withdraw(200)