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
  


# Classe Jogador que representa a nave 2
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
        self.rect.centerx = 200
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

    

# Classe Bullet que representa os tiros
class Bullet(pygame.sprite.Sprite):
    
    # Construtor da classe.
    def __init__(self, x, y):
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
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


# Classe Bullet que representa os tiros do player 2 
class Bullet2(pygame.sprite.Sprite):
    
    # Construtor da classe.
    def __init__(self, x, y):
        
        tipo = 1
        if tipo == 1:
            # Construtor da classe pai (Sprite).
            pygame.sprite.Sprite.__init__(self)
            
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

    # Metodo que atualiza a posição da navinha
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

#Fontes
#Fonte e tamanho para título
titulo_negrito = pygame.font.Font(path.join(font_dir, "BitBold.ttf"), 50)
#Fonte e tamanho outros textos
t_padrao = pygame.font.Font(path.join(font_dir, "RetroGaming.ttf"), 30)
# Carrega a fonte para desenhar o score.
score_font = pygame.font.Font(path.join(font_dir, "PressStart2P.ttf"), 28)

# Carrega os sons do jogo
pygame.mixer.music.load(path.join(snd_dir, 'tgfcoder-FrozenJam-SeamlessLoop.ogg'))
pygame.mixer.music.set_volume(0.005)
boom_sound = pygame.mixer.Sound(path.join(snd_dir, 'expl3.wav'))
destroy_sound = pygame.mixer.Sound(path.join(snd_dir, 'expl6.wav'))
pew_sound = pygame.mixer.Sound(path.join(snd_dir, 'pew.wav'))

#Imagens para o tutorial

teclas = {}

imgSetas = []
for indiceSetas in range (5):
    arquivoSetas = 'setinhas{}.png'.format(indiceSetas)
    img = pygame.image.load(path.join(img_dir, arquivoSetas))
    img = pygame.transform.scale (img, (250,125))
    imgSetas.append(img)

posSetas = []
for i in range (5):
    img = imgSetas[i]
    pos = img.get_rect()
    posSetas.append(pos)

imgTeclas = []
for indiceTeclas in range (5):
    arquivoTeclas = 'key{}.png'.format(indiceTeclas)
    img = pygame.image.load(path.join(img_dir, arquivoTeclas))
    img = pygame.transform.scale(img, (250,200))
    imgTeclas.append(img)

posTeclas = []
for i in range (5):
    img = imgTeclas[i]
    pos = img.get_rect()
    posTeclas.append(pos)

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

try:
    score1 = 0
    score2 = 0
    tutorial = True
    comando = 0
    testeplayer1 = 0
    testeplayer2 = 0


    while tutorial:

        # Ajusta a velocidade do jogo.
        clock.tick(FPS)  

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                tutorial = False
                comando = -1

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pass
                    
            if event.type == pygame.KEYUP:     
                if event.key == pygame.K_SPACE:
                    comando = 1 

            
            #Movimentação

            if event.type == pygame.KEYDOWN:
                #Subir 
                if event.key == pygame.K_w: #comando para o player 1
                    player.speedy = -8
                    
                if event.key == pygame.K_UP: #comando para o player 2
                    player2.speedy = -8 
                    

                #Descer
                if event.key == pygame.K_s: #comando para o player 1
                    player.speedy = 8
                    
                if event.key == pygame.K_DOWN: #comando para o player 2
                    player2.speedy = 8 

                
                #Esquerda
                if event.key == pygame.K_a: #comando para o player 1
                    player.speedx = -8

                if event.key == pygame.K_LEFT:#comando para o player 2
                    player2.speedx = -8 


                #Direita
                if event.key == pygame.K_d: #comando para o player 1
                    player.speedx = 8

                if event.key == pygame.K_RIGHT:#comando para o player 2
                    player2.speedx = 8 
    
                
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w: #comando para o player 1
                    player.speedy = 0
                    teclas["w"] = "w"
                if event.key == pygame.K_UP: #comando para o player 2
                    player2.speedy = 0
                    teclas["^"] = "^"
                
                if event.key == pygame.K_s: #comando para o player 1
                    player.speedy = 0
                    teclas["s"] = "s"
                if event.key == pygame.K_DOWN: #comando para o player 2
                    player2.speedy = 0
                    teclas["^^"] = "^^"
            
                if event.key == pygame.K_a: #comando para o player 1
                    player.speedx = 0
                    teclas["a"] = "a"
                if event.key == pygame.K_LEFT:#comando para o player 2
                    player2.speedx = 0
                    teclas["<"] = "<"

                if event.key == pygame.K_d: #comando para o player 1
                    player.speedx = 0
                    teclas["d"] = "d"

                if event.key == pygame.K_RIGHT:#comando para o player 2
                    player2.speedx = 0 
                    teclas[">"] = ">"

        screen.fill(WHITE)
        screen.blit(background, background_rect)        

        if comando == 0:
            #Inserir texto de apresentação
            instrucao1 = t_padrao.render("Use essas teclas para movimentação", True, YELLOW)
            #Posicionando-o                
            instrucao1_rect = instrucao1.get_rect()
            instrucao1_rect.midtop = ((WIDTH/2), (HEIGHT/8))
            #Mostrando na tela
            screen.blit(instrucao1, instrucao1_rect) 

            #Inserindo as imagens com as teclas para cada jogador e mostrando-as na tela
            posTeclas[comando].topleft = ((WIDTH/7), (HEIGHT/4))
            screen.blit(imgTeclas[comando], posTeclas[comando])
            
            posSetas[comando].topleft = (WIDTH/1.8, HEIGHT/3)
            screen.blit(imgSetas[comando],posSetas[comando])

            #Texto para continuar
            continuar = t_padrao.render("Pressione espaço para continuar", True, YELLOW)
            #Posicionando
            continuar_rect = continuar.get_rect()
            continuar_rect.midtop = ((WIDTH/2), (HEIGHT/5))
            #Mostrando na tela
            screen.blit(continuar, continuar_rect)

            if "_" in teclas:
                comando = 1


        if comando == 1:     
            instrucao2 = t_padrao.render("Pressione a seguinte tecla", True, YELLOW)
            #Posicionando-o                
            instrucao2_rect = instrucao1.get_rect()
            instrucao2_rect.midtop = ((WIDTH/2), (HEIGHT/8))
            #Mostrando na tela
            screen.blit(instrucao2, instrucao2_rect) 

            #Inserindo as imagens com as teclas para cada jogador e mostrando-as na tela
            posTeclas[comando].topleft = ((WIDTH/7), (HEIGHT/4))
            screen.blit(imgTeclas[comando], posTeclas[comando])
            
            posSetas[comando].topleft = (WIDTH/1.8, HEIGHT/3)
            screen.blit(imgSetas[comando],posSetas[comando])

            if ("w" in teclas) and ("^" in teclas):
                comando = 2


        if comando == 2:     
            instrucao2 = t_padrao.render("Pressione a seguinte tecla", True, YELLOW)
            #Posicionando-o                
            instrucao2_rect = instrucao1.get_rect()
            instrucao2_rect.midtop = ((WIDTH/2), (HEIGHT/8))
            #Mostrando na tela
            screen.blit(instrucao2, instrucao2_rect) 

            #Inserindo as imagens com as teclas para cada jogador e mostrando-as na tela
            posTeclas[comando].topleft = ((WIDTH/7), (HEIGHT/4))
            screen.blit(imgTeclas[comando], posTeclas[comando])
            
            posSetas[comando].topleft = (WIDTH/1.8, HEIGHT/3)
            screen.blit(imgSetas[comando],posSetas[comando])

            if ("s" in teclas) and ("^^" in teclas):
                comando = 3
                    
        if comando == 3:     
            instrucao2 = t_padrao.render("Pressione a seguinte tecla", True, YELLOW)
            #Posicionando-o                
            instrucao2_rect = instrucao1.get_rect()
            instrucao2_rect.midtop = ((WIDTH/2), (HEIGHT/8))
            #Mostrando na tela
            screen.blit(instrucao2, instrucao2_rect) 

            #Inserindo as imagens com as teclas para cada jogador e mostrando-as na tela
            posTeclas[comando].topleft = ((WIDTH/7), (HEIGHT/4))
            screen.blit(imgTeclas[comando], posTeclas[comando])
            
            posSetas[comando].topleft = (WIDTH/1.8, HEIGHT/3)
            screen.blit(imgSetas[comando],posSetas[comando])

            if ("a" in teclas) and ("<" in teclas):
                comando = 4

        if comando == 4:     
            instrucao2 = t_padrao.render("Pressione a seguinte tecla", True, YELLOW)
            #Posicionando-o                
            instrucao2_rect = instrucao1.get_rect()
            instrucao2_rect.midtop = ((WIDTH/2), (HEIGHT/8))
            #Mostrando na tela
            screen.blit(instrucao2, instrucao2_rect) 

            #Inserindo as imagens com as teclas para cada jogador e mostrando-as na tela
            posTeclas[comando].topleft = ((WIDTH/7), (HEIGHT/4))
            screen.blit(imgTeclas[comando], posTeclas[comando])
            
            posSetas[comando].topleft = (WIDTH/1.8, HEIGHT/3)
            screen.blit(imgSetas[comando],posSetas[comando])
                

        print ("Comando: ", comando)
        # A cada loop, redesenha o fundo e os sprites
        all_sprites.draw(screen)
        all_sprites.update()

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

finally:
    pygame.quit() 