"""
Exemplo de uso da Classe Bandeirinhas, com mudança de cor 'mouse over'
clique para acrescentar um objeto, tecle 'espaço' para remover
"""

bandeirinhas = []  # lista de objetos

def setup():
    """ Define área de desenho e popula lista de bandeirinhas """
    size(400, 400)  # área de desenho
    meia_largura, meia_altura = width / 2, height / 2
    for _ in range(50):
        nova_bandeirinha = Bandeirinha(meia_largura, meia_altura)
        bandeirinhas.append(nova_bandeirinha)

def draw():
    """ Limpa a tela, desenha e atualiza bandeirinhas """
    background(0)  # atualização do desenho, fundo preto
    #fill(0, 2)
    #rect(0, 0, width, height)
    for bandeira in bandeirinhas:
        bandeira.desenha()
        bandeira.anda()
    # para salvar frames 
    #f = frameCount            
    #if  f < 1000 and not f % 10:
    #    saveFrame("../s4_####.png")
    
def mousePressed():
    """ Acrescenta pequena bandeirinha branca """
    nova_bandeirinha = Bandeirinha(mouseX, mouseY, 25)
    nova_bandeirinha.cor = color(255)  # forçando que seja branca!
    bandeirinhas.append(nova_bandeirinha)
    
def keyPressed():  
    """ tecla 'espaço' remove a última bandeirinha da lista """
    if key == ' ' and len(bandeirinhas) > 1:
        removida = bandeirinhas.pop()    

class Bandeirinha():
    """ Classe Bandeirinha, cor sorteada, tamanho sorteado por default """

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
            # se o mouse estiver longe, normal, senão, branca
            if dist(mouseX, mouseY, self.x, self.y) > metade:
                fill(self.cor)
            else:
                fill(255,100)
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

