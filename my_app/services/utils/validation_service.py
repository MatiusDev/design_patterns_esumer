from design_patterns.factory.user_factory import CommonUserFactory, AdminUserFactory
from design_patterns.factory.payment_factory import DonationFactory

USER_FACTORIES = {
    "administrador": AdminUserFactory,
    "regular": CommonUserFactory
}

PAYMENT_FACTORIES = {
    "donacion": DonationFactory
}

def validate_user_type(user_type):
    if user_type not in USER_FACTORIES:
        raise ValueError("Tipo de usuario no permitido")
    return USER_FACTORIES[user_type]

def validate_payment_type(payment_type):
    if payment_type not in PAYMENT_FACTORIES:
        raise ValueError("Tipo de pago no permitido")
    return PAYMENT_FACTORIES[payment_type]