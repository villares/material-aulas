from estrela import Estrela

estrelas = []  # lista de objetos

def setup():
    """ Define área de desenho e popula lista de estrelas """
    # fullScreen()
    size(600, 800)  # área de desenho (width, height)
    meia_largura, meia_altura = width / 2., height / 2. # floats
    for _ in range(6):
        e = Estrela(random(width),random(height))
        estrelas.append(e)

def draw():
    """ Limpa a tela, desenha e atualiza estrelas """
    background(0)  # atualização do desenho, fundo preto
    for i, estrela in enumerate(estrelas):
        estrela.desenha(i, pontas=7, raio1=50, raio2=10)
        estrela.anda()
