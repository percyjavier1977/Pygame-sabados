#Crear un juego donde el usuario ingresa un número. Si el número es par 
# debe ganar el juego, de lo contrario debe perder el juego.

numero = int(input("Ingrese un número: "))
if numero % 2 == 0:
    print("¡Felicidades!..ganaste el juego")
else:
    print("Perdiste el juego :(")