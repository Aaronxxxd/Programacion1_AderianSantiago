
# Mayor y su posición: 
# Cargar un array de 7 números enteros. Determinar el valor más alto y en qué posición se encuentra.

vector_enteros = [0] * 7
valor_mas_alto = None
posicion_mayor = None

for entero in range(len(vector_enteros)):
    vector_enteros[entero] = int(input("Ingrese un numero: "))
    if valor_mas_alto == None or vector_enteros[entero] > valor_mas_alto:
        valor_mas_alto = vector_enteros[entero]
        posicion_mayor = entero

print(f"El numero mas alto ingresado es: {valor_mas_alto} y se encuentra en el indice numero {posicion_mayor + 1}")