# Día de la semana: Escribe un programa que solicite un número del 1 al 7 y muestre el día de la semana correspondiente (1 es lunes, 7 es domingo).

Dias = int(input("Ingrese un numero del 1 al 7: "))


if Dias == 1:
    print("== Lunes ==")
elif Dias == 2:
    print("== Martes ==")
elif Dias == 3:
    print("== Miercoles ==")
elif Dias == 4:
    print("== Jueves ==")
elif Dias == 5:
    print("== Viernes ==")
elif Dias == 6:
    print("== Sabado ==")
elif Dias == 7:
    print("== Domingo ==")
else:
    print("El numero ingresado no es valido")
