
# Ingresar un número. Determinar si el número es primo o no.

numero = int(input("Ingrese un numero: "))
es_primo = True

for i in range (2, numero):
    if numero % i == 0:
        es_primo = False
        break

if es_primo == True:
    print("El numero es primo")
else: 
        print("No es primo")