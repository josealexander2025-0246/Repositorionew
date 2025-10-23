# Clasificación de números
# Pide al usuario tres números y determina si son todos positivos, todos negativos,
# mixtos o si hay ceros.


num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))

if num1 > 0 and num2 > 0 and num3 > 0:
    print("Los tres números son positivos.")
elif num1 < 0 and num2 < 0 and num3 < 0:
    print("Los tres números son negativos.")
elif num1 == 0 or num2 == 0 or num3 == 0:
    print("Al menos uno de los números es cero.")
else:
    print("Los números son mixtos (positivos y negativos).")
