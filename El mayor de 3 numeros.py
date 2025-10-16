numero1 = float(input("Introduce el primer valor:"))
numero2 = float(input("Introduce el segundo valor:"))
numero3 = float(input("Introduce el tercer valor:"))


if numero1 > numero2 and numero1 > numero3:
    print("El número mayor es:", numero1)

elif numero2 > numero1 and numero2 > numero3:
    print("\nEl número mayor es:", numero2)

elif numero3 > numero1 and numero3 > numero2:
    print("El número mayor es:", numero3)

else:
    print("Hay números que son igual de mayor")
