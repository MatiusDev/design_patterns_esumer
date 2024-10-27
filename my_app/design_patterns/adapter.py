# Patron de diseño Adapter (Estructural)
# Permite que dos clases que no son compatibles puedan interactuar entre sí o en su defecto objetos de una clase que no es compatible para una acción
# En este caso usamos el adapter para convertir una moneda a otra, ya que el sistema solo permite pagos en US
# Para permitir el pago, se adapta las otras monedas a US y se realiza el pago
# Otro ejemplo: Un sistema que maneje solo archivos XML y desee usar archivos JSON, los JSON serán adaptados

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