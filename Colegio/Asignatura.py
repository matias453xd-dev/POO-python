from Estudiante import Estudiante
# Se importa la clase para poder utilizarla dentro de esta

class Asignatura:
    
    def __init__(self, nombre=str, codigo=str, semestre=int):
        self.__nombre = ""
        self.__codigo = ""
        self.__semestre = 0
        # __estudiantes guardará objetos del tipo Estudiante
        self.__estudiantes = []

        # Validación
        self.SetNombre(nombre)
        self.SetCodigo(codigo)
        self.SetSemestre(semestre)
        
    # Getters
    def GetNombre(self):
        return self.__nombre
    def GetCodigo(self):
        return self.__codigo
    def GetSemestre(self):
        return self.__semestre
    def ListarEstudiantes(self):
        return self.__estudiantes
    
    # Setters
    def SetNombre(self, nombre=str):
        if(len(nombre) >=  3):
            self.__nombre = nombre
            return 1
        else:
            print("Nombre invalido")
            return 0
    def SetCodigo(self,codigo=str):
        if(len(codigo) >= 4):
            self.__codigo = codigo
            return 1
        else:
            print("Codigo invalido")
            return 0
    def SetSemestre(self, semestre=int):
        if(semestre == 1 or semestre == 2):
            self.__semestre = semestre
            return 1
        else:
            print("Semestre invalido")
            return 0
    
    def AgregarEstudiantes(self):
        # Se crea un estudiante y se agrega a la lista
        nombre = input("Nombre: ")
        rut = input("Rut: ")
        Matricula = int(input("Año de la matricula: "))
        # Si ocurre un error en la creacion del estudiante
        # No se detendra la ejecucion del programa
        try:
            estudiante1 = Estudiante(rut,nombre,Matricula)
            self.__estudiantes.append(estudiante1)
            print("Estudiante agregado")
        except ValueError as e:
            print(e)
    
    def BuscarPorRut(self, rut=str):
        # Si hay al menos un estudiante en la lista
        if self.__estudiantes:
            for i in self.__estudiantes:
                if(i.GetRut() == rut):
                    # Retorna al estudiante
                    return i
            return 0
    def EliminarPorRut(self, rut=str):
        if self.__estudiantes:
            for i in self.__estudiantes:
                if(i.GetRut() == rut):
                    # Se elimina al estudiante
                    indice = self.__estudiantes.index(i)
                    self.__estudiantes.pop(indice)
                    return 
            return 0
    def ContarEstudiantes(self):
        # Retorna el numero de estudiantes
        return len(self.__estudiantes)
    def __str__(self):
        return f"Nombre: {self.GetNombre()}\nCodigo: {self.GetCodigo()}\nSemestre: {self.GetSemestre()}\nCantidad de estudiantes: {self.ContarEstudiantes()}"