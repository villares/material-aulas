# Como desenhar em 3D

Nessa página vamos ver como desenhar objetos tridimensionais, ou ainda objetos 2D no espaço

## Primeiros passos

Para começar, dentro do `setup()` é preciso usar o argumento `P3D` em `size()`, como neste exemplo:

```python
def setup():
    size(500, 500, P3D)
```

Passa então a ser possivel modificar o sistema de coordenadas com `translate(x, y, z)` (agora com **z**) e `rotate_x()`, `rotate_y()` e `rotate_z()` (que giram em torno dos eixos).

Desta maneira é possível desenhar os mesmos elementos 2D que utilizamos até agora, porém deslocados e girados no espaço. Mas além dessa estratégia, também acontecem as seguintes mudanças:

- Linhas podem receber coordenadas 3D: `line(x1, y1, z1, x2, y2, z2)`

- Os elementos `Py5Shape` criados com `begin_shape()` e `end_shape()` passam a poder ser desenhados no espaço, usando, por exemplo, `vertex(x, y, z)`. Esse comando desenha a partir de uma sequência de vértices dados nas coordenadas recebidas.

- A função `box(w, h, d)` desenha um paralelepípedo, ou um cubo com `box(side)`, sempre na origem(0, 0, 0) do sistema de coordenadas, sendo então em geral acompanhada de uma estrutura com `push_matrix()`/`pop_matrix()` e `translate(x, y, z)` para que seja posicionada no lugar desejado.

- A função `sphere(raio)` desenha uma aproximação de uma esfera, também na origem. O numero de faces da esfera pode ser controlado pela função[`sphere_detail()`](https://py.processing.org/reference/sphere_detail.html).


# Alguns objetos desenhados em 3D

![imagem exemplo 3D](assets/passos3D.gif)

```python

def setup():
    size(500, 500, P3D)
    rect_mode(CENTER)

def draw():
    background(200)
    lights()
    translate(width / 2, height / 2)
    rotate_x(radians(frame_count))
    stroke(255)
    fill(0, 200, 0)
    caixa(50, 50, 0, 20, 100, 50)
    fill(255, 0, 0)
    caixa(20, 20, -20, 20)
    fill(0, 0, 200)
    caixa(0, 20, 20, 20)
    stroke(0)
    line(0, 0, 0, 50, 50, 100)

    begin_shape()
    vertex(0, 0, 0)
    vertex(100, 100, 100)
    vertex(100, -100, 50)
    end_shape(CLOSE)

    # rotateY(QUARTER_PI + radians(frameCount))
    translate(0, 0, 100)
    fill(255)
    rect(0, 0, 100, 100)

def caixa(x, y, z, *tam):
    push_matrix()
    translate(x, y, z)
    box(*tam)
    pop_matrix()
```

# Desenhando uma caixa entre dois pontos

Usando um volume `box()` girado em 3D.

```python
def setup():
    size(500, 500, P3D)
    hint(DISABLE_DEPTH_MASK)  # https://processing.org/reference/hint_.html

def draw():
    background(200)
    lights()
    fill(255, 0, 0, 100)
    bar_line(50, 50, 0, mouse_x, mouse_y, 250, 30)
    bar_line(450, 450, 0, 250, 250, 250, 30)

def bar_line(x1, y1, z1, x2, y2, z2, weight=10):
    """Draw a box rotated in 3D like a bar_line/edge."""
    p1, p2=(x1, y1, z1), (x2, y2, z2)
    dist_p1_p2=dist(x1, y1, z1, x2, y2, z2)
    v1=(x2 - x1, y2 - y1, z2 - z1)
    phi, the=acos(v1[2] / dist_p1_p2), atan2(v1[1], v1[0])
    push_matrix()
    translate(x1 + v1[0] / 2.0, y1 + v1[1] / 2.0, z1 + v1[2] / 2.0)
    rotate_z(the)
    rotate_y(phi)
    box(weight, weight, dist_p1_p2)
    pop_matrix()
```

# Desenhando um prisma girado em 3D

```python
def prism_line(x1, y1, z1, x2, y2, z2, radius=10, num_points=6):
    """
    Desenha um prisma girado em 3D como uma barra.
    Requer as funções auxiliares draw_face e z_circle.
    """
    p1, p2=(x1, y1, z1), (x2, y2, z2)
    dist_p1_p2=dist(x1, y1, z1, x2, y2, z2)
    v1=(x2 - x1, y2 - y1, z2 - z1)
    phi, the=acos(v1[2] / dist_p1_p2), atan2(v1[1], v1[0])
    push_matrix()
    translate(x1 + v1[0] / 2.0, y1 + v1[1] / 2.0, z1 + v1[2] / 2.0)
    rotate_z(the)
    rotate_y(phi)
    # box(radius, radius, dist_p1_p2) # antiga barra
    rotate_x(HALF_PI)  # deixa circlulos perpendiculares a direção da barra
    base=z_circle(0, -dist_p1_p2 / 2.0, radius, num_points)
    draw_face(base)  # fechamento base
    top=z_circle(0, dist_p1_p2 / 2.0, radius, num_points)
    draw_face(top)  # fechamento topo
    pairs=zip(top, base)
    for i, (point_a, point_b) in enumerate(pairs):
        point_c, point_d=pairs[i - 1]
        face=(point_a, point_b, point_d, point_c)
        draw_face(face)  # faces laterais
    pop_matrix()

def draw_face(points):
    begin_shape()
    for x, y, z in points:
        vertex(x, y, z)
    end_shape(CLOSE)

def z_circle(x, y, radius, num_points=16):
    a=TWO_PI / num_points
    return [(x + cos(a * i) * radius, y, sin(a * i) * radius)
             for i in range(num_points)]
```

# Carregando arquivos OBJ externos

Usando `size()` com `P3D` é possível carregar arquivos OBJ com a função `load_shape('arquivo.obj')` e mostrá-los com `shape(s, x, y)`.
Procure o exemplo que vem no IDE na janela de exemplos: `Basic > Shape > LoadDisplayOBJ`.

<!-- # PeasyCam, uma biblioteca que permite orbitar em torno dos objetos

É possível baixar uma biblioteca chamada **PeasyCam** que acrescenta com poucas linhas a funcionalidade de uma câmera que com o arrastar do mouse clicado 'orbita' em torno dos elementos desenhados, a câmera também oferece zoom com a rodinha do mouse. Note que o uso desta biblioteca desloca o sistema de coordenadas levando a origem para o centro da área de desenho.

```python
add_library('peasycam')  # é preciso baixar/instalar pelo IDE

def setup():
    global cam
    size(500, 500, P3D)
    cam=PeasyCam(this, 100)
    cam.set_minimum_distance(100)
    cam.set_maximum_distance(200)

def draw():
    # Desenho 3D que pode ser "orbitado" com drag do mouse
    lights()
    background(200)
    fill(96, 255, 0)
    box(30)
    push_matrix()
    translate(0, 0, 20)
    fill(0, 96, 255)
    box(5)
    pop_matrix()

    cam.begin_hud()  # inicia "Heads Up Display"
    # elementos 2D alinhados com a tela (como num vidro)
    fill(0, 128)
    rect(0, 0, 60, 30)
    fill(255)
    text("{:.2f}".format(frame_rate), 10, 18)
    cam.end_hud()  # termina o "HUD"
```
-->

# Explorando ajustes avançados com a função `hint()`

É possível controlar alguns aspectos do cálculo da apresentação 3D, meio que um ajuste fino, que tem impacto na performance (velocidade de execução) e aparência. 

O exemplo abaixo permite testar algos dos ajustes, conhecidos como *hints*, do motor de apresentação (*render engine*) `P3D`, mostrando a diferença entre as opções documentadas em [py5coding.org/reference/sketch_hint.html](https://py5coding.org/reference/sketch_hint.html).

```python
# Inspirado na conversa em:
# https://discourse.processing.org/t/program-to-test-hint-with-transparency/4361

# ["name", hint_enabled, hint_disable_constant, hint_enable_constant]
hints=(["DEPTH_TEST", False,
          DISABLE_DEPTH_TEST, ENABLE_DEPTH_TEST],
         ["DEPTH_SORT", False,
          DISABLE_DEPTH_SORT, ENABLE_DEPTH_SORT],
         ["DEPTH_MASK", False,
          DISABLE_DEPTH_MASK, ENABLE_DEPTH_MASK],
         ["OPTIMIZED_STROKE", True,
          DISABLE_OPTIMIZED_STROKE, ENABLE_OPTIMIZED_STROKE],
         ["STROKE_PERSPECTIVE", False,
          DISABLE_STROKE_PERSPECTIVE, ENABLE_STROKE_PERSPECTIVE],
         )
use_sphere=False

def setup():
    size(800, 600, P3D)
    sphere_detail(12)
    apply_hints()

def draw():
    window_title('FPS: {}'.format(round(get_frame_rate())))
    background(255)

    fill(0)
    for i, (name, status, _, _) in enumerate(hints):
        text("{} {}".format(name, str(status)), 20, 20 + i * 20)
    text("<- use the mouse to toggle settings", 200, 40)
    text("click here to toggle shape", 300, 580)

    fill(255, 40, 20, 100)
    translate(width / 2, height / 2)
    rotate_y(frame_count * 0.005)
    for x in range(-200, 201, 200):
        for y in range(-200, 201, 200):
            push_matrix()
            translate(x, 0, y)
            if use_sphere:
                sphere(90)
            else:
                box(180)
            pop_matrix()

def mouse_pressed():
    global use_sphere
    if mouse_y > height - 100:
        use_sphere=not use_sphere

    id = mouse_y // 20
    if id < len(hints):
        hints[id][1] = not hints[id][1]

    apply_hints()

def apply_hints():
    for _, status, disable_const, enable_const in hints:
        hint(enable_const if status else disable_const)
```

## Assuntos relacionados

- [Exemplos de caixa com furos e outros sólidos desenhados em 3D e desdobrados em 2D](https://github.com/villares/Paper-objects-with-Processing-and-Python) (link externo)
