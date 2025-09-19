# El usuario debe ingresar una cantidad indefinida de números (termina con cero). Calcular el promedio de los números positivos y el promedio de los negativos por separado. 

suma_positivos = 0
contador_positivos = 0
suma_negativos = 0
contador_negativos = 0

while True:
    numero = float(input("Ingrese un numero (0 para terminar): "))
    
    if numero == 0:
        break 
    
    if numero > 0:
        suma_positivos += numero
        contador_positivos += 1
    elif numero < 0:
        suma_negativos += numero
        contador_negativos += 1

if contador_positivos > 0:
    promedio_positivos = suma_positivos / contador_positivos
    print(f"Promedio de los números positivos: {promedio_positivos:.2f}")
else:
    print("No se ingresaron números positivos.")

if contador_negativos > 0:
    promedio_negativos = suma_negativos / contador_negativos
    print(f"Promedio de los números negativos: {promedio_negativos:.2f}")
else:
    print("No se ingresaron números negativos.")
