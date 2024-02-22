# Detectando a sobreposição de elementos geométricos

Um conjunto interessante de perguntas, especialmente no domínio dos jogos e dos programas gráficos interativos, é se um ponto ou elemento geométrico está encostando ou sobreposto a outro. Isso é também chamdo de "colisão".

- O mouse está sobre o botão retangular?
- O ponto que se move está sobre o círculo?
- Este elemento está dentro do polígono?
- O círculo encostou no triângulo?

As bibliotecas de simulação física respondem estas perguntas o tempo todo e não só as respondem como implementam sofisticados comportamentos resultantes das colisões simuladas entre objetos.

Mas mesmo sem a complexidade adicional da simulação física, pra fazer sketches animados e interativos pode ser muito útil saber responder este tipo de perguntas. Uma referência inestimável de funções que respondem as principais perguntas de colisões entre formas é o site incrível [www.jeffreythompson.org/collision-detection/](http://www.jeffreythompson.org/collision-detection/).

vamos experimentar aqui mostrar alguns dos casos mais simples.


## Ponto e círculo

A resposta neste depende  da distância do ponto ao centro do círculo ser menor do que o raio.

```python
# usando a função dist do py5
def point_in_circle(px, py, cx, cy, r):
    return dist(px, py, cx, cy) <= r
```


## Retângulo e retângulo

```python
def rect_in_area(xm, ym, wm, hm, xa, ya, wa, ha):
    return (xa < xm < xa + wa - wm and
            ya < ym < ya + ha - hm)

```

## Ponto e polígono

```python
def point_in_poly(*args):
    # ray-casting algorithm based on
    # https://wrf.ecse.rpi.edu/Research/Short_Notes/pnpoly.html
    if len(args) == 2:
        (x, y), poly = args
    else:
        x, y, poly = args
    inside = False
    for i, p in enumerate(poly):
        pp = poly[i - 1]
        xi, yi = p
        xj, yj = pp
        intersect = ((yi > y) != (yj > y)) and (x < (xj - xi) * (y - yi) / (yj - yi) + xi)
        if intersect:
            inside = not inside
    return inside
```
