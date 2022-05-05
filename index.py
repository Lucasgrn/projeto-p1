import random
import pygame
from bullet import BulletDown, BulletRight, BulletUp
from player import Player
from enemy import EnemyToLeft, EnemyToUp, EnemyToDown
pygame.init()

display = pygame.display.set_mode([1280, 720]) #Tamanho da janela
pygame.display.set_caption('Wave Slayer') #Nome do jogo (podem mudar!)

drawGroup = pygame.sprite.Group()
player = Player(drawGroup)

def draw(): #Renderiza os objetos na tela 
    display.fill([12, 102, 15])
    drawGroup.draw(display)
    

gameloop = True
timer = 0
clock = pygame.time.Clock()

while gameloop:
    clock.tick(60) #Limitando a 60 FPS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameloop = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT :
                newBullet = BulletRight(drawGroup)
                newBullet.rect.center = player.rect.center
            elif event.key == pygame.K_UP:
                newBullet = BulletUp(drawGroup)
                newBullet.rect.center = player.rect.center
            elif event.key == pygame.K_DOWN:
                newBullet = BulletDown(drawGroup)
                newBullet.rect.center = player.rect.center


        
    draw()
    drawGroup.update() #Aplica movimentação 

    #Gerando Inimigos
    timer += 1
    if timer == 15:
        timer = 0
        newEnemyLeft = EnemyToLeft(drawGroup)
        newEnemyUp = EnemyToUp(drawGroup)
        newEnemyDown = EnemyToDown(drawGroup)
        


    pygame.display.update()