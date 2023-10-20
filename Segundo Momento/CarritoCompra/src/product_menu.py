from database.table_products import ProductDatabase

class ProductMenu:

    def __init__(self, product_db):
        self._product_db = product_db

    @property
    def product_db(self):
        return self._product_db

    def show_menu(self):
        while True:
            print("\nOpciones de Producto:\n")
            print("1. Mostrar productos")
            print("2. Crear producto")
            print("3. Actualizar producto")
            print("4. Buscar producto")
            print("5. Eliminar producto")
            print("0. Volver al menú principal")

            choice = input("Ingrese el número de la opción deseada: ")

            if choice == "1":
                self.product_db.mostrar_productos()
            elif choice == "2":
                name = input("\nIngrese el nombre del producto: ")
                price = float(input("Ingrese el precio del producto: "))
                stock = int(input("Ingrese el stock del producto: "))
                self.product_db.crear_producto(name, price, stock)
            elif choice == "3":
                producto_id = int(input("\nIngrese el ID del producto a actualizar: "))
                new_name = input("Ingrese el nuevo nombre del producto: ")
                new_price = float(input("Ingrese el nuevo precio del producto: "))
                new_stock = int(input("Ingrese el nuevo stock del producto: "))
                self.product_db.actualizar_producto(producto_id, new_name, new_price, new_stock)
            elif choice == "4":
                producto_id = int(input("\nIngrese el ID del producto a buscar: "))
                self.product_db.buscar_producto(producto_id)
            elif choice == "5":
                producto_id = int(input("\nIngrese el ID del producto a eliminar: "))
                self.product_db.eliminar_producto(producto_id)
            elif choice == "0":
                print("\nVolviendo al menú principal.")
                break
            else:
                print("Opción no válida. Por favor, elija una opción correcta.")