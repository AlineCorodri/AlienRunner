import pygame
import sys
from menu import Menu
from level import Level  # Importa o arquivo do nível

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(700, 480))
        self.running = True  # Controla o loop do jogo

    def run(self):
        while self.running:
            menu = Menu(self.window)
            option = menu.run()  # Aguarda a seleção do usuário

            if option == "PLAY":
                level = Level(self.window, "Level 1", "normal")  # Inicia o nível
                level.run()
            elif option == "EXIT":
                self.running = False  # Sai do jogo

        pygame.quit()