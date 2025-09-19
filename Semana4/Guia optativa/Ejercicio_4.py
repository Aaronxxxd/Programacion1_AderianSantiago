# Pedir al usuario la cantidad de alumnos en una clase. Luego ingresar la nota de cada alumno 

alumnos = int(input("Ingrese la cantidad de alumnos de la clase: "))

suma_notas = 0  
for i in range(1, alumnos + 1):
    nota = float(input(f"Ingrese la nota del alumno {i}: "))
    print(f"La nota del alumno {i} es: {nota}")