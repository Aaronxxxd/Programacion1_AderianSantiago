# Clase 25-8

# Crear una función que le solicite al usuario el ingreso de un número entero y lo retorne.

def solicitar_entero() -> int:
    numero = int(input("Ingrese un numero entero: "))
    return numero

num = solicitar_entero()
print(f"El número ingresado fue: {num}")


