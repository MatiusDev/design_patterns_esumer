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