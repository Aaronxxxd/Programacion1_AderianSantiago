
# Solicitarle al usuario el ingreso de un color. Validar que el mismo sea Rojo, Verde o Azul.

color = input("Ingrese un color (Rojo, Verde o Azul): ")

while color != "Rojo" and color != "Verde" and color != "Azul":
    color = input("Colores invalidos... Vuelva a intentarlo: ")