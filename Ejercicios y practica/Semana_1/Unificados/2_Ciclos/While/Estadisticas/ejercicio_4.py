
# Mostrar la suma de los números pares desde el 1 hasta el 10.

suma = 0
numero = 1

while numero <= 10:
    if numero % 2 == 0:
        suma = suma + numero
    numero += 1
print(f"La suma de los numeros del 1 al 10 es: {suma}")
