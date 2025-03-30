import pygame

# COLORS

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN_BLACK = (0, 100, 0)
GREEN = (0, 255, 0)
ORANGE = (255, 165, 0)
LIGHT_GREEN = (0, 255, 100)

# speed

ENTITY_SPEED = {
    'level1Bg0': 0,
    'level1Bg1': 1,
    'level1Bg2': 2,
    'level1Bg3': 3,
    'level1Bg4': 4,
    'level1Bg5': 5,
    'level1Bg6': 6,
  #  'level2Bg0': 0,
   #'level2Bg2': 2,
  #  'level2Bg3': 3,
  #  'level2Bg4': 4,
  #  'Player1': 3,
  #  'Player1Shot': 1,
  #  'Player2': 3,
  #  'Player2Shot': 3,
  #  'Enemy1': 1,
  #  'Enemy1Shot': 5,
  #  'Enemy2': 1,
  #  'Enemy2Shot': 2,
}

# Menu

MENU_OPTION = ('PLAY',
               'SCORE',
               'EXIT')

# Screen settings

WIN_WIDTH = 800
WIN_HEIGHT = 400
fps = 60

# Physics settings

GRAVITY = 1
GROUND_Y = 300

# KEYS

KEY_UP = pygame.K_UP  # Seta para cima
KEY_DOWN = pygame.K_DOWN  # Seta para baixo
KEY_LEFT = pygame.K_LEFT  # Seta para esquerda
KEY_RIGHT = pygame.K_RIGHT  # Seta para direita

KEY_SPACE = pygame.K_SPACE  # Barra de espaço
KEY_ENTER = pygame.K_RETURN  # Tecla Enter
KEY_ESCAPE = pygame.K_ESCAPE  # Tecla ESC (para sair do jogo)

KEY_W = pygame.K_w  # Tecla W (para cima)
KEY_A = pygame.K_a  # Tecla A (para esquerda)
KEY_S = pygame.K_s  # Tecla S (para baixo)
KEY_D = pygame.K_d  # Tecla D (para direita)

KEY_JUMP = pygame.K_SPACE  # Barra de espaço para pular
KEY_FIRE = pygame.K_LCTRL  # Tecla Ctrl esquerdo para atirar
