num = int(input("Digite un numero\n"))
hasta = int(input("Digite el numero limite de la tabla\n"))

print(f"el numero a multiplicar es {num}")

inicial = 1
while inicial <= hasta:
    print(f"{num} x {inicial} = {num*inicial}")
    inicial = inicial + 1
