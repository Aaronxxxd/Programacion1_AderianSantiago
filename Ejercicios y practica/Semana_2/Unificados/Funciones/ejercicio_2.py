
# Crear una función que le solicite al usuario el ingreso de un número flotante y lo retorne.

def solicitar_flotante() -> float:
    numero = float(input("Ingrese un numero entero: "))
    return numero

num = solicitar_flotante()
print(f"El número ingresado fue: {num}")