
# Escribir una función operaciones(num1, num2) que reciba dos números y muestre su suma, resta y multiplicación. Luego, el programa debe pedir dos números al usuario y llamar a la función. 

def operaciones (num1: int, num2: int):
    suma = num1 + num2
    resta = num1 - num2
    multiplicacion = num1 * num2
    return suma, resta, multiplicacion


num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese otro numero: "))

suma, resta, multiplicacion = operaciones(num1, num2)

print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicacion: {multiplicacion}")