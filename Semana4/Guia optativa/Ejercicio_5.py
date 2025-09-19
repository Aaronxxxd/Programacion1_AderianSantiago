# Solicitar al usuario un número entero y determinar si es primo (solo divisible por 1 y por sí mismo). 

numero = int(input("Ingrese un numero: "))

if numero > 1:
    es_primo = True
    for i in range(2, numero):
        if numero % i == 0:
            es_primo = False
            break
    if es_primo:
        print(f"El numero {numero} es primo.")
    else:
        print(f"El numero {numero} no es primo.")
else:
    print("El número debe ser mayor que 1 para poder analizar si es primo.")
