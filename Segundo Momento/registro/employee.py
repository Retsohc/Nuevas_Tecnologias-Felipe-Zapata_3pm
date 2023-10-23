from person import Persona


class Empleado(Persona):

    def __init__(self, id, nombre, apellido, correo, contrasena, cargo, salario):
        super().__init__(id, nombre, apellido, correo, contrasena)
        self._cargo = cargo
        self._salario = salario

    @property
    def cargo(self):
        return self._cargo

    @cargo.setter
    def cargo(self, cargo):
        self._cargo = cargo

    @property
    def salario(self):
        return self._salario

    @salario.setter
    def salario(self, salario):
        self._salario = salario

    def registrar(self):
        super().registrar()
        self.cargo = input("Ingrese el cargo: ")
        self.salario = float(input("Ingrese el salario: "))

    def ver_registro(self):
        super().ver_registro()
        print(f" Cargo: {self.cargo} \n Salario: {self.salario} \n")

    def iniciar_sesion(self):
        correo_reg = input("\nIngrese el correo registrado: ")
        contrasena_reg = input("Ingrese la contraseña registrada: ")

        if correo_reg == self.correo and contrasena_reg == self.contrasena:
            print(f"\n¡Bienvenido {self.nombre}!")
            return True
        else:
            print("Invalida sus credenciales")
            return False

    def iniciar_negocio_empleado(self):
        init = self.iniciar_sesion()

        while init:
            print("1. Ver datos usuario \n2. -------- \n3. Salir")
            opcion = int(input("\nSeleccione una opción: "))

            if opcion == 1:
                print("\nVer datos usuario \n")
                self.ver_registro()

            elif opcion == 2:
                print("\n-------- \n")

            elif opcion == 3:
                print("\nSaliendo....")
                init = False

            else:
                print("Seleccione una opción correcta...")