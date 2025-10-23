# Tipo de triángulo
# Pide tres longitudes y determina si el triángulo es equilátero, isósceles o escaleno.

longitud = float(input("Ingrese la longitud del primer lado: "))
longitud2 = float(input("Ingrese la longitud del segundo lado: "))
longitud3 = float(input("Ingrese la longitud del tercer lado: "))

if longitud == longitud2 and longitud2 == longitud3:
    print("El triángulo es equilátero.")
elif longitud == longitud2 or longitud == longitud3 or longitud2 == longitud3:
    print("El triángulo es isósceles.")
else:
    print("El triángulo es escaleno.")
