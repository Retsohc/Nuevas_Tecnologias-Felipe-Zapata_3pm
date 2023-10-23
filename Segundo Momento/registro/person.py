class Persona:

    def __init__(self, id=None, nombre=None, apellido=None, correo=None, contrasena=None):
        self._id = id
        self._nombre = nombre
        self._apellido = apellido
        self._correo = correo
        self._contrasena = contrasena

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        self._nombre = value

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, value):
        self._apellido = value

    @property
    def correo(self):
        return self._correo

    @correo.setter
    def correo(self, value):
        self._correo = value

    @property
    def contrasena(self):
        return self._contrasena

    @contrasena.setter
    def contrasena(self, value):
        self._contrasena = value

    def registrar(self):
        self.id = input("Indique el id: ")
        self.nombre = input("Indique su nombre: ")
        self.apellido = input("Indique su apellido: ")
        self.correo = input("Indique su correo: ")
        self.contrasena = input("Indique la contraseña: ")

    def ver_registro(self):
        print(f"\nId: {self.id} \nNombre: {self.nombre} \nApellido: {self.apellido} \nCorreo: {self.correo}\n")