
# Ingresar 10 números enteros. Determinar el máximo y el mínimo.

contador = 1
numero = int(input("Ingrese un numero: "))
maximo = numero
minimo = numero

contador += 1

while contador <= 10:
    numero = int(input("Ingrese un numero: "))
    contador += 1
    if numero >= maximo:
        maximo = numero
    if numero <= minimo:
        minimo = numero

print(f"El numero mas grande ingresado fue: {maximo}")
print(f"El numero mas chico ingresado fue: {minimo}")