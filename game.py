import pygame
from const import *
from player import Player
from enemy import Obstacle  # Certifique-se de que o caminho está correto

pygame.init()
window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
obstacles = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

running = True
while running:
    clock.tick(fps)

    print("Game is running...")  # Mensagem para verificar se o loop está em execução

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.jump()

    # Gerar obstáculos aleatórios
    if random.randint(1, 100) > 98:
        obstacle = Obstacle()
        all_sprites.add(obstacle)
        obstacles.add(obstacle)

    all_sprites.update()

    # Colisão
    if pygame.sprite.spritecollide(player, obstacles, False):
        print("Game Over!")  # Verifica se houve colisão
        running = False

    window.fill(WHITE)
    all_sprites.draw(window)
    pygame.display.flip()

pygame.quit()
