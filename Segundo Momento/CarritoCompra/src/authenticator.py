from database.table_users import UserDatabase

class Authenticator:

    def __init__(self):
        self._user_db = UserDatabase() 
        self._logged_in = False
        self._current_user = None

    @property
    def user_db(self):
        return self._user_db 

    @property
    def logged_in(self):
        return self._logged_in 

    @property
    def current_user(self):
        return self._current_user 

    def authenticate(self, username, password):
        self.user_db.cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
        user_data = self.user_db.cursor.fetchone()

        if user_data:
            print("Inicio de sesión exitoso!")
            self._logged_in = True
            self._current_user = user_data
        else:
            print("Nombre de usuario o contraseña incorrectos.")

    def register(self, name, email, username, password, registration_date):
        self.user_db.guardar_usuario(name, email, username, password, registration_date)

    def login_or_register(self):
        while not self.logged_in:
            print("\n1. Iniciar sesión")
            print("2. Registrarse")
            print("0. Salir")

            choice = input("Ingrese el número de la opción deseada: ")

            if choice == "1":
                username = input("\nIngrese su nombre de usuario: ")
                password = input("Ingrese su contraseña: ")
                self.authenticate(username, password)
            elif choice == "2":
                name = input("\nIngrese nombre: ")
                email = input("Ingrese correo electrónico: ")
                username = input("Ingrese nombre de usuario: ")
                password = input("Ingrese contraseña: ")
                registration_date = input("Ingrese fecha de registro (AA/MM/DD): ")
                self.register(name, email, username, password, registration_date)
            elif choice == "0":
                print("\nSaliendo del programa. Hasta luego.")
                break
            else:
                print("Opción no válida. Por favor, elija una opción correcta.")