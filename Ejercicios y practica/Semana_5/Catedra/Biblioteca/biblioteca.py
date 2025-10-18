# Clase 15-9

# VECTORES
titulos = [""] * 3
ejemplares = [0] * 3

# FUNCIONES
def carga_ejemplares():
    for x in range(len(titulos)):
        titulos[x] = input("Ingrese el nombre del libro: ")
        ejemplares[x] = int(input(f"Ingrese la cantidad de ejemplares de '{titulos[x]}': "))

        continuar = input("Desea continuar? s/n: ")
        if continuar == "n":
            break

    else:
        print("Se alcanzo el limite del vector.")
        
def muestra_catalogo():
    for x in range(len(titulos)):
        if titulos[x] != "": 
            print(f"{titulos[x]} --> {ejemplares[x]} ejemplares")

def consulta_libros():
    libro_consultado = input("Que libro solicita?: ")
    for x in range(len(titulos)):
        if libro_consultado == titulos[x]:
            print(f"El libro solicitado es: {libro_consultado}, del cual tenemos {ejemplares[x]} ejemplares")
            return
    print("No se encontro el libro solicitado")

def muestra_agotados():
    contador = 0

    for x in range(len(titulos)):
        if titulos[x] != "" and ejemplares[x] == 0:
            print(f"El libro: {titulos[x]} posee 0 ejemplares")
            contador += 1

    if contador == 0:
        print("No hay ningún libro agotado.")

def agregar_titulo():
    agregado = False  

    for x in range(len(titulos)):
        if titulos[x] == "":  
            titulos[x] = input("Agrega el nombre del libro nuevo: ")
            ejemplares[x] = int(input(f"Ingrese la cantidad de ejemplares de '{titulos[x]}': "))
            agregado = True
            break 

    if not agregado:
        print("Se alcanzó el límite del vector, no se pueden añadir más libros.")
    else:
        print("Libro agregado correctamente.")

def actualizar_ejemplares():
    libro = input("Ingrese el título del libro a modificar: ")
    encontrado = False

    for x in range(len(titulos)):
        if titulos[x] == libro:  
            encontrado = True
            print(f"Libro encontrado: {titulos[x]} — ejemplares actuales: {ejemplares[x]}")
            
            accion = input("¿Desea realizar un préstamo (p) o una devolución (d)? ")
            
            if accion == "p":
                cantidad = int(input("¿Cuantos ejemplares desea prestar?: "))
                if cantidad <= ejemplares[x]:
                    ejemplares[x] -= cantidad
                    print(f"Préstamo realizado. Quedan {ejemplares[x]} ejemplares disponibles.")
                else:
                    print("No hay suficientes ejemplares disponibles para el préstamo.")
            
            elif accion == "d":
                cantidad = int(input("¿Cuantos ejemplares desea devolver?: "))
                ejemplares[x] += cantidad
                print(f"Devolucion registrada. Ahora hay {ejemplares[x]} ejemplares disponibles.")
            
            else:
                print("Opción no válida.")
            
            break

    if not encontrado:
        print("No se encontró el libro ingresado.")

# MENU
while True:
    print("-----¡Bienvenido a nuestra biblioteca!-----")
    print("Opcion 1: Cargar ejemplares")
    print("Opcion 2: Mostrar catalogo completo")
    print("Opcion 3: Consultar disponibilidad")
    print("Opcion 4: Listar titulos agotados")
    print("Opcion 5: Agregar nuevo titulo")
    print("Opcion 6:")
    print("Opcion 7: Salir")

    opcion = input("Ingrese una opcion: ")

    if opcion == "1":
        carga_ejemplares()
        print(titulos)
        print(ejemplares)

    if opcion == "2":
        muestra_catalogo()

    if opcion == "3":
        consulta_libros()

    if opcion == "4":
        muestra_agotados()

    if opcion == "5":
        agregar_titulo()

    if opcion == "6":
        actualizar_ejemplares()

    if opcion == "7":
        break