
# Una empresa dedicada a la toma de datos para realizar estadísticas y censos, nos pide realizar la carga y validación de datos.
# Los datos requeridos son:
# Apellido
# Edad, entre 18 y 90 años inclusive.
# Estado civil: “Soltero/a”, ”Casado/a”, “Divorciado/a” o “Viudo/a”.
# Número de legajo: valor numérico de 4 cifras, sin ceros a la izquierda.
# Una vez ingresados y validados los datos, mostrarlos por pantalla.

apellido = input("Ingrese su apellido: ")

edad = int(input("Ingrese su edad (valido entre 18 y 90): "))

while edad < 18 or edad > 90: 
    edad = int(input("Edad invalida... Ingrese su edad (valido entre 18 y 90): "))

estado_civil = input("Ingrese su estado civil: ")

while estado_civil != "Soltero" and estado_civil != "Soltera" and estado_civil != "Casado" and estado_civil != "Casada" and estado_civil != "Divorciado" and estado_civil != "Divorciada" and estado_civil != "Viudo" and estado_civil != "Viuda":
    estado_civil = input("Estado civil invalido... Ingrese su estado civil: ")

legajo = int(input("Ingrese su legajo: "))

while legajo < 1000 or legajo > 9999:
    legajo = int(input("Legajo invalido... Ingrese su legajo: "))

print(f"Apellido: {apellido}")
print(f"Edad: {edad}")
print(f"Estado civil: {estado_civil}")
print(f"Legajo: {legajo}")