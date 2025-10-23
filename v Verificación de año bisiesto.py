# Verificación de año bisiesto
# Solicita al usuario un año y determina si es bisiesto o no. (Es bisiesto si es divisible
# por 4, pero no por 100, salvo que también sea divisible por 400).


bisiesto = int(input("ingrese un año: "))

if (bisiesto % 4 == 0 and bisiesto % 100 != 0) or (bisiesto % 400 == 0):
    print("El año es bisiesto")
else:
    print("El año no es bisiesto")
