
# Escribir una función que reciba una lista de enteros, la misma calculará y devolverá el promedio de todos los números. 


def crear_vector(cantidad):
    vector = [0] * cantidad
    return vector

def cargar_vector(cantidad):
    vector = crear_vector(cantidad)
    for entero in range(len(vector)):
        vector[entero] = int(input(f"Ingrese el número {entero + 1}: "))
    return vector

def calcular_promedio(vector):
    suma = 0
    for entero in range(len(vector)):
        suma += vector[entero]
        promedio = suma / len(vector)
    return promedio

cantidad_elementos = int(input("Ingrese la cantidad de elementos: "))
mi_vector = cargar_vector(cantidad_elementos)

promedio = calcular_promedio(mi_vector)

print(f"Array cargado: {mi_vector}")
print(f"El promedio de los números es: {promedio}")
