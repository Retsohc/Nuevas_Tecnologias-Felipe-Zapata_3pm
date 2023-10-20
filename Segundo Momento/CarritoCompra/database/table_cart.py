import re
from src.database_connector import DatabaseConnector

class CartDatabase(DatabaseConnector):

    def mostrar_carrito(self):
        self.cursor.execute("SELECT * FROM cart")
        rows = self.cursor.fetchall()
        for row in rows:
            print(row)

    def verificar_existencia_producto_usuario(self, id_producto, id_user):
        self.cursor.execute("SELECT * FROM products WHERE product_id = %s", (id_producto,))
        product_row = self.cursor.fetchone()

        self.cursor.execute("SELECT * FROM users WHERE user_id = %s", (id_user,))
        user_row = self.cursor.fetchone()

        if product_row is None:
            print(f"Error: El producto con ID {id_producto} no existe en la base de datos.")
            return False

        if user_row is None:
            print(f"Error: El usuario con ID {id_user} no existe en la base de datos.")
            return False

        return True

    def agregar_al_carrito(self, id_producto, id_user, quantity, date_add):
        if self.verificar_existencia_producto_usuario(id_producto, id_user):
            self.cursor.execute("SELECT price, stock FROM products WHERE product_id = %s", (id_producto,))
            result = self.cursor.fetchone()

            if result:
                price, stock = result

                if stock >= quantity:
                    self.cursor.execute("INSERT INTO cart (id_product, id_user, quantity, date_add) VALUES (%s, %s, %s, %s)", (id_producto, id_user, quantity, date_add))
                    self.connection.commit()

                    new_stock = stock - quantity
                    self.cursor.execute("UPDATE products SET stock = %s WHERE product_id = %s", (new_stock, id_producto))
                    self.connection.commit()

                    return quantity * price
                else:
                    print("Error: La cantidad solicitada excede el stock disponible.")
            else:
                print("Error al obtener información del producto.")
        else:
            print("Por favor, ingrese ID de producto y usuario válidos.")
            return None

    def actualizar_carrito(self, cart_id, quantity, date_add):
        self.cursor.execute("SELECT id_product FROM cart WHERE cart_id = %s", (cart_id,))
        id_producto = self.cursor.fetchone()[0]

        self.cursor.execute("SELECT price FROM products WHERE product_id = %s", (id_producto,))
        price = self.cursor.fetchone()[0]

        # Elimina la línea que define la variable subtotal
        # subtotal = quantity * price

        self.cursor.execute("UPDATE cart SET quantity = %s, date_add = %s WHERE cart_id = %s", (quantity, date_add, cart_id))
        self.connection.commit()
        print("Elemento actualizado correctamente.")

    def buscar_en_carrito(self, cart_id):
        self.cursor.execute("SELECT * FROM cart WHERE cart_id = %s", (cart_id,))
        row = self.cursor.fetchone()
        if row:
            print(row)
        else:
            print("Elemento del carrito no encontrado")

    def eliminar_del_carrito(self, cart_id):
        self.cursor.execute("DELETE FROM cart WHERE cart_id = %s", (cart_id,))
        self.connection.commit()
        print("Elemento eliminado correctamente.")
        
    def close_connection(self):
        super().close_connection()
        print("Conexión de la base de datos del carrito cerrada.")