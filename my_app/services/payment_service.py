from design_patterns.factory import UserFactory, PaymentFactory
from design_patterns.observer import PaymentObserver
from design_patterns.adapter import CurrencyAdapter

from domain.payment import Donation
from domain.user import CommonUser

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

    def pay(self, user: CommonUser, payment):
        try:
            if payment.completed:
                raise ValueError("El pago ya ha sido completado.")

            if not isinstance(user, CommonUser):
                raise ValueError("Solo los usuarios regulares pueden realizar pagos.")

            currency_adapter = CurrencyAdapter(user)
            adapted_user = currency_adapter.adapt_to_usd()

            if isinstance(payment, Donation):
                adapted_user.balance = payment.donate(adapted_user.currency, adapted_user.balance)
                
                if user.currency != "US":
                    currency_adapter = CurrencyAdapter(adapted_user)
                    adapted_user = currency_adapter.adapt_to_other_currency(user.currency)

                self.db_adapter.execute_query(
                    "UPDATE users SET balance = ? WHERE id = ?", (adapted_user.balance, user.id)
                )
            else:
                raise ValueError("Tipo de pago no soportado.")
            self.db_adapter.execute_query(
                "UPDATE payments SET status = ? WHERE id = ?", (payment.completed, payment.id)
            )
            self.observer.notify(f"El pago {payment.id} ha sido completado correctamente...")
            return payment
        except ValueError as e:
            self.observer.notify(f"Error al procesar el pago: {str(e)}")
            return None
    
    def get_payments(self):
        return self.db_adapter.fetch_data("SELECT * FROM payments")