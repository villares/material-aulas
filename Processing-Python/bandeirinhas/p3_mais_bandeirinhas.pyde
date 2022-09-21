"""
Classe Bandeirinha, cujo objeto instanciado reproduz o comportamento
anterior de polígono animado por variáveis globais.
"""

def setup():
    """ Instancia três bandeirinhas """
    global bandeira_0, bandeira_1, bandeira_2
    size(100, 100)  # área de desenho (width, height)
    meia_largura, meia_altura = width / 2, height / 2
    bandeira_0 = Bandeirinha(meia_largura, meia_altura)
    bandeira_1 = Bandeirinha(80, 10, 30)
    bandeira_2 = Bandeirinha(10, 40, 20)

def draw():
    """ Limpa a tela, desenha e atualiza bandeirinhas """
    background(0)  # atualização do desenho, fundo preto
    bandeira_0.desenha()
    bandeira_0.anda()
    bandeira_1.desenha()
    bandeira_1.anda()
    bandeira_2.desenha()
    bandeira_2.anda()

class Bandeirinha():
    """ Classe Bandeirinha, com métodos de desenho e atualizaçao ('anda') """

    def __init__(self, px, py, ptamanho=50):
        self.x = px
        self.y = py
        self.tamanho = ptamanho

    def desenha(self):
        """ Desenha polígono em torno das coordenadas do objeto """
        metade = self.tamanho / 2
        with pushMatrix():   # preseservando o sistema de coordenadas anterior
            translate(self.x, self.y)  # translada o sistema de coordenadas
            beginShape()  # inicia polígono
            vertex(-metade, -metade)
            vertex(-metade, metade)
            vertex(0, 0)
            vertex(metade, metade)
            vertex(metade, -metade)
            endShape(CLOSE)  # encerra polígono, fechando no primeiro vértice

    def anda(self):
        """ atualiza a posição do objeto """
        self.x += 1
        self.y += 1
        if self.x > width + 25:
            self.x = -25
        if self.y > height + 25:
            self.y = -25
