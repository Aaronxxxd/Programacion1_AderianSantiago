
# Función para buscar la primera aparición de un valor: 
# Escribir una función que reciba un array de enteros y un número a buscar. La función debe retornar la posición de la primera aparición de ese número o -1 si no se encuentra.

def buscar_numero(vector, num_encontrar):
    for buscar in range(len(vector)):
        if vector[buscar] == num_encontrar:
            print(f"El numero a encontrar se encuentra en el indice: {buscar}")
    print("-1")

numero_a_encontrar = 5

vector_enteros = [0] * 5
for entero in range(len(vector_enteros)):
    vector_enteros[entero] = int(input("Ingrese un numero: "))

buscar_numero(vector_enteros, numero_a_encontrar)
