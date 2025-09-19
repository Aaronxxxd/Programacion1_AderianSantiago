numeros = [0] * 7

for i in range(7):
    numeros[i] = int(input(f"Ingrese el numero {i+1}: "))

mayor = numeros[0]
posicion = 0

for i in range(1, 7):
    if numeros[i] > mayor:
        mayor = numeros[i]
        posicion = i

print("El numero mayor es:", mayor, "y esta en la posicion:", posicion)
