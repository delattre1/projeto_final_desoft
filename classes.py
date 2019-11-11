from config import *
import pygame
import random

# Classe Jogador que representa a nave
class Player(pygame.sprite.Sprite):
    
    # Construtor da classe.
    def __init__(self, screen, id):

        self.screen = screen
        self.id = id
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        # Carregando a imagem de fundo.
        img = "player1.png"
        posx = 100
        if id == 2:
            img = "p2.png"
            posx = 400

        player_img = pygame.image.load(path.join(img_dir, img)).convert()
        self.image = player_img
        
        # Diminuindo o tamanho da imagem.
        self.image = pygame.transform.scale(player_img, (100, 100))

        if id == 2:
            self.image = pygame.transform.scale(player_img, (90,90))
        
        # Deixando transparente.
        self.image.set_colorkey(WHITE)
        
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()
        
        # Centraliza embaixo da tela.
        self.rect.centerx = posx
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
        
        #Mantem dentro da tela
        if self.rect.bottom > 570:
            self.rect.bottom = 570
        if self.rect.top < -28:
            self.rect.top = -28

        if self.id == 1:
            if self.rect.left < 0:
                self.rect.left = 0
            if self.rect.right > WIDTH / 2 - 30:
                self.rect.right =  WIDTH / 2 - 30

        if self.id == 2:
            if self.rect.right > WIDTH:
                self.rect.right = WIDTH
            if self.rect.left < WIDTH / 2 + 30:
                self.rect.left =  WIDTH / 2 + 30
            

    def lifeBar(self):
        pygame.draw.rect(self.screen, (255,0,0), (self.rect.x, self.rect.y - 60, 100,10))
        if self.health >= 0:
            pygame.draw.rect(self.screen, (0,255,0), (self.rect.x, self.rect.y - 60, 100 - (100 - self.health),10))

# Classe Bullet que representa os tiros
class Bullet(pygame.sprite.Sprite):
    
    # Construtor da classe.
    def __init__(self, x, y, id):
        
        self.id = id
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        img = "laserRed16.png"
        if id == 2:
            img = "laser2.png"


        # Carregando a imagem de fundo.
        bullet_img = pygame.image.load(path.join(img_dir, img)).convert()
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

        if id == 2:
            # Coloca no lugar inicial definido em x, y do constutor
            self.rect.bottom = y + 80
            self.rect.centerx = x - 60
            self.speedx = -10

    # Metodo que atualiza a posição da bullet
    def update(self):
        self.rect.x += self.speedx
        
        # Se o tiro passar do inicio da tela, morre.
        if self.id == 1:
            if self.rect.left > WIDTH:
                self.kill()
        elif self.id == 2:
            if self.rect.left < 0:
                self.kill()

# Classe curas
class Heal(pygame.sprite.Sprite):
    
    # Construtor da classe.
    def __init__(self):
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
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
        
    # Metodo que atualiza a posição da navinha
    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        
        # Se a cura passar do final da tela, volta para cima
        if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 20:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedx = random.randrange(-3, 3)
            self.speedy = random.randrange(2, 9)


# Classe explosao ---- por enquanto tá com o exemplo do ex das naves
class Explosion(pygame.sprite.Sprite):

    # Construtor da classe.
    def __init__(self, center, explosion_anim):
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)

        # Carrega a animação de explosão
        self.explosion_anim = explosion_anim

        # Inicia o processo de animação colocando a primeira imagem na tela.
        self.frame = 0
        self.image = self.explosion_anim[self.frame]
        self.rect = self.image.get_rect()
        self.rect.center = center

        # Guarda o tick da primeira imagem
        self.last_update = pygame.time.get_ticks()

        # Controle de ticks de animação: troca de imagem a cada self.frame_ticks milissegundos.
        self.frame_ticks = 50

    def update(self):
        # Verifica o tick atual.
        now = pygame.time.get_ticks()

        # Verifica quantos ticks se passaram desde a ultima mudança de frame.
        elapsed_ticks = now - self.last_update

        # Se já está na hora de mudar de imagem...
        if elapsed_ticks > self.frame_ticks:

            # Marca o tick da nova imagem.
            self.last_update = now

            # Avança um quadro.
            self.frame += 1

            # Verifica se já chegou no final da animação.
            if self.frame == len(self.explosion_anim):
                # Se sim, tchau explosão!
                self.kill()
            else:
                # Se ainda não chegou ao fim da explosão, troca de imagem.
                center = self.rect.center
                self.image = self.explosion_anim[self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center

# Classe Mob que representa os meteoros
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