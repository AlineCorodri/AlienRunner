import random
import pygame

from const import BLACK


class Obstacle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = 800
        self.rect.y = 320

    def update(self):
        self.rect.x -= 5  # Movimento para a esquerda
        if self.rect.x < -30:
            self.kill()
