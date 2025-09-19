def buscar(array, valor, longitud):
    for i in range(longitud):
        if array[i] == valor:
            return i
    return -1

# Programa principal
array = [0] * 10
for i in range(10):
    array[i] = int(input(f"Ingrese el número {i+1}: "))

buscado = int(input("Ingrese el número a buscar: "))
posicion = buscar(array, buscado, 10)

if posicion != -1:
    print(f"El número {buscado} aparece primero en la posición {posicion}")
else:
    print("El número no se encuentra en el array")
