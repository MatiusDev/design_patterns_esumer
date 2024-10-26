from design_patterns.factory import UserFactory
from design_patterns.observer import UserObserver

class UserService:
    def __init__(self, db_adapter) -> None:
        self.db_adapter = db_adapter
        self.observer = UserObserver()

    def create_user(self, user_type, name, currency = "US", balance = 0):
        user = UserFactory.create_user(user_type, name, currency, balance)
        self.db_adapter.execute_query(
			"INSERT INTO users (type, name, currency, balance) values(?, ?, ?, ?)", (user_type, name, currency, balance)
		)
        user.id = self.db_adapter.last_inserted_id()
        self.observer.notify(f"El usuario {name} tipo {user_type} ha sido creado correctamente...")
        return user
    
    def update_user(self, user_id, user):
        self.db_adapter.execute_query(
			"UPDATE users SET name = ?, currency = ?, balance = ? WHERE id = ?", (user.name, user.currency, user.balance, user_id)
		)
        self.observer.notify(f"El usuario {user.name} ha sido actualizado correctamente...")
        return user


    def get_users(self):
        return self.db_adapter.fetch_data("SELECT * FROM users")
        