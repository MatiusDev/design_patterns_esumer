from design_patterns.factory import UserFactory
from design_patterns.observer import UserObserver

class UserService:
    def __init__(self, db_adapter) -> None:
        self.db_adapter = db_adapter
        self.observer = UserObserver()
    
    def create_user(self, user_type, name):
        user = UserFactory.create_user(user_type, name)
        self.db_adapter.execute_query(
			"INSERT INTO users (type, name) values(?, ?)", (user_type, name)
		)
        self.observer.notify(f"El usuario {name} tipo {user_type} ha sido creado correctamente...")
        return user
    
    def get_users(self):
        return self.db_adapter.fetch_data("SELECT * FROM users")
        