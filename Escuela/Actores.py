
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
        
    def AgregarNota(self, nota):
        self.__notas.append(nota)
        print("Nota guardada")
        
    def BorrarNota(self, nota):
        if(nota in self.__notas):     
            self.__notas.remove(nota)
            print("Nota borrada")
        else:
            print("Nota no encontrada")
            
    def GetNotas(self):
        return self.__notas
    
    def EstadoCarrera(self, estado):
        if(estado == True or estado == False):
            self.__PerdidaDeCarrera = estado
            
    def GetEstado(self):
        return self.__PerdidaDeCarrera

class Profesor(Persona):
    
    def __init__(self, nombre, rut, telefono):
        super().__init__(nombre, rut, telefono)
        # Alumnos será una lista de objetos
        self.__alumnos = []
        
    def AgregarAlumno(self, alumno):
        self.__alumnos.append(alumno)
        
    # El profesor tendrá acceso al metodo de EstadoCarrera del alumno
    def Reprobar(self, alumno):
        for i in range(len(self.__alumnos)):
            if(self.__alumnos[i] == alumno):
                self.__alumnos[i].EstadoCarrera(False)
                return
        print("Alumno no encontrado")
    def Aprobar(self, alumno):
        for i in range(len(self.__alumnos)):
            if(self.__alumnos[i] == alumno):
                self.__alumnos[i].EstadoCarrera(True)
                return
        print("Alumno no encontrado")
        
            
        