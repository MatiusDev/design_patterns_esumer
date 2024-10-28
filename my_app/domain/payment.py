from abc import ABC, abstractmethod

class Payment(ABC):
    def __init__(self, value = 10) -> None:
        self.id = None
        self.value = value
        self._completed = False  

    @abstractmethod
    def pay(self, currency, balance):
        pass
  
class Donation(Payment):
    def __init__(self, value = 10) -> None:
        super().__init__(value)
    
    def pay(self, currency, balance):
        if (currency != "US"):
            return ValueError("La única moneda permitida para pagar es dolares")
        
        if (balance < self.value):
            return ValueError("No tienes fondos suficientes")
        
        new_balance = balance - self.value
        self._completed = True
        return new_balance

    def completed(self):
        return self._completed