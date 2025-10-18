
# Ingresar un número. Mostrar cada número primo que hay entre el 1 y el número ingresado. Informar cuántos números primos se encontraron.

contador_divisores = 0

numero = int(input("Ingrese un numero: "))

for i in range (2, numero + 1):
    es_primo = True
    for j in range (2, i):
        if i % j == 0:
            es_primo = False
            break
    if es_primo == True:
        print(f"{i} es primo")
        contador_divisores =+ 1

print (f"Cantidad de primos: {contador_divisores}")