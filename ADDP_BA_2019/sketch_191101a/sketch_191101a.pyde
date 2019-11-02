
from bola import Bola

lista_bolas = []

def setup():
    size(500, 500)
    for i in range(100):
        nova_bola = Bola(250, 250, random(10, 50))
        lista_bolas.append(nova_bola)
    
def draw():
    # background(0)
    fill(0, 10)
    rect(0, 0, width, height)
    for bola in lista_bolas:
        bola.move()
        bola.plot()

def mousePressed():
    nova_bola = Bola(mouseX, mouseY, 10)
    nova_bola.cor = color(255)
    lista_bolas.append(nova_bola)



    
    
