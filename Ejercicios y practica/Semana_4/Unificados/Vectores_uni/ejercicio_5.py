
# Escribir una función que calcule y retorne el producto de todos los elementos de la lista que recibe como parámetro.

def crear_vector(cantidad):
    vector = [0] * cantidad
    return vector

def cargar_vector(cantidad):
    vector = crear_vector(cantidad)
    
    for i in range(len(vector)):
        numero = int(input(f"Ingrese el número {i + 1}: "))
        vector[i] = numero 

    return vector 

def retorno_producto(vector):
    producto = 1
    
    for elementos in range(len(vector)):
        producto *= vector[elementos]
    return producto

cantidad_elementos = int(input("Ingrese la cantidad de elementos: "))
mi_vector = cargar_vector(cantidad_elementos)

producto_total = retorno_producto(mi_vector)

print(f"Array cargado: {mi_vector}")
print(f"El producto de los elementos del vector es: {producto_total}")