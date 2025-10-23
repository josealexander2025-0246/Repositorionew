# Número mayor entre dos Pide al usuario que ingrese dos números y determina cuál es el mayor o si son iguales

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))


if num1 > num2:
    print("El número mayor es:", num1)
elif num2 > num1:
    print("El número mayor es:", num2)
else:
    print("Ambos números son iguales.")
