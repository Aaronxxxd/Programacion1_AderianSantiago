
# Crear una función que le solicite al usuario el ingreso de una cadena y la retorne. 

def solicitar_cadena() -> str:
    cadena = input("Ingrese una cadena de texto: ")
    return cadena

cad = solicitar_cadena()
print(f"La cadena ingresada fue: {cad}")