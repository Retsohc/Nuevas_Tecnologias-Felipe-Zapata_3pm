import re
from src.database_connector import DatabaseConnector

class UserDatabase(DatabaseConnector):

    def __init__(self):
        super().__init__()

    @property
    def cursor(self):
        return self._cursor

    @property
    def connection(self):
        return self._connection

    def mostrar_usuarios(self):
        self.cursor.execute("SELECT * FROM users")
        rows = self.cursor.fetchall()
        for row in rows:
            print(row)

    def _validar_nombre_usuario(self, username):
        username_lower = username.lower()
        if not re.match("^[a-zA-Z0-9]+$", username_lower):
            print("Error: El nombre de usuario debe contener solo letras y números.")
            return False

        self.cursor.execute("SELECT * FROM users WHERE LOWER(username) = %s", (username_lower,))
        existing_user = self.cursor.fetchone()

        return not existing_user
    
    def guardar_usuario(self, name, email, username, password, registration_date):
        if self._validar_nombre_usuario(username):
            self.cursor.execute("INSERT INTO users (name, email, username, password, registration_date) VALUES (%s, %s, %s, %s, %s)", (name, email, username, password, registration_date))
            self.connection.commit()
            print("Usuario creado correctamente.")
        else:
            print("Error: El nombre de usuario ya existe.")

    def actualizar_usuario(self, user_id, new_name, new_email, new_username, new_password, new_date_registro):
        if self._validar_nombre_usuario(new_username):
            self.cursor.execute("UPDATE users SET name = %s, email = %s, username = %s, password = %s, registration_date = %s WHERE user_id = %s", (new_name, new_email, new_username, new_password, new_date_registro, user_id))
            self.connection.commit()
            print("Usuario actualizado correctamente.")
        else:
            print("Error: El nuevo nombre de usuario ya existe.")

    def buscar_usuario(self, user_id):
        self.cursor.execute("SELECT * FROM users WHERE user_id = %s", (user_id,))
        row = self.cursor.fetchone()
        if row:
            print(row)
        else:
            print("Usuario no encontrado")

    def eliminar_usuario(self, user_id):
        self.cursor.execute("DELETE FROM users WHERE user_id = %s", (user_id,))
        self.connection.commit()
        print("Usuario eliminado correctamente.")
        
    def close_connection(self):
        super().close_connection()
        print("Conexión de la base de datos del carrito cerrada.")