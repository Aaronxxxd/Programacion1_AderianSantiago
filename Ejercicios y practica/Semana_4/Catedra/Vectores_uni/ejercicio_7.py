
# Invertir orden: 
# Cargar un array de 6 enteros y mostrarlo invertido, es decir, desde el último al primero. 

vector_enteros = [0] * 6

for entero in range(len(vector_enteros)):
    vector_enteros[entero] = int(input("Ingrese un numero: "))

print("El array invertido es: ")
for i in range(5, -1, -1):
    print(vector_enteros[i])

