import pygame

from EntityFactory import EntityFactory
from const import WIN_WIDTH, WIN_HEIGHT, WHITE, BLACK
from entity import Entity


class Level:
    def __init__(self, window, name, game_mode):
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
        while self.running:
            self.window.fill(BLACK)  # Preenche a tela com fundo preto

            # Desenha as entidades (incluindo a imagem de fundo)
            for ent in reversed(self.entity_list):
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()

            # Renderiza o título do nível
            level_text = self.font.render("LEVEL 01", True, WHITE)
            level_rect = level_text.get_rect(topleft=(10, 10))  # Posição no canto superior esquerdo
            self.window.blit(level_text, level_rect)

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
