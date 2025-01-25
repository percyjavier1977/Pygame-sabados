#Crear un juego donde el usuario ingrese un número y debe adiviar el número
# de la suerte. 
numero_secreto = 7

respuesta = int(input("¿Cual es tu número de la suerte?"))
if respuesta == numero_secreto:
    print("¡Felicidades! Adivinaste el número")
else:
    print("No adivisnaste el número...Sigue intentando")
