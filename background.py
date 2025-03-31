from const import WIN_WIDTH
from entity import Entity


class Background(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self):
        self.rect.x -= 2  # Velocidade do scroll (ajuste conforme necessário)

        # Se a imagem sair totalmente da tela pela esquerda, reposiciona para o final da fila
        if self.rect.right <= 0:
            self.rect.left = WIN_WIDTH