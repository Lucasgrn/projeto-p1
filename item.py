import random
import pygame

class Item(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load('assets/blueItem.png')
        self.image = pygame.transform.scale(self.image, [20, 20])
        self.rect = pygame.Rect(0, 0, 50, 50)
        self.rect.x = random.randint(1, 1200)
        self.rect.y = random.randint(1, 700)