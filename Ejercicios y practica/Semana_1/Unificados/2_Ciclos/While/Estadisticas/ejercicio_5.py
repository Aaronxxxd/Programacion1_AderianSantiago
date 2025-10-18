
# Solicitar el ingreso de 5 números, calcular la suma de los números ingresados y el promedio. Mostrar la suma y el promedio por pantalla.

ingreso = 5
suma = 0

while ingreso > 0:
    numero = int(input("Ingrese un numero: "))
    ingreso -= 1
    suma += numero
promedio = suma / 5

print(f"La suma de los 5 numeros es: {suma}")
print(f"El promedio de los 5 numeros es: {promedio}")