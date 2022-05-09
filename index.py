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
itemGroup = pygame.sprite.Group()
player = Player(drawGroup)

def draw(): #Renderiza os objetos na tela 
    display.fill([12, 102, 15])
    drawGroup.draw(display)
    enemyGroup.draw(display)
    bulletGroup.draw(display)
    itemGroup.draw(display)
    

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
            newItemB = Item(itemGroup).image = pygame.image.load('assets/blueItem.png')
        elif random.random() < 0.1:    
            newItemB = Item(itemGroup).image = pygame.image.load('assets/yellowItem.png')
        elif random.random() < 0.01:
            newItemB = Item(itemGroup).image = pygame.image.load('assets/purpleItem.png')

    collects = pygame.sprite.spritecollide(player, itemGroup, True)

    if collide:
        print('Fim de jogo')
        gameloop = False

    pygame.display.update()