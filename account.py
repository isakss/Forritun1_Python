class Account(object):
    def __init__(self, balance):
        self._balance = balance
    
    def __str__(self):
        return "Balance: {:.2f}".format(self._balance)

class SavingsAccount(Account):
    INTERST_RATE = 0.05
    BONUS_RATE = 0.10

    def update_balance(self):
        self._balance = self._balance * (1 + self.INTERST_RATE + self.BONUS_RATE)

class DebitAccount(Account):
    INTEREST_RATE = 0.02

    def update_balance(self):
        self._balance = self._balance * (1 + self.INTEREST_RATE)






def print_accounts(accounts):
    for account in accounts:
        print(account)
    print()

def update_accounts(accounts):
    for account in accounts:
        account.update_balance()

sav1 = SavingsAccount(1000)
deb1 = DebitAccount(1000)
sav2 = SavingsAccount(2000)
deb2 = DebitAccount(4000)

accounts = [sav1, deb1, sav2, deb2]
print_accounts(accounts)
update_accounts(accounts)

print_accounts(accounts)
update_accounts(accounts)

print_accounts(accounts)
update_accounts(accounts)

print_accounts(accounts)