import pygame
import random

class EnemyToLeft(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load('assets/enemy.png')
        self.image = pygame.transform.scale(self.image, [50, 50])
        self.rect = pygame.Rect(0, 0, 50, 50)
        self.rect.x = 1280 + random.randint(1, 100)
        self.rect.y = random.randint(1, 700)
        self.speed = random.randint(2, 4)

    def update(self, *args):
            #Movimentação
            self.rect.x -= self.speed
            if self.rect.right < 0:
                self.kill()

class EnemyToRight(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load('assets/enemy.png')
        self.image = pygame.transform.scale(self.image, [50, 50])
        self.rect = pygame.Rect(0, 0, 50, 50)
        self.rect.x = 0 - random.randint(1, 100)
        self.rect.y = random.randint(1, 700)
        self.speed = random.randint(2, 4)

    def update(self, *args):
            #Movimentação
            self.rect.x += self.speed
            if self.rect.left > 1280:
                self.kill()

class EnemyToUp(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load('assets/enemy.png')
        self.image = pygame.transform.scale(self.image, [50, 50])
        self.rect = pygame.Rect(0, 0, 50, 50)
        self.rect.x = random.randint(1, 1200)
        self.rect.y = 720 + random.randint(1, 100)
        self.speed = random.randint(2, 4)

    def update(self, *args):
            #Movimentação
            self.rect.y -= self.speed
            if self.rect.bottom < 0:
                self.kill()

class EnemyToDown(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load('assets/enemy.png')
        self.image = pygame.transform.scale(self.image, [50, 50])
        self.rect = pygame.Rect(0, 0, 50, 50)
        self.rect.x = random.randint(1, 1200)
        self.rect.y = 0 - random.randint(1, 100)
        self.speed = random.randint(2, 4)

    def update(self, *args):
            #Movimentação
            self.rect.y += self.speed
            if self.rect.top > 1280:
                self.kill()