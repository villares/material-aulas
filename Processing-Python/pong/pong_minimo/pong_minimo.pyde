"""
PONG - Sesc Av. Paulista
começando com Processing Modo Python
"""
TAM_BOLA = 10
MEIA_BOLA = TAM_BOLA / 2
TAM_JOGADOR = 80
MEIO_JOGADOR = TAM_JOGADOR / 2
game_over = False

vx, vy = -5, 2

def setup():
    """ Executado no início """
    global x, y, p1x, p1y, p2x, p2y
    size(700, 400)
    rectMode(CENTER)
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
    p1y = mouseY
    p2y = y
    # desenha bola
    rect(x, y, TAM_BOLA, TAM_BOLA)
    # anda com a bola
    if game_over == False:
        x = x + vx
        y = y + vy
    else:
        textSize(100)
        textAlign(CENTER, CENTER)
        text("GAME OVER", width / 2, height / 2)    
    # regras de rebatimento da bola
    if x > width - MEIA_BOLA:
        vx = -vx 
    if y < MEIA_BOLA or y > height - MEIA_BOLA:
        vy = -vy
    if x < MEIA_BOLA:
        if p1y + MEIO_JOGADOR > y > p1y - MEIO_JOGADOR:
            vx = -vx
        else:
            game_over = True    
    # desenha jogadores
    rect(p1x, p1y, TAM_BOLA, TAM_JOGADOR)
    rect(p2x, p2y, TAM_BOLA, TAM_JOGADOR)
