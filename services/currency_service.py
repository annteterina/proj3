import random

class CurrencyService:
    def __init__(self):
        self.rate = 40.0

    def random_update(self):
        change = random.uniform(-1, 1)
        self.rate += change
        print(f"Новий курс валюти: {self.rate:.2f}")
