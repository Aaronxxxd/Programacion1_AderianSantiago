vector1 = [0] * 5
vector2 = [0] * 5
iguales = True

print("Cargar el primer array:")
for i in range(5):
    vector1[i] = int(input(f"Ingrese el número {i+1}: "))

print("Cargar el segundo array:")
for i in range(5):
    vector2[i] = int(input(f"Ingrese el número {i+1}: "))

for i in range(5):
    if vector1[i] != vector2[i]:
        iguales = False
        break

if iguales:
    print("Los arrays son iguales")
else:
    print("Los arrays NO son iguales")
