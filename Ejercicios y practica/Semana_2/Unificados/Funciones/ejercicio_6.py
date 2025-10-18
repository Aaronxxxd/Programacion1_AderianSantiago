
# Crea una función que verifique si un número dado es par o impar. La función debe imprimir un mensaje indicando si el número es par o impar.

def verificar_par(numero):
    if numero % 2 == 0:
        print(f"El numero {numero} es par")
    else:
        print("El numero es impar")

num = int(input("Ingrese un numero: "))
verificar_par(num)