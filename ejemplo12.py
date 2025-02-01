#Crea un programa donde se repita un mensaje hasta que el uusario escriba salir.

mensaje = ""
while mensaje != "salir":
    mensaje = input("Escriba algo (o salir para terminar el juego): ").lower()
    print(f"Escribiste: {mensaje}")
    
    