from .factory import CommonUser

COP_VALUE = 4241.62

class CurrencyAdapterToUSD(CommonUser):
    def __init__(self, user: CommonUser) -> None: 
        balance = user.balance / COP_VALUE
        currency = "US"
        super().__init__(user.name, currency, balance)

class CurrencyAdapterToCOP(CommonUser):
    def __init__(self, user: CommonUser) -> None: 
        balance = user.balance * COP_VALUE
        currency = "COP"
        super().__init__(user.name, currency, balance)
        
    