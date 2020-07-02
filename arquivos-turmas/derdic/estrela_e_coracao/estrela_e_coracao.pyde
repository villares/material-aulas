x, y = 0, 150
vx, vy = 5, 3

def setup():
    size(500, 500)
    frameRate(50)
    background(200, 250, 200)

    
def draw():
    global x, y, vx, vy
    stroke(255, 0, 0) # cor da linha
    fill(150, 0, 255) # roxo
    strokeWeight(1) # linha fina
    fill(255, 255, 0)
    estrela(260, 350, 50 ,100, 40)
    stroke(0)
    estrela(x, y, 9,
            50 * sin(radians(frameCount)),
            25)
    x = x + vx
    if x > width or x < 0:
        vx = -vx
    y = y + vy
    if y > width or y < 0:
        vy = -vy

    stroke(0, 100, 0) # verde escuro
    strokeWeight(10) # linha grossa com 10
    fill(255, 0, 0) # cor de preenchimento
    estrela(250, 250, 12, 100, 50)
    coracao(200, 100)
        
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
    
    
def coracao(x, y, t=1):
    pushMatrix()
    noStroke()
    translate(x, y)
    scale(t)
    beginShape()
    vertex(50, 15)
    bezierVertex(50, -5, 90, 5, 50, 40)
    vertex(50, 15)
    bezierVertex(50, -5, 10, 5, 50, 40)
    endShape()
    popMatrix()
