"""
Exemplo de uso da Classe Bandeirinhas, objetos com velocidade
e tamanhos sorteados instanciados em uma lista.
"""

bandeirinhas = []  # lista de objetos


def setup():
    """ Define área de desenho e popula lista de bandeirinhas """
    size(400, 400)  # área de desenho (width, height)
    meia_largura, meia_altura = width / 2., height / 2.  # floats
    for _ in range(50):
        nova_bandeirinha = Bandeirinha(meia_largura, meia_altura)
        bandeirinhas.append(nova_bandeirinha)


def draw():
    """ Limpa a tela, desenha e atualiza bandeirinhas """
    background(0)  # atualização do desenho, fundo preto
    for bandeira in bandeirinhas:
        bandeira.desenha()
        bandeira.anda()


class Bandeirinha():
    """ Classe Bandeirinha, cor sorteada, tamanho sorteado por default """

    def __init__(self, px, py, ptamanho=None):
        self.x = px
        self.y = py
        if ptamanho:
            self.tamanho = ptamanho
        else:
            self.tamanho = random(50, 200)
        self.vx = random(-1, 1)
        self.vy = random(-1, 1)
        self.cor = color(random(255),  # R
                         random(255),  # G
                         random(255),  # B
                         200)  # alpha

    def desenha(self):
        """ Desenha polígono em torno das coordenadas do objeto """
        metade = self.tamanho / 2
        with push_matrix():   # preseservando o sistema de coordenadas anterior
            translate(self.x, self.y)  # translada o sistema de coordenadas
            no_stroke()  # sem contorno
            fill(self.cor)
            begin_shape()  # inicia polígono
            vertex(-metade, -metade)
            vertex(-metade, metade)
            vertex(0, 0)
            vertex(metade, metade)
            vertex(metade, -metade)
            end_shape(CLOSE)  # encerra polígono, fechando no primeiro vértice

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
