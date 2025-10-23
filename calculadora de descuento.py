# Calculadora de descuentos
# Solicita el precio de un producto y aplica descuentos según el monto:
# Menos de $50: sin descuento
# Entre $50 y $100: 5%
# Más de $100: 10%

Cantidad = float(input("Ingrese el precio del producto: "))

if Cantidad < 50:
    descuento = 0
elif 50 <= Cantidad <= 100:
    descuento = Cantidad * 0.05
else:
    descuento = Cantidad * 0.10
precio_final = Cantidad - descuento
print(f"Descuento aplicado: {descuento}")
print(f"Precio final: {precio_final}")
