import pygame
from Player import *
from inimigos import *
from mapa import *
import variaviesGlobais as p

derrota = False

# constantes
width = 32 * 30 # largura da tela
height = 32 * 20 # altura da tela

cor_barra_cheia = (0, 254, 0)
cor_barra_vazia = (255, 0, 0)

largura_barra = 200
altura_barra = 20
posicao_barra = [50, 20]
vida_maxima = 100
vida_atual = 100


def barra_de_vida(screen):
    global derrota
    pygame.draw.rect(screen, cor_barra_cheia, (posicao_barra[0], posicao_barra[1], largura_barra, altura_barra))
<<<<<<< HEAD
=======
    print(p.vida_atual)
>>>>>>> c7ef9f61f49c280686e8ce87ef5d2175089515fa
    largura_atual = int((p.vida_atual / vida_maxima) * largura_barra)
    pygame.draw.rect(screen, cor_barra_vazia, (posicao_barra[0] + largura_atual, posicao_barra[1], largura_barra - largura_atual, altura_barra))

    if p.vida_atual <= -25:
        p.derrota = True
    if ((p.tempo_atual/100) >= 20):
        p.derrota = True

def chaves(screen):
    fonte = pygame.font.Font("Fonte.ttf", 36)
    texto = f"Chaves: {p.qtdChaves}/5"
    text = fonte.render(texto, True, (255, 192, 0))
    screen.blit(text, (720, 20))

def formatar_tempo(tempo_em_milissegundos):
    segundos = tempo_em_milissegundos / 100
    return str(segundos)

def cronometro(screen):
    fonte = pygame.font.Font("Fonte.ttf", 36)
    text = f'Tempo: {formatar_tempo(p.tempo_atual)}'
    texto = fonte.render(text, True, (255, 192, 0))
<<<<<<< HEAD
    screen.blit(texto, (450, 20))
=======
    screen.blit(texto, (500, 20))
>>>>>>> c7ef9f61f49c280686e8ce87ef5d2175089515fa
    

    
    
    
   
