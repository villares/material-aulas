from botao import Botao  # precisa do módulo botao.py (um outro arquivo na pasta do sketch)

estado_inicial = True

def setup():
    global b1, b2
    size(400, 400)
    b1 = Botao(100, 150, 200, 50, "clique aqui")
    b2 = Botao(100, 250, 200, 50, "de novo!")

def draw():
    global estado_inicial
    
    if estado_inicial:
        background(200)
    else:
        background(10)

    resultado1 = b1.display()
    resultado2 = b2.display()
    if resultado1 or resultado2:
        print('clique')
        estado_inicial = not estado_inicial
