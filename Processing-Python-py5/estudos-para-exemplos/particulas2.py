from py5_tools import animated_gif
    

def setup():
    """ Instancia três particulas """
    global pa, pb, pc
    size(100, 100)  # área de desenho (width, height)
    pa = Particula(50, 50, 40)
    pb = Particula(80, 10, 30)
    pc = Particula(10, 40, 20)
    animated_gif('particulas2.gif', count=100, period=0.10, duration=0.10)


def draw():
    """ Limpa a tela, desenha e atualiza particulas """
    background(0)  # atualização do desenho, fundo preto
    pa.desenhar()
    pa.atualizar()
    pb.desenhar()
    pb.atualizar()
    pc.desenhar()
    pc.atualizar()


class Particula():
    """ Classe Particula, cor sorteada, velocidade sorteada """

    def __init__(self, x, y, tamanho=None):
        self.x = float(x)
        self.y = float(y)
        if tamanho:
            self.tamanho = tamanho
        else:
            self.tamanho = random(10, 50)
        self.vx = random(-1, 1)
        self.vy = random(-1, 1)
        self.cor = color(random(256),  # R
                         random(256),  # G
                         random(256),  # B
                         200)  # alpha

    def desenhar(self):
        """ Desenha círculo """
        no_stroke()
        fill(self.cor)
        circle(self.x, self.y, self.tamanho)

    def atualizar(self):
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