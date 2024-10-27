# Patron de diseño Factory (Creacional)
# Sirve para crear objetos de diferentes clases a través de una única fabrica (Fabrica de objetos)
# En este caso usamos una fabrica de usuarios y una fabrica de pagos
# y dentro de cada fabrica se crean los objetos de las clases correspondientes ayudandonos del tipo de usuario o de pago

from domain.user import AdminUser, CommonUser
from domain.payment import Donation

class UserFactory:
    @staticmethod
    def create_user(user_type, name, currency, balance):
        if user_type == "administrador":
            return AdminUser(name)
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