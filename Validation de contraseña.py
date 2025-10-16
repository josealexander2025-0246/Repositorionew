Password1 = "5467"
Nombre1 = "Monky D Luffy"

while True:
    Nombre = input("Introducir usuario: ")
    Password = input("Introducir password: ")

    if Nombre == Nombre1 and Password == Password1:
        print("Bienvenido", Nombre)
        break
    else:
        print("El usuario o password son incorrecto, por favor intentelo una vez mas")
