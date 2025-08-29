# Definir una función area_triangulo que reciba la base y la altura de un triángulo y devuelva su área. Luego, el programa debe pedir los valores y mostrar el resultado. Fórmula: area = (b * h) / 2.

def area_triangulo(base, altura):
    return (base * altura) / 2

base = float(input("Ingresa la base del triangulo: "))
altura = float(input("Ingresa la altura del triangulo: "))

print("El area del triangulo es:", area_triangulo(base, altura))