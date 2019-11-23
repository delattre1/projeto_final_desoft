# -*- coding: utf-8 -*-
import pygame, time, random
from os import path
from classes import Player, Bullet, Heal, Explosion, Meteor, load_assets, verif_colisao_nave_cura 
from config import *

# Estabelece a pasta que contem as figuras.
img_dir = path.join(path.dirname(__file__), 'img')
snd_dir = path.join(path.dirname(__file__), 'snd')
font_dir = path.join(path.dirname(__file__), 'font')

                 
                    
# Inicialização do Pygame.
pygame.init()
pygame.mixer.init()

# Tamanho da tela.
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Nome do jogo
pygame.display.set_caption("Warzinha")

# Variável para o ajuste de velocidade
clock = pygame.time.Clock()

""" Dados tela inicial"""
#Carrega a imagem
arquivo_fundo = pygame.image.load(path.join(img_dir, 'florestScreen1.png')).convert()
#Redimensionando
fundo = pygame.transform.scale(arquivo_fundo, (WIDTH, HEIGHT))
#Comando para colocar na superficie
fundo_rect = fundo.get_rect()

#Fontes
#Fonte e tamanho para título
titulo_negrito = pygame.font.Font(path.join(font_dir, "BitBold.ttf"), 50)
#Fonte e tamanho outros textos
t_padrao = pygame.font.Font(path.join(font_dir, "RetroGaming.ttf"), 30)


# Carrega o fundo do jogo
background = pygame.image.load(path.join(img_dir, 'bg2.jpg')).convert()
background_rect = background.get_rect()

# Carrega a fonte para desenhar o score.
score_font = pygame.font.Font(path.join(font_dir, "PressStart2P.ttf"), 28)

# Carrega os sons do jogo
pygame.mixer.music.load(path.join(snd_dir, 'tgfcoder-FrozenJam-SeamlessLoop.ogg'))
pygame.mixer.music.set_volume(0.005)
boom_sound = pygame.mixer.Sound(path.join(snd_dir, 'expl3.wav'))
destroy_sound = pygame.mixer.Sound(path.join(snd_dir, 'expl6.wav'))
pew_sound = pygame.mixer.Sound(path.join(snd_dir, 'pew.wav'))


# Cria uma nave. O construtor será chamado automaticamente.
player = Player(screen, 1)
player2 = Player(screen, 2)


# Cria um grupo para tiro

bullets = pygame.sprite.Group()
bullets2 = pygame.sprite.Group()
# Cria um grupo de sprites e adiciona a nave.
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
all_sprites.add(player2)


# Cria um grupo só de curas
curas = pygame.sprite.Group()

# Cria 8 meteoros e adiciona no grupo meteoros
meteoros = pygame.sprite.Group()

"""Tela inicial"""
#Tela inicial 
tela1 = True
countTela1 = 0 #Variável para fazer o pisca do texto
    
while tela1:
    # Ajusta a velocidade do jogo.
    clock.tick(FPS)
    #Processa o evento (se aconteceu algo)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            tela1 = False 
            running = False 
            #state = False #(relacionado a máquina de estados)

        if event.type == pygame.KEYUP:
            #state = True #(relacionado a máquina de estados)
            tela1 = False
                
        #Redesenhando o fundo
        screen.blit(fundo, fundo_rect)
        
        #Mostrando os textos da tela inicial
        #O texto do título
        texto_titulo = titulo_negrito.render("O famoso jogo de DESOFT", True, YELLOW)
        #Posicionando
        textoT_rect = texto_titulo.get_rect()
        textoT_rect.midtop = ((WIDTH/2), (HEIGHT/4))
        #Inserindo na tela
        screen.blit(texto_titulo, textoT_rect)
        
        countTela1 += 1 #Incrementa na variável de pisca texto
        #Coloca o texto na tela se o contador é par
        if countTela1%2 == 0:
            #Pressione qualquer tela
            texto_tecla = t_padrao.render("Pressione qualquer tela para jogar", True, YELLOW)
            #Posicionando
            textoP_rect = texto_tecla.get_rect()
            textoP_rect.midbottom = ((WIDTH/2), (HEIGHT/1.6))
            #Inserindo na tela
            screen.blit(texto_tecla, textoP_rect)
            #Tempo entre pisca
            pygame.time.delay(500)
        #Quando o contador é impar, o texto some
            
        
        #O texto para mostrar quem desenvolveu 
        texto_criadores = t_padrao.render("Desenvolvido por:", True, YELLOW)
        #Posicionando
        textoD_rect = texto_criadores.get_rect()
        textoD_rect.midbottom = ((WIDTH/2), (HEIGHT-50))
        #Inserindo na tela
        screen.blit(texto_criadores, textoD_rect)
        texto_criadores = t_padrao.render("Barbara e Daniel", True, YELLOW)
        #Posicionando
        textoC_rect = texto_criadores.get_rect()
        textoC_rect.midbottom = ((WIDTH/2), (HEIGHT-20))
        #Inserindo na tela
        screen.blit(texto_criadores, textoC_rect)
        
        #Depois de desenhar, inverte o fundo 
        pygame.display.flip()


assets = load_assets(img_dir)

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

try:
    running = False

    #Tutorial 
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
                if event.key == pygame.K_y:
                    pass
                    
            if event.type == pygame.KEYUP:     
                if event.key == pygame.K_y:
                    teclas["y"] = "y"
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
                    teclas[">"] = ""

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
            continuar = t_padrao.render("Pressione Y para continuar", True, YELLOW)
            #Posicionando
            continuar_rect = continuar.get_rect()
            continuar_rect.midtop = ((WIDTH/2), (HEIGHT/5))
            #Mostrando na tela
            screen.blit(continuar, continuar_rect)

            if "y" in teclas:
                comando = 1



        if comando == 1:     
            instrucao2 = t_padrao.render("Pressione a seguinte tecla", True, YELLOW)
            #Posicionando-o                
            instrucao2_rect = instrucao1.get_rect()
            instrucao2_rect.midtop = ((WIDTH/1.75), (HEIGHT/5))
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
            instrucao2_rect.midtop = ((WIDTH/2), (HEIGHT/5))
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
            instrucao2_rect.midtop = ((WIDTH/2), (HEIGHT/5))
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
            instrucao2_rect.midtop = ((WIDTH/2), (HEIGHT/5))
            #Mostrando na tela
            screen.blit(instrucao2, instrucao2_rect) 

            #Inserindo as imagens com as teclas para cada jogador e mostrando-as na tela
            posTeclas[comando].topleft = ((WIDTH/7), (HEIGHT/4))
            screen.blit(imgTeclas[comando], posTeclas[comando])
            
            posSetas[comando].topleft = (WIDTH/1.8, HEIGHT/3)
            screen.blit(imgSetas[comando],posSetas[comando])

            if ("s" in teclas) and (">" in teclas):
                running = True
                tutorial = False

        print ("Comando: ", comando)
        # A cada loop, redesenha o fundo e os sprites
        all_sprites.draw(screen)
        all_sprites.update()

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

    #main loop
    for i in range(5):
        m = Meteor()
        all_sprites.add(m)
        meteoros.add(m)

    score  = 0
    score2 = 0
    
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

                # Se for um espaço atira!
                if event.key == pygame.K_SPACE:
                    bullet = Bullet(player.rect.centerx, player.rect.top, 1)
                    all_sprites.add(bullet)
                    bullets.add(bullet)
                    pew_sound.play()
                                        

            # Verifica se soltou alguma tecla.
            if event.type == pygame.KEYUP:
                # Dependendo da tecla, altera a velocidade.
                if event.key == pygame.K_w:
                    player.speedy = 0
                if event.key == pygame.K_s:
                    player.speedy = 0
                if event.key == pygame.K_a:
                    player.speedx = 0
                if event.key == pygame.K_d:
                    player.speedx = 0   
                    
            #  P2  -- -Verifica se apertou alguma tecla.
            if event.type == pygame.KEYDOWN:
                # Dependendo da tecla, altera a velocidade.
                if event.key == pygame.K_UP:
                    player2.speedy = -8
                if event.key == pygame.K_DOWN:
                    player2.speedy = 8
                if event.key == pygame.K_LEFT:
                    player2.speedx = -8
                if event.key == pygame.K_RIGHT:
                    player2.speedx = 8    

                # Se for um L atira!
                if event.key == pygame.K_RETURN:
                    bullet2 = Bullet(player2.rect.centerx, player2.rect.top, 2)
                    all_sprites.add(bullet2)
                    bullets2.add(bullet2)
                    pew_sound.play()
                                        

            # Verifica se soltou alguma tecla.
            if event.type == pygame.KEYUP:
                # Dependendo da tecla, altera a velocidade.
                if event.key == pygame.K_UP:
                    player2.speedy = 0
                if event.key == pygame.K_DOWN:
                    player2.speedy = 0
                if event.key == pygame.K_LEFT:
                    player2.speedx = 0
                if event.key == pygame.K_RIGHT:
                    player2.speedx = 0  

            
                    
        # Verifica se houve colisão entre BULLET e P2
        hits = pygame.sprite.spritecollide(player2, bullets, False, pygame.sprite.collide_circle)

        for hit in hits:
            #print(hit==player2)
            # Toca o som da colisão
            boom_sound.play()    
            hit.kill() #destrói a bala quando bate 
            score += 1
            #if player2.health >= 0:
            player2.health -= player.damage            

        # Verifica se houve colisão entre BULLET2 e P1
        hits2 = pygame.sprite.spritecollide(player, bullets2, False, pygame.sprite.collide_circle)
        for hit in hits2:
            # Toca o som da colisão
            boom_sound.play()    
            hit.kill() 
            score2 += 1 
            #if player.health >= 0:
            player.health -= player2.damage 
                                    

        # Verifica se houve colisão entre BULLET1 e BULLET2
        hits3 = pygame.sprite.groupcollide(bullets, bullets2, True, True)
        if hits3:# Toca o som da colisão
            destroy_sound.play()  

        # Verifica se houve colisão entre bullet e meteoro
        hits = pygame.sprite.groupcollide(meteoros, bullets, True, True)
        for hit in hits: # Pode haver mais de um
            destroy_sound.play()
            m = Meteor() 
            all_sprites.add(m)
            meteoros.add(m)
            var_aleatoria = random.randint(0,8)
            if var_aleatoria == 1:
                h = Heal()
                all_sprites.add(h)
                curas.add(h)
            player.damage += 0.15
                        # No lugar do meteoro antigo, adicionar uma explosão.
            explosao = Explosion(hit.rect.center, assets["explosion_anim"])
            all_sprites.add(explosao)

        # Verifica se houve colisão entre bullet2 e meteoro
        hits = pygame.sprite.groupcollide(meteoros, bullets2, True, True)
        for hit in hits: # Pode haver mais de um
            destroy_sound.play()
            m = Meteor() 
            all_sprites.add(m)
            meteoros.add(m)
            var_aleatoria = random.randint(0,10)
            if var_aleatoria == 1:
                h = Heal()
                all_sprites.add(h)
                curas.add(h)
            player2.damage += 0.15
            # No lugar do meteoro antigo, adicionar uma explosão.
            explosao = Explosion(hit.rect.center, assets["explosion_anim"])
            all_sprites.add(explosao)            
        
        # Verifica se houve colisão entre meteoro e P1
        hits1p = pygame.sprite.spritecollide(player, meteoros, False, pygame.sprite.collide_circle)
        for hit in hits1p:
            # Toca o som da colisão
            boom_sound.play()    
            hit.kill() 
            #score2 += 1 
            player.health -= 5
            m = Meteor() 
            all_sprites.add(m)
            meteoros.add(m)    
            explosao = Explosion(hit.rect.center, assets["explosion_anim"])
            all_sprites.add(explosao)                 

        # Verifica se houve colisão entre meteoro e P2
        hits2p = pygame.sprite.spritecollide(player2, meteoros, False, pygame.sprite.collide_circle)
        for hit in hits2p:
            # Toca o som da colisão
            boom_sound.play()    
            hit.kill() 
            #score2 += 1 
            player2.health -= 5  
            m = Meteor() 
            all_sprites.add(m)
            meteoros.add(m)    
            explosao = Explosion(hit.rect.center, assets["explosion_anim"])
            all_sprites.add(explosao)                      

        verif_colisao_nave_cura(player,player2, curas)          

        # Depois de processar os eventos.
        # Atualiza a acao de cada sprite.
        all_sprites.update()


        # A cada loop, redesenha o fundo e os sprites
        screen.fill(WHITE)
        screen.blit(background, background_rect)        
        all_sprites.draw(screen)

        #cria a barra de vida
        player.lifeBar()
        player2.lifeBar()


        # Desenha o score p1 
        text_surface = score_font.render("{:04d}".format(score), True, YELLOW)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (100,  10)
        screen.blit(text_surface, text_rect)

        # Desenha o score p2
        text_surface = score_font.render("{:04d}".format(score2), True, YELLOW)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (WIDTH - 100,  10)
        screen.blit(text_surface, text_rect) 


        print(player.health)
        print(player2.health)
        if player.health <= 0 or player2.health <= 0:
            running = False

        # # Desenha as vidas
        # text_surface = score_font.render(chr(9829) * lives, True, RED)
        # text_rect = text_surface.get_rect()
        # text_rect.bottomleft = (10, HEIGHT - 10)
        # screen.blit(text_surface, text_rect)               
                
        
        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()
        
finally:
    pygame.quit()      