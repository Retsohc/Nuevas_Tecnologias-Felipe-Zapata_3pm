usuarios = []
prestamos = []

def registrar_usuario():
    nombre = input("\nIngrese el nombre del usuario: ")
    numero_tarjeta = int(input("Ingrese el número de tarjeta del usuario: "))
    usuario = {"nombre": nombre, "numero_tarjeta": numero_tarjeta}
    usuarios.append(usuario)
    print("Registro finalizado con éxito!...")


def prestar_bicicleta():
    
    conti = True

    if conti:
        bicicleta_disponible = 0
        numero_tarjeta = int(input("Ingresar número tarjeta de usuario: "))
        usuario = next((u for u in usuarios if u["numero_tarjeta"] == numero_tarjeta), None)
        if usuario:
            bicicleta_disponible += 1
            origen = input("Ingrese la estación de origen: ")
            destino = input("Ingrese la estación de destino: ")
            bicicleta = {"id_bicicleta": bicicleta_disponible, "origen": origen, "destino": destino}
            prestamos.append((usuario, bicicleta))
            print(f"{usuario['nombre']} ha tomado la bicicleta {bicicleta_disponible} desde {origen} hacia {destino}")
            
        else:
            print("Usuario no encontrado. No se puede tomar una bicicleta.")
            conti= False
    else:        
        conti=False
            

def listar_usuarios():
    print("Lista de Usuarios:")
    for usuario in usuarios:
        print("/----------------------------------------------------------------------------/")
        print(f"Nombre: {usuario['nombre']}, Número de Tarjeta: {usuario['numero_tarjeta']}")
        print("/----------------------------------------------------------------------------/")

def listar_prestamos():
    print("Lista de Prestamos:")
    for usuario, bicicleta in prestamos:
        print("/----------------------------------------------------------------------------/")
        print(f"Usuario: {usuario['nombre']}, Bicicleta: {bicicleta['id_bicicleta']}, Origen: {bicicleta['origen']}, Destino: {bicicleta['destino']}")
        print("/----------------------------------------------------------------------------/")

option = True
while option:
    print("\nPréstamo de bicicletas:")
    print("1. Registrar Usuario")
    print("2. Tomar Bicicleta")
    print("3. Lista Usuarios")
    print("4. Lista Prestamos")
    print("5. Salir\n")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        registrar_usuario()
    elif opcion == "2":
        prestar_bicicleta()
    elif opcion == "3":
        listar_usuarios()
    elif opcion == "4":
        listar_prestamos()
    elif opcion == "5":
        option = False
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
