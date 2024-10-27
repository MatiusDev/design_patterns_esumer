# Patron de diseño Observer (Comportamiento)
# Sirve para notificar cambios en un objeto a sus observadores
# Para este caso usamos un observador general y dos observadores específicos
# El observador general es el que notificará los cambios a los observadores específicos a través del metodo notify
# En el proyecto se usa observer para notificar cuando hay cambios en un usuario o en un pago (CRUD)

class Observer:
    def __init__(self) -> None:
        self.notifications = []
        
    def notify(self, message):
        self.notifications.append(message)
        print(f"Notificación: {message}")

class UserObserver(Observer):
    pass

class PaymentObserver(Observer):
    pass