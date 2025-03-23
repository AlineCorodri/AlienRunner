import pygame

from menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(700, 480))

    def run(self, ):
        while True:
            menu = Menu(self.window)
            menu.run()
            pass


