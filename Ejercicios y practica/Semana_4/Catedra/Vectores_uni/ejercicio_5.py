
# Buscar un valor: 
# Cargar un array de 10 enteros. Solicitar al usuario un número y verificar si se encuentra en el array. Informar la posición en caso afirmativo, o indicar que no se encuentra.

vector_enteros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for entero in range(len(vector_enteros)):
    numero_verificar = int(input("Ingrese un numero: "))
    if numero_verificar == vector_enteros[entero]:
        print("El numero ingresado se encuentra dentro del vector.")
    else:
        print("El numero ingresado no se encuentra en el vector.")

