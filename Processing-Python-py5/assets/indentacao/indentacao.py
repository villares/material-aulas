from pyp5js import *


def setup():
    size(200, 200)

def draw():
    background(0, 0, 200)  # para limpar a área de desenho
    
    x, y = 100, 100  # coordenadas do centro
    mx = mouseX if mouseX < 200 else 200
    mx = mx if mouseX > 0 else 0
    my = mouseY if mouseY < 200 else 200
    my = my if mouseY > 0 else 0
    
        
    largura_a, largura_b = mx / 2, my / 2
    mm, m = largura_a / 2, largura_b / 2

    beginShape()
    vertex(x - mm, y - mm)
    vertex(x - m, y)
    vertex(x - mm, y + mm)
    vertex(x, y + m)
    vertex(x + mm, y + mm)
    vertex(x + m, y)
    vertex(x + mm, y - mm)
    vertex(x, y - m)
    endShape(CLOSE)