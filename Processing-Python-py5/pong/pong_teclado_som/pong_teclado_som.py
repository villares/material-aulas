add_library('sound')
"""
PONG - Sesc Av. Paulista
começando com Processing Modo Python
"""
TAM_BOLA = 10
MEIA_BOLA = TAM_BOLA / 2
TAM_JOGADOR = 80
MEIO_JOGADOR = TAM_JOGADOR / 2
VEL_PLAYER = 5
game_over = False

p1_desce = p1_sobe = p2_desce = p2_sobe = False

vx, vy = 0, 0


def setup():
    """ Executado no início """
    global x, y, p1x, p1y, p2x, p2y
    global s1, s2, s3
    size(700, 400)
    rect_mode(CENTER)
    x = width / 2
    y = height / 2
    p1y = p2y = y
    p1x = MEIA_BOLA * 2
    p2x = width - MEIA_BOLA * 2
    s1 = SoundFile(this, "rebate1.wav")
    s2 = SoundFile(this, "rebate2.wav")
    s3 = SoundFile(this, "game_over.wav")


def draw():
    """ Desenho dos frames """
    global x, y, vx, vy, p1y, p2y
    background(0)
    # p1y = mouseY
    # p2y = y
    # desenha bola
    rect(x, y, TAM_BOLA, TAM_BOLA)
    # anda com a bola
    if not game_over:
        x = x + vx
        y = y + vy
        if p1_sobe:
            p1y = p1y - VEL_PLAYER
        if p1_desce:
            p1y = p1y + VEL_PLAYER
        if p2_sobe:
            p2y = p2y - VEL_PLAYER
        if p2_desce:
            p2y = p2y + VEL_PLAYER
    else:
        text_size(100)
        text_align(CENTER, CENTER)
        text("GAME OVER", width / 2, height / 2)

    # regras de rebatimento da bola
    if y < MEIA_BOLA or y > height - MEIA_BOLA:
        vy = -vy
        s1.play(1., 0.5)
    # checa rebatimento player 1 (lareral esquerda)
    if x < MEIA_BOLA * 3:
        if p1y + MEIO_JOGADOR > y > p1y - MEIO_JOGADOR:
            vx = -vx
            s2.play(1., 0.5)
        else:
            aciona_game_over()
    # checa rebatimento player 2 (lateral direita)
    if x > width - MEIA_BOLA * 3:
        if p2y + MEIO_JOGADOR > y > p2y - MEIO_JOGADOR:
            vx = -vx
            s2.play(1., 0.5)
        else:
            aciona_game_over()
    # desenha rede
    fill(255)
    for y_rede in range(0, height, TAM_BOLA * 2):
        rect(width / 2, y_rede, TAM_BOLA, TAM_BOLA)

    # desenha jogadores
    rect(p1x, p1y, TAM_BOLA, TAM_JOGADOR)
    rect(p2x, p2y, TAM_BOLA, TAM_JOGADOR)


def key_pressed():
    global x, y, vx, vy, game_over
    global p1_sobe, p1_desce, p2_sobe, p2_desce
    if key == ' ':
        if game_over:
            game_over = 0
            x = width / 2
            y = height / 2
        if random(100) > 50:
            vx = -5
            x = width - MEIA_BOLA * 3
            y = p2y
        else:
            vx = 5
            x = MEIA_BOLA * 3
            y = p1y
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


def aciona_game_over():
    global game_over
    if not game_over:
        game_over = True
        s3.play(.5, 1)
