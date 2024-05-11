# Detectando a sobreposição de elementos geométricos

Um conjunto interessante de perguntas, no domínio conhecido como geometria computacional, e que tem diversas apliações em jogos e programas gráficos interativos, é se um ponto ou elemento geométrico está encostando ou sobreposto a outro. Esse tipo de problemas são por vezes chamados também de "detecção de colisões".

- O mouse está sobre o botão retangular?
- O ponto que se move neste jogo está sobre o círculo?
- Este elemento está dentro do polígono?
- O círculo encostou no triângulo?

As bibliotecas de simulação física respondem estas perguntas o tempo todo e não só as respondem como implementam sofisticados comportamentos resultantes das colisões simuladas entre objetos. Mas mesmo sem a complexidade adicional da simulação física, pra fazer sketches animados e interativos pode ser muito útil saber responder este tipo de perguntas. 

Uma referência inestimável de funções que respondem as principais perguntas de colisões entre formas é o site [www.jeffreythompson.org/collision-detection/](http://www.jeffreythompson.org/collision-detection/).

Vamos experimentar aqui mostrar alguns dos casos mais simples. Para casos mais complexos, pode ser útil também experimentar usar uma biblioteca especializada em processar geometrias 2D, como *shapely*

## Algumas implementações 

### Ponto e círculo

Um dos casos mais simples, saber se um ponto está em um círculo, pode ser resolvido calculando a distância do ponto ao centro do círculo e comparando essa distância com o raio do círculo (se a distância for menou ou igual ao raio, o ponto está dentro).

```python
# usando a função dist do py5
def point_in_circle(px, py, cx, cy, r):
    return dist(px, py, cx, cy) <= r
```

### Retângulo e retângulo

Esta funçao indica se há sobreposição entre dois retângulos descritos pelas coordenadas do canto superior esquerdo, largura e altura de cada um deles.

```python
def rect_in_area(xm, ym, wm, hm, xa, ya, wa, ha):
    return (xa < xm < xa + wa - wm and
            ya < ym < ya + ha - hm)

```

### Ponto e polígono

Um dos mais importantes problemas da geometria comptutacional, esta função, baseada em [Point Inclusion in Polygon Test](https://wrf.ecse.rpi.edu/Research/Short_Notes/pnpoly.html) de W. Randolph Franklin, recebe as coordenadas de um ponto e uma coleção de pontos (ou um iterável com tuplas de coordenadas, por exemplo).

```python
def point_in_poly(x, y, poly_pts):
    inside = False
    for i, p in enumerate(poly_pts):
        pp = poly_pts[i - 1]
        xi, yi = p
        xj, yj = pp
        intersect = ((yi > y) != (yj > y)) and (x < (xj - xi) * (y - yi) / (yj - yi) + xi)
        if intersect:
            inside = not inside
    return inside
```

Um sketch de demonstração da função.

![collision_point_poly](https://github.com/villares/material-aulas/assets/3694604/bf5f8efe-a6dd-4b73-a358-4d053c355565)


```python
poly_pts = ((100, 100), (200, 100), (150, 150), (200, 200), (100, 200))

def setup():
    size(400, 400)

def draw():
    if point_in_poly(mouse_x, mouse_y, poly_pts):
        fill(0, 200, 0)
    else:
        fill(255)    
    with begin_closed_shape():
        vertices(poly_pts)
    
def point_in_poly(x, y, poly_pts):
    inside = False
    for i, p in enumerate(poly_pts):
        pp = poly_pts[i - 1]
        xi, yi = p
        xj, yj = pp
        intersect = ((yi > y) != (yj > y)) and (x < (xj - xi) * (y - yi) / (yj - yi) + xi)
        if intersect:
            inside = not inside
    return inside
```


## Experimentando com *shapely*

Ponto em polígono usando o shapely

```python
import shapely

poly_pts = ((100, 100), (200, 100), (150, 150), (200, 200), (100, 200))
shapely_poly = shapely.Polygon(poly_pts)

def setup():
    size(400, 400)

def draw():
    shapely_point = shapely.Point(mouse_x, mouse_y)
    if shapely_poly.contains(shapely_point):
        fill(0, 200, 0)
    else:
        fill(255)
    
    with begin_closed_shape():
        vertices(poly_pts)
```





