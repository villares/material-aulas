from py5_tools import animated_gif
    

def setup():
    """ Instancia três particulas """
    global pa, pb, pc
    size(100, 100)  # área de desenho (width, height)
    pa = Particula(50, 50, 40)
    pb = Particula(80, 10, 30)
    pc = Particula(10, 40, 20)
    animated_gif('particulas1.gif', count=100, period=0.10, duration=0.10)


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
    """ Classe Particula, com métodos de desenho e atualização."""

    def __init__(self, x, y, tamanho):
        self.x = x
        self.y = y
        self.tamanho = tamanho

    def desenhar(self):
        """ Desenha círculo """
        circle(self.x, self.y, self.tamanho)

    def atualizar(self):
        """ atualiza a posição do objeto """
        self.x += 1
        self.y += 1
        if self.x > width + self.tamanho / 2:
            self.x = - self.tamanho / 2
        if self.y > height +  self.tamanho / 2:
            self.y = - self.tamanho / 2