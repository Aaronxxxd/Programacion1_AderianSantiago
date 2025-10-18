
# Define una función que encuentre el máximo de tres números. La función debe aceptar tres argumentos y devolver el número más grande.

def encontrar_maximo(num1, num2, num3): 
    if num1 >= num2 and num1 >= num3:
        if num2 >= num3:
            return num1, num2, num3
        else:
            return num1, num3, num2
    elif num2 >= num1 and num2 >= num3: 
        if num1 >= num3:
            return num2, num1, num3
        else: 
            return num2, num3, num1
    elif num3 >= num1 and num3 >= num2:
        if num1 >= num2:
            return num3, num1, num2
        else: 
            return num3, num2, num1