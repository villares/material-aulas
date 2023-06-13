"""
PONG - Inicialmente para atividade no Sesc Av. Paulista, convertido para py5

Dois jogadores com teclado.
Use as teclas, A, Z e setas para cima e para baixo.
Espaço para iniciar.
"""

TAM_BOLA = 10
MEIA_BOLA = TAM_BOLA / 2
TAM_JOGADOR = 80
MEIO_JOGADOR = TAM_JOGADOR / 2
game_over = False

p1_desce = p1_sobe = p2_desce = p2_sobe = False

vx, vy = 0, 0

def setup():
    """ Executado no início """
    global x, y, p1x, p1y, p2x, p2y
    size(900, 500)
    rect_mode(CENTER)
    x = width / 2
    y = height / 2
    p1y = p2y = y
    p1x = MEIA_BOLA
    p2x = width - MEIA_BOLA


def draw():
    """ Desenho dos frames """
    global x, y, vx, vy, p1y, p2y
    global game_over
    background(0)
    # p1y = mouseY
    # p2y = y
    # desenha bola
    rect(x, y, TAM_BOLA, TAM_BOLA)
    # anda com a bola
    if not game_over:
        x = x + vx
        y = y + vy
    else:
        text_size(100)
        text_align(CENTER, CENTER)
        text("GAME OVER", width / 2, height / 2)
    # regras de rebatimento da bola
    if y < MEIA_BOLA or y > height - MEIA_BOLA:
        vy = -vy
    # checa rebatimento player 1 (lareral esquerda)
    if x < MEIA_BOLA:
        if p1y + MEIO_JOGADOR > y > p1y - MEIO_JOGADOR:
            vx = -vx
        else:
            game_over = True
    # checa rebatimento player 2 (lateral direita)
    if x > width - MEIA_BOLA:
        if p2y + MEIO_JOGADOR > y > p2y - MEIO_JOGADOR:
            vx = -vx
        else:
            game_over = True

            # desenha jogadores
    rect(p1x, p1y, TAM_BOLA, TAM_JOGADOR)
    rect(p2x, p2y, TAM_BOLA, TAM_JOGADOR)
    vp = 5
    if p1_sobe:
        p1y = p1y - vp
    if p1_desce:
        p1y = p1y + vp
    if p2_sobe:
        p2y = p2y - vp
    if p2_desce:
        p2y = p2y + vp


def key_pressed():
    global x, y, vx, vy, game_over
    global p1_sobe, p1_desce, p2_sobe, p2_desce
    if key == ' ':
        if game_over:
            x = width / 2
            y = height / 2
            game_over = False
        if random(100) > 50:
            vx = -5
        else:
            vx = 5
        if random(100) > 50:
            vy = -2
        else:
            vy = 2

    if key == 'a' or key == 'A':
        p1_sobe = True
    if key == 'z' or key == 'Z':
        p1_desce = True
    if key_code == UP:
        p2_sobe = True
    if key_code == DOWN:
        p2_desce = True


def key_released():
    global p1_sobe, p1_desce, p2_sobe, p2_desce
    if key == 'a' or key == 'A':
        p1_sobe = False
    if key == 'z' or key == 'Z':
        p1_desce = False
    if key_code == UP:
        p2_sobe = False
    if key_code == DOWN:
        p2_desce = False
