from domain.user import CommonUser

class CurrencyAdapter:
    COP_VALUE = 4263.90
    MX_VALUE = 19.96

    def __init__(self, user: CommonUser) -> None: 
        self.user = user

    def adapt_to_usd(self): 
        adapted_user = self.user
        if (self.user.currency != "US"):
            balance = self.user.balance / self.COP_VALUE
            adapted_user = CommonUser(self.user.name, "US", balance)
        return adapted_user

    def adapt_to_other_currency(self, currency_origin):
        if (currency_origin == "US"):
            return self.user

        adapted_user = self.user
        if (currency_origin == "COP"):
            balance = self.user.balance * self.COP_VALUE
            adapted_user = CommonUser(self.user.name, "COP", balance)
        elif (currency_origin == "MX"):
            balance = self.user.balance * self.MX_VALUE
            adapted_user = CommonUser(self.user.name, "MX", balance)
        else:
            raise ValueError("Tipo de moneda no soportada")
        return adapted_user