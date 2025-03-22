import pygame
from const import *
from player import Player

pygame.init()
screen = pygame.display.set_mode((tela_largura, tela_altura))
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
obstacles = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

running = True
while running:
    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.pular()

    # Gerar obstáculos aleatórios
    if random.randint(1, 100) > 98:
        obstacle = Obstacle()
        all_sprites.add(obstacle)
        obstacles.add(obstacle)

    all_sprites.update()

    # Colisão
    if pygame.sprite.spritecollide(player, obstacles, False):
        print("Game Over!")
        running = False

    screen.fill(branco)
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()
