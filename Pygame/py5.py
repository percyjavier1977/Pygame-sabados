import pygame
import sys

#Iniciar el Pygame
pygame.init()

#Dimenciones de la ventana
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Juego: Jugador, Enemigo y Meta")

#Colores
COLOR_FONDO = (100,150,200)
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
GREEN = (50,255,50)
RED = (255,50,50)

# Definir de los rectnagulos para el jugador, meta, enemigo

player = pygame.Rect(50,HEIGHT// 2-25,50,50) # (x,y,ancho,alto)
goal = pygame.Rect(WIDTH-100,HEIGHT//2-25,50,50)
enemy = pygame.Rect(WIDTH//2-25,50,50,50)

# variables de velocidad
player_speed = 3
enemy_speed = 2
enemy_direcction = 1

clock = pygame.time.Clock()
font = pygame.font.SysFont(None,48)

game_over = False
win = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    if not game_over:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.left > 0:
            player.x -= player_speed
        if keys[pygame.K_RIGHT] and player.right < WIDTH:
            player.x += player_speed 
        if keys[pygame.K_UP] and player.top > 0:
            player.y -= player_speed
        if keys[pygame.K_DOWN] and player.bottom < HEIGHT:
            player.y += player_speed
        
        #Movimiento del enemigo
        enemy.x += enemy_speed * enemy_direcction
        #Canbiar la direccion cuando alza los bored
        if enemy.left <=0 or enemy.right >=WIDTH:
            enemy_direcction *=-1
            
        #Comprobar si toca al enemigo o a la meta
        if player.colliderect(goal):
            win = True
            game_over = True
        if player.colliderect(enemy):
            win = False
            game_over = True
    
    #Color de la pantalla
    screen.fill(COLOR_FONDO) #Color de la pantalla
    pygame.draw.rect(screen,GREEN,player)
    pygame.draw.rect(screen,RED,goal)
    pygame.draw.rect(screen,BLACK,enemy)
    
    if game_over:
        if win:
            text = font.render("¡Ganaste el juego",True,WHITE)
        else:
            text = font.render("¡perdiste el juego",True,WHITE)
        
        text_rect = text.get_rect(center=(WIDTH//2,HEIGHT//2))
        screen.blit(text,text_rect)
            

     
    pygame.display.flip() #Actualiza la pantalla
    clock.tick(60)



    