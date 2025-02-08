#Importar pygame y sys para manejar eventos del sistema
import pygame
import sys

#nicializamos Pygame para el diseño del juego
pygame.init()

#Configuración de la ventana
ANCHO, ALTO = 800,600  #Dimenciones de la venatana
ventana = pygame.display.set_mode((ANCHO,ALTO))
pygame.display.set_caption("Juego en Python") #texto que se muestra en la barra de titulo
COLOR_FONDO = (200,200,200)
NEGRO = (0,0,0)
ROJO = (255,0,0)
VERDE = (0,255,0)
AZUL = (0,0,255)

#Bucle principal del programa
while True:
    #---manejo de los eventos----
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT: #Si cierra la ventana
            pygame.quit()
            sys.exit() #Cerramos la ventana
            
    #Aplica el color a la ventana
    ventana.fill(COLOR_FONDO)
    
    #Dibujar una linea
    pygame.draw.line(ventana,NEGRO,(300,300),(500,200),5)
    
    #Dibujar un rectangulo
    pygame.draw.rect(ventana,ROJO,(50,400,700,100))
    
    #Dibujar el circulo
    pygame.draw.circle(ventana,VERDE,(400,100),60)
    
    #Dibujar el elipse
    pygame.draw.ellipse(ventana,AZUL,(250,200,300,100))
    
    

    #Actualiza la venta para mostrar algun cambio
    pygame.display.flip()