# Generar un número secreto entre 1 y 50 (puede fijarse manualmente). El usuario debe adivinarlo. El programa le debe indicar si el número ingresado es mayor o menor al secreto, y terminar cuando lo adivine. 

import random

numero_secreto = random.randint(1, 50)

print("Adivina el numero secreto (entre 1 y 50)")

while True:
    intento = int(input("Ingrese un numero: "))
    
    if intento == numero_secreto:
        print("¡Felicidades! ¡Adivinaste el número secreto!")
        break
    elif intento < numero_secreto:
        print("El número secreto es mayor. Intenta de nuevo.")
    else:
        print("El número secreto es menor. Intenta de nuevo.")
