
# Solicitar al usuario que ingrese números (hasta que no quiera ingresar más). Calcular la suma de los números ingresados y el promedio de los mismos.

contador = 1
suma = 0

respuesta = input("Desea ingresar un numero? ('s' o 'n' para responder): ")

while respuesta == "s": 
    numero = int(input("Ingrese un numero: "))
    contador += 1
    suma += numero
    respuesta = input("Desea ingresar otro numero? ('s' o 'n' para responder): ")
    if respuesta == "n":
        break
    
promedio = suma / contador

print(f"La suma de los numeros es: {suma}")
print(f"El promedio de los numeros es: {promedio}")