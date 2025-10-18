
# Solicitar al usuario que ingrese 5 números como mínimo y como máximo 10. Calcular la suma de los números ingresados y el promedio de los mismos.

contador = 0
suma = 0
continuar = "s"

while contador < 5:
    numero = int(input("Ingresa un numero: "))
    suma += numero
    contador += 1

while contador < 10 and continuar == "s":
    continuar = input("¿Queres ingresar otro numero? (s/n): ")
    numero = int(input("Ingresa un numero: "))
    suma += numero
    contador += 1

promedio = suma / (contador - 1)

print(f"La suma total es: {suma}")
print(f"El promedio es: {promedio}")