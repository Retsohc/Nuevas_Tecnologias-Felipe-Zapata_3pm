import psycopg2

class DatabaseConnector:
    def __init__(self, database="CarritoCompra", user="postgres", password="S3rv3r", host="localhost", port="5432"):
        try:
            self._connection = psycopg2.connect(
                database=database,
                user=user,
                password=password,
                host=host,
                port=port
            )
            self._cursor = self._connection.cursor()
            #print("Conexión exitosa!")
        except Exception as ex:
            print(ex)

    def close_connection(self):
        if hasattr(self, '_cursor') and self._cursor:
            self._cursor.close()
        if hasattr(self, '_connection') and self._connection:
            self._connection.close()
            print("Conexión cerrada.")

    @property
    def connection(self):
        return self._connection

    @property
    def cursor(self):
        return self._cursor

    def execute_query(self, query):
        try:
            self._cursor.execute(query)
            self._connection.commit()
            print("Consulta ejecutada exitosamente!")
        except Exception as ex:
            print(ex)

if __name__ == "__main__":
    connector = DatabaseConnector()

    query = "SELECT * FROM tabla"
    connector.execute_query(query)
    
    connector.close_connection()
