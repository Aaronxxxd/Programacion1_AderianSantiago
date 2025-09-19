numeros = [0.0] * 6
suma = 0

for i in range(6):
    numeros[i] = float(input(f"Ingrese el numero {i+1}: "))
    suma += numeros[i]

promedio = suma / 6
print("El promedio de los valores es:", promedio)
