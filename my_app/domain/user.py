class User:
    def __init__(self, name) -> None:
        self.id = None
        self.name = name
        
class CommonUser(User):
    def __init__(self, name, currency, balance) -> None:
        self.currency = currency
        self.balance = balance
        super().__init__(name)

class AdminUser(User):
    def __init__(self, name) -> None:
        # Tenica de composición, me permite que un administrador pueda ser usuario al mismo tiempo
        # En este código es necesario, ya que solo los usuarios regulares pueden hacer pagos
        self.user_profile = None
        super().__init__(name)

    def assign_common_profile(self, currency, balance):
        self.user_profile = CommonUser(self.name, currency, balance)
        self.user_profile.id = self.id
        return self.user_profile