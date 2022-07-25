"""
PONG - Sesc Av. Paulista
começando com Processing Modo Python
"""

TAM_BOLA = 10
MEIA_BOLA = TAM_BOLA / 2
TAM_JOGADOR = 80
MEIO_JOGADOR = TAM_JOGADOR / 2

vx, vy = -2, 1

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
    global x, y, vx, vy
    background(0)
    
    # desenha bola
    rect(x, y, TAM_BOLA, TAM_BOLA)
    # anda com a bola
    x = x + vx
    y = y + vy
    # regras de rebatimento da bola
    if x < MEIA_BOLA or x > width - MEIA_BOLA:
        vx = -vx 
    if y < MEIA_BOLA or y > height - MEIA_BOLA:
        vy = -vy
    # desenha jogadores
    rect(p1x, mouseY, TAM_BOLA, TAM_JOGADOR)
    rect(p2x, y, TAM_BOLA, TAM_JOGADOR)
