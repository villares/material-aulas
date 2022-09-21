"""
Ampliando a classe Bandeirinha, com cores e velocidades sorteadas.
"""

def setup():
    """ Instancia três bandeirinhas """
    global bandeira_a, bandeira_b, bandeira_c
    size(100, 100)  # área de desenho (width, height)
    meia_largura, meia_altura = width / 2, height / 2
    bandeira_a = Bandeirinha(meia_largura, meia_altura, 50)
    bandeira_b = Bandeirinha(meia_largura, meia_altura, 70)
    bandeira_c = Bandeirinha(meia_largura, meia_altura, 80)

def draw():
    """ Limpa a tela, desenha e atualiza bandeirinhas """
    background(0)  # atualização do desenho, fundo preto
    bandeira_a.desenha()
    bandeira_a.anda()
    bandeira_b.desenha()
    bandeira_b.anda()
    bandeira_c.desenha()
    bandeira_c.anda()

class Bandeirinha():
    """ Classe Bandeirinha, cor sorteada, velocidade sorteada """

    def __init__(self, px, py, ptamanho=None):
        self.x = float(px)
        self.y = float(py)
        if ptamanho:
            self.tamanho = ptamanho
        else:
            self.tamanho = random(50, 200)
        self.vx = random(-1,1)
        self.vy = random(-1,1)
        self.cor = color(random(255),  # R
                         random(255),  # G
                         random(255),  # B
                         200)  # alpha

    def desenha(self):
        """ Desenha polígono em torno das coordenadas do objeto """
        metade = self.tamanho / 2
        with pushMatrix():   # preseservando o sistema de coordenadas anterior
            translate(self.x, self.y)  # translada o sistema de coordenadas
            noStroke()  # sem contorno
            fill(self.cor)
            beginShape()  # inicia polígono
            vertex(-metade, -metade)
            vertex(-metade, metade)
            vertex(0, 0)
            vertex(metade, metade)
            vertex(metade, -metade)
            endShape(CLOSE)  # encerra polígono, fechando no primeiro vértice

    def anda(self):
        """ atualiza a posição do objeto e devolve do lado oposto se sair """
        self.x += self.vx
        self.y += self.vy
        metade = self.tamanho / 2
        if self.x > width + metade:
            self.x = -metade
        if self.y > height + metade:
            self.y = -metade
        if self.x < -metade:
            self.x = width + metade
        if self.y < -metade:
            self.y = height + metade
