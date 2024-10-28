from design_patterns.observer import UserObserver
from dtos.user_dto import UserDTO
from .utils.validation_service import validate_user_type

class UserService:
    def __init__(self, db_adapter) -> None:
        self.db_adapter = db_adapter
        self.observer = UserObserver()

    def create_user(self, user_type, name, currency = "US", balance = 0):
        # Se crea un DTO, ya que enviar los datos por separado en create_user representa un problema para la interfaz
        # Ya que los diferentes usuarios manejan varios tipos de datos diferentes
        # El DTO me permite transportar los datos y elegir que datos del objeto usar desde las clases
        user_dto = UserDTO(name, currency, balance)
        # Creo la fabrica dependiendo del tipo de usuario que se desee crear
        factory = validate_user_type(user_type)
        user = factory.create_user(user_dto)
        
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
        