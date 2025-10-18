
# Desarrollar una función que permita crear un array de números con la cantidad de elementos que establezca el parámetro recibido.

def crear_array(cantidad):
    vector = [0] * cantidad
    return vector

cantidad_elementos = 5
mi_vector = crear_array(cantidad_elementos)
print(mi_vector)