from factory import CommonUser, ForeignUser

class CurrencyAdapter(CommonUser):
    def __init__(self, user: ForeignUser) -> None:
        super().__init__(user.name, user.balance)
        
    