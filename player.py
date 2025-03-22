import pygame
from const import BLUE, GRAVITY, GROUND_Y

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = GROUND_Y - 50
        self.vel_y = 0
        self.on_ground = True

    def update(self):
        self.vel_y += GRAVITY  # Gravity
        self.rect.y += self.vel_y

        if self.rect.y >= GROUND_Y - 50:
            self.rect.y = GROUND_Y - 50
            self.on_ground = True

    def jump(self):
        if self.on_ground:
            self.vel_y = -15
            self.on_ground = False
