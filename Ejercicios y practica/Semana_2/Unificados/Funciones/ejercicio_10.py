
# Crear una función que reciba un número y retorne True si el número es primo, False en caso contrario.

def verificar_primo(numero) -> bool:
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True
    
numero = int(input("Ingrese un numero: "))
print(verificar_primo(numero))


