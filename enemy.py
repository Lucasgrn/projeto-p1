import pygame
import random

class Enemy(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load('assets/enemy.png')
        self.image = pygame.transform.scale(self.image, [50, 50])
        self.rect = pygame.Rect(0, 0, 50, 50)
        self.rect.x = 1280 + random.randint(1, 100)
        self.rect.y = random.randint(1, 700)
        self.speed = random.randint(4, 6)

    def update(self, *args):
            #Movimentação
            self.rect.x -= self.speed
            if self.rect.right < 0:
                self.kill()