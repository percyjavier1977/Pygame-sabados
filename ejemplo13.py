import time
while True:
    pregunta = input("¿Desea seguir jugando?..S/N: ").lower()
    if pregunta == "n":
        print("Sliste del juego....")
        break #cerrar el bucle
    else:
        print("Continua jugando")
        time.sleep(2)
