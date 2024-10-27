# Patron de diseño Strategy (Comportamiento)
# Permite definir una familia de algoritmos, colocar cada uno de ellos en una clase separada y hacer sus objetos intercambiables.
# En términos más simples, este patrón permite la flexbilidad de usar diferentes estrategias para aplicarlas en el objeto principal
# En este caso usamos una familia de estrategias de pago, cada estrategia corresponde un medio de pago diferente que implementa la interfaz PaymentStrategy
# En la clase contexto o PaymentMethod vemos como usamos un objeto estrategia para realizar el pago, esto va permitir recibir diferentes estrategias (PSE, PayPal, Tarjeta de crédito)
# Y en el objeto instancia de PaymentMethod, enviar la estrategia que se desea usar para realizar el pago

from abc import ABC, abstractmethod

class PaymentStrategy(ABC):
    @abstractmethod
        def pay(self, amount):
            pass

class PSE(PaymentStrategy):
    def pay(self, amount):
        print(f"Pago PSE de ${amount}")

class PayPal(PaymentStrategy):
    def pay(self, amount):
        print(f"Pago PayPal de ${amount}")

class CreditCard(PaymentStrategy):
    def pay(self, amount):
        print(f"Pago tarjeta de crédito de ${amount}")

# Context
class PaymentMethod:
    def __init__(self, payment_method: PaymentStrategy):
        self._payment_method = payment_method

    @payment_method.setter
    def payment_method(self, payment_method: PaymentStrategy):
        self._payment_method = payment_method

    def pay(self, amount):
        self.payment_method.pay(amount)