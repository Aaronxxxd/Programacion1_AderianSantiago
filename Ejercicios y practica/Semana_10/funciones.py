def cargar_nombres(nombre_archivo: str):
    with open(nombre_archivo, "a") as archivo:
        while True:
            nombre = input("Ingrese un nombre (en blanco para finalizar): ").strip()
            if nombre == "":
                break
            archivo.write(nombre + "\n")

def mostrar_excepto_excluido(archivo: str , nombre: str):
    with open(archivo, "r") as a:
        lista_nombres: list = a.readlines()
        print("== Nombres alacenados ==")
        for n in lista_nombres:
            if n.strip().lower() != nombre.strip().lower():
                print(n)