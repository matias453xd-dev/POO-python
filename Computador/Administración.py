from Pc import Computador
opcion = 0
computadores = []
while(opcion != 6):
    opcion = int(input("Menú:\n1) Ingresar computador\n2) Listar computador\n3) Buscar por marca\n4) Eliminar computador\n5) Actualizar RAM de un computador\n6) Salir\n"))
    if(opcion == 1):
        marca = input("Marca: ")
        procesador = input("Procesador: ")
        ram = int(input("RAM: "))
        almacenamiento = int(input("Almacenamiento: "))
        year = int(input("Year: "))
        computadores.append(Computador(marca,procesador,ram,almacenamiento,year))
        print("Pc creado exitosamente")
    elif(opcion == 2):
        print("Computadores:")
        if computadores:
            for i in computadores:
                print(i)
        else:
            print("No hay computadores")
    elif(opcion == 3):
        if computadores:
            brand = input("Ingrese la marca del pc: ")
            for i in computadores: # i va a representar a un objeto Computador
                if(brand.lower() == i.get_marca().lower()):
                    print(i) # Se muestra la infomación completa del pc 
        else:
            print("No hay computadores")     
    elif(opcion == 4):
        if computadores:
            for index, pc in enumerate(computadores):
                print(f"{index}) {pc}")
            eleccion = int(input("Seleccione el índice del pc a eliminar: "))
            if(eleccion >= 0 and eleccion <= len(computadores)-1):
                computadores.pop(eleccion)
                print("PC eliminado")
        else:
            print("No hay computadores")
    elif(opcion == 5):
        if computadores:
            for index, pc in enumerate(computadores):
                print(f"{index}) {pc}")
            eleccion = int(input("Seleccione el índice del pc a cambiar la RAM: "))
            NewRam = int(input("Ingrese la nueva RAM: \n"))
            computadores[eleccion].set_ram(NewRam)
        else:
            print("No hay computadores")
        
    elif(opcion == 6):
        print("Saliendo....")
    else:
        print("Opcion invalida")