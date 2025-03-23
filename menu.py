import pygame
import time
from pygame import Surface, Rect
from pygame.font import Font

from const import WIN_WIDTH, GREEN_BLACK, MENU_OPTION, WHITE


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./assets/menu.png')
        self.rect = self.surf.get_rect(center=(430, 300))

        # Controle de tempo para alternar a visibilidade do texto
        self.last_time = time.time()
        self.show_text_1 = True  # Controle da visibilidade do texto "ALIEN"
        self.show_text_2 = True  # Controle da visibilidade do texto "RUNNER"

    def run(self):
        pygame.mixer_music.load('./assets/menu.mp3')
        pygame.mixer_music.play(-1)

        while True:
            self.window.blit(source=self.surf, dest=self.rect)

            # Controla o efeito de piscamento para o texto "ALIEN"
            if time.time() - self.last_time >= 0.5:  # Intervalo de 0.5 segundos
                self.last_time = time.time()
                self.show_text_1 = not self.show_text_1  # Alterna a visibilidade do texto "ALIEN"

            # Controla o efeito de piscamento para o texto "RUNNER"
            if time.time() - self.last_time >= 0.5:  # Intervalo de 0.5 segundos
                self.last_time = time.time()
                self.show_text_2 = not self.show_text_2  # Alterna a visibilidade do texto "RUNNER"

            # Exibe o texto "ALIEN" se a visibilidade estiver ativada
            if self.show_text_1:
                self.menu_text(150, "ALIEN", GREEN_BLACK, ((WIN_WIDTH / 2), 70))

            # Exibe o texto "RUNNER" se a visibilidade estiver ativada
            if self.show_text_2:
                self.menu_text(150, "RUNNER", GREEN_BLACK, ((WIN_WIDTH / 2), 120))

            for i in range(len(MENU_OPTION)):
                self.menu_text(80, MENU_OPTION, WHITE, ((WIN_WIDTH / 2), 200 + 30 * i))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        if not isinstance(text, str):
            text = str(text)
        text_font: Font = pygame.font.Font('./assets/game_over.ttf', size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
