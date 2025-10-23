# Cálculo de impuestosPide al usuario su salario mensual y aplica los siguientes impuestos: ○ Menos de 10,000: 0% ○ Entre 10,000 y 30,000: 10%
# ○ Más de 30,000: 20%

impu = float(input("Por favor, ingrese su salario: "))

if impu < 10000:
    tasa = 0
elif 10000 <= impu <= 30000:
    tasa = 0.10
else:
    tasa = 0.20
impuesto = impu * tasa
salario = impu - impuesto
print(f"impuesto aplicado: {impuesto}")
print(f"salario neto: {salario}")
