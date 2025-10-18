
# Sumar todos los elementos: 
# Declarar un array de 10 enteros. Cargarlo por teclado. Calcular y mostrar la suma de todos los elementos.

suma = 0
vector_enteros = [0] * 10

for entero in range(len(vector_enteros)):
    vector_enteros[entero] = int(input("Ingrese un numero: "))
    suma += vector_enteros[entero]

print(f"El total de la suma es: {suma}")