

estrelas = []  # lista de objetos

def setup():
    """ Define área de desenho e popula lista de estrelas """
    # fullScreen()
    size(400, 400)  # área de desenho (width, height)
    meia_largura, meia_altura = width / 2., height / 2. # floats
    for _ in range(6):
        e = Estrela(meia_largura, meia_altura)
        estrelas.append(e)

def draw():
    """ Limpa a tela, desenha e atualiza estrelas """
    background(0)  # atualização do desenho, fundo preto
    for estrela in estrelas:
        estrela.desenha(10 if mouseX > 200 else 30)
        estrela.anda()

class Estrela():
    """ Classe Estrela, cor sorteada, tamanho sorteado por default """

    def __init__(self, px, py, ptamanho=None):
        self.x = px
        self.y = py
        if ptamanho:
            self.tamanho = ptamanho
        else:
            self.tamanho = random(50, 200)
        self.vx = random(-2,2)
        self.vy = random(-2,-4)
        sorteio = random(128)
        self.cor = color(128 + sorteio,  # R
                         0,  # G
                         128 + sorteio,  # B
                         200)  # alpha

    def desenha(self,pontas=30, raio1=50, raio2=100):
        """ Desenha polígono em torno das coordenadas do objeto """
        noStroke()
        fill(self.cor)
        pushMatrix()
        translate(self.x, self.y)
        rotate(radians(frameCount))
        estrela(0, 0, pontas, mouseY, raio2)
        popMatrix()
    
    
    def anda(self):
        """ atualiza a posição do objeto e devolve do lado oposto se sair """
        self.x += self.vx
        self.y += self.vy
        metade = self.tamanho / 2
        if self.x > width + metade:
            self.vx = -self.vx
        if self.y > height + metade:
            self.vy = -self.vy
        if self.x < -metade:
            self.vx = -self.vx
        if self.y < -metade:
            self.vy = -self.vy
            
            
def estrela(cx, cy, pontas, raio1, raio2):    
    pontos = pontas * 2
    parte = 360. / pontos
    beginShape() # comece a forma!
    for p in range(pontos): # para cada p
        angulo = radians(p * parte) # calcula angulo
        if p % 2 == 0: # se for par
            raio = raio1
        else: # senão, se for impar
            raio = raio2
        x = cx + raio * sin(angulo)
        y = cy + raio * cos(angulo)
        vertex(x, y) # vertex é um ponto
    endShape(CLOSE) # termina forma
