# Mais exemplos de 3D


# Desenhado em 3D usando a informação de cor para alterar a profundidade
# de um elemento

```python


def setup():
    size(640, 360, P3D)
    # The image file must be in the data folder of the current sketch
    # to load successfully
    global img
    img = load_image("moonwalk.jpg")    # Load the image into the program


def draw():
    lights()
    # Displays the image at its actual size at point (0,0)
    translate(width / 2, height / 2, -200)
    rotate_y(radians(frame_count))
    translate(-width / 2, -height / 2)
    background(0)
    no_stroke()
    # stroke(255)
    passo = 5
    sphere_detail(5)
    for x in range(0, width, passo):
        for y in range(0, height, passo):
            cor = img.get(x, y)
            bri = saturation(cor)
            fill(cor)
            push_matrix()
            translate(x, y, bri)
            sphere(passo)
            #circle(x, y, passo)
            pop_matrix()


```
