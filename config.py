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


cronometro_iniciado = False

def barra_de_vida(screen):
    global derrota
    pygame.draw.rect(screen, cor_barra_cheia, (posicao_barra[0], posicao_barra[1], largura_barra, altura_barra))
    print(p.vida_atual)
    largura_atual = int((p.vida_atual / vida_maxima) * largura_barra)
    pygame.draw.rect(screen, cor_barra_vazia, (posicao_barra[0] + largura_atual, posicao_barra[1], largura_barra - largura_atual, altura_barra))

    if p.vida_atual <= -25:
        print("perdeu")
        p.derrota = True


def chaves(screen):
    #qtdKeys = getQtdChaves() # pega a quantidade de chaves atualizada
    fonte = pygame.font.Font("Fonte.ttf", 36)
    texto = f"Chaves: {p.qtdChaves}/5"
    text = fonte.render(texto, True, (255, 192, 0))
    screen.blit(text, (720, 20))
    
def reiniciar_jogo():
    pass
    # personagem
    anim_pos_x = 20 # x inicial
    anim_pos_y = 270 # y inicial
    anim_frame = 1
    anim_time = 0  # variavel para controle do tempo da animação
    qtdChaves = 0 # variavel que vai atualizar a pontuação
    vida_atual = 100
    inim_pos_x_v1 = 200  # x inicial
    inim_pos_y_v1 = 400  # y inicial
    sentido_x_v1 = 1
    sentido_y_v1 = 1
    inim_pos_x_v2 = 400  # x inicial
    inim_pos_y_v2 = 100  # y inicial
    sentido_x_v2 = 1
    sentido_y_v2 = 1

def formatar_tempo(tempo_em_milissegundos):
    segundos = tempo_em_milissegundos // 1000
    segundos %= 60
    return str(segundos)

"""
while True:
    current_ticks = pygame.time.get_ticks()

    # [...]

    if not game_over:
        ticks = current_ticks - start_ticks
        # [...]

    else:
        start_ticks = current_ticks
        # [...]
"""

def cronometro(screen):

    """current_time = pygame.time.get_ticks()
    if(p.tempo_inicial == 0):
        tempo_atual = current_time - p.tempo_inicial
    else:
        tempo_atual = p.tempo_inicial + pygame.time.get_ticks()
        p.tempo_inicial = 1"""
    fonte = pygame.font.Font("Fonte.ttf", 36)
    text = f'Tempo: {formatar_tempo(p.tempo_inicial)}'
    texto = fonte.render(text, True, (255, 192, 0))
    screen.blit(texto, (500, 20))
    

    
    
    
   
