tamanho_inicial = 5 # tamanho da bolinha pequena
tamanho_atual = tamanho_inicial
px, py = 250, 250 # posição inicial pra bola
alvo_py = 250
vx = 15 # velocidade no x da bola
cor_bola = color(200, 200, 0) # amarelo inicial

def setup(): # este é o pedaço do começo
    size(900, 500) # tamanho da tela de desenho

def draw():
    global px, py, tamanho_atual, cor_bola # aviso pra poder mudar os números
    fill(240, 32) # fundo (255 é branco) (255, 0, 0 é vermelho)
    rect(0, 0, width, height)
    fill(cor_bola) # cor do miolo da bola 
    circle(px, py, tamanho_atual) # desenha a bola
    
    px = px + vx # aqui estamos somando a velocidade no px
    if px > 900: # se a posição x > 900
        px = 0 # ponha px valendo 0
        
    # Regra para quando ela passar pelo meio aumentar
    if px > 250 and px < 600:  # se px entre 400 e 500
        tamanho_atual = lerp(tamanho_atual, 300, 0.2) # então muda tamanho para 300
    else: # senão
        tamanho_atual = lerp(tamanho_atual, tamanho_inicial, 0.2) # volta o tamanho para o inicial (50)
        
    if py != alvo_py:
        py = py + (alvo_py - py) * .1
        
def keyPressed():
    global vx  # aviso para poder mudar a velocidade
    if key == "a": # tecla "a" pra aumentar a velocidade
        vx = vx + 5
    if key == "z":  # tecla "z" para diminuir a velocidade
        vx = vx - 5
    print(vx)
    global cor_bola # aviso pra poder mudar a cor
    if key == "b": # tecla "b"
        cor_bola = color(0, 0, 200) # azul
    if key == "n": # tecla "n"
        cor_bola = color(200, 200, 0) # amarelo inicial
    global alvo_py
    if key == "1":
        alvo_py = 100
    if key == "2":
        alvo_py = 200
    if key == "3":
        alvo_py = 300
    if key == "4":
        alvo_py = 400
    if key == "5":
        alvo_py = 500

        
