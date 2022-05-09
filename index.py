import pygame
from bullet import BulletDown, BulletLeft, BulletRight, BulletUp
from player import Player
from enemy import EnemyToLeft, EnemyToUp, EnemyToDown, EnemyToRight
pygame.init()

display = pygame.display.set_mode([1280, 720]) #Tamanho da janela
pygame.display.set_caption('Wave Slayer') #Nome do jogo (podem mudar!)

drawGroup = pygame.sprite.Group()
enemyGroup = pygame.sprite.Group()
bulletGroup = pygame.sprite.Group()
player = Player(drawGroup)

def draw(): #Renderiza os objetos na tela 
    display.fill([12, 102, 15])
    drawGroup.draw(display)
    enemyGroup.draw(display)
    bulletGroup.draw(display)
    

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
    if timer == 30:
        timer = 0
        newEnemyLeft = EnemyToLeft(enemyGroup)
        newEnemyUp = EnemyToUp(enemyGroup)
        newEnemyDown = EnemyToDown(enemyGroup)
        newEnemyRight = EnemyToRight(enemyGroup)
    
    collide = pygame.sprite.spritecollide(player, enemyGroup, False)
    killEnemy = pygame.sprite.groupcollide(bulletGroup, enemyGroup, True, True)

    if collide:
        print('Fim de jogo')
        gameloop = False

    pygame.display.update()