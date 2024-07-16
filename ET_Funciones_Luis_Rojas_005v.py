#Importacion de funciones que utilice
import random
import csv
import math

#Lista de los 10 trabajadores
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

#Esto es un diccionario en donde se van a almacenar los sueldos generados aleatoriamente en la opcion 1
sueldos = {}

#Opcion 1: asignacion aleatoria de sueldos a los 10 trabajadores:
def Asignar_Sueldos_Aleatorios():
    global sueldos
    sueldos = {trabajador:random.randint(300000,2500000) for trabajador in Trabajadores}
    print("Sueldos aleatorios asignados exitosamente!")

#Opcion 2: clasificacion en orden de menor a mayor los sueldos generados aletoriamente en la opcion 1
def Clasificar_Sueldos():
    menores_800k = []
    entre_800k_y_2M = []
    superiores_2M = []
    
    for trabajador, sueldo in sueldos.items():
        if sueldo < 800000:
            menores_800k.append((trabajador, sueldo))
        elif 800000 <= sueldo <= 2000000:
            entre_800k_y_2M.append((trabajador, sueldo))
        else:
            superiores_2M.append((trabajador, sueldo))
    
    print("\nSueldos Menores a $800,000")
    print("TOTAL:", len(menores_800k))
    for trabajador, sueldo in menores_800k:
        print(f"{trabajador} ${sueldo}")

    print("\nSueldos entre $800,000 y $2,000,000")
    print("TOTAL:", len(entre_800k_y_2M))
    for trabajador, sueldo in entre_800k_y_2M:
        print(f"{trabajador} ${sueldo}")

    print("\nSueldos Superiores a $2,000,000")
    print("TOTAL:", len(superiores_2M))
    for trabajador, sueldo in superiores_2M:
        print(f"{trabajador} ${sueldo}")

    print("\nTotal Sueldos: $", sum(sueldo for _, sueldo in sueldos.items()))

#Opcion 3: estas son las estadisticas de el sueldo mas alto, el sueldo mas bajo, el promedio de sueldos y la media geometrica
def Ver_Estadisticas():
    Sueldos_Lista = list(sueldos.values())
    if Sueldos_Lista:
        Max_sueldo = max(Sueldos_Lista)
        Min_sueldo = min(Sueldos_Lista)
        Promedio_Sueldos = sum(Sueldos_Lista) / len(Sueldos_Lista)
        
        #Aqui se calcula la media geometrica
        Producto_Sueldos = math.prod(Sueldos_Lista)
        Media_Geometrica = Producto_Sueldos ** (1 / len(Sueldos_Lista))
        
        print(f"\nSueldo mas alto: ${Max_sueldo}")
        print(f"Sueldo mas bajo: ${Min_sueldo}")
        print(f"Promedio de sueldos: ${Promedio_Sueldos:.2f}")
        print(f"Media geometrica: ${Media_Geometrica:.2f}")
    else:
        print("No se han asignado sueldos aun.")

#Opcion 4: aqui el programa elabora un archivo csv con el reporte de sueldos, esto contiene : Nombre_Empleado, Sueldo_Base, Descuento_Salud, Descuento_Afp y Sueldo_Liquido
def Reporte_Sueldos():

    #Elaboracion del archivo csv
    with open('reporte_sueldos.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Nombre empleado", "Sueldo Base", "Descuento Salud", "Descuento AFP", "Sueldo Liquido"])
        
        #Aqui se realiza lo que va a ir en el archivo csv: Trabajador, Sueldo_Base, Descuento_Salud, Descuento_Afp, Sueldo_Liquido
        for trabajador, sueldo_base in sueldos.items():
            descuento_salud = sueldo_base * 0.07
            descuento_afp = sueldo_base * 0.12
            sueldo_liquido = sueldo_base - descuento_salud - descuento_afp
            writer.writerow([trabajador, sueldo_base, descuento_salud, descuento_afp, sueldo_liquido])
        
    print("El reporte de sueldos ha sido exportado a 'reporte_sueldos.csv'. exitosamente")

