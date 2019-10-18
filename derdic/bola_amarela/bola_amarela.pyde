
tamanho_inicial = 50 # tamanho da bolinha quando pequena
tamanho_atual = tamanho_inicial
px, py = 250, 250 # posição inicial pra bola
vx = 15 # velocidade no x da bola
cor_bola = color(200, 200, 0) # amarelo inicial

def setup():
    size(900, 500) # tamanho o desenho

def draw():
    global px, tamanho, cor_bola
    background(255) # fundo branco
    fill(cor_bola)
    circle(px, py, tamanho_atual) # desenha a bola
    
    px = px + vx
    if px > 900: # se a posição x > 900
        px = 0 # ponha px valendo 0
        
    # quando ela passar pelo meio aumenta
    if px > 400 and px < 500:  # entre estes valores
        tamanho_atual = 300
    else: # senão
        tamanho_atual = tamanho_inicial
        
