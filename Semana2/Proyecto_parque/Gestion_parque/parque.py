# Funciones

precio_montaña_rusa = 5000
edad_montaña_rusa = 12

precio_carrusel = 2000
edad_carrusel = 0

precio_autitos_chocadores = 3000
edad_autitos_chocadores = 8

precio_kamikaze = 4000
edad_kamikaze = 12

def mostrar_atracciones():
    print("Atracciones disponibles:")
    print("1. Montaña Rusa - $5000 (Edad minima 12)")
    print("2. Carrusel - $2000 (Edad minima 0)")
    print("3. Autitos Chocadores - $3000 (Edad minima 8)")
    print("4. Kamikaze - $4000 (Edad minima 12)")

def puede_subir(edad, atraccion) -> bool:
    if atraccion == "1" and edad >= edad_montaña_rusa:
        return True
    elif atraccion == "2" and edad >= edad_carrusel:
        return True
    elif atraccion == "3" and edad >= edad_autitos_chocadores:
        return True
    elif atraccion == "4" and edad >= edad_kamikaze:
        return True
    else:
        return False

def calcular_precio(atraccion) -> int:
    if atraccion == "1":
        return precio_montaña_rusa
    elif atraccion == "2":
        return precio_carrusel
    elif atraccion == "3":
        return precio_autitos_chocadores
    elif atraccion == "4":
        return precio_kamikaze
    else:
        return 0

def registrar_visita():
    nombre = input("Ingresa tu nombre: ")
    edad = int(input("Ingresa tu edad: "))

    total = 0
    contador_atracciones = 0

    while True:
        mostrar_atracciones()
        eleccion = input("Eleji una atraccion por numero (o 'fin' para terminar): ")
        if eleccion == "fin":
            break
        if puede_subir(edad, eleccion):
            total += calcular_precio(eleccion)
            contador_atracciones += 1
            print(eleccion + " agregada.")
        else:
            print("No cumplis la edad minima para " + eleccion)

    # Aplicamos un descuento si elegiste 3 o mas atracciones
    if contador_atracciones >= 3:
        total = total * 0.9

    print("--- Resumen de la visita ---")
    print(f"Visitante: {nombre} ({edad} años)")
    print(f"Total a pagar: ${total}")
