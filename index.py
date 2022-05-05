import random
import pygame
from player import Player
from enemy import Enemy
pygame.init()

display = pygame.display.set_mode([1280, 720]) #Tamanho da janela
pygame.display.set_caption('Wave Slayer') #Nome do jogo (podem mudar!)

drawGroup = pygame.sprite.Group()
player = Player(drawGroup)
for i in range(20):
    enemy = Enemy(drawGroup)

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
        
    draw()
    drawGroup.update() #Aplica movimentação 

    #Gerando Inimigos
    timer += 1
    if timer == 4:
        timer = 0
        newEnemy = Enemy(drawGroup)

    pygame.display.update()