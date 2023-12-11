import time
global anim_pos_x,anim_pos_y, anim_frame, anim_time, qtdChaves, inim_pos_x_v1, inim_pos_y_v1, sentido_x_v1, sentido_y_v1, inim_pos_x_v2, inim_pos_y_v2, sentido_x_v2, sentido_y_v2, vida_atual, derrota, tempo_inicial,  vitoria, tempo_atual

def novo_jogo():
    global anim_pos_x, anim_pos_y, anim_frame, anim_time, qtdChaves, inim_pos_x_v1, inim_pos_y_v1, sentido_x_v1, sentido_y_v1, inim_pos_x_v2, inim_pos_y_v2, sentido_x_v2, sentido_y_v2, vida_atual, derrota, tempo_inicial, vitoria, tempo_atual
    derrota = False
    vitoria = False
    anim_pos_x = 50
    anim_pos_y = 400 # y inicial
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
    tempo_inicial = 0
    tempo_atual = 0
