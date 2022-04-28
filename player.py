import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load('assets/player.png')
        self.image = pygame.transform.scale(self.image, [50, 50])
        self.rect = pygame.Rect(50, 50, 50, 50)

    def update(self, *args):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.rect.y -= 1
        elif keys[pygame.K_s]:
            self.rect.y += 1
        elif keys[pygame.K_a]:
            self.rect.x -= 1
        elif keys[pygame.K_d]:
            self.rect.x += 1