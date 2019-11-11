from os import path

# Dados gerais do jogo.
WIDTH = 960 # Largura da tela
HEIGHT = 540 # Altura da tela
FPS = 60 # Frames por segundo

# cores em rgb pra usar depois 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Estabelece a pasta que contem as figuras.
img_dir = path.join(path.dirname(__file__), 'img')
snd_dir = path.join(path.dirname(__file__), 'snd')
font_dir = path.join(path.dirname(__file__), 'font')