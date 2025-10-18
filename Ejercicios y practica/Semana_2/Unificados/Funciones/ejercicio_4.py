
# Escribir una función que calcule el área de un rectángulo. La función recibe la base y la altura y retorna el área. 

def calcular_area_rectangulo(base, altura) -> float:
    area = base * altura
    print(f"El area del rectangulo es: {area}")
    return area

b = float(input("Ingrese la base del rectangulo: "))
a = float(input("Ingrese la altura del rectangulo: "))

calcular_area_rectangulo(b, a)