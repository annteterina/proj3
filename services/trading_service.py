import random

class TradingService:
    def __init__(self, customer_repo, account_repo, trade_repo, currency_service):
        self.customer_repo = customer_repo
        self.account_repo = account_repo
        self.trade_repo = trade_repo
        self.currency_service = currency_service

    def trade_random(self):
        customer = self.customer_repo.random()
        delta = random.randint(-300, 300)
        rate = self.currency_service.rate
        adj = delta * rate
        customer.balance += adj
        self.trade_repo.store(customer.name, adj)
        print(f"{customer.name} торговав: зміна {adj:.2f} за курсом {rate:.2f}")
