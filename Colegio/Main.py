from Estudiante import Estudiante
from Asignatura import Asignatura

asig1 = Asignatura("Programacion","23100", 2)
opcion = 0
while(opcion != 5):
    print("Menu:\n1- Agregar Estudiante\n2- Listar Estudiantes\n3- Buscar por Rut\n4- Eliminar por Rut\n5- Salir")
    opcion = int(input("Ingrese una opcion: "))
    if(opcion == 1):
        # Se agregan estudiantes
        asig1.AgregarEstudiantes()
        
    elif(opcion == 2):
        # Si la lista de estudiantes tiene algun elemento
        if(asig1.ListarEstudiantes()):
            for i in asig1.ListarEstudiantes():
                print(i)
                print("------------")
        else:
            print("No hay estudiantes")
    elif(opcion == 3):
        rut = input("Ingrese el rut: ")
        if(asig1.ListarEstudiantes()):
            for i in asig1.ListarEstudiantes():
                if(i.GetRut() == rut):
                    print(i)
                    break
            
        else:
            print("No hay estudiantes")
    elif(opcion == 4):
        # Eliminar estudiantes por el rut
        rut = input("Ingrese el rut: ")
        if(asig1.ListarEstudiantes()):
            for i in asig1.ListarEstudiantes():
                if(i.GetRut() == rut):
                    # Una vez seleccionado el estudiante
                    # Se consigue su indice en la lista
                    # Para borrarlo con pop()
                    indice = asig1.ListarEstudiantes().index(i)
                    asig1.ListarEstudiantes().pop(indice)
                    break
        else:
            print("No hay estudiantes")
    elif(opcion == 5):
        print("Saliendo....")
    else:
        print("Opcion invalida")


