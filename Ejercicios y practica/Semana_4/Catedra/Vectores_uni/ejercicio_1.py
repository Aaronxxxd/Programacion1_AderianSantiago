# Clase 8-9

# Cargar y mostrar array: 
# Declarar un array de 5 enteros. Cargarlo por teclado y mostrar su contenido por pantalla usando un ciclo for.

vector_enteros = [0] * 5

for entero in range(len(vector_enteros)):
    vector_enteros[entero] = int(input("Ingrese un numero: "))

print(vector_enteros)