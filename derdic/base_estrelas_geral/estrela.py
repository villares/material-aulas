# -*- coding: utf-8 -*-
from cores import *

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


    def desenha(self,id, pontas=10, raio1=50, raio2=100):
        """ Desenha polígono em torno das coordenadas do objeto """
        colorMode(RGB)
        global cor1, cor2, cor3
        if keyPressed:
            cor1 = color(*coresB[0])
            cor2 = color(*coresB[1])
            cor3 = color(*coresB[2])
        else:
            cor1 = color(*coresB[3])
            cor2 = color(*coresB[4])
            cor3 = color(*coresB[5])

        noStroke()
        # fill(self.cor)
        stroke(cor2)
        fill(triangulo(cor1, cor2, cor3, map(mouseX, 0, width, 0, 360)))
        strokeWeight(5)
        strokeJoin(ROUND)
        # if keyPressed: raio2 = 300
        estrela(self.x, self.y, pontas, raio1 + 50 * sin(frameCount/3.),
                raio2 + 50 * sin(frameCount/3.))
        self.tamanho -=  (self.tamanho + raio2 / 5)
    
    
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
    
