
contador_ingresos = 2
contador_masculinos = 0
contador_total = 0
contador_no_IA = 0
mayor_edad = 0
mayor_nombre = 0
mayor_tecnologia = ""

while contador_ingresos != 0:

    nombre = input("Ingrese su nombre: ")
    if nombre == "":    
        print("El nombre no puede quedar en blanco.")
        break

    edad = int(input("Ingrese su edad: "))
    while edad < 18:
        edad = int(input("Edad invalida... Ingrese su edad: "))

    genero = input("Ingrese su genero (Masculino o Femenino): ")
    while genero != "Masculino" and genero != "Femenino":
        genero = input("Genero invalido... Ingrese su genero (Masculino o Femenino): ")

    tecnologia = input("Ingrese la tecnologia a la que voto: ")
    while tecnologia != "IA" and tecnologia != "RV" and tecnologia != "RA" and tecnologia != "IOT":
        tecnologia = input("Tecnologia invalida... Ingrese la tecnologia a la que voto: ")

    if genero == "Masculino" and edad >= 25 and edad <= 50 and tecnologia == "IOT" and tecnologia == "IA":
        contador_masculinos += 1

    if genero != "Femenino" or edad > 33 and edad < 40:
        contador_total += 1
        if tecnologia != "IA":
            contador_no_IA += 1

    if genero == "Masculino" and edad >= 18:
        mayor_edad = edad
        mayor_nombre = nombre
        mayor_tecnologia = tecnologia

    contador_ingresos -= 1

if contador_total > 0:
    porcentaje_ia = (contador_no_IA / contador_total) * 100
else: contador_porcentaje_total = 0

print(f"Empleados masculinos entre 25 y 50 años que votaron por IOT o IA: {contador_masculinos}")
print(f"Porcentaje de empleados no femeninos entre 33 y 40 que no votaron por IA: {porcentaje_ia}")
print(f"Empleado Masculino de mayor edad: {mayor_nombre}, Tecnologia: {mayor_tecnologia}")