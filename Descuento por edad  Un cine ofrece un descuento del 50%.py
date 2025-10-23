# Descuento por edad: Un cine ofrece un descuento del 50% a personas mayores de 60 años. Solicita la edad del usuario y determina si aplica para el descuento.

edad = int(input("ingrese la edad: "))

if edad >= 60:
    print("Usted aplica para el descuento")
else:
    print("Su edad no aplica para el descuento")
