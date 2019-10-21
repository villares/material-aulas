tamanho_inicial = 5 # tamanho da bolinha pequena
tamanho_atual = tamanho_inicial
px, py = 250, 250 # posição inicial pra bola
vx = 15 # velocidade no x da bola
cor_bola = color(200, 200, 0) # amarelo inicial
py_alvo = 100 # onde o py vai chegar

def setup(): # este é o pedaço do começo
    size(900, 500) # tamanho da tela de desenho

def draw():
    global px, py, tamanho_atual, cor_bola # aviso pra poder mudar os números
    # lá em cima no global puz py  # aviso de que vou mudar o py
    py = py + (py_alvo - py) / 4
    fill(255, 10) # branco um pouco transparente
    rect(0, 0, width, height) 
    fill(cor_bola) # cor do miolo da bola 
    circle(px, py, tamanho_atual) # desenha a bola
    
    px = px + vx # aqui estamos somando a velocidade no px
    if px > 900: # se a posição x > 900
        px = 0 # ponha px valendo 0
        
    # Regra para quando ela passar pelo meio aumentar
    if px > 400 and px < 500:  # se px entre 400 e 500
        tamanho_atual += (300 - tamanho_atual) / 4 
    else: # senão
        tamanho_atual += (tamanho_inicial - tamanho_atual) / 4
                
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
    global py_alvo # vou mudar o alvo!!!
    if key == "1": # tecla "1"
        py_alvo = 100
    if key == "4": # tecla "4"
        py_alvo = 400        
    if key == "1": # tecla "1"
        py_alvo = 100
    if key == " ": # tecla epaço
        py_alvo = 250  
        
