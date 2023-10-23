import os
def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')

limpiar_consola()
class Vehiculo:
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color

    def ver_vehiculo(self):
        print(f"\nMarca: {self.marca}\nModelo: {self.modelo}\nColor: {self.color}\n")

def main():
    vehiculo_1 = Vehiculo("Tesla", "Modelo X", "Negro")

    print(vehiculo_1.marca)
    print(vehiculo_1.modelo)
    print(vehiculo_1.color)

    vehiculo_1.modelo = "Modelo Y"

    vehiculo_1.ver_vehiculo()

if __name__ == '__main__':
    main()
