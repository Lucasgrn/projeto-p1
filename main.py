from dis import dis
import random
import pygame
import sys
from bullet import BulletDown, BulletLeft, BulletRight, BulletUp
from player import Player
from enemy import EnemyToLeft, EnemyToUp, EnemyToDown, EnemyToRight
from item import Item
from menu import Button

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

BG = pygame.image.load("assets/Background.png")

#parte dos audios
pygame.mixer.music.set_volume(0.12)
musica_fundo = pygame.mixer.music.load("assets/opening_theme.wav")
som_colisao_item = pygame.mixer.Sound("assets/colisao_item.wav")
som_tiro = pygame.mixer.Sound("assets/tiro.wav")
som_colisao_inimigo = pygame.mixer.Sound("assets/colisao_inimigo.wav")
som_gameOver = pygame.mixer.Sound("assets/gameOver.wav")



pygame.mixer.music.play(-1)

def get_font(size):
    return pygame.font.Font("assets/font.ttf", size)

def draw(): #Renderiza os objetos na tela 
    display.fill([12, 102, 15])
    drawGroup.draw(display)
    enemyGroup.draw(display)
    bulletGroup.draw(display)
    itemBGroup.draw(display)
    itemYGroup.draw(display)
    itemPGroup.draw(display)

def coletas(itemAzul, itemAmarelo, itemRoxo):
    soma = (itemAzul* 100) + (itemAmarelo * 500) + (itemRoxo * 1000)
    total_ = f"Total: {soma}"
    itemAzul = str(itemAzul)
    itemAmarelo = str(itemAmarelo)
    itemRoxo = str(itemRoxo)

    cor_azul = get_font(25).render("Azul", True, "blue")
    cor_azul_rect = cor_azul.get_rect(center=(600, 350))

    pontos_azul = get_font(25).render(itemAzul, True, "blue")
    pontos_azul_rect = pontos_azul.get_rect(center=(800, 350))

    cor_amarela = get_font(25).render("Amarela", True, "yellow")
    cor_amarela_rect = cor_amarela.get_rect(center=(640, 430))

    pontos_amarela = get_font(25).render(itemAmarelo, True, "yellow")
    pontos_amarela_rect = pontos_amarela.get_rect(center=(800, 430))

    cor_roxa = get_font(25).render("Roxo", True, "purple")
    cor_roxa_rect = cor_roxa.get_rect(center=(604, 510))

    pontos_roxa = get_font(25).render(itemRoxo, True, "purple")
    pontos_roxa_rect = pontos_roxa.get_rect(center=(800, 510))

    total = get_font(25).render(total_, True, "white")
    total_rect = total.get_rect(center=(650, 600))

    '''total_pontos = get_font(25).render(total, True, "White")
    total_pontos_rect = total_pontos.get_rect(center=(800, 650))'''

    display.blit(cor_azul, cor_azul_rect)
    display.blit(cor_amarela, cor_amarela_rect)
    display.blit(cor_roxa, cor_roxa_rect)
    display.blit(pontos_azul, pontos_azul_rect)
    display.blit(pontos_amarela, pontos_amarela_rect)
    display.blit(pontos_roxa, pontos_roxa_rect)
    display.blit(total, total_rect)
    '''display.blit(total_pontos, total_pontos_rect)'''
    

def game_over(v1, v2, v3):
    while True:
        display.blit(BG, (0, 0))

        menu_mouse_pos = pygame.mouse.get_pos()

        menu_text = get_font(80).render("Game Over", True, "#b68f40")
        menu_rect = menu_text.get_rect(center=(640, 100))

        pontuacao = get_font(25).render("Sua pontuação é a seguinte", True, "white")
        pontuacao_rect = pontuacao.get_rect(center=(640, 250))

        display.blit(menu_text, menu_rect)
        display.blit(pontuacao, pontuacao_rect)
        coletas(v1, v2, v3)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
        pygame.display.update()


def play(): # transforma o jogo principal numa função que será executada no menu principal
    timer, itemAzul, itemAmarelo, itemRoxo = 0, 0, 0, 0
    gameloop = True
    clock = pygame.time.Clock()

    mostrar_azul = f'Azul:{itemAzul}'
    mostrar_amarelo = f'Amarelo:{itemAmarelo}'
    mostrar_roxo = f'Roxo:{itemRoxo}'

    while gameloop:
        clock.tick(60) #Limitando a 60 FPS
        mostrar_azul = f'Azul: {itemAzul}'
        mostrar_amarelo = f'Amarelo: {itemAmarelo}'
        mostrar_roxo = f'Roxo: {itemRoxo}'

        msg_azul = get_font(10).render(mostrar_azul, True, "white")
        msg_azul_rect = msg_azul.get_rect(center=(800, 50))

        msg_amarelo = get_font(10).render(mostrar_amarelo, True, "white")
        msg_amarelo_rect = msg_amarelo.get_rect(center=(950, 50))

        msg_roxo = get_font(10).render(mostrar_roxo, True, "white")
        msg_roxo_rect = msg_roxo.get_rect(center=(1100, 50))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameloop = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    som_tiro.play()
                    newBullet = BulletRight(bulletGroup)
                    newBullet.rect.center = player.rect.center

                elif event.key == pygame.K_LEFT:
                    som_tiro.play()
                    newBullet = BulletLeft(bulletGroup)
                    newBullet.rect.center = player.rect.center

                elif event.key == pygame.K_UP:
                    som_tiro.play()
                    newBullet = BulletUp(bulletGroup)
                    newBullet.rect.center = player.rect.center

                elif event.key == pygame.K_DOWN:
                    som_tiro.play()
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
            som_colisao_inimigo.play()
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
            som_colisao_item.play()
        if collectY:
            itemAmarelo += 1
            print(f'Amarelo: {itemAmarelo}')
            som_colisao_item.play()
        if collectP:
            itemRoxo += 1
            print(f'Roxo: {itemRoxo}')
            som_colisao_item.play()
        if collide:
            print('Fim de jogo')
            pygame.mixer.music.set_volume(0)
            som_gameOver.play()
            game_over(itemAzul, itemAmarelo, itemRoxo)

        display.blit(msg_azul, msg_azul_rect)
        display.blit(msg_amarelo, msg_amarelo_rect)
        display.blit(msg_roxo, msg_roxo_rect)

        pygame.display.update()

def main_menu(): # menu principal. Tem apenas o botão de jogar
    while True:

        # mostrar a tela do menu principal e quantos pontos valhem cada item

        i_azul = pygame.image.load('assets/blueItem.png')
        i_azul = pygame.transform.scale(i_azul, [20, 20])
        valor_i_azul = ' = 100 pontos'
        msg_azul = get_font(15).render(valor_i_azul, True, 'white')

        i_amarelo = pygame.image.load('assets/yellowItem.png')
        i_amarelo = pygame.transform.scale(i_amarelo, [20, 20])
        valor_i_amarelo = ' = 500 pontos'
        msg_amarelo = get_font(15).render(valor_i_amarelo, True, 'white')

        i_roxo = pygame.image.load('assets/purpleItem.png')
        i_roxo = pygame.transform.scale(i_roxo, [20, 20])
        valor_i_roxo = ' = 1000 pontos'
        msg_roxo = get_font(15).render(valor_i_roxo, True, 'white')

        display.blit(BG, (0, 0))

        menu_mouse_pos = pygame.mouse.get_pos()

        menu_text = get_font(80).render("Wave Slayer", True, "#b68f40")
        menu_rect = menu_text.get_rect(center=(640, 120))

        play_button = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 360),
                             text_input="JOGAR", font=get_font(40), base_color="#d7fcd4", hovering_color="White")

        

        display.blit(menu_text, menu_rect)
        
        display.blit(i_azul, (550, 500))
        display.blit(msg_azul, (570, 500))

        display.blit(i_amarelo, (550, 550))
        display.blit(msg_amarelo, (570, 550))

        display.blit(i_roxo, (550, 600))
        display.blit(msg_roxo, (570, 600))

        
        for button in [play_button]:
            button.changeColor(menu_mouse_pos)
            button.update(display)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.checkForInput(menu_mouse_pos):
                    play()

        pygame.display.update()

main_menu()