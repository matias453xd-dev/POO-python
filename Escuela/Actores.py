
class Persona:
    
    def __init__(self, nombre, rut, telefono):
        self.__nombre = nombre
        self.__rut = rut
        self.__telefono = telefono
    
    def SetNumero(self, num):
        self.__telefono = num
    
    def MostrarDatos(self):
        return f"Nombre: {self.__nombre}\nRut: {self.__rut}\nTelefono: {self.__telefono}"
    
class Alumno(Persona):
    
    def __init__(self, nombre, rut, telefono, notas):
        super().__init__(nombre, rut, telefono)
        self.__notas = notas
        self.__PerdidaDeCarrera = False
        
    def AgregarNotas(self, nota):
        # Append modifica la lista en sitio y devuelve None, no hay que reasignar
        self.__notas.append(nota)
        