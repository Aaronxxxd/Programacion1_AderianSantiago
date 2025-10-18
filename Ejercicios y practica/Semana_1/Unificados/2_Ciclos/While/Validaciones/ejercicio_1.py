# Clase 22-8

# Pedir el ingreso de una clave. Validar que el ingreso del usuario sea correcto. Tendrá intentos indeterminados.

clave = input("Ingrese una clave: ")
clave = int(clave)

while clave != 619:
    clave = input("Error... vuelta a intentarlo: ")
    clave = int(clave)