import re
from src.database_connector import DatabaseConnector

class ProductDatabase(DatabaseConnector):

    def __init__(self):
        super().__init__()

    @property
    def cursor(self):
        return self._cursor

    @property
    def connection(self):
        return self._connection

    def mostrar_productos(self):
        self.cursor.execute("SELECT * FROM products")
        rows = self.cursor.fetchall()
        for row in rows:
            print(row)

    def _validar_nombre_producto(self, name):
        self.cursor.execute("SELECT * FROM products WHERE name = %s", (name,))
        existing_product = self.cursor.fetchone()
        return existing_product is None
    
    def crear_producto(self, name, price, stock):
        if not self._validar_nombre_producto(name):
            print("Error: Ya existe un producto con el mismo nombre.")
            return

        self.cursor.execute("INSERT INTO products (name, price, stock) VALUES (%s, %s, %s)", (name, price, stock))
        self.connection.commit()
        print("Producto agregado correctamente.")

    def actualizar_producto(self, producto_id, new_name, new_price, new_stock):
        if not self._validar_nombre_producto(new_name):
            print("Error: Ya existe un producto con el mismo nombre.")
            return

        self.cursor.execute("UPDATE products SET name = %s, price = %s, stock = %s WHERE product_id = %s",(new_name, new_price, new_stock, producto_id))
        self.connection.commit()
        print("Producto actualizado correctamente.")

    def buscar_producto(self, producto_id):
        self.cursor.execute("SELECT * FROM products WHERE product_id = %s", (producto_id,))
        row = self.cursor.fetchone()
        if row:
            print(row)
        else:
            print("Producto no encontrado")

    def eliminar_producto(self, producto_id):
        self.cursor.execute("DELETE FROM products WHERE product_id = %s", (producto_id,))
        self.connection.commit()
        print("Producto eliminado correctamente.")


