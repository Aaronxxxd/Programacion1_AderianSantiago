
# Comparar dos arrays: 
# Cargar dos arrays de 5 elementos cada uno. Comparar si ambos son iguales elemento a elemento y mostrar un mensaje indicando si son o no iguales. 

vector_elementos1 = [0] * 5
vector_elementos2 = [0] * 5

for elemento1 in range(len(vector_elementos1)):
    vector_elementos1[elemento1] = int(input("Ingrese un numero para el primer vector: "))

for elemento2 in range(len(vector_elementos2)):
    vector_elementos2[elemento2] = int(input("Ingrese un numero para el segundo vector: "))

if vector_elementos1[elemento1] == vector_elementos2[elemento2]:
    print("Los vectores son iguales (poseen los mismos elementos)")
else:
    print("Los vectores no son iguales (no poseen los mismos elementos)")