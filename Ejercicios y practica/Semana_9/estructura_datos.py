# REPASO

# * Listas dinamicas

# * Mutables
# * Heterogeneas
# * Indexables
# * Ordenadas
# * Iterables 

ejemplo_lista = []
ejemplo_lista = list()
ejemplo_lista= [159, True, "cadena"]

# * Tuplas

# * Inmutables
# * Ordenadas
# * Heterogeneas
# * Indexables

ejemplo_tupla = ("nombre", 85)

# Pasaje de tuplas a lista y viceversa

nueva_tupla = tuple(ejemplo_lista)
print(nueva_tupla)
print(ejemplo_lista)

nueva_lista = list(nueva_tupla)
nueva_lista = ["Pedro", 30]

tupla_modifica = tuple(nueva_lista)

print("-----")
print(ejemplo_tupla)
print(tupla_modifica)

# ------------------------------------------------

# *Conjuntos

# * No ordenados
# * No admite repetidos
# * Heterogeneos - No es una buena practica 
# * No indexables
# * Mutables
# * Iterables

ejemplo_conjunto = set()
ejemplo_conjunto = {1, 4, 8}

# ejemplo_conjunto { } # No es un conjunto, es un diccionario

# * Pasaje de listas a conjuntos

lista_lenguajes = []

while True:
    lenguaje = input("Ingresar lenguaje (Espacio vacio para finalizar carga): ")
    if lenguaje == "":
        break
    lista_lenguajes.append(lenguaje)

set_lenguajes = set(lista_lenguajes)

lista_ordenada = list(set_lenguajes)
lista_ordenada.sort()

print(lista_ordenada)

# ------------------------------------------------

# * Diccionarios

# * Mutables
# * Ordenados
# * Funcionan con pares de clave valor
# * No se pueden repetir 

# ejemplo_diccionario = {}
# ejemplo_diccionario = dict()
# ejemplo_diccionario = {
#     1: "pelicula",
#     2: "series"
# }

# ejemplo_diccionario[3] = "videojuegos"

ejemplo_diccionario = {}
ejemplo_diccionario = dict()
ejemplo_diccionario = {
    "peliculas": ["Terminator", "Avatar", "Volver al futuro"],
    "series": {"Twisted Metal", "Friends", "Peaky Blinders"},
    "precio": (20000, 25000),
    "categorias": {1: "Terror", 2: "Comedia", 3: "Suspenso"}
}

ejemplo_diccionario["URL"] = "www.sitio.com"

ejemplo_diccionario["peliculas"].append("Harry Potter")
ejemplo_diccionario["series"].add("Lost")

# print(ejemplo_diccionario["categorias"].values())

for i in ejemplo_diccionario["categorias"].values():
    print(i)