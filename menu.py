import pygame
import time
from pygame import Surface, Rect
from pygame.font import Font

from const import WIN_WIDTH, GREEN_BLACK, MENU_OPTION, WHITE, BLACK, ORANGE, GREEN, LIGHT_GREEN, KEY_UP, KEY_DOWN, KEY_ENTER

class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./assets/menu.png').convert_alpha()
        self.rect = self.surf.get_rect(center=(430, 300))

        self.last_time = time.time()
        self.show_text_1 = True
        self.show_text_2 = True

        self.font_size = 80
        self.menu_rects = []
        self.title_rects = []

        self.selected_index = 0

    def run(self):
        pygame.mixer_music.load('./assets/menu.mp3')
        pygame.mixer_music.play(-1)

        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            mouse_pos = pygame.mouse.get_pos()

            if time.time() - self.last_time >= 0.2:
                self.last_time = time.time()
                self.show_text_2 = not self.show_text_2

            self.title_rects.clear()
            title_color = LIGHT_GREEN if self.is_hovering(mouse_pos, (WIN_WIDTH / 2, 70)) else GREEN_BLACK
            self.title_rects.append(self.menu_text(150, "ALIEN", title_color, ((WIN_WIDTH / 2), 70)))

            if self.show_text_2:
                title_color = LIGHT_GREEN if self.is_hovering(mouse_pos, (WIN_WIDTH / 2, 120)) else GREEN_BLACK
                self.title_rects.append(self.menu_text(150, "RUNNER", title_color, ((WIN_WIDTH / 2), 120)))

            self.menu_rects.clear()
            for i, option in enumerate(MENU_OPTION):
                option_pos = ((WIN_WIDTH / 2), 200 + 50 * i)
                color = ORANGE if self.is_hovering(mouse_pos, option_pos) or i == self.selected_index else BLACK
                option_rect = self.menu_text(self.font_size, option, color, option_pos)
                self.menu_rects.append(option_rect)

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    for i, rect in enumerate(self.menu_rects):
                        if rect.collidepoint(mouse_pos):
                            return self.handle_menu_selection(i)  # Retorna a opção escolhida
                elif event.type == pygame.KEYDOWN:
                    if event.key == KEY_UP:
                        self.selected_index = (self.selected_index - 1) % len(MENU_OPTION)
                    elif event.key == KEY_DOWN:
                        self.selected_index = (self.selected_index + 1) % len(MENU_OPTION)
                    elif event.key == KEY_ENTER:
                        return self.handle_menu_selection(self.selected_index)  # Retorna a opção escolhida

    def is_hovering(self, mouse_pos, text_center_pos):
        x, y = text_center_pos
        return abs(mouse_pos[0] - x) < 100 and abs(mouse_pos[1] - y) < 25

    def handle_menu_selection(self, index):
        if index == 0:  # PLAY
            return "PLAY"
        elif index == 1:  # SCORE
            return "SCORE"
        elif index == 2:  # EXIT
            return "EXIT"

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        if not isinstance(text, str):
            text = str(text)
        text_font: Font = pygame.font.Font('./assets/game_over.ttf', size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
        return text_rect
