# Crear una función convertir_minutos(minutos) que reciba una cantidad de minutos y devuelva cuántas horas y minutos sobran.

def convertir_minutos(minutos):
    horas = minutos // 60
    minutos_restantes = minutos % 60
    return horas, minutos_restantes

minutos = int(input("Ingresa la cantidad de minutos: "))
horas, minutos_restantes = convertir_minutos(minutos)

print(f"{minutos} minutos son {horas} horas y {minutos_restantes} minutos.")