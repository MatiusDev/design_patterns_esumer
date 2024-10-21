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