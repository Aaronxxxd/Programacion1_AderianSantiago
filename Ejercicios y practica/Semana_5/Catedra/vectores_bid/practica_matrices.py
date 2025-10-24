# Una empresa de logistica tiene 3 repartidores en Avellaneda 
# Necesita registrar las entregas realizadas los 5 dias de esta semana 

# Se debe almacenar en una matriz de 5x3 o 3x5

# Desarrollar menu con las siguientes opciones 
    # Cargar datos
    # Mostrar matriz
    # Total por repartidor 

#                  L M M J V
entregas = [[0, 0, 0, 0, 0], # Repartidor 1
                    [0, 0, 0, 0, 0], # Repartidor 2
                    [0, 0, 0, 0, 0]] # Repartidor 3

FILAS = 3
COLUMNAS = 5

def cargar_datos(matriz: list):
    print("Cargar datos: ")

    for i in range(FILAS):
        print(f"Repartidor: {i + 1}")

        for j in range(COLUMNAS):
            valor_valido = False
            while valor_valido == False:
                cantidad_entregas = int(input("Ingrese la cantidad de entregas: "))

                if cantidad_entregas >= 0:
                    matriz[i][j] = cantidad_entregas
                    valor_valido = True
                else: 
                    print("No se permiten negativos")

def mostrar_matriz(matriz: list):
    for i in range(FILAS):
        print(f"El repartidor: {i + 1}")
        for j in range(COLUMNAS):
            print(f"Repartio las siguientes cantidades: ")
            print(f"El dia {j + 1}, repartio: {matriz[i][j]}")

def total_repartidor(matriz: list):
    total1 = 0
    total2 = 0
    total3 = 0

    for i in range(FILAS):
        total = 0
        for j in range(COLUMNAS):
            total += matriz[i][j]

        if i == 0:
            total1 = total
        elif i == 1:
            total2 = total
        elif i == 2:
            total3 = total

        print(f"El repartidor {i + 1} entrego un total de {total} paquetes en la semana.")

    return total1, total2, total3


salir = False

while salir == False:
    print("Menu principal")
    print("1. Cargar datos")
    print("2. Mostrar Matriz")
    print("3. Total por repartidor")
    print("4. Salir")

    opcion = input("Elija una opcion: ")

    if opcion == "1":
        cargar_datos(entregas)
    elif opcion == "2":
        mostrar_matriz(entregas)
    elif opcion == "3":
        t1, t2, t3 = total_repartidor(entregas)
        print(t1, t2, t3)
    elif opcion == "4":
        salir = True