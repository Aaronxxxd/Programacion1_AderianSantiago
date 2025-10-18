
# Pedir el ingreso de una clave. Validar que el ingreso del usuario sea correcto. Solo tendrá 3 intentos.

contador_intentos = 3

clave = input("Ingrese una clave: ")
clave = int(clave)
contador_intentos -= 1

while clave != 619:
    clave = input("Error... vuelta a intentarlo: ")
    clave = int(clave)
    contador_intentos -= 1
    if contador_intentos == 0:
        break