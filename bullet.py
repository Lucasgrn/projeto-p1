import pygame

class BulletRight(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load('assets/bullet.png')
        self.image = pygame.transform.scale(self.image, [10, 10])
        self.rect = self.image.get_rect()

        self.speed = 6

    def update(self, *args):
        self.rect.x += self.speed
        if self.rect.left > 1280:
            self.kill()

class BulletUp(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load('assets/bullet.png')
        self.image = pygame.transform.scale(self.image, [10, 10])
        self.rect = self.image.get_rect()

        self.speed = 6

    def update(self, *args):
        self.rect.y -= self.speed
        if self.rect.bottom < 0:
            self.kill()

class BulletDown(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load('assets/bullet.png')
        self.image = pygame.transform.scale(self.image, [10, 10])
        self.rect = self.image.get_rect()

        self.speed = 6

    def update(self, *args):
        self.rect.y += self.speed
        if self.rect.top > 720:
            self.kill()