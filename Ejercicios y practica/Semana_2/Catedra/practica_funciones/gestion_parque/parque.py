#VARIABLES

precio_montaña_rusa = 1500
precio_casa_del_terror = 1200
precio_carrusel = 800

# FUNCIONES

def mostrar_atracciones():
    print("Bienvenido al menu de atracciones!")
    print("1. Montaña Rusa")
    print("2. Casa del Terror")
    print("3. Carrusel")

def puede_subir(edad: int, atraccion: str) -> bool:
    if edad >= 12 and atraccion == "Montaña Rusa":
        return True
    elif edad >= 6 and atraccion == "Casa del Terror":
        return True
    elif edad > 0 and atraccion == "Carrusel":
        return True
    else: 
        return False

def calcular_precio(atraccion):
    if atraccion == "Montaña Rusa":
        return precio_montaña_rusa
    elif atraccion == "Casa del Terror":
        return precio_casa_del_terror
    elif atraccion == "Carrusel": 
        return precio_carrusel

def registrar_visita():
    total_atracciones = 0
    atracciones_elegidas = ""

    nombre = input("Ingrese su nombre: ")
    edad = int(input("Ingrese su edad: "))
    cantidad_atracciones = int(input("A cuantas atracciones desea subir?: "))

    for i in range (cantidad_atracciones):
        mostrar_atracciones()
        nombre_atraccion = input("A que atraccion desea subir? (escriba 'fin' para salir del menu): ")
        if nombre_atraccion == "fin":
            break   
        atracciones_elegidas += nombre_atraccion + " | "

        if puede_subir(edad, nombre_atraccion):
            print("Usted puede subir a la atraccion: ")
            total_atracciones += calcular_precio(nombre_atraccion)
        else:
            print("Usted no puede subir a la atraccion")
    
    def mostrar_resumen():
        print(f"Visitante: {nombre}")
        print(f"Edad: {edad}")
        print(f"Se subio a {cantidad_atracciones} atracciones")
        print(f"Eligi estas atracciones: {atracciones_elegidas}")
        print(f"Gasto un total de: {total_atracciones}")
    
    mostrar_resumen()
