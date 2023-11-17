# *Perlin noise*
# Ruído de Perlin

Nesta altura você possívelmente já experimentou fazer algo usando[números(pseudo)aleatórios](aleatoriedade_1.md), e talvez tenha notado o quão abruptas são as variações produzidas por esse tipo de estratégia, os números produzidos a cada chamada de `random()` tem uma chance igual de estar em qualquer lugar da faixa indicada, isso gera facilmente paletas e tamanhos imprevisíveis, mas, frequentemente, por conta de contrastes muito acentuados, não tão interessantes. O Ruído de Perlin, que pode ser obtido com a função embutida do Processing, `noise()`, ao contrário, produz valores que tem algum grau de semelhança entre "vizinhos", valores que se relacionam de alguma forma ao longo do tempo ou do espaço. Estes valores então permitem gerar variações de cor e formas que nos remetem a elementos naturais como topografias ou névoas, entre outras texturas.

>*An algorithm known as “Perlin noise, ” named for its inventor Ken Perlin, takes this concept into account. Perlin developed the noise function while working on the original Tron movie in the early 1980s; it was designed to create procedural textures for computer-generated effects. In 1997 Perlin won an Academy Award in technical achievement for this work. Perlin noise can be used to generate various effects with natural qualities, such as clouds, landscapes, and patterned textures like marble.*
>
>*Perlin noise has a more organic appearance because it produces a naturally ordered(“smooth”) sequence of pseudo-random numbers. The graph on the left below shows Perlin noise over time, with the x-axis representing time; note the smoothness of the curve.*
>
>(Trecho de [*The Nature of Code*](https://natureofcode.com/book/introduction /), 2012, de Daniel Shiffman.)

# *Perlin Noise* 1D

O primeiro exemplo de Ruído de Perlin, apresentado a seguir, usa a função `noise()` do py5, que gera um número entre **0** e **1**, inicialmente com apenas um argumento. Vamos comparar o resultado com `random(1)` na parte de cima da àrea de desenho. Note que na parte de baixo, com `noise()` os valores produzidos tem relação com os vizinhos, ao contrário do `random()`, produzindo uma curva relativamente suave. A amplitude pode ser ajustada mudando o valor pelo qual multiplicamos o resultado de `noise()`, ou então, usando `lerp()`.

Pense no argumento que usamos na chamada de `noise()` como um X, um valor que deslocamos no espaço com uma certa * velocidade*. A velocidade é ajustada pela variável `escala` que vai multiplicar o X. Podemos experimentar mudar o valor dessa * escala * ou * velocidade * dos passos dados pelo argumento de entrada no espaço e também podemos deslocar esse X uma certa distância arbitraria(somando `desloca_x`). Saiba que os resultados de `noise()` são simétricos para valores negativos de X.

```python
escala = 0.01
desloca_x = 0


def setup():
    size(400, 400)


def draw():
    background(240)
    random_seed(1001)  # para 'travar' o random()
    for x in range(width):
        y = random(height / 2)
        line(x, 0, x, y)

    for x in range(width):
        n = noise((desloca_x + x) * escala)
        y = lerp(height / 2, height, n)
        # y = height / 2 + (height / 2) * n
        line(x, height / 2, x, y)


def key_pressed():
    global escala, desloca_x
    if key == 'a':
        escala += 0.001
    if key == 'z':
        escala -= 0.001
    if key == 's':
        desloca_x += 5
    if key == 'x':
        desloca_x -= 5


```

![](assets/perlin1D.gif)

> Na imagem acima, na parte superior a altura das linha é calculada a partir do `random(height / 2)`,
> já as linhas da parte de baixo tem suas alturas produzidas a partir de uma chamada a `noise()`.

Com o teclado podemos alterar o valor da escala e do deslocamente em X.

Note que não é necessário usar `noise_seed()` no `draw()` pois a semente do `noise()` é inicializada no início da execução do * sketch * e os valores obtidos são consultados por meio dos argumentos, determinísticos, calculados, como posições a serem consultadas em um 'campo' fixo.

# *Perlin Noise* em 2D, acrescentando um Y

Agora acrescentaremos uma segunda dimensão, um Y, que serve de segundo argumento na função `noise()`. Ambos X e Y são multiplicados pela escala, e, no exemplo abaixo, serão deslocados pela posição do mouse.

Com essa segunda dimensão, perpendicular à primeira, é como se estivéssemos movendo o corte de um terreno. O `mouse_y` move o corte em uma direção perpendicular à tela, que é paralela ao corte.

```python
escala = 0.004


def setup():
    size(400, 400)


def draw():
    background(200)
    for x in range(width):
        n = noise((mouse_x + x) * escala,
                  mouse_y * escala)
        y = height * n
        line(x, height, x, height - y)


```

![](assets/perlin2D_1.gif)

Agora o mesmo exemplo desenhando um único polígono com `begin_shape()` e `end_shape()`

```python
escala = 0.004


def setup():
    size(400, 400)


def draw():
    background(200)
    stroke_weight(3)
    no_fill()
    begin_shape()
    for x in range(width):
        n = noise((mouse_x + x) * escala,
                  mouse_y * escala)
        y = height * n
        vertex(x, height - y)
    end_shape()


```

![](assets/perlin2D_3.gif)

# *Perlin Noise* em uma grade 2D

Uma segunda maneira de usar o ruído de Perlin é distribuindo os valores em uma grade, de maneira que as coordenadas no plano da tela informam os passos tanto em X como em Y.

```python
escala = 0.01
desloca_x = 100
desloca_y = 100
tam = 10


def setup():
    size(400, 400)
    no_stroke()


def draw():
    background(0)
    for x in range(0, width, tam):
        for y in range(0, height, tam):
            n = noise((desloca_x + x) * escala,
                      (desloca_y + y) * escala)
            ellipse(tam / 2 + x,
                    tam / 2 + y,
                    2 + tam * n,
                    2 + tam * n)


def key_pressed():
    global escala, desloca_x, desloca_y
    if key == 'a':
        escala += 0.001
    if key == 'z':
        escala -= 0.001
    if key_code == LEFT:
        desloca_x += 5
    if key_code == RIGHT:
        desloca_x -= 5
    if key_code == UP:
        desloca_y += 5
    if key_code == DOWN:
        desloca_y -= 5


```
![](assets/perlin2D_2.gif)

# *Perlin Noise* 3D, acrescentando um Z

Este é um exemplo de Ruído de Perlin com três dimensões. O mouse desloca o campo em X e Y, as setas para cima e para baixo deslocam em Z.

```python
escala_noise = 0.1
z = 0


def setup():
    size(400, 400)
    no_stroke()
    color_mode(HSB)


def draw():
    background(0)
    cols = 50
    tam = width / cols
    for x in range(cols):
        for y in range(cols):
            n = noise(
    (mouse_x + x) * escala_noise,
    (mouse_y + y) * escala_noise,
     z * escala_noise)
            fill(240 * n, 255, 255)
            ellipse(tam / 2 + x * tam, tam / 2 + y * tam,
                    tam - tam * n, tam - tam * n)


def key_pressed():
    global z
    if key_code == UP:
        z += 1
    if key_code == DOWN:
        z -= 1


```
![](assets/perlin3D.gif)

Agora, praticamente a mesma ideia mas visualizada em 3D

```python
escala_noise = 0.1
xo = yo = zo = 0


def setup():
    size(400, 400, P3D)
    # noStroke()
    color_mode(HSB)


def draw():
    background(0)
    translate(width / 2, height / 2, -height * 1.3)
    rotate_y(QUARTER_PI * .9)
    translate(-width / 2, -height / 2)
    translate(-width / 2, 0)
    cols = 30
    tam = width / cols
    for x in range(cols):
        for y in range(cols):
            for z in range(cols):
                n = noise((xo + x) * escala_noise,
                          (yo + y) * escala_noise,
                          (zo + z) * escala_noise)
                fill(240 * n, 255, 255)
                push()
                translate(tam / 2 + x * tam,
                          tam / 2 + y * tam,
                          tam / 2 + z * tam)
                box(tam - tam * n)
                pop()


def key_pressed():
    global xo, yo, zo
    if key_code == UP:
        zo += 1
    if key_code == DOWN:
        zo -= 1
    if key_code == LEFT:
        xo += 1
    if key_code == RIGHT:
        xo -= 1
    if key_code == SHIFT:
        yo += 1
    if key_code == CONTROL:
        yo -= 1


```

![](assets/perlin3D_3D.gif)

# Campo "vetorial" de ruído

Um campo em que o valor do ruído Perlin gira um ângulo.

```python
escala = 0.003
z = 0


def setup():
    size(400, 400)
    stroke(255)


def draw():
    background(0)
    for x in range(0, width, 10):
        for y in range(0, height, 10):
            n = noise((mouse_x + x) * escala,
                     (mouse_y + y) * escala,
                     z * escala)
            push_matrix()
            translate(x, y)
            rotate(TWO_PI * n)
            line(-5, 0, 5, 0)
            pop_matrix()


def key_pressed():
    global z
    if key_code == UP:
        z += 1
    if key_code == DOWN:
        z -= 1


```
![](assets/campo_perlin.gif)

# Perlin em uma grade variável com `while`

```python


def setup():
    size(650, 650)


def draw():
    background(0)
    total_h = 0
    while total_h < 600:
        total_w = 0
        nh = noise(total_w * 0.005,
                  total_h * 0.005,
                  frame_count * 0.001)
        true_h = h = 36 * nh
        if total_h + h > 600:
                h = 600 - total_h
        while total_w < 600:
            nw = noise(total_w * 0.005,
                      total_h * 0.005,
                      frame_count * 0.001)
            w = 36 * nw
            fill(0, w * 8, true_h * 8)
            if total_w + w > 600:
                w = 600 - total_w
            rect(25 + total_w,
                25 + total_h, w, h)
            total_w += w
        total_h += h
 ```
 
 ![](assets/perlin_while.gif)
