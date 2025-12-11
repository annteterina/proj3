class SimulationService:
    def __init__(self, customer_repo, account_repo, loan_service, deposit_service, trading_service, currency_service):
        self.customer_repo = customer_repo
        self.account_repo = account_repo
        self.loan_service = loan_service
        self.deposit_service = deposit_service
        self.trading_service = trading_service
        self.currency_service = currency_service

    def run(self):
        print("=== FULL BANK SIMULATION ===")
        self.customer_repo.load_mock()
        self.account_repo.load_accounts(self.customer_repo.customers)

        while True:
            print("\n1 - Loan process")
            print("2 - Deposit process")
            print("3 - Trading process")
            print("4 - Currency update")
            print("5 - Show customers")
            print("0 - Exit")
            c = input("> ")
            if c=='1': self.loan_service.apply_random()
            elif c=='2': self.deposit_service.apply_random()
            elif c=='3': self.trading_service.trade_random()
            elif c=='4': self.currency_service.random_update()
            elif c=='5': self.customer_repo.show()
            elif c=='0': break
            else: print("Invalid")
