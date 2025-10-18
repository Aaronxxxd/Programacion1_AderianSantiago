
# Contar mayores a un valor: 
# Cargar un array de 8 enteros. Contar cuántos son mayores al valor 100 e informar el resultado.

contador = 0
vector_enteros = [0] * 8

for entero in range(len(vector_enteros)):
    vector_enteros[entero] = int(input("Ingrese un numero: "))
    if vector_enteros[entero] >= 100:
        contador += 1

print(f"La cantidad de numeros que son mayores que 100 es: {contador}")