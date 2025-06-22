def setup():
    size(400, 400)

def draw():
    background(200)
    no_stroke()
    dots(width / 2, height / 2,
         mouse_x, mouse_y,
         color(255, 255, 0),
         color(0, 255, 255),
         steps = 10,
         dot_size = 25)

def dots(x1, y1, x2, y2, ca, cb, steps=10, dot_size=10):
    L = dist(x1, y1, x2, y2)
    A = atan2(x1 - x2, y2 - y1)
    push_matrix()
    translate(x1, y1)
    rotate(A)
    if L < steps * dot_size:
        steps=int(L / dot_size)
    for i in range(steps + 1):
        y=0
        if steps > 0:
            p=i / steps
            y=lerp(0, L, p)
            cor=lerp_color(ca, cb, p)
            fill(cor)
        rect_mode(CENTER)
        rect(0, y, dot_size, dot_size)
    pop_matrix()