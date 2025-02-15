#Importamos pygame y sys para manejar eventos del sistema
import pygame
import sys
import random

#nicializamos Pygame para el diseño del juego

pygame.init()
pygame.mixer.init()

#Configuración de la ventana
ANCHO, ALTO = 800,600  #Dimenciones de la venatana
ventana = pygame.display.set_mode((ANCHO,ALTO))
pygame.display.set_caption("Evita al enemigo y gana puntos") #texto que se muestra en la barra de titulo

#Definir colores
COLOR_FONDO = (247, 241, 54)
NEGRO = (0,0,0)
ROJO = (255,0,0)
VERDE = (0,255,0)
AZUL = (0,0,255)
FUCSIA = (255,0,251)
LILA = (146,0,218)
COLOR_ACTUAL = AZUL

#configuracion del circulo (Jugador)
x,y = ANCHO // 2, ALTO // 2
radio = 30
velocidad = 1

#Configuracion del enemigo
enemigo_x, enemigo_y = random.randint(50,ANCHO-50),random.randint(50,ALTO-50)
enemigo_velocidad = 3

#Meta
meta_x, meta_y =  random.randint(50,ANCHO-50),random.randint(50,ALTO-50)

#Lista de colores y sonido
colores = [AZUL,ROJO,VERDE,NEGRO,FUCSIA,LILA]
indice_color = 0
#sonido_cambio = pygame.mixer.Sound("sonido.ogg")

#Fuente para el texto
fuente = pygame.font.Font(None,36)
puntos = 0
tiempo_maximo = 1800

#Bucle principal del juego
while True:
    #control del tiempo
    tiempo_maximo -=1
    tiempo_maximo = tiempo_maximo - 1
    if tiempo_maximo <=0:
        print("Teimpo terminado. Puntuación final:",puntos)
        pygame.quit()
        sys.exit()
    #---Manejo de eventos----
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT: #Si cierra la ventana
            pygame.quit()
            sys.exit() #Cerramos la ventana
        
        #Cambia el color con la barra espaciadora
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:
                #sonido_cambio.play() #Cuando se preciona la barra espaciadora ejecute el sonido
                indice_color = (indice_color + 1) % len(colores)
                COLOR_ACTUAL = colores[indice_color]

    #Movimiento del jugador
    teclas = pygame.key.get_pressed()
    
    if teclas[pygame.K_UP]:
        y -= velocidad
    if teclas[pygame.K_DOWN]:
        y += velocidad
    if teclas[pygame.K_LEFT]:
        x -= velocidad
    if teclas[pygame.K_RIGHT]:
        x += velocidad

     #--Límites de la venatana
    x = max(radio,min(ANCHO-radio,x))
    y = max(radio,min(ALTO-radio,y))
    
    #Programacion del juego

   


    #Dibujando los objetos
    ventana.fill(COLOR_FONDO) 
    pygame.draw.circle(ventana,COLOR_ACTUAL,(x,y),radio)
    pygame.draw.circle(ventana,NEGRO,(enemigo_x,enemigo_y),radio)
    pygame.draw.circle(ventana,LILA,(meta_x,meta_y),15)

    pygame.display.flip()
    pygame.time.delay(16)






    
    
