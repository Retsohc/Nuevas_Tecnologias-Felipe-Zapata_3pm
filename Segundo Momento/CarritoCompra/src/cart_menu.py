from database.table_cart import CartDatabase

class CartMenu:

    def __init__(self, cart_db):
        self._cart_db = cart_db

    @property
    def cart_db(self):
        return self._cart_db 

    def show_menu(self):
        while True:
            print("\nOpciones de Carrito:")
            print("1. Mostrar carrito")
            print("2. Agregar al carrito")
            print("3. Actualizar carrito")
            print("4. Buscar en el carrito")
            print("5. Eliminar del carrito")
            print("0. Volver al menú principal")

            choice = input("Ingrese el número de la opción deseada: ")

            if choice == "1":
                self.cart_db.mostrar_carrito()
            elif choice == "2":
                id_producto = int(input("\nIngrese el ID del producto: "))
                id_user = int(input("Ingrese el ID del usuario: "))
                quantity = int(input("Ingrese la cantidad: "))
                date_add = input("Ingrese la fecha de agregado (AA/MM/DD): ")
                self.cart_db.agregar_al_carrito(id_producto, id_user, quantity, date_add)
                print("Elemento agregado correctamente.")
            elif choice == "3":
                cart_id = int(input("\nIngrese el ID del elemento en el carrito a actualizar: "))
                quantity = int(input("Ingrese la nueva cantidad: "))
                date_add = input("Ingrese la nueva fecha de agregado (AA/MM/DD): ")
                self.cart_db.actualizar_carrito(cart_id, quantity, date_add)
            elif choice == "4":
                cart_id = int(input("\nIngrese el ID del elemento en el carrito a buscar: "))
                self.cart_db.buscar_en_carrito(cart_id)
            elif choice == "5":
                cart_id = int(input("\nIngrese el ID del elemento en el carrito a eliminar: "))
                self.cart_db.eliminar_del_carrito(cart_id)
            elif choice == "0":
                print("\nVolviendo al menú principal.")
                break
            else:
                print("Opción no válida. Por favor, elija una opción correcta.")