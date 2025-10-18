# Clase 25-8

# Escribir una función llamada saludar(nombre) que reciba un nombre como parámetro e imprima un saludo. Luego, el programa debe pedir el nombre del usuario y llamar a la función.

def saludar(nombre: str):
    print(f"Hola {nombre}!")

nombre = input("Ingrese su nombre: ")
saludar(nombre)
