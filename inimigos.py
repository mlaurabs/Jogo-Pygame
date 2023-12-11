import pygame
from config import *
import variaviesGlobais as p

# bomba 1
bomba_v1 = pygame.image.load("images/Bomba.png")


# bomba 2
bomba_v2 = pygame.image.load("images/Bomba.png")

bomba_v1 = pygame.transform.scale(bomba_v1, (48, 48))
bomba_v2 = pygame.transform.scale(bomba_v2, (48, 48))
explosao = pygame.image.load("images/Explosão.png")
explosao = pygame.transform.scale(explosao, (52, 52))

def getExplosao():
    return explosao

def getBomba_V1():
    return bomba_v1

def getBomba_V2():
    return bomba_v2

def animacao_inimigo(dt):
    # bomba 1
    if (p.sentido_x_v1 == 1):  # se ela estiver indo para direita (ida)
        p.inim_pos_x_v1 += 0.2 * dt
        if (p.inim_pos_x_v1 > 910):
            p.sentido_x_v1 = 2
    elif (p.sentido_x_v1 == 2):  # se ela estiver indo para esquerda (volta)
        p.inim_pos_x_v1 -= 0.2 * dt
        if (p.inim_pos_x_v1 < 1):
            p.sentido_x_v1 = 1

    if (p.sentido_y_v1 == 1):  # se ele estiver subindo
        p.inim_pos_y_v1 += 0.2 * dt
        if (p.inim_pos_y_v1 > 580):
            p.sentido_y_v1 = 2

    elif (p.sentido_y_v1 == 2):  # se ele estiver descendo
        p.inim_pos_y_v1 -= 0.2 * dt
        if (p.inim_pos_y_v1 < 1):
            p.sentido_y_v1 = 1

    # bomba 2
    if (p.sentido_x_v2 == 1):  # se ela estiver indo para direita (ida)
        p.inim_pos_x_v2 += 0.3 * dt
        if (p.inim_pos_x_v2 > 910):
            p.sentido_x_v2 = 2
    elif (p.sentido_x_v2 == 2):  # se ela estiver indo para esquerda (volta)
        p.inim_pos_x_v2 -= 0.3 * dt
        if (p.inim_pos_x_v2 < 1):
            p.sentido_x_v2 = 1

    if (p.sentido_y_v2 == 1):  # se ele estiver subindo
        p.inim_pos_y_v2 += 0.2 * dt
        if (p.inim_pos_y_v2 > 580):
            p.sentido_y_v2 = 2

    elif (p.sentido_y_v2 == 2):  # se ele estiver descendo
        p.inim_pos_y_v2 -= 0.2 * dt
        if (p.inim_pos_y_v2 < 1):
            p.sentido_y_v2 = 1

def getInimsPos():
    return [p.inim_pos_x_v1, p.inim_pos_y_v1, p.inim_pos_x_v2, p.inim_pos_y_v2]

# desenha o personagem animado na tela
def draw_inimigo_1(screen):
    global bomba_v1, bomba_v2
    screen.blit(bomba_v1, (p.inim_pos_x_v1, p.inim_pos_y_v1))
    screen.blit(bomba_v2, (p.inim_pos_x_v2, p.inim_pos_y_v2))
