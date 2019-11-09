# -*- coding: utf-8 -*-

# Importando as bibliotecas necessárias.
import pygame, time, random
from os import path

# Estabelece a pasta que contem as figuras.
img_dir = path.join(path.dirname(__file__), 'img')
snd_dir = path.join(path.dirname(__file__), 'snd')
font_dir = path.join(path.dirname(__file__), 'font')


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

def verif_colisao_nave_cura():
    #verivica colisao entre p1 e heal
    hit_heal = pygame.sprite.spritecollide(player, curas, False, pygame.sprite.collide_circle)
    for hit in hit_heal:
        # Toca o som da colisão
        #boom_sound.play()
        hit.kill()
        player.health += 15

# Classe Jogador que representa a nave
class Player(pygame.sprite.Sprite):
    
    # Construtor da classe.
    def __init__(self):
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        # Carregando a imagem de fundo.
        player_img = pygame.image.load(path.join(img_dir, "player1.png")).convert()
        self.image = player_img
        
        # Diminuindo o tamanho da imagem.
        self.image = pygame.transform.scale(player_img, (100, 100))
        
        # Deixando transparente.
        self.image.set_colorkey(WHITE)
        
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()
        
        # Centraliza embaixo da tela.
        self.rect.centerx = 100
        self.rect.bottom = HEIGHT / 2

        # Velocidade da nave
        self.speedx = 0
        self.speedy = 0

        # Melhora a colisão estabelecendo um raio de um circulo
        self.radius = 25

        #health stats
        self.health = 100

        #contador da cura
        self.cont_vida = 0

        #dano do tiro do p1 
        self.damage = 1

    
    # Metodo que atualiza a posição da navinha
    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        
        # Mantem dentro da tela
        if self.rect.bottom > 570:
            self.rect.bottom = 570
        if self.rect.top < -28:
            self.rect.top = -28

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH / 2 - 30:
            self.rect.right =  WIDTH / 2 - 30
            
    def lifeBar(self):
        pygame.draw.rect(screen, (255,0,0), (self.rect.x, self.rect.y - 60, 100,10))
        if self.health >= 0:
            pygame.draw.rect(screen, (0,255,0), (self.rect.x, self.rect.y - 60, 100 - (100 - self.health),10))
  


# Classe Bullet que representa os tiros
class Bullet(pygame.sprite.Sprite):
    
    # Construtor da classe.
    def _init_(self, x, y):
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite._init_(self)
        
        # Carregando a imagem de fundo.
        bullet_img = pygame.image.load(path.join(img_dir, "laserRed16.png")).convert()
        self.image = bullet_img

        self.image = pygame.transform.scale(bullet_img, (70, 30))

        # Deixando transparente.
        self.image.set_colorkey(BLACK)
        
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()
        
        # Coloca no lugar inicial definido em x, y do constutor
        self.rect.bottom = y + 80
        self.rect.centerx = x + 60
        self.speedx = 10

    # Metodo que atualiza a posição da navinha
    def update(self):
        self.rect.x += self.speedx
        
        # Se o tiro passar do inicio da tela, morre.
        if self.rect.left > WIDTH:
            self.kill()        

#clase que cria as curas
class Heal(pygame.sprite.Sprite):
    
    # Construtor da classe.
    def _init_(self):
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite._init_(self)
        
        # Carregando a imagem de fundo.
        heal_img = pygame.image.load(path.join(img_dir, "medicine.png")).convert()
        
        # Diminuindo o tamanho da imagem.
        self.image = pygame.transform.scale(heal_img, (40, 40))
        
        # Deixando transparente.
        self.image.set_colorkey(WHITE)
        
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()
        
        # Sorteia um lugar inicial em x
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        # Sorteia um lugar inicial em y
        self.rect.y = random.randrange(-100, -40)
        # Sorteia uma velocidade inicial
        self.speedx = random.randrange(-3, 3)
        self.speedy = random.randrange(2, 9)

#classe cria p2 
class Player2(pygame.sprite.Sprite):
    
    # Construtor da classe.
    def __init__(self):
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        # Carregando a imagem de fundo.
        player_img = pygame.image.load(path.join(img_dir, "p2.png")).convert()
        self.image = player_img
        
        # Diminuindo o tamanho da imagem.
        self.image = pygame.transform.scale(player_img, (90, 90))
        
        # Deixando transparente.
        self.image.set_colorkey(WHITE)
        
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()
        
        # Centraliza embaixo da tela.
        self.rect.centerx = 100
        self.rect.bottom = HEIGHT / 2

        # Velocidade da nave
        self.speedx = 0
        self.speedy = 0

        # Melhora a colisão estabelecendo um raio de um circulo
        self.radius = 25

        #health stats
        self.health = 100

        #contador da cura
        self.cont_vida = 0      

        #dano tiro p2 
        self.damage = 1  
     
    
    # Metodo que atualiza a posição da navinha
    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        
        # Mantem dentro da tela0
        if self.rect.bottom > 570:
            self.rect.bottom = 570
        if self.rect.top < -28:
            self.rect.top = -28

        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < WIDTH / 2 + 30:
            self.rect.left =  WIDTH / 2 + 30        

    def lifeBar(self):    
        pygame.draw.rect(screen, (255,0,0), (self.rect.x, self.rect.y - 60, 100,10))
        if self.health >= 0:
            pygame.draw.rect(screen, (0,255,0), (self.rect.x, self.rect.y - 60, 100 - (100 - self.health),10))


class Meteor(pygame.sprite.Sprite):
    
    # Construtor da classe.
    def __init__(self):
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        # Carregando a imagem de fundo.
        meteor_img = pygame.image.load(path.join(img_dir, "meteor.png")).convert()
        
        # Diminuindo o tamanho da imagem.
        self.image = pygame.transform.scale(meteor_img, (45, 45))
        
        # Deixando transparente.
        self.image.set_colorkey(BLACK)
        
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()
        
        # Sorteia um lugar inicial em xa
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        # Sorteia um lugar inicial em y
        self.rect.y = random.randrange(-100, -40)
        # Sorteia uma velocidade inicial
        self.speedx = random.randrange(-3, 3)
        self.speedy = random.randrange(2, 9)
        
    # Metodo que atualiza a posição da navinha
    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        
        # Se o meteoro passar do final da tela, volta para cima
        if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 20:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedx = random.randrange(-3, 3)
            self.speedy = random.randrange(2, 9)   
            

#classe cria bullet p2 
class Bullet2(pygame.sprite.Sprite):
    
    # Construtor da classe.
    def _init_(self, x, y):
        
        tipo = 1
        if tipo == 1:
            # Construtor da classe pai (Sprite).
            pygame.sprite.Sprite._init_(self)
            
            # Carregando a imagem de fundo.
            bullet_img = pygame.image.load(path.join(img_dir, "laser2.png")).convert()
            self.image = bullet_img
            
            # Deixando transparente.
            self.image.set_colorkey(BLACK)

            self.image = pygame.transform.scale(bullet_img, (70, 30))

            # Detalhes sobre o posicionamento.
            self.rect = self.image.get_rect()
            
            # Coloca no lugar inicial definido em x, y do constutor
            self.rect.bottom = y + 80
            self.rect.centerx = x - 60
            self.speedx = -10

    # Metodo que atualiza a posição da bullet2
    def update(self):
        self.rect.x += self.speedx
        
        # Se o tiro passar do inicio da tela, morre.
        if self.rect.left < 0:
            self.kill()

# Inicialização do Pygame.
pygame.init()
pygame.mixer.init()

# Tamanho da tela.
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Nome do jogo
pygame.display.set_caption("Warzinha")

# Variável para o ajuste de velocidade
clock = pygame.time.Clock()

# Carrega o fundo do jogo
background = pygame.image.load(path.join(img_dir, 'bg2.jpg')).convert()
background_rect = background.get_rect()

# Carrega a fonte para desenhar o score.
score_font = pygame.font.Font(path.join(font_dir, "PressStart2P.ttf"), 28)

# Carrega os sons do jogo
pygame.mixer.music.load(path.join(snd_dir, 'tgfcoder-FrozenJam-SeamlessLoop.ogg'))
pygame.mixer.music.set_volume(0.4)
boom_sound = pygame.mixer.Sound(path.join(snd_dir, 'expl3.wav'))
destroy_sound = pygame.mixer.Sound(path.join(snd_dir, 'expl6.wav'))
pew_sound = pygame.mixer.Sound(path.join(snd_dir, 'pew.wav'))

# Cria uma nave. O construtor será chamado automaticamente.
player = Player()
player2 = Player2()


# Cria um grupo para tiro

bullets = pygame.sprite.Group()
bullets2 = pygame.sprite.Group()
# Cria um grupo de sprites e adiciona a nave.
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
all_sprites.add(player2)


# Cria um grupo só de curas
curas = pygame.sprite.Group()

# Cria curas e adiciona nos grupos 
# h = Heal()
# all_sprites.add(h)
# curas.add(h)

# Cria 8 meteoros e adiciona no grupo meteoros
meteoros = pygame.sprite.Group()

for i in range(5):
    m = Meteor()
    all_sprites.add(m)
    meteoros.add(m)


assets = load_assets(img_dir)

try:
    #main loop

    score  = 0
    score2 = 0
    running = True
    while running:
        # Ajusta a velocidade do jogo.
        clock.tick(FPS)  

      # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                running = False
            
            #  P1  -- -Verifica se apertou alguma tecla.
            if event.type == pygame.KEYDOWN:
                # Dependendo da tecla, altera a velocidade.
                if event.key == pygame.K_w:
                    player.speedy = -8
                if event.key == pygame.K_s:
                    player.speedy = 8
                if event.key == pygame.K_a:
                    player.speedx = -8
                if event.key == pygame.K_d:
                    player.speedx = 8
            