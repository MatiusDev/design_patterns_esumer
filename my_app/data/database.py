import sqlite3

class DataBaseAdapter:
    def __init__(self, db_name) -> None:
        # Crea la conexión SQL
        self.connection = sqlite3.connect(db_name)
        # Objeto que permite crear, listar
        self.cursor = self.connection.cursor() 
        
    def execute_query(self, query, params=()):
        self.cursor.execute(query, params)
        self.connection.commit()
        
    def fetch_data(self, query, params=()):
        self.cursor.execute(query, params)
        # Me devuelve toda la data solicitada en el query anterior
        return self.cursor.fetchall()

    def last_inserted_id(self):
        return self.cursor.lastrowid
    
    def close_connection(self):
        self.connection.close()