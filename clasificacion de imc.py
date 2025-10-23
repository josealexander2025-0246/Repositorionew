# Clasificación de IMC
# Solicita el peso (kg) y la altura (m) de una persona, calcula su Índice de Masa
# Corporal (IMC = peso / altura²) y clasifícalo:
# ○ <18.5: Bajo peso
# ○ 18.5-24.9: Normal
# ○ 25-29.9: Sobrepeso
# ○ 30 o más: Obesidad


peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))

imc = peso / (altura**2)
if imc < 18.5:
    print("Bajo peso")
elif 18.5 <= imc <= 24.9:
    print("Normal")
elif 25 <= imc <= 29.9:
    print("Sobrepeso")
else:
    print("Obesidad")
print(f"Su IMC es: {imc:.2f}")
