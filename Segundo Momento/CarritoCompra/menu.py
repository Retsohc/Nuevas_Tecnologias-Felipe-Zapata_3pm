from src.authenticator import Authenticator
from src.product_menu import ProductMenu
from src.cart_menu import CartMenu
from database.table_products import ProductDatabase
from database.table_cart import CartDatabase

class MenuApp:

    def __init__(self):
        self._authenticator = Authenticator()
        self._product_db = ProductDatabase()
        self._cart_db = CartDatabase()
        self._product_menu = ProductMenu(self._product_db)
        self._cart_menu = CartMenu(self._cart_db)

    @property
    def authenticator(self):
        return self._authenticator

    @property
    def product_db(self):
        return self._product_db

    @property
    def cart_db(self):
        return self._cart_db

    @property
    def product_menu(self):
        return self._product_menu

    @property
    def cart_menu(self):
        return self._cart_menu

    def run(self):
        self.authenticator.login_or_register()

        if self.authenticator.logged_in:
            self.show_menu()

    def show_menu(self):
        menu_options = {
            "1": lambda: self.product_menu.show_menu(),
            "2": lambda: self.cart_menu.show_menu(),
            "0": lambda: print("Saliendo del programa. Hasta luego."),
        }

        while True:
            print("\nMenú Principal:\n")
            print("1. Opciones de Producto")
            print("2. Opciones de Carrito")
            print("0. Salir")

            choice = input("Ingrese el número de la opción deseada: ")

            callback = menu_options.get(choice, lambda: print("Opción no válida. Por favor, elija una opción correcta."))
            callback()

            if choice == "0":
                break

if __name__ == "__main__":
    app = MenuApp()
    app.run()