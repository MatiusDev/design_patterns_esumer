class User:
    def __init__(self, name) -> None:
        self.name = name
        
class AdminUser(User):
    def __init__(self, name) -> None:
        super().__init__(name)
        
class CommonUser(User):
    def __init__(self, name, balance) -> None:
        super().__init__(name)
        self.currency = "US"
        self.balance = balance
        
class ForeignUser(User):
    def __init__(self, name, currency, balance) -> None:
        super().__init__(name)
        self.currency = currency
        self.balance = balance
        
        
class UserFactory:
    @staticmethod
    def create_user(user_type, name):
        if user_type == "administrador":
            return AdminUser(name)
        elif user_type == "regular":
            return CommonUser(name)
        else:
            raise ValueError("Tipo de usuario no permitido")
      
class Payment:
    def __init__(self, value = 50000) -> None:
        self.value = value
        self.completed = False   
  
class Donation(Payment):
    def __init__(self, value = 50000) -> None:
        super().__init__(value)
    
    def donate(self, user: CommonUser):
        if (user.currency != "US"):
            return ValueError("La única moneda permitida es dolares")
        
        if (user.balance < self.value):
            return ValueError("No tienes fondos suficientes")
        
        new_balance = user.balance - self.value
        self.completed = True
        return new_balance