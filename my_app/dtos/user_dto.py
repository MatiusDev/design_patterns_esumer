class UserDTO:
    def __init__(self, name, currency="US", balance=0) -> None:
        self.name = name
        self.currency = currency
        self.balance = balance