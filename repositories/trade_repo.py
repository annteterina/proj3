class TradeRepository:
    def __init__(self):
        self.data = []

    def store(self, customer, change):
        self.data.append((customer, change))
