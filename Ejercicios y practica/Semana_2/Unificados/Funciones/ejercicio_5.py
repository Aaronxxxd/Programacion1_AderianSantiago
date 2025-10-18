
# Escribe una función que calcule el área de un círculo. La función debe recibir el radio como parámetro y devolver el área.

def calcular_area_circulo(radio) -> float:
    area = 3.14 * (radio ** 2)
    print(area)
    return area

rad = float(input("Ingrese el valor del radio: "))
calcular_area_circulo(rad)