
# Intercambiar elementos pares por ceros: 
# Cargar un array de 10 enteros. Reemplazar todos los elementos pares por cero y mostrar el array 
# resultante. 

vector_enteros = [0] * 10


for entero in range(len(vector_enteros)):
    vector_enteros[entero] = int(input("Ingrese un numero: "))
    if vector_enteros[entero] % 2 == 0:
        vector_enteros[entero] = 0

print(vector_enteros)