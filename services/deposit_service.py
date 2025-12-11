import random

class DepositService:
    def __init__(self, customer_repo, account_repo, deposit_repo):
        self.customer_repo = customer_repo
        self.account_repo = account_repo
        self.deposit_repo = deposit_repo

    def apply_random(self):
        customer = self.customer_repo.random()
        amount = random.randint(500, 5000)
        if customer.balance >= amount:
            customer.balance -= amount
            rate = random.uniform(2.0, 5.0)
            self.deposit_repo.store(customer.name, amount, rate)
            print(f"{customer.name} відкрив депозит {amount} під {rate:.2f}%")
        else:
            print(f"{customer.name} не має достатньо коштів")
