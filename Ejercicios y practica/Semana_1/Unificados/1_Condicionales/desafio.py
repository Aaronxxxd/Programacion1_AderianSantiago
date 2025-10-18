# Clase 18-8 / Repaso y condicionales (no hubo ejercicios para la catedra asi que realizo ejercicios unificados)

# Facturación del Servicio de Agua Potable

# PRECIOS
tarifa_base = 7000
costo_metro_cubico = 200
IVA = 0.21

# VARIABLES
subtotal_consumo = 0
subtotal_bonos = 0
total_sin_iva = 0
recargo = 0
descuento = 0
descuento_especial = 0

# ENTRADA DE DATOS
metros_consumidos = int(input("Ingrese la cantidad de metros consumidos: "))
tipo_cliente = input("Ingrese que tipo de cliente es (Residencial, Comercial o Industrial: )")

# CALCULOS 1
subtotal_consumo = costo_metro_cubico * metros_consumidos
total_sin_iva = tarifa_base + subtotal_consumo

# CONDICIONES
if tipo_cliente == "Residencial":
    if metros_consumidos < 30:
        descuento = 0.30
    elif metros_consumidos > 80:
        recargo = 0.15
    if total_sin_iva < 35000:
        descuento_especial = 0.05

elif tipo_cliente == "Comercial":
    if metros_consumidos > 150:
        descuento = 0.8
    elif metros_consumidos  > 300:
        descuento = 0.12
    elif metros_consumidos < 50:
        recargo = 0.15

elif tipo_cliente == "Industrial":
    if metros_consumidos > 500:
        descuento = 0.20
    elif metros_consumidos > 1000:
        descuento = 0.30
    elif metros_consumidos < 200:
        recargo = 0.10

# CALCULOS 2
descuento = total_sin_iva * descuento
recargo = total_sin_iva * recargo
total_bonos = total_sin_iva + descuento - recargo

total_bonos -= total_bonos * descuento_especial

iva_aplicado = total_bonos * IVA
total = total_bonos + iva_aplicado

# * Salida de los datos
print(f"El subtotal de consumo es: {subtotal_consumo}")
print(f"La bonificacion aplicada es de: {descuento}")
print(f"El recargo aplicado es de: {recargo}")
print(f"El descuento especial es: {total_bonos * descuento_especial}")
print(f"El subtotal final es: {total_bonos}")
print(f"El valor con IVA es: {iva_aplicado}")
print(f"El total a pagar es: {total}")

