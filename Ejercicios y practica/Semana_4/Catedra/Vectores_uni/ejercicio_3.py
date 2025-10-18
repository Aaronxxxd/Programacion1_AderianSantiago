
# Promedio de valores: 
# Declarar un array de 6 números reales (floats). Cargarlo por teclado. Calcular y mostrar el promedio de los valores. 

suma = 0
vector_reales = [0] * 6

for real in range(len(vector_reales)):
    vector_reales[real] = float(input("Ingrese un numero: "))
    suma += vector_reales[real]

promedio = suma / len(vector_reales)

print(f"El total de la suma es: {suma}")
print(f"El promedio de los 6 numeros es: {promedio}")
