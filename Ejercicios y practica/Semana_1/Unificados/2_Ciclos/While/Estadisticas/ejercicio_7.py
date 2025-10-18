
# Solicitar al usuario que ingrese números (hasta que no quiera ingresar más). Calcular la suma de los números positivos y el producto de los negativos.


suma = 0
producto = 1

respuesta = input("Desea ingresar un numero? ('s' o 'n' para responder): ")

while respuesta == "s": 
    numero = int(input("Ingrese un numero: "))
    if numero > 0:
        suma += numero
    elif numero < 0:
        producto *= numero

    respuesta = input("Desea ingresar otro numero? ('s' o 'n' para responder): ")
    if respuesta == "n":
        break
    

print(f"La suma de los numeros es: {suma}")
print(f"El producto de los negativos es: {producto}")
