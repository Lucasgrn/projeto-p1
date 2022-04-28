from platform import platform
import pygame
from player import Player
pygame.init()

display = pygame.display.set_mode([1280, 720]) #Tamanho da janela
pygame.display.set_caption('Wave Slayer') #Nome do jogo (podem mudar!)

drawGroup = pygame.sprite.Group()
player = Player(drawGroup)

def draw():
    display.fill([12, 102, 15])
    drawGroup.draw(display)
    

gameloop = True
#pressW = False

while gameloop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameloop = False

        # elif event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_w:
        #         pressW = True
        #         print('apertou')
        # elif event.type == pygame.KEYUP:
        #     if event.key == pygame.K_w:
        #         pressW = False
        #         print('soltou')

    draw()
    drawGroup.update()
    pygame.display.update()