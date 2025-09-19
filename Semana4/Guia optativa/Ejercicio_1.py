# Escribir un programa que pida un número entero positivo n y muestre en pantalla todos los números pares desde 1 hasta n.

numero = int(input("Ingrese un numero entero positivo: "))

if numero > 0:
    print(f"Numeros pares desde 1 hasta {numero}: ")
    for i in range(1, numero + 1):
        if i % 2 == 0: 
            print(i)
else:
    print("El numero debe ser positivo.")