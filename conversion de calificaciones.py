# Conversión de calificaciones
# Solicita la calificación numérica de un estudiante (0-100) y conviértela en una letra:
# ○ 90-100: A
# ○ 80-89: B
# ○ 70-79: C
# ○ 60-69: D
# ○ 0-59: F

Calificacion = float(input("Ingrese la calificacion de 0 a 100: "))

if 90 <= Calificacion <= 100:
    print("Su calificación es A")
elif 80 <= Calificacion < 90:
    print("Su calificación es B")
elif 70 <= Calificacion < 80:
    print("Su calificación es C")
elif 60 <= Calificacion < 70:
    print("Su calificación es D")
elif 0 <= Calificacion < 60:
    print("Su calificación es F")
else:
    print("Error. Por favor ingrese un valor de 0 a 100.")
