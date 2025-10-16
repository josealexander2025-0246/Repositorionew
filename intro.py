print("=== CALCULADORA ===")

Numero1 = float(input("Introducir numero"))
Numero2 = float(input("Introducir numero"))


print("=== MENU ===")
print("1-SUMA")
print("2-RESTA")
print("3-MULTIPLICACION")
print("4-RAIZ CUADRADA")
print("5-DIVISION")
print("6-MODULO")
print("7-POTENCIA")


Opcion = input("===Elige una opcion del 1 al 7===")

if Opcion == "1":
    print("resultado", Numero1 + Numero2)
elif Opcion == "2":
    print("resultado", Numero1 - Numero2)
elif Opcion == "3":
    print("resultado", Numero1 * Numero2)
elif Opcion == "4":
    Numero = float(input("introduce un numero"))
    print("resultado", Numero**0.5)
elif Opcion == "5":
    if Numero2 != 0:
        print("resultado", Numero1 / Numero2)
    else:
        print("No se puede dividir entre 0")
elif Opcion == "6":
    print("resultado", Numero1 % Numero2)
elif Opcion == "7":
    print("resultado", Numero1**numero2)

else:
    print("opcion fuera de alcance")
