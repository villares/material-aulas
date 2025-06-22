
TAM_BOLA = 20
MEIA_BOLA = TAM_BOLA / 2
vx, vy = -2, 1


def setup():
    """ Executado no início """
    global x, y
    size(700, 400)
    rect_mode(CENTER)
    x, y = width / 2, height / 2


def draw():
    # parte do desenho
    global x, y, vx, vy
    # background(255, 0, 0)
    TAM_BOLA = random(10, 50)
    no_stroke()
    fill(random(256), random(256), random(256), 100)
    if random(100) > 50:
        ellipse(x, y, TAM_BOLA, TAM_BOLA)
    else:
        rect(x, y, TAM_BOLA, TAM_BOLA)
    x = x + vx
    y = y + vy

    if x < MEIA_BOLA or x > width - MEIA_BOLA:
        vx = -vx
    if y < MEIA_BOLA or y > height - MEIA_BOLA:
        vy = -vy
