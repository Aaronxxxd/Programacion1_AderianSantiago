# Realizar un programa que permita que el usuario ingrese todos los números que desee. Una vez finalizada la carga determinar:
# La suma acumulada de los números negativos.
# La suma acumulada de los números positivos.
# La cantidad de números negativos ingresados.
# El promedio de los números positivos.
# El número positivo más grande.
# El porcentaje de números negativos ingresados, respecto del total de ingresos.


suma_negativos = 0
suma_positivos = 0
contador_numeros = 0
contador_positivos = 0
contador_negativos = 0
positivo_mas_grande = 0

respuesta = input("Desea ingresar un numero? 's' o 'n': ")

while respuesta == 's':
    numero = int(input("Ingrese un numero: "))
    if numero < 0: 
        contador_negativos += 1
        contador_numeros += 1
        suma_negativos += numero

    elif numero > 0:
        contador_positivos += 1
        contador_numeros += 1
        suma_positivos += numero
        if numero > positivo_mas_grande:
            positivo_mas_grande = numero
    
    respuesta = input("Desea ingresar otro numero? 's' o 'n': ")
    
promedio_positivos = suma_positivos / contador_positivos
porcentaje_negativos = (contador_negativos / contador_numeros) * 100 

print(f"Suma de positivos: {suma_positivos}")
print(f"Promedio de positivos: {promedio_positivos}")
print(f"Suma de negativos: {suma_negativos}")
print(f"Cantidad de negativos: {contador_negativos}")
print(f"Porcentaje de negativos: {porcentaje_negativos}")
print(f"Número positivo más grande: {positivo_mas_grande}")
