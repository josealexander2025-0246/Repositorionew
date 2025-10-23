# Escribe un programa que solicite un número al usuario y determine si es positivo, negativo o cero.

num = float(input("Por favor, ingrese un número: "))

if num > 0:
    print("El número es positivo.")
elif num < 0:
    print("El número es negativo.")
else:
    print("El número es cero.")
