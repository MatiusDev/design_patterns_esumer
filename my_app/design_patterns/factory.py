class User:
    def __init__(self, name) -> None:
        self.id = None
        self.name = name
        
class AdminUser(User):
    def __init__(self, name, currency, balance) -> None:
        self.currency = currency
        self.balance = balance
        super().__init__(name)
        
class CommonUser(User):
    def __init__(self, name, currency, balance) -> None:
        self.currency = currency
        self.balance = balance
        super().__init__(name)
  
class UserFactory:
    @staticmethod
    def create_user(user_type, name, currency, balance):
        if user_type == "administrador":
            return AdminUser(name, currency, balance)
        elif user_type == "regular":
            return CommonUser(name, currency, balance)
        else:
            raise ValueError("Tipo de usuario no permitido")
      
class PaymentFactory:
    @staticmethod
    def create_payment(payment_type, value):
        if payment_type == "donacion":
            return Donation(value)
        else:
            raise ValueError("Tipo de pago no permitido")

class Payment:
    def __init__(self, value = 10) -> None:
        self.id = None
        self.value = value
        self.completed = False   
  
class Donation(Payment):
    def __init__(self, value = 10) -> None:
        super().__init__(value)
    
    def donate(self, currency, balance):
        if (currency != "US"):
            return ValueError("La única moneda permitida para pagar es dolares")
        
        if (balance < self.value):
            return ValueError("No tienes fondos suficientes")
        
        new_balance = balance - self.value
        self.completed = True
        return new_balance