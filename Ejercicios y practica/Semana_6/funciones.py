
def burbuja_ascendente(vector: list):
    tamaño = len(vector)

# Intercambio de numeros para ordenarlos de menor a mayor
    for i in range(tamaño - 1):
        for j in range(tamaño - i - 1):
            if vector[j] > vector[j + 1]:
                vector[j], vector[j + 1] = vector[j + 1], vector[j]

# Intercambio de numeros para ordenarlos de mayor a menor 

def burbuja_descendente(vector: list):
    tamaño = len(vector)

    for i in range(tamaño - 1):
        for j in range(tamaño - i - 1):
            if vector[j] < vector[j + 1]:
                vector[j], vector[j + 1] = vector[j + 1], vector[j]

# Funcion mejorada la cual para cuando ya se termino de ordenar omitiendo vueltas innecesarias 

def burbuja_mejorado(vector: list):
    tamaño = len(vector)

    for i in range(tamaño - 1):
        intercambio = False
        for j in range(tamaño - i - 1):
            if vector[j] > vector[j + 1]:
                vector [j], vector[j + 1] = vector[j + 1], vector[j]
                intercambio = True
        
        if not intercambio:
            print(i)
            break 

# Intercambio de letras (teniendo en cuenta minusculas)

def burbuja_mejorado_letras(vector: list):
    tamaño = len(vector)

    for i in range(tamaño - 1):
        intercambio = False
        for j in range(tamaño - i - 1):
            if vector[j].lower() > vector[j + 1].lower():
                vector [j], vector[j + 1] = vector[j + 1], vector[j]
                intercambio = True
        
        if not intercambio:
            print(i)
            break 

