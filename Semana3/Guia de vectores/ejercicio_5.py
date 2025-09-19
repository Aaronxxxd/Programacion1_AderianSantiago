numeros = [0] * 10

for i in range(10):
    numeros[i] = int(input(f"Ingrese el numero {i+1}: "))

buscado = int(input("Ingrese el número a buscar: "))
posicion = -1

for i in range(10):
    if numeros[i] == buscado:
        posicion = i
        break

if posicion != -1:
    print(f"El numero {buscado} se encuentra en la posición {posicion}")
else:
    print("El número no se encuentra en el array")
