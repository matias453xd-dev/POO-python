class Estudiante:
    
    def __init__(self, rut=str, nombre=str, yearMatricula=int):
        self.__rut = ""
        self.__nombre = ""
        self.__yearMatricula = 0
        
        # Verificadores
        self.SetNombre(nombre)
        self.SetRut(rut)
        self.SetYear(yearMatricula)
        
    # Getters
    def GetRut(self):
        return self.__rut
    def GetNombre(self):
        return self.__nombre
    def GetYear(self):
        return self.__yearMatricula
    
    # Setters
    def SetRut(self, rut=str):
        # El rut debe tener guion y una longitud >= 9
        if("-" in rut and len(rut) >= 9):
            self.__rut = rut
            
        else:
            raise ValueError("Rut invalido")
        
    def SetNombre(self, nombre=str):
        if(len(nombre) >=  3):
            self.__nombre = nombre
    
        else:
            raise ValueError("Nombre invalido")
            
    def SetYear(self, year=int):
        if(year >= 2010 and year <= 2025):
            self.__yearMatricula = year
            
        else:
            raise ValueError("Año de matricula invalido")
            
    # Mostrar los datos
    def __str__(self):
        return f"Nombre: {self.GetNombre()}\nRut: {self.GetRut()}\nAño de matricula: {self.GetYear()}"