
# Escribir una función verificar_acceso(edad) que reciba la edad de una persona y determine si es mayor de edad (18 años o más) devolviendo un booleano. Luego, el programa debe pedir la edad al usuario y mostrar un mensaje apropiado. 

def verificar_acceso(edad: int) -> bool:
    if edad >= 18:
        es_mayor = True
    else:
        es_mayor = False
    return es_mayor

edad = int(input("Ingrese su edad: "))

if verificar_acceso(edad):
    print("Acceso permitido: sos mayor de edad.")
else:
    print("Acceso denegado: sos menor de edad.")
