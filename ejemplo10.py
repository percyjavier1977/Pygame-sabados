import random

numero_secreto = random.randint(1,5)
print("Tienes 3 intentos para adivinar un número entre 1 y 5")

for intento in range(1,4):
    numero = int(input(f"Intento: {intento}: "))
    if numero == numero_secreto:
        print("Felicidades, adivinaste!")
        break #permite cerrar el bucle
    else:
        print("Incorrecto..No es el número secreto")
        
else:
    #Solo sale cuando se cumple todos los bucles
    print("Has perdido el juego")
    print(f"El número secreto era: {numero_secreto}")



        
        
