
# Escribir una función que permita ingresar la cantidad de números que reciba como parámetro.  Crear el array con la función del punto 1.

def crear_vector(cantidad):
    vector = [0] * cantidad
    return vector

def cargar_vector(cantidad):
    vector = crear_vector(cantidad)
    
    for i in range(len(vector)):
        numero = int(input(f"Ingrese el número {i + 1}: "))
        vector[i] = numero 

    return vector 

cantidad_elementos = int(input("Ingrese la cantidad de elementos: "))
mi_vector = cargar_vector(cantidad_elementos)

print(f"Array cargado: {mi_vector}")

