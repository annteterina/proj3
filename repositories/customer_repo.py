import random
from models.customer import Customer

class CustomerRepository:
    def __init__(self):
        self.customers = []

    def load_mock(self):
        self.customers = [
            Customer("Anna"), Customer("Oleh"),
            Customer("Sofa"), Customer("Ivan")
        ]

    def random(self):
        return random.choice(self.customers)

    def show(self):
        for c in self.customers:
            print(c)
