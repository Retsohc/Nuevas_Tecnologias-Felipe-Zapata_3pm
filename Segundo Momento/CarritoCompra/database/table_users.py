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

    def _validar_campo_obligatorio(self, valor, campo):
        if not valor or not valor.strip():
            print(f"Error: {campo} no puede estar vacío.")
            return False
        return True

    def _validar_email(self, email):
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            print("Error: El formato del correo electrónico no es válido.")
            return False
        return True

    def _validar_nombre_usuario(self, username):
        username_lower = username.lower()
        if not re.match("^[a-zA-Z0-9]+$", username_lower):
            print("Error: El nombre de usuario debe contener solo letras y números.")
            return False

        self.cursor.execute("SELECT 1 FROM users WHERE LOWER(username) = %s LIMIT 1", (username_lower,))
        return not self.cursor.fetchone()

    def guardar_usuario(self, name, email, username, password, registration_date):
        name, email, username = name.lower(), email.lower(), username.lower()

        if all([
            self._validar_campo_obligatorio(name, 'Nombre'),
            self._validar_campo_obligatorio(email, 'Correo electrónico'),
            self._validar_campo_obligatorio(username, 'Nombre de usuario'),
            self._validar_campo_obligatorio(password, 'Contraseña'),
            self._validar_email(email),
            self._validar_nombre_usuario(username)
        ]):
            query = "INSERT INTO users (name, email, username, password, registration_date) VALUES (%s, %s, %s, %s, %s)"
            self.cursor.execute(query, (name, email, username, password, registration_date))
            self.connection.commit()
            print("Usuario creado correctamente.")
        else:
            print("Error: No se pudo crear el usuario debido a problemas en los datos.")

    def close_connection(self):
        super().close_connection()
        print("Conexión de la base de datos del carrito cerrada.")