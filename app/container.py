from services.simulation_service import SimulationService
from services.loan_service import LoanService
from services.deposit_service import DepositService
from services.trading_service import TradingService
from repositories.customer_repo import CustomerRepository
from repositories.account_repo import AccountRepository
from repositories.loan_repo import LoanRepository
from repositories.deposit_repo import DepositRepository
from repositories.trade_repo import TradeRepository
from services.currency_service import CurrencyService

class Container:
    def __init__(self):
        self.customer_repo = CustomerRepository()
        self.account_repo = AccountRepository()
        self.loan_repo = LoanRepository()
        self.deposit_repo = DepositRepository()
        self.trade_repo = TradeRepository()
        self.currency_service = CurrencyService()

        self.loan_service = LoanService(self.customer_repo, self.account_repo, self.loan_repo)
        self.deposit_service = DepositService(self.customer_repo, self.account_repo, self.deposit_repo)
        self.trading_service = TradingService(self.customer_repo, self.account_repo, self.trade_repo, self.currency_service)

        self.sim_service = SimulationService(self.customer_repo, self.account_repo,
                                             self.loan_service, self.deposit_service,
                                             self.trading_service, self.currency_service)

    def simulation(self):
        return self.sim_service
