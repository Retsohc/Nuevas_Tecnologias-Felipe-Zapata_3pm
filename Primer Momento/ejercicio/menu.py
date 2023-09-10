import minijuego as minijuego
import tarjeta as tarjeta

database = {
    "usuario1": "contraseña1",
    "usuario2": "contraseña2"
}

def login():
    while True:
        usuario = input("Usuario: ")
        contraseña = input("Contraseña: ")
        
        if usuario in database and database[usuario] == contraseña:
            print("\n¡Inicio de sesión exitoso!")
            return usuario
        else:
            print("\nUsuario o contraseña incorrectos. ¿Deseas crear una cuenta?")
            crear_cuenta = input("1. Sí / 2. No: ")
            
            if crear_cuenta == '1':
                nuevo_usuario = input("Nuevo usuario: ")
                nueva_contraseña = input("Nueva contraseña: ")
                database[nuevo_usuario] = nueva_contraseña
                print("\nCuenta creada exitosamente.")
            else:
                print("\nVolviendo al inicio de sesión.\n")
def menu():
    print("\nMenú de opciones:")
    print("1. Opción 1")
    print("2. Tarjeta de crédito")
    print("3. Salir del menú")
    
    opcion = input("Selecciona una opción: ")
    return opcion
def main():
    usuario_actual = None
    
    while usuario_actual is None:
        usuario_actual = login()
    
    while True:
        opcion = menu()
        
        if opcion == '1':
            print("Opción 1 Minijuego.")
            minijuego.chances()
        elif opcion == '2':
            print("Accediendo a usar la tarjeta de crédito...")
            tarjeta.tarjeta_credito()
        elif opcion == '3':
            print("Cerrando sesión.")
            usuario_actual = None
            break
        else:
            print("Opción no válida. Por favor, selecciona una opción correcta.")
if __name__ == "__main__":
    main()