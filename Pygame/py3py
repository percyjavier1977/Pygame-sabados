#Importar pygame y sys para manejar eventos del sistema
import pygame
import sys

#nicializamos Pygame para el diseño del juego
pygame.init()

#Configuración de la ventana
ANCHO, ALTO = 800,600  #Dimenciones de la venatana
ventana = pygame.display.set_mode((ANCHO,ALTO))
pygame.display.set_caption("Juego en Python") #texto que se muestra en la barra de titulo
COLOR_FONDO = (247, 241, 54)
NEGRO = (0,0,0)
ROJO = (255,0,0)
VERDE = (0,255,0)
AZUL = (0,0,255)
FUCSIA = (255,0,251)
LILA = (146,0,218)
COLOR_ACTUAL = AZUL

x,y = ANCHO // 2, ALTO // 2 #Posisionar el circulo al centro
radio = 30
velocidad = 1

colores = [AZUL,ROJO,VERDE,NEGRO,FUCSIA,LILA]
indice_color = 0

#Bucle principal del programa
while True:
    #---manejo de los eventos----
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT: #Si cierra la ventana
            pygame.quit()
            sys.exit() #Cerramos la ventana
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:
                indice_color = (indice_color + 1) % len(colores)
                COLOR_ACTUAL = colores[indice_color]
            
    
    #---Control del teclado-----
    teclas = pygame.key.get_pressed()
    
    #Mover el circulo segun las teclas que presionas.
    if teclas[pygame.K_UP]:
        y -= velocidad
    if teclas[pygame.K_DOWN]:
        y += velocidad
    if teclas[pygame.K_LEFT]:
        x -= velocidad
    if teclas[pygame.K_RIGHT]:
        x += velocidad

     #--Crear limite de la ventana
    if x - radio < 0:   #Limite izquierdo
        x = radio

    if x + radio > ANCHO: #limite derecho
        x = ANCHO - radio
    
    if y - radio <0: #Limite superior
        y = radio
    
    if y + radio > ALTO: #Limite inferior
        y = ALTO - radio
    
    
    
    ventana.fill(COLOR_FONDO) 
    
    pygame.draw.circle(ventana,COLOR_ACTUAL,(x,y),radio)
         
    pygame.display.flip()