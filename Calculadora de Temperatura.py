print("=== CALCULADORA DE TEMPERATURA ===")


print("¿Qué conversión desea hacer?")
print("1-Fahrenheit a Celsius")
print("2-Celsius a Fahrenheit")


opcion = input("Elige una opción 1-2: ")

if opcion == "1":
    fahrenheit = float(input("Introduce la temperatura en Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5 / 9
    print(fahrenheit, "°F =", celsius, "°C")

elif opcion == "2":
    celsius = float(input("Introduce la temperatura en Celsius: "))
    fahrenheit = (celsius * 9 / 5) + 32
    print(celsius, "°C =", fahrenheit, "°F")

else:
    print("Opción no válida")
