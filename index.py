import pygame
from player import Player
pygame.init()

display = pygame.display.set_mode([1280, 720]) #Tamanho da janela
pygame.display.set_caption('Wave Slayer') #Nome do jogo (podem mudar!)

drawGroup = pygame.sprite.Group()
player = Player(drawGroup)

def draw(): #Renderiza os objetos na tela 
    display.fill([12, 102, 15])
    drawGroup.draw(display)
    

gameloop = True

while gameloop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameloop = False
        
    draw()
    drawGroup.update() #Aplica movimentação
    pygame.display.update()