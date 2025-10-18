
# Crea una función que verifique si un número dado es par o impar. La función retorna True si el número es par, False en caso contrario.

def verificar_par(numero) -> bool:
    if numero % 2 == 0:
        return True
    else: 
        return False

num = int(input("Ingrese un numero: "))
resultado = verificar_par(num)   
print(resultado)