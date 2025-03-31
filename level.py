import sys

import pygame
from pygame import Rect, Surface
from pygame.font import Font

from EntityFactory import EntityFactory
from const import WIN_WIDTH, WIN_HEIGHT, WHITE, BLACK
from entity import Entity


class Level:
    def __init__(self, window, name, game_mode):
        self.timeout = 20000
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.running = True  # Controla o loop do nível
        self.font = pygame.font.Font('./assets/game_over.ttf', 80)  # Fonte para o texto do nível
        self.score_font = pygame.font.Font('./assets/game_over.ttf', 30)  # Fonte para o score
        self.score = 0  # Inicializa o score
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('level1Bg'))  # Adiciona a entidade de fundo

    def update_background_positions(self):
        # Ajusta a posição de cada fundo para que fiquem contínuos e ajustado
        for i, entity in enumerate(self.entity_list):
            entity.rect.x = i * WIN_WIDTH  # Garante que as imagens fiquem contínuas para a direita
            entity.rect.y = WIN_HEIGHT - entity.rect.height  # Alinha o fundo com o chão da tela

    def run(self):
        pygame.mixer_music.load(f'./assets/level1.mp3.wav')
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()
        while self.running:
            clock.tick(60)
            self.window.fill(BLACK)  # Preenche a tela com fundo preto

            # Desenha as entidades (incluindo a imagem de fundo)
            for ent in reversed(self.entity_list):
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()

            # Renderiza o título do nível
           # level_text = self.font.render("LEVEL 01", True, WHITE)
           # level_rect = level_text.get_rect(topleft=(10, 10))  # Posição no canto superior esquerdo
           # self.window.blit(level_text, level_rect)

            # Renderiza o score
            score_text = self.score_font.render(f"Score: {self.score}", True, WHITE)
            score_rect = score_text.get_rect(topleft=(10, 100))  # Posição abaixo do "LEVEL 01"
            self.window.blit(score_text, score_rect)

            pygame.display.flip()  # Atualiza a tela

            self.score += 1  # Aumenta o score a cada iteração

            # Verifica eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:  # Pressionou ESC para retornar ao menu
                        self.running = False  # Encerra o loop, retornando ao menu

            # printed text
            self.level_text(14, f'{self.name} - Timeout: {self.timeout / 1000:.1f}s', WHITE, (10, 5))
            self.level_text(14, f'fps: {clock.get_fps():.0f}', WHITE, (10, WIN_HEIGHT - 35))
            self.level_text(14, f'entidades: {len(self.entity_list)}', WHITE, (10, WIN_HEIGHT - 20))
            pygame.display.flip()

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)
