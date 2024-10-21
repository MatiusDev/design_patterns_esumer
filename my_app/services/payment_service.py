from design_patterns.factory import UserFactory, PaymentFactory, Payment, Donation
from design_patterns.observer import PaymentObserver
from design_patterns.adapter import CurrencyAdapterToUSD, CurrencyAdapterToCOP

class PaymentService:
    def __init__(self, db_adapter) -> None:
        self.db_adapter = db_adapter
        self.observer = PaymentObserver()
        
    def create_payment(self, payment_type, value):
        payment = PaymentFactory.create_payment(payment_type, value)
        self.db_adapter.execute_query(
			"INSERT INTO payments (type, value, status) values(?, ?, ?)", (payment_type, value, payment.completed)
		)
        payment.id = self.db_adapter.last_inserted_id()
        self.observer.notify(f"Se ha registrado un nuevo pago, transacción {payment.id}...")
        return payment

    def pay(self, user, payment):
        if user.currency == "US":
            if isinstance(payment, Donation):
                user.balance = payment.donate(user.currency, user.balance)
                self.db_adapter.execute_query(
                    "UPDATE users SET balance = ? WHERE id = ?", (user.balance, user.id)
                )
            else:
                raise ValueError("Tipo de pago no soportado.")
        elif user.currency == "COP":
            adapted_user = CurrencyAdapterToUSD(user)
            if isinstance(payment, Donation):
                adapted_user.balance = payment.donate(adapted_user.currency, adapted_user.balance)
                adapted_user = CurrencyAdapterToCOP(adapted_user)
                self.db_adapter.execute_query(
                    "UPDATE users SET balance = ? WHERE id = ?", (adapted_user.balance, user.id)
                )
            else:
                raise ValueError("Tipo de pago no soportado.")
        else:
            raise ValueError("Moneda no soportada.")

        self.db_adapter.execute_query(
            "UPDATE payments SET status = ? WHERE id = ?", (payment.completed, payment.id)
        )
        self.observer.notify(f"El pago {payment.id} ha sido completado correctamente...")
        return payment
    
    def get_payments(self):
        return self.db_adapter.fetch_data("SELECT * FROM payments")