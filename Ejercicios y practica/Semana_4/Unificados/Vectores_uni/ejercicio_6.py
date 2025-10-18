
# Escribir una función que reciba como parámetros una lista de enteros y retorne la posición del valor máximo encontrado.

def crear_vector(cantidad: int): 
    vector = [0] * cantidad
    return vector

def cargar_vector(vector: list): 
    vector = crear_vector(cantidad_elementos)
    
    for entero in range(len(vector)):
        numero = int(input(f"Ingrese un numero: "))
        vector[entero] = numero
    return vector

def encontrar_maximo(vector: list):
    valor_mas_alto = None
    posicion_mayor = None

    for entero in range(len(vector)):
        if valor_mas_alto == None or vector[entero] > valor_mas_alto:
            valor_mas_alto = vector[entero]
            posicion_mayor = entero
    return valor_mas_alto, posicion_mayor


cantidad_elementos = int(input("Ingrese la cantidad de elementos del vector: "))
mi_vector = cargar_vector(cantidad_elementos)
valor_mas_alto, posicion_mayor = encontrar_maximo(mi_vector)


print(f"El vector es: {mi_vector}")
print(f"El numero mas alto ingresado es: {valor_mas_alto} y se encuentra en el indice numero {posicion_mayor + 1}")
