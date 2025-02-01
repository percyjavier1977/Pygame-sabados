#Importar pygame
import pygame
#Manejar eventos
import sys
pygame.init()
#Configurar la ventana del juego
ancho,alto = 800,600
ventana = pygame.display.set_mode((ancho,alto))  #Crear la ventana
pygame.display.set_caption("Bienvenido a mi juego")

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT: #Si se cierra la venatana
            pygame.quit() #Cerra Pygame
            sys.exit() #cerrar el programa
            
            
#Actualizamos la pantalla 
pygame.display.flip()
            




