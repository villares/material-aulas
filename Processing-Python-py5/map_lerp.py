# Manipulando números com `map()` e `lerp()`

# Sumário

- [A função `map()` do processing](  # a-função-map-do-processing)
- [A função `lerp()`: interpolação linerar](  # a-função-lerp-interpolação-linear)
- [A função `lerp_color()`: interpolando cores](  # a-função-lerpcolor-interpolando-cores)

# A função `map()` do Processing

> no processing modo python temos uma situação um pouco curiosa, por ser uma ferramenta híbrida com elementos de processing e de python. essas duas linguagens tem funções de nome `map()` mas com comportamentos/significados totalmente distintos. nesta página vamos explorar o comportamento do `map()` do processing(mas é possível obter o comportamento de `map()` do python também, que explicaremos em outra página).

A função `map()` converte um valor de uma faixa de números devolvendo um valor equivalente em outra faxia. recebendo um número, que vamos chamar de **`a`**, que está em uma faixa de origem de `a0`  a `a1` , devolve um número **`b`**  na faixa de destino de `b0` a `b1`, de forma que 'mapeia' valores de uma faixa para outra. A sintaxe fica assim, entregamos 5 argumentos e obtemos um valor como resposta:

```python
b=map(a, a0, a1, b0, b1)
```

veja uma animação que tenta mostrar como funciona essa conversão de valores de uma escala ou faixa para outra.

![](assets/map_2.gif)

note que se você entregar um número **`a`** fora da faixa de origem indicada(entre `a0` e `a1`) vai receber um número 'para fora' da faixa de destino entre `b0` e `b1`.

em um caso de uso bem simples, o `map()` podemos transformar o valor da posição horizontal do mouse, `mouse_x`, que é um número entre ** 0 ** e a largura da área de desenho(`width`), em um valor para controlar elementos do desenho(na faixa que desejarmos).  no exemplo abaixo, cinzas entre preto e branco podem são criados com números na faixa entre ** 0 ** e ** 255**, e um círculo vai ser movido entre as posições ** x ** de ** 100 ** a ** 300**.

```python
def setup():
    size(400, 400)
    stroke_we

def draw():
    background(200)

    cinza=map(mouse_x, 0, width, 0, 255)
    x=map(mouse_x, 0, width, 100, 300)

    fill(cinza)
    circle(x, height / 2, 100)
```

![](assets/map_1.gif)

# A função `lerp()`: interpolação linear

O nome vem, de  < i > **l**inear int**erp**olation < /i > (interpolação linear) e a função permite obter um número intermediário ente do outros números `v0` e `v1` de maneira proporcional a um parâmetro **`t`** . você pode interpretar **`t`** como uma porcentagem, **0 ** faz `lerp()` devolver o primeiro número, `v0`, e ** 1 **  produz o segundo, `v1`.  com o **`t`**  valendo  ** 0.5 ** (50 %) o valor devolvido fica bem no meio do caminho entre os dois números (uma média aritmética).

isso lembra o `map()` que acabamos de ver, mas com uma faixa de origem (para o **`t`** ) predeterminada de  ** 0 ** a ** 1 ** , veja na animação abaixo.

![](assets/lerp_1.gif)

note que assim como em `map()` valores fora da faixa esperada de origem(no caso entre ** 0 ** e ** 1**) produzem valores além dos limites fornecidos.


# A função `lerpColor()`: interpolando cores

podemos também obter cores intermediárias com a função `lerp_color()`, um * lerp * especial para cores.

![](assets/lerp_3.gif)

veja exemplos de uso abaixo.

```python
from __future__ import division

def setup():
    size(400, 400)
    stroke_weight(3)
    no_fill()

def draw():
    background(240)
    xa, ya=100, 100
    xb, yb=300, 300
    ca=color(200, 0, 0)
    cb=color(0, 0, 200)
    n=1 + int(mouse_x / 10)  # ou 1 + int(map(mouseX, 0, width, 0, 40))
    for t in range(n + 1):
        xc=lerp(xa, xb, t / n)
        yc=lerp(ya, yb, t / n)
        cc=lerp_color(ca, cb, t / n)
        stroke(cc)
        ellipse(xc, yc, 200, 200)
```
![](assets/lerp_3b.gif)

```python
from __future__ import division

def setup():
    size(400, 400)

def draw():
    background(200)
    no_stroke()
    dots(width / 2, height / 2,
         mouse_x, mouse_y,
         color(255, 255, 0),
         color(0, 255, 255),
         steps=10,
         dot_size=25)

def dots(x1, y1, x2, y2, ca, cb, steps=10, dot_size=10):
    L=dist(x1, y1, x2, y2)
    A=atan2(x1 - x2, y2 - y1)
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
```

# Assuntos relacionados

- [transições com * easing*](easing.md)
