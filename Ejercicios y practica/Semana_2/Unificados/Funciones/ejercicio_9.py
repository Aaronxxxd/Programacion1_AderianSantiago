
# Diseña una función que calcule la potencia de un número. La función debe recibir la base y el exponente como argumentos y devolver el resultado.

def potencia_numero (numero, exponente):
    resultado = numero ** exponente
    return resultado

numero = int(input("Ingrese el numero: "))
exponente = int(input("Ingrese el exponente: "))

resultado = potencia_numero(numero, exponente)
print(f"El resultado es: {resultado}")