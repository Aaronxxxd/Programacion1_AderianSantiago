
# Crear una función convertir_minutos(minutos) que reciba una cantidad de minutos y devuelva cuántas horas y minutos sobran.

def convertir_minutos(minutos: int):
    horas = minutos // 60
    restantes = minutos % 60
    return horas, restantes

minutos = int(input("Ingrese los minutos: "))

horas, restantes = convertir_minutos(minutos)

print(f"Quedan {horas} horas y {restantes} minutos restantes")