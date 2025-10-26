# Archivo de prueba de tuplas

#Las tuplas son INMUTABLES, no se puede modificar

tupla = ("Maria", "40856927")

# nombre = tupla[0]
nombre, dni = tupla
nombre = "SilverMaria"

print(f"Nombre: {tupla[0]} - DNI: {dni} - Nick: {nombre}")

for i in tupla: 
    print(i)

tupla_nombre = ("Leandro", "Gomez")
lista_persona = [tupla_nombre, "15-5-90", True, 4.2]

nombre_2 = lista_persona[0][0]

print(nombre_2)

tupla_2 = ("objeto1", "objeto2", "objeto1")
cantidad = tupla_2.count("Objeto1")

print(cantidad)

libro = []
libro.append("Divergente")
libro.append("Roth")
libro.append("2005")

tupla_libro = (libro)

print(tupla_libro)