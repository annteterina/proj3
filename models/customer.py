class Customer:
    def __init__(self, name):
        self.name = name
        self.balance = 10000

    def __str__(self):
        return f'{self.name} | Баланс: {self.balance:.2f}'
