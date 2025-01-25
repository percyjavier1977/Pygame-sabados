import random
numero_secreto = random.randint(1,5)

respuesta = int(input("Ingrese su números de la suerte y ¡GANA UN PREMIO!: "))
if respuesta == numero_secreto:
    print("¡Felicidades! Adivinaste el número")
    print("Ganaste un premio")
elif respuesta < numero_secreto:
    print("PERDISTE....El número secreto es mayor")
    
else:
    print("PERDISTE....El número secreto es menor")


print("El número secreto era:", numero_secreto)