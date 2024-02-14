# Mais exemplos de 3D



## Cubo 3D com texturas

```python

"""
Baseado no exemplo Texture Cube de Dave Bollinger pra o Processing
"""

half_width = None
half_height = None
tex = None
rotx = PI / 4
roty = PI / 4
textures = []

def setup():
    size(640, 360, P3D)
    global half_width, half_height, tex
    global other_tex
    half_width = width / 2.0
    half_height = height / 2.0
    texture_mode(NORMAL)
    fill(255)
    stroke(color(44, 48, 32))
    w, h = 300, 300
    t = create_graphics(w, h)
    print(t)
    for _ in range(6):
        t.begin_draw()
        t.background(random(256), random(256), random(256))
        for i in range(10):
            t.circle(random(w), random(h), 10 + i * 10)
        t.end_draw()
        textures.append(t.copy())
    print(textures[0])

def draw():
    background(0)
    no_stroke()

 
    textured_cube(half_width, half_height, -100,
                  90, textures,
                  rotx=rotx, roty=roty)


def textured_cube(x, y, z, extent, textures, rotx=0, roty=0):
    try:
        textures = tuple(textures)
    except TypeError:
        textures = (textures, )
    textures *= 6
    
    A = ((-1, -1, 1, 0, 0),  # +Z "front" face.
         (1, -1, 1, 1, 0), 
         (1, 1, 1, 1, 1),
         (-1, 1, 1, 0, 1))
    B = ((-1, -1, -1, 0, 0), # -Z "back" face. 
         (1, -1, -1, 1, 0),
         (1, -1, 1, 1, 1),
         (-1, -1, 1, 0, 1))
    C = ((1, -1, -1, 0, 0),  # +Y "bottom" face.
         (-1, -1, -1, 1, 0),
         (-1, 1, -1, 1, 1),
         (1, 1, -1, 0, 1))
    D = ((-1, 1, 1, 0, 0),   # -Y "top" face.
         (1, 1, 1, 1, 0),
         (1, 1, -1, 1, 1),
         (-1, 1, -1, 0, 1))
    E = ((1, -1, 1, 0, 0),   # +X "right" face.
         (1, -1, -1, 1, 0),
         (1, 1, -1, 1, 1),
         (1, 1, 1, 0, 1))
    F = ((-1, -1, -1, 0, 0), # -X "left" face.
         (-1, -1, 1, 1, 0),
         (-1, 1, 1, 1, 1),
         (-1, 1, -1, 0, 1))

    with push_matrix():
        translate(x, y, z)
        scale(extent)
        rotate_x(rotx)
        rotate_y(roty)
        for face, tex in zip((A, B, C, D, E, F), textures):
            with begin_shape(QUADS):
                texture(tex)
                vertices(face)
                

def mouse_dragged():
    global rotx, roty
    rate = 0.01
    rotx += (pmouse_y - mouse_y) * rate
    roty += (mouse_x - pmouse_x) * rate


```

## Usando a cor para alterar a profundidade de um elemento

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
