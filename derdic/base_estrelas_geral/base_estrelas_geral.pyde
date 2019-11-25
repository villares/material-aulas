from estrela import Estrela
add_library('oscP5') # precisa instalar no IDE do Processing oscP5!

estrelas = []  # lista de objetos

def setup():
    """ Define área de desenho e popula lista de estrelas """
    # fullScreen()
    size(600, 800)  # área de desenho (width, height)
    setup_dados()

    meia_largura, meia_altura = width / 2., height / 2. # floats
    for _ in range(len(instrumentos)):
        e = Estrela(random(width),random(height))
        estrelas.append(e)

def draw():
    """ Limpa a tela, desenha e atualiza estrelas """
    background(0)  # atualização do desenho, fundo preto
    
    for i, estrela in enumerate(estrelas):
        tom, amp, cor, ins = dados[instrumentos[i]]
        estrela.desenha(cor, pontas=7, raio1=amp, raio2=tom)
        estrela.anda()

def oscEvent(theOscMessage):
    for instrumento in instrumentos:   
            if theOscMessage and theOscMessage.addrPattern() == "/"+ instrumento:
                ins = theOscMessage.get(0).intValue() if theOscMessage.get(0) else 0
                tom = theOscMessage.get(1).intValue() if theOscMessage.get(1) else 0
                amp = theOscMessage.get(2).intValue() if theOscMessage.get(2) else 0
                cor = theOscMessage.get(3).intValue() if theOscMessage.get(3) else 0               
                dados[instrumento] = (ins, tom, amp, cor)
                if cor == 0 or amp == 0 or tom == 0:
                    print(instrumento, dados[instrumento])
     
def setup_dados():
    global dados, instrumentos, oscP5
    oscP5 = OscP5(this, 12000)
    dados = dict()
    instrumentos = ("verdesol",
                    "laranjare",
                    "verdefa",
                    "vermelhodo1",
                    "vermelhodo2",
                    "amarelomi",
                    "roxosi"
                    )
    for instrumento in instrumentos:
            dados[instrumento] = (0, 100, 100, 100) 
