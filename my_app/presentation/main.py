import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")

from data.database import DataBaseAdapter
from services.user_service import UserService

def main(db_adapter):
    user_service = UserService(db_adapter)
    
    # Crear usuarios
    user_1 = user_service.create_user("administrador", "Bob Marley")
    user_2 = user_service.create_user("regular", "Paul McCartney")
    
    print(f"¨Usuarios nuevos {user_1.name} y {user_2.name}")
    
    # Mostrar usuarios creados
    users = user_service.get_users()
    print("Listado de usuarios")
    for (id, type, user) in users:
        print(f"[{id}]: {user} con rol {type}.")

    db_adapter.close_connection()

if __name__ == "__main__":
    db_adapter = DataBaseAdapter("users.db")
    db_adapter.execute_query(
        "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, type TEXT, name TEXT)"
    )
    main(db_adapter)