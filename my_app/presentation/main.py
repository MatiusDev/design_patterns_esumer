import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")

from data.database import DataBaseAdapter
from services.user_service import UserService
from services.payment_service import PaymentService

def main(db_adapter):
    user_service = UserService(db_adapter)
    payment_service = PaymentService(db_adapter)

    # Crear usuarios
    admin_user_1 = user_service.create_user("administrador", "Bob Marley")
    user_1 = admin_user_1.assign_common_profile("US", 50)
    user_service.update_user(user_1.id, user_1)

    user_2 = user_service.create_user("regular", "Paul McCartney", "COP", 500000)
    user_3 = user_service.create_user("regular", "John Lennon", "COP", 1000000)

    admin_user_4 = user_service.create_user("administrador", "Michael Jackson")
    user_4 = admin_user_4.assign_common_profile("COP", 1000000)
    user_service.update_user(user_4.id, user_4)

    admin_user_5 = user_service.create_user("administrador", "Freddy Mercury")
    user_5 = admin_user_5.assign_common_profile("COP", 2000000)
    user_service.update_user(user_5.id, user_5)

    # Listando los usuarios
    print(f"Usuario nuevo {user_1.name} - Balance inicial: {user_1.balance}")
    print(f"Usuario nuevo {user_2.name} - Balance inicial: {user_2.balance}")
    print(f"Usuario nuevo {user_3.name} - Balance inicial: {user_3.balance}")
    print(f"Usuario nuevo {user_4.name} - Balance inicial: {user_4.balance}")
    print(f"Usuario nuevo {user_5.name} - Balance inicial: {user_5.balance}")
    print("")

    # Payments
    payment_1 = payment_service.create_payment("donacion", 10)
    payment_service.pay(user_1, payment_1)

    payment_2 = payment_service.create_payment("donacion", 20)
    payment_service.pay(user_2, payment_2)

    payment_3 = payment_service.create_payment("donacion", 50)
    payment_service.pay(user_3, payment_3)

    payment_4 = payment_service.create_payment("donacion", 100)
    payment_service.pay(user_4, payment_4)

    # Intento de pago con error, no se puede realizar el pago por ser administrador
    payment_5 = payment_service.create_payment("donacion", 200)
    payment_service.pay(admin_user_5, payment_5)

    # Mostrar pagos creados
    payments = payment_service.get_payments()

    # Listando los pagos
    print("Listado de pagos")
    for (id, type, value, completed) in payments:
        print(f"[{id}]: {value} {type} con estado {completed}")
    print("")

    # Listando el saldo de usuarios despues del pago
    users = user_service.get_users()
    print("Listado de usuarios")
    for (id, type, user, currency, balance) in users:
        print(f"[{id}]: {user} con rol {type}.")
        print(f"Moneda: {currency}. Balance: {balance}")
    print("")

    db_adapter.close_connection()

if __name__ == "__main__":
    db_adapter = DataBaseAdapter("users.db")
    db_adapter.execute_query(
        "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, type TEXT, name TEXT, currency TEXT, balance REAL)"
    )
    db_adapter.execute_query(
        "CREATE TABLE IF NOT EXISTS payments (id INTEGER PRIMARY KEY, type TEXT, value REAL, status INTEGER)"
    )
    main(db_adapter)