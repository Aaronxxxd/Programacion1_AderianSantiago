
precio_montaña_rusa = 1500
precio_casa_del_terror = 1200
precio_carrusel = 800
precio_total = 0
atracciones_elegidas = ""
atracciones_usadas = ""

# Ingreso de datos
nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
cantidad_atracciones = int(input("Cuantas atracciones desea usar? (3 como maximo): "))

# Ciclos
for i in range(cantidad_atracciones):
    atraccion = input("A que atraccion desea subir? (Montaña rusa, Casa del terror, Carrusel): ")
    atracciones_elegidas += atraccion + " | "

# Condicionales
    if edad >= 12 and atraccion == "Montaña rusa":
        print("Podes subirte a la atraccion!")
        precio_total += precio_montaña_rusa
        atracciones_usadas += atraccion + " | "
    elif edad >= 6 and atraccion == "Casa del terror":
        print("Podes subirte a la atraccion!")
        precio_total += precio_casa_del_terror
        atracciones_usadas += atraccion + " | "
    elif edad > 0 and atraccion == "Carrusel":
        print("Podes subirte a la atraccion!")
        precio_total += precio_carrusel
        atracciones_usadas += atraccion + " | "
    else:
        print("No podes subirte a la atraccion!")

print(f"El visitante {nombre} gastó un total de: ${precio_total}")
print(f"Atracciones elegidas: {atracciones_elegidas}")
print(f"Atracciones a las que pudo subir: {atracciones_usadas}")