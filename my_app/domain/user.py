from abc import ABC, abstractmethod

class User(ABC):
    # Se usa un constructor en una interfaz de acuerdo a la flexibilidad de python
    # Este permite agrupar parametros en común de las subclases, algo así como un hibrido entre herencia e interfaz
    def __init__(self, name) -> None:
        self.id = None
        self.name = name
        self._is_logged = False

    @abstractmethod
    def login(self):
        pass

    @abstractmethod
    def logout(self):
        pass
        
class CommonUser(User):
    def __init__(self, name, currency, balance) -> None:
        self.currency = currency
        self.balance = balance
        super().__init__(name)

    def login(self):
        self._is_logged = True
        return self._is_logged

    def logout(self):
        self._is_logged = False
        return self._is_logged
        

class AdminUser(User):
    def __init__(self, name) -> None:
        # Tenica de composición, me permite que un administrador pueda ser usuario al mismo tiempo
        # En este código es necesario, ya que solo los usuarios regulares pueden hacer pagos
        self.user_profile = None
        super().__init__(name)

    def assign_common_profile(self, currency, balance):
        self.user_profile = CommonUser(self.name, currency, balance)
        self.user_profile.id = self.id
        self.user_profile._is_logged = self._is_logged
        return self.user_profile

    def login(self):
        self._is_logged = True
        return self._is_logged

    def logout(self):
        self._is_logged = False
        return self._is_logged