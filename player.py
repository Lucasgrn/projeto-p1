import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load('assets/player.png')
        self.image = pygame.transform.scale(self.image, [50, 50])
        self.rect = pygame.Rect(640, 360, 50, 50)

    def update(self, *args):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.rect.y -= 5

        elif keys[pygame.K_s]:
            self.rect.y += 5

        elif keys[pygame.K_a]:
            self.rect.x -= 5

        elif keys[pygame.K_d]:
            self.rect.x += 5

        if self.rect.top < 0:
            self.rect.top = 0
        elif self.rect.bottom > 720:
            self.rect.bottom = 720
        elif self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > 1280:
            self.rect.right = 1280