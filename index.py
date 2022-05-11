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

display = pygame.display.set_mode([1280, 720])  # Tamanho da janela
pygame.display.set_caption('Wave Slayer')  # Nome do jogo (podem mudar!)

drawGroup = pygame.sprite.Group()
enemyGroup = pygame.sprite.Group()
bulletGroup = pygame.sprite.Group()
itemGroup = pygame.sprite.Group()
player = Player(drawGroup)

BG = pygame.image.load("assets/Background.png")

def get_font(size):
    return pygame.font.Font("assets/font.ttf", size)


def draw():  # Renderiza os objetos na tela
    display.fill([12, 102, 15])
    drawGroup.draw(display)
    enemyGroup.draw(display)
    bulletGroup.draw(display)
    itemGroup.draw(display)


def coletas():
    cor_verde = get_font(25).render("Verde", True, "green")
    cor_verde_rect = cor_verde.get_rect(center=(640, 350))

    pontos_verde = get_font(25).render("X", True, "green")
    pontos_verde_rect = pontos_verde.get_rect(center=(800, 350))

    cor_amarela = get_font(25).render("Amarela", True, "yellow")
    cor_amarela_rect = cor_amarela.get_rect(center=(640, 450))

    pontos_amarela = get_font(25).render("X", True, "yellow")
    pontos_amarela_rect = pontos_amarela.get_rect(center=(800, 450))

    cor_roxa = get_font(25).render("Roxo", True, "purple")
    cor_roxa_rect = cor_roxa.get_rect(center=(640, 550))

    pontos_roxa = get_font(25).render("X", True, "purple")
    pontos_roxa_rect = pontos_roxa.get_rect(center=(800, 550))

    total = get_font(25).render("TOTAL", True, "white")
    total_rect = total.get_rect(center=(640, 650))

    total_pontos = get_font(25).render("X", True, "White")
    total_pontos_rect = total_pontos.get_rect(center=(800, 650))

    display.blit(cor_verde, cor_verde_rect)
    display.blit(cor_amarela, cor_amarela_rect)
    display.blit(cor_roxa, cor_roxa_rect)
    display.blit(pontos_verde, pontos_verde_rect)
    display.blit(pontos_amarela, pontos_amarela_rect)
    display.blit(pontos_roxa, pontos_roxa_rect)
    display.blit(total, total_rect)
    display.blit(total_pontos, total_pontos_rect)


def game_over():
    while True:
        display.blit(BG, (0, 0))

        menu_mouse_pos = pygame.mouse.get_pos()

        menu_text = get_font(80).render("Game Over", True, "#b68f40")
        menu_rect = menu_text.get_rect(center=(640, 100))

        pontuacao = get_font(25).render("Sua pontuação é a seguinte", True, "white")
        pontuacao_rect = pontuacao.get_rect(center=(640, 250))

        display.blit(menu_text, menu_rect)
        display.blit(pontuacao, pontuacao_rect)
        coletas()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()


def play():
    gameloop = True
    timer = 0
    clock = pygame.time.Clock()

    while gameloop:
        clock.tick(60)  # Limitando a 60 FPS
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameloop = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
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
        drawGroup.update()  # Aplica movimentação
        enemyGroup.update()
        bulletGroup.update()

        # Gerando Inimigos
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
            game_over()

        pygame.display.update()


def main_menu():
    while True:
        i_azul = Item(itemGroup).image = pygame.image.load('assets/blueItem.png')
        i_amarelo = Item(itemGroup).image = pygame.image.load('assets/yellowItem.png')
        i_roxo = Item(itemGroup).image = pygame.image.load('assets/purpleItem.png')

        display.blit(BG, (0, 0))

        menu_mouse_pos = pygame.mouse.get_pos()

        menu_text = get_font(80).render("Wave Slayer", True, "#b68f40")
        menu_rect = menu_text.get_rect(center=(640, 100))

        play_button = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 500),
                             text_input="JOGAR", font=get_font(40), base_color="#d7fcd4", hovering_color="White")

        display.blit(menu_text, menu_rect)
        display.blit(i_azul, (640, 700))

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
game_over()