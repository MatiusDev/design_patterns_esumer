from abc import ABC, abstractmethod
from domain.payment import Donation
from dtos.payment_dto import PaymentDTO

class PaymentFactory(ABC):
    @staticmethod
    @abstractmethod
    def create_payment(payment: PaymentDTO):
        raise NotImplementedError("Not implemented create payment method.")

class DonationFactory(PaymentFactory):
    @staticmethod
    def create_payment(payment: PaymentDTO):
        return Donation(payment.value)