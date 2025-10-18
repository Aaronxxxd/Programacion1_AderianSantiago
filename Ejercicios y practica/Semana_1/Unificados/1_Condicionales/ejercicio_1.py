# Clase 18-8 / Repaso y condicionales (no hubo ejercicios para la catedra asi que realizo ejercicios unificados)

# A partir del ingreso de la altura en centímetros de un jugador de baloncesto, el programa deberá determinar la posición del jugador en la cancha, considerando los siguientes parámetros:
# Menos de 160 cm: Base
# Entre 160 cm y 179 cm: Escolta
# Entre 180 cm y 199 cm: Alero
# 200 cm o más: Ala-Pívot o Pívot

altura = int(input("Ingrese su altura en cm (160, 170, etc): "))

if altura < 160:
    print("Su posicion es base")
elif altura >= 160 and altura < 180:
    print("Su posicion es escolta")
elif altura >= 180 and altura < 200:
    print("Su posicion es alero")
else: 
    print("Su posicion es ala-pivot")