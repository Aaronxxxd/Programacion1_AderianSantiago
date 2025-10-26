# Archivo de prueba de listas dinamicas


#Metodo .append siempre agrega un elemento al FINAL de la lista (tambien puede agregar otras listas)
lista_objetos = []
print(lista_objetos)

lista_objetos.append("Vaso")
lista_objetos.append(25)

lista_segunda = [True, 5.0]
especificaciones = ["AMD", 500]
# lista_objetos.append(lista_segunda)

#El metodo .extend lo que hace es desempaquetar dicha lista y agrega los elementos al vector principal (a diferencia del append que añade la lista entera como una sublista)
lista_objetos.extend(lista_segunda)

print(lista_objetos)

#El metodo .insert recibe como parametro un objeto a ingresar y su numero de indice, es decir que con este metodo podemos añadir elementos en la posicion que deseemos 
lista_objetos.insert(1, "Pc")
lista_objetos.extend(especificaciones)

print(lista_objetos)  

#El metodo .remove elimina elementos de la lista (cabe aclarar que necesitamos enviarle el elemento literal, no el indice)
# lista_objetos.remove("AMD")

print(lista_objetos)

#El metodo .pop tambien elimina el cual va a recibir como parametro su indice un elemento pero a su vez nos devuelve su tipo de dato
borrado = lista_objetos.pop(3)

# print(lista_objetos)
# print(f"El elemento borrado {borrado} es de tipo {type(borrado)}")
# print(lista_objetos)

#El metodo .clear vacia la lista, es decir solo borra los elementos
# lista_objetos.clear


#El metodo .index nos devuelve el indice del primero elemento que coincida, osea el que estamos buscando(ademas podemos indicarle donde empezar)
posicion = lista_objetos.index("AMD")
print(f"El elemento AMD esta en el indice: {posicion}")

#El metodo .sort hace lo mismo que hace el metodo de burbuja de ordenamiento (tenemos que usarla con elementos homogeneos, es decir con elementos de un mismo tipo)

lista_numeros = [8, 7, 15, 1, 3]
lista_palabras = ["Techo", "Arbol", "Camara", "Computadora"]

lista_numeros.sort()
print(lista_numeros)

lista_palabras.sort()
print(lista_palabras) 