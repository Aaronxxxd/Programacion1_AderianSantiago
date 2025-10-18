
# Escribir una función parecida a la anterior, pero la misma deberá calcular y devolver el promedio de los números positivos.


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
    cantidad_positivos = 0
    for entero in range(len(vector)):
        if vector[entero] > 0:
            cantidad_positivos += 1
            suma += vector[entero]
            promedio = suma / cantidad_positivos
    return promedio

cantidad_elementos = int(input("Ingrese la cantidad de elementos: "))
mi_vector = cargar_vector(cantidad_elementos)

promedio = calcular_promedio(mi_vector)

print(f"Array cargado: {mi_vector}")
print(f"El promedio de los números es: {promedio}")