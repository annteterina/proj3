class LoanRepository:
    def __init__(self):
        self.data = []

    def store(self, customer, amount, rate):
        self.data.append((customer, amount, rate))
