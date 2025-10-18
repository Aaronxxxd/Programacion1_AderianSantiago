
# Definir una función es_par(numero) que reciba un número y devuelva True si es par y False si es impar. Luego, el programa debe pedir un número y mostrar si es par o impar usando la función. 

def es_par(numero: int)-> bool:
    if numero % 2 == 0:
        numero_par = True
    else:
        numero_par = False
    return numero_par
    
numero = int(input("Ingrese un numero: "))

par = es_par(numero)
print(par)