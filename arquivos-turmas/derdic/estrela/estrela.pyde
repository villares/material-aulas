

def setup():
    size(500, 500)
    
def draw():
    background(240, 250, 250)
    estrela(250, 250, 6, 200, 100)
    estrela(260, 350, 50 ,100, 40)
    estrela(350, 150, 9, 50, 25)
        
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
