
# #* Practica de archivos

# #* Apertura de archivo: motodo / funcion open(nombre o ruta del archivo, modo de apertura)
# #* 1. nombre o ruta del archivo
# #* 2. modo de apertura:
# #*      * r: read (leer)
# #*      * w: write (escribir): si el archivo no existe lo crea. Si existe lo pisa (sobre escribe y perdemos info anterior) 
# #*      * a: append (agregar): Si el archivo no existe lo crea. Si existe agrega al final sin borrar nada

# #* Cierre del archivo: metodo o funcion close()
# #*     - Siempre que se abre una conexion a un archivo se debe cerrar 

# # ---------- ESCRITURA ----------

# archivo = open("personas.txt", "w") #* abro archivo en escritura. Pisa si hay contenido previo
# # archivo.write("Voy a pisar el contenido anterior") #* Solo escribimos una linea
# lista_persona = ["Pedro ", "Lopez ", "Mar del Plata"]
# archivo.writelines(lista_persona)
# archivo.write("\n")
# # archivo.writelines(["Pedro\n", "Lopez\n", "Mar del Plata\n"])
# archivo.close()

# # ---------- LECTURA ----------
# nombre_archivo = "personas.txt"
# modo_lectura = "r"
# arc = open(nombre_archivo, modo_lectura)
# texto = arc.read()

# print(f"El contenido del archivo es: {texto}")
# arc.close( )

# # ---------- Agregar al final ----------

# with open(nombre_archivo, "a") as archivo:
#     archivo.write("agrego algo al final")

# # ---------- EJEMPLO ----------

# #* Realizar un programa que solicite los nombre de los alumnos de un curso y los guarde en un archivo txt.
# #* El corte de ingresos se da con un nombre en blanco
# #* Luego el programa debe pedir al usuario un nombre y mostrar por pantalla todos los almacenados 

from funciones import cargar_nombres, mostrar_excepto_excluido

nombre_archivo = "nombres.txt"

# cargar nombres
cargar_nombres(nombre_archivo)

#pedir nombres para filtrar
nombre_excluir = input("Ingresar nombre a excluir: ")


# mostrar contenido filtrado 
mostrar_excepto_excluido(nombre_archivo, nombre_excluir)