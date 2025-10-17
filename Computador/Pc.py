class Computador:
    PROCESADORES = ["i3", "i5", "i7", "i9", "Ryzen3", "Ryzen5", "Ryzen7"]
    ANIO_MIN = 1990
    ANIO_MAX = 2025

    def __init__(self, marca, procesador, ram, almacenamiento, year):
        self.__marca = ""
        self.__procesador = ""
        self.__ram = 0
        self.__almacenamiento = 0
        self.__year = 0

        self.set_marca(marca)
        self.set_procesador(procesador)
        self.set_ram(ram)
        self.set_almacenamiento(almacenamiento)
        self.set_year(year)

    # Métodos set
    def set_marca(self, nombre):
        if len(nombre) >= 2:
            self.__marca = nombre
        else:
            print("La marca no puede tener menos de 2 caracteres")

    def set_procesador(self, pro):
        if pro.replace(" ","") in self.PROCESADORES:
            self.__procesador = pro
        else:
            print("Procesador no encontrado")

    def set_ram(self, ram):
        if ram > 0 and ram % 2 == 0:
            self.__ram = ram
        else:
            print("Memoria ram invalida")

    def set_almacenamiento(self, almacenamiento):
        if almacenamiento >= 64:
            self.__almacenamiento = almacenamiento
        else:
            print("Almacenamiento insuficiente")

    def set_year(self, year):
        if self.ANIO_MIN <= year <= self.ANIO_MAX:
            self.__year = year
        else:
            print("Año invalido")

    # Métodos get
    def get_marca(self):
        return self.__marca

    def get_procesador(self):
        return self.__procesador

    def get_ram(self):
        return self.__ram

    def get_almacenamiento(self):
        return self.__almacenamiento

    def get_year(self):
        return self.__year

    # Representación del objeto
    def __str__(self):
        return f"Marca: {self.__marca}, Procesador: {self.__procesador}, RAM: {self.__ram}GB, Almacenamiento: {self.__almacenamiento}GB, Año: {self.__year}"