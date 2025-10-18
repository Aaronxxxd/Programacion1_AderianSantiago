
# Realizar un pequeño sistema de gestion en  consola para que una concecionaria pueda cargar ventas, la misma se detiene cuando se ingresa 0. El programa debe informar al finalizar 
# 1. La venta mayor
# 2. La venta menor
#3. La cantidad de ventas realizadas 
#4. El total de ventas 

# VARIABLES
venta_mayor = 0
venta_menor = None
cantidad_ventas = 0
total_ventas = 0

# PROCESOS

while True:
    ventas = int(input("Ingrese una venta (ingrese '0' para terminar): "))
    if ventas == 0:
        break
    cantidad_ventas += 1
    total_ventas += ventas

# PROCESO DE VENTA MAYOR Y MENOR
    if cantidad_ventas == 1:
        venta_mayor = ventas
        venta_menor = ventas
    else:
        if ventas > venta_mayor:
            venta_mayor = ventas
        if ventas < venta_menor:
            venta_menor = ventas

# MOSTRAMOS POR PANTALLA
print(f"La cantidad de ventas fue de: {cantidad_ventas}")
print(f"El precio total de ventas fue de: {total_ventas}")
if cantidad_ventas > 0:
    print(f"La venta mayor fue de: {venta_mayor}")
    print(f"La venta menor fue de: {venta_menor}")
else:
    print("No se realizo ninguna venta")
