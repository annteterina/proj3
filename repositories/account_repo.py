from models.account import Account

class AccountRepository:
    def __init__(self):
        self.accounts = []

    def load_accounts(self, customers):
        for c in customers:
            self.accounts.append(Account(c.name, c.balance))
