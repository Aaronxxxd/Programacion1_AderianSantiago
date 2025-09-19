# El Parque de Diversiones "PythonLand" necesita un programa inicial para registrar la entrada de visitantes. 
# El sistema debe: 
# 1. Ingreso de datos secuenciales 
# ○ Pedir el nombre y edad de un visitante. 
# ○ Pedir cuántas atracciones quiere usar (por ahora, el parque tiene solo 3 atracciones: Montaña Rusa, Casa del Terror y Carrusel). 
# 2. Uso de condicionales 
# ○ Determinar si el visitante puede subir a la Montaña Rusa (solo si tiene 12 años o más). 
# ○ Si el visitante tiene menos de 6 años, solo puede subir al Carrusel. 
# ○ Los demás pueden acceder a todas las atracciones. 
# 3. Uso de ciclos 
# ○ Preguntar por cada atracción que el visitante desea usar y mostrar si puede subir o no según su edad. 
# ○ Calcular el costo total de las entradas (ejemplo: Montaña Rusa = $1500, Casa del Terror = $1200, Carrusel = $800). 
# 4. Salida de resultados 
# ○ Mostrar un resumen con el nombre del visitante, la lista de atracciones que eligió, cuáles pudo usar y el costo total a pagar. 

Montaña_rusa = 1500
Casa_terror = 1200
Carrusel = 800
Costo_entradas = 0 

nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
cantidad_atracciones = int(input(f"Bienvenido {nombre}, ¿A cuantas atracciones desea subir?: "))

for i in range(cantidad_atracciones):
    opcion = input(
        f"\nAtracción {i+1} de {cantidad_atracciones}, "
        "Elija nuevamente una atraccion\n"
        "1. Montaña Rusa\n"
        "2. Casa del Terror\n"
        "3. Carrusel\n"
        "Ingrese el número de su elección: "
    )

    if opcion == "1" and edad >= 12: 
        Costo_entradas += Montaña_rusa
        print("Podes subirte a la atraccion!")
    elif opcion == "2" and edad >= 6:
        Costo_entradas += Casa_terror
        print("Podes subirte a la atraccion!")
    elif opcion == "3" and edad > 0:
        Costo_entradas += Carrusel
        print("Podes subirte a la atraccion")
    else: 
        print("No podes subirte a la atraccion")
    
print(f"\nEl visitante {nombre} gasto un total de: ${Costo_entradas}")









