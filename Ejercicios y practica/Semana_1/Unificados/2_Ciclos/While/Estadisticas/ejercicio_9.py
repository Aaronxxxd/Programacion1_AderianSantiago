
# Solicitar al usuario que ingrese como mínimo 5 números. Calcular la suma de los números ingresados y el promedio de los mismos.

contador = 0
suma = 0

while contador < 5:
    numero = int(input(f"Ingresa un numero: "))
    suma += numero
    contador += 1

continuar = input("¿Queres ingresar mas numeros? (s/n): ")

while continuar == "s":
    numero = int(input("Ingresa un numero: "))
    suma += numero
    contador += 1
    continuar = input("¿Queres ingresar otro numero? (s/n): ")

promedio = suma / (contador - 1)

print(f"La suma total es: {suma}")
print(f"El promedio es: {promedio}")