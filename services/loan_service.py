import random

class LoanService:
    def __init__(self, customer_repo, account_repo, loan_repo):
        self.customer_repo = customer_repo
        self.account_repo = account_repo
        self.loan_repo = loan_repo

    def apply_random(self):
        customer = self.customer_repo.random()
        amount = random.randint(1000, 10000)
        rate = random.uniform(3.0, 12.0)
        customer.balance += amount
        self.loan_repo.store(customer.name, amount, rate)
        print(f"{customer.name} взяв кредит {amount} під {rate:.2f}%")
