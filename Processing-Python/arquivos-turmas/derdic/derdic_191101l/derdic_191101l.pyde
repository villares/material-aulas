x, y = 0, 0

def setup():
    size(500, 500)
    background(0)

def draw():
    global x, y
    # background(240, 250, 250)
    fill(255, 0, 0, 100)
    estrela(250, 250, int(random(3,9)), frameCount % 100, 100)
    fill(random(255), 0, random(255), 100)
    estrela(x, y, 16, random(100), 40)
    fill(random(255), random(255), 0, 100)
    estrela(mouseX, mouseY, 8, 10, random(100))
    x = x + 5
    y = y + 5
    if x > width: x = 0
    if y > height: y = 0

def estrela(cx, cy, pontas, raio1, raio2):
    pontos = pontas * 2
    parte = 360. / pontos
    beginShape()  # comece a forma!
    for p in range(pontos):  # para cada p
        angulo = radians(p * parte)  # calcula angulo
        if p % 2 == 0:  # se for par
            raio = raio1
        else:  # senão, se for impar
            raio = raio2
        x = cx + raio * sin(angulo)
        y = cy + raio * cos(angulo)
        vertex(x, y)  # vertex é um ponto
    endShape(CLOSE)  # termina forma
