import random
import pygame
from bullet import BulletDown, BulletLeft, BulletRight, BulletUp
from player import Player
from enemy import EnemyToLeft, EnemyToUp, EnemyToDown, EnemyToRight
from item import Item
pygame.init()

display = pygame.display.set_mode([1280, 720]) #Tamanho da janela
pygame.display.set_caption('Wave Slayer') #Nome do jogo (podem mudar!)

drawGroup = pygame.sprite.Group()
enemyGroup = pygame.sprite.Group()
bulletGroup = pygame.sprite.Group()
itemBGroup = pygame.sprite.Group()
itemYGroup = pygame.sprite.Group()
itemPGroup = pygame.sprite.Group()
player = Player(drawGroup)

def draw(): #Renderiza os objetos na tela 
    display.fill([12, 102, 15])
    drawGroup.draw(display)
    enemyGroup.draw(display)
    bulletGroup.draw(display)
    itemBGroup.draw(display)
    itemYGroup.draw(display)
    itemPGroup.draw(display)
    

gameloop = True
timer, itemAzul, itemAmarelo, itemRoxo = 0, 0, 0 ,0
clock = pygame.time.Clock()

while gameloop:
    clock.tick(60) #Limitando a 60 FPS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameloop = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT :
                newBullet = BulletRight(bulletGroup)
                newBullet.rect.center = player.rect.center
            elif event.key == pygame.K_LEFT:
                newBullet = BulletLeft(bulletGroup)
                newBullet.rect.center = player.rect.center
            elif event.key == pygame.K_UP:
                newBullet = BulletUp(bulletGroup)
                newBullet.rect.center = player.rect.center
            elif event.key == pygame.K_DOWN:
                newBullet = BulletDown(bulletGroup)
                newBullet.rect.center = player.rect.center


        
    draw()
    drawGroup.update() #Aplica movimentação 
    enemyGroup.update()
    bulletGroup.update()

    #Gerando Inimigos
    timer += 1
    if timer == 50:
        timer = 0
        newEnemyLeft = EnemyToLeft(enemyGroup)
        newEnemyUp = EnemyToUp(enemyGroup)
        newEnemyDown = EnemyToDown(enemyGroup)
        newEnemyRight = EnemyToRight(enemyGroup)
    
    collide = pygame.sprite.spritecollide(player, enemyGroup, False)
    killEnemy = pygame.sprite.groupcollide(bulletGroup, enemyGroup, True, True)

    if killEnemy:
        if random.random() < 0.2:
            newItem = Item(itemBGroup).image = pygame.image.load('assets/blueItem.png')
        elif random.random() < 0.1:    
            newItem = Item(itemYGroup).image = pygame.image.load('assets/yellowItem.png')
        elif random.random() < 0.01:
            newItem = Item(itemPGroup).image = pygame.image.load('assets/purpleItem.png')
    
    collectB = pygame.sprite.spritecollide(player, itemBGroup, True)
    collectY = pygame.sprite.spritecollide(player, itemYGroup, True)
    collectP = pygame.sprite.spritecollide(player, itemPGroup, True)

    if collectB:
        itemAzul += 1
        print(f'Azul: {itemAzul}')
    if collectY:
        itemAmarelo += 1
        print(f'Amarelo: {itemAmarelo}')
    if collectP:
        itemRoxo += 1
        print(f'Roxo: {itemRoxo}')

    if collide:
        print('Fim de jogo')
        gameloop = False

    pygame.display.update()