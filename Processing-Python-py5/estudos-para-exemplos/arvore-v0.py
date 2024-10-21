def setup():
    size(500, 500)

def draw():
    background(240, 240, 200) 
    translate(250, 300)     # desloca a origem, o (0,0) das coordenadas do canvas de desenho
    galho(60)

def galho(tamanho):
    angulo = radians(30)    # 30 graus em radianos
    encurtamento = 0.8      # fator para encurtar 20% o galho
    line(0, 0, 0, -tamanho) # uma linha vertical, subindo da origem a distância "tamanho"
    translate(0, -tamanho)  # desloca origem para ponta da linha
    rotate(angulo)          # gira o sistema de coordenadas do canvas 30° no sentido anti-horário
    line(0, 0, 0, -tamanho * encurtamento)  # desenha uma linha (será a da direita depois)
    rotate(2 * -angulo)     # gira o sistema de coordenadas 60° no sentido horário
    line(0, 0, 0, -tamanho * encurtamento)  # desenha outra linha  (será a da esquerda depois)
    rotate(angulo)          # gira 30° o canvas o deixando como no início.
    translate(0, tamanho)   # essa translação desfaz deslocamento da origem inicial da função
