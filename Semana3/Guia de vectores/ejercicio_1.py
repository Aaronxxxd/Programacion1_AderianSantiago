numeros = [0] * 5  

for i in range(5):
    numeros[i] = int(input(f"Ingrese el numero {i+1}: "))

print("Contenido del array:")
for i in range(5):
    print(numeros[i])
