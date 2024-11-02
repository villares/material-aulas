from py5_tools import animated_gif
    
particulas = []  # lista de objetos

def setup():
    """ Define área de desenho e popula lista de particulas """
    size(400, 400)  # área de desenho (width, height)
    meia_largura, meia_altura = width / 2, height / 2
    for _ in range(50):
        nova_particula = Particula(meia_largura, meia_altura)
        particulas.append(nova_particula)
    animated_gif('particulas3.gif', count=100, period=0.10, duration=0.10)



def draw():
    """ Limpa a tela, desenha e atualiza particulas """
    background(0)  # atualização do desenho, fundo preto
    for particula in particulas:
        particula.desenhar()
        particula.atualizar()
class Particula():
    """ Classe Particula, cor sorteada, velocidade sorteada """

    def __init__(self, x, y, tamanho=None):
        self.x = float(x)
        self.y = float(y)
        if tamanho:
            self.tamanho = tamanho
        else:
            self.tamanho = random(50, 200)
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