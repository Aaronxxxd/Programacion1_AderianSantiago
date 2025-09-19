# Pedir al usuario un número entero e imprimir la tabla de multiplicar de ese número desde el 1 hasta el 10. 

numero = int(input("Ingrese un numero entero: "))

print(f"Tabla de multiplicar del {numero}:")

for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
