# Conversión de horas a turnos
# Pide la hora (0-23) y determina si es "Mañana" (6-11), "Tarde" (12-17), "Noche"
# (18-23) o "Madrugada" (0-5).


hora = int(input("Ingrese la hora (0-23): "))

if 6 <= hora <= 11:
    print("Mañana")
elif 12 <= hora <= 17:
    print("Tarde")
elif 18 <= hora <= 23:
    print("Noche")
elif 0 <= hora <= 5:
    print("Madrugada")
else:
    print("Hora inválida. Por favor ingrese un valor entre 0 y 23.")
