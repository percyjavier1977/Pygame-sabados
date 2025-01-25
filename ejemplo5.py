#Crear un juego donde ingresemos una edad y debe mostrar un mesanje
#si podemos subir a la Montaña rusa.

print("BIENVENIDO AL JUEGO DE LA MONTAÑA RUSA")
edad = int(input("Ingrese su edad: "))
if edad < 8:
    print("Lo siento, eres demasiado pequeño para subir a la montaña rusa")   

elif edad <= 12:
    print("Puedes subir a la montaña rusa, pero acompañado")
else:
    print("Puedes subir solo...DIVIÉRTETE")

