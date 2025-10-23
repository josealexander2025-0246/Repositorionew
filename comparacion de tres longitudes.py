# Comparación de tres longitudes
# Solicita tres números que representan longitudes y determina si pueden formar un
# triángulo (la suma de dos lados debe ser mayor que el tercero).


longitud1 = float(input("Ingrese la primera longitud: "))
longitud2 = float(input("Ingrese la segunda longitud: "))
longitud3 = float(input("Ingrese la tercera longitud: "))

if (
    (longitud1 + longitud2 > longitud3)
    and (longitud1 + longitud3 > longitud2)
    and (longitud2 + longitud3 > longitud1)
):
    print("Las longitudes pueden formar un triángulo.")
else:
    print("Las longitudes no pueden formar un triángulo.")
