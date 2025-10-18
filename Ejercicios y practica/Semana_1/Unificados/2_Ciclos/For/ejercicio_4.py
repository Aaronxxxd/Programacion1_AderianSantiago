
# Ingresar un número y mostrar la tabla de multiplicar de ese número. Por ejemplo si se ingresa el numero 5:

numero = int(input("Ingrese un numero: "))

for i in range(1, 11):
    multiplicacion = numero * i
    print(f"{numero} x {i} = {multiplicacion}")
