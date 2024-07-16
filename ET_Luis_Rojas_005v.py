from ET_Funciones_Luis_Rojas_005v import*
#Link del repositorio publico de GitHub: 

Trabajadores = [
 "Juan Perez",
 "Maria Garcia",
 "Carlos Lopez",
 "Ana Martinez",
 "Pedro Rodriguez",
 "Laura Hernandez",
 "Miguel Sanchez",
 "Isabel Gomez",
 "Francisco Diaz",
 "Elena Fernandez"
]


print("¡Bienvenido al programa de gestion de la empresa en python!")

while True:
    print("Menu")
    print("1.) Asignar sueldos aleatorios")
    print("2.) Clasificar sueldos")
    print("3.) Ver estadisticas")
    print("4.) Reporte de sueldos")
    print("5.)Salir del programa")
    opcion = input("Ingrese una opcion porfavor: ")
        
    if opcion == '1':
            Asignar_Sueldos_Aleatorios()
    elif opcion == '2':
            Clasificar_Sueldos()
    elif opcion == '3':
            Ver_Estadisticas()
    elif opcion == '4':
            Reporte_Sueldos()
    elif opcion == '5':
            print("¡Hasta luego!, Saliendo del programa........")
            print("Este programa esta desarrollado por: Luis Rojas")
            print("Rut: 27.204.304-3")
            break
    else:
            print("Opcion no valida, por favor, intentalo de nuevo.")
