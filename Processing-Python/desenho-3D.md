# Como desenhar em 3D

## Primeiros passos

Para começar, dentro do `setup()` é preciso usar o argumento `P3D` em `size()`, como neste exemplo:

```python
def setup():
    size(500, 500, P3D)
```

Passa então a ser possivel modificar o sistema de coordenadas com `translate(x, y, z)` (agora com **z**) e `rotateX()`, `rotateY()` e `rotateZ()` (que giram em torno dos eixos). 

Desta maneira é possível desenhar os mesmos elementos 2D que utilizamos até agora, porém deslocados e girados no espaço. Mas além dessa estratégia, também acontecem as seguintes mudanças:

- Linhas podem receber coordenadas 3D: `line(x1, y1, z1, x2, y2, z2)`

- Os elementos `PShape` criados com `beginShape()/endShape()` passam a poder ser desenhados no espaço, usando, por exemplo, `vertex(x, y, z)`.

- A função `box(w, h, d)` desenha um paralelepípedo, ou um cubo com `box(side)`, sempre na origem (0, 0, 0) do sistema de coordenadas, sendo então em geral acompanhada de uma estrutura com `pushMatrix()`/`popMatrix()` e `translate(x, y, z)` para que seja posicionada no lugar desejado.


### Um exemplo com objetos desenhados em 3D

```python
    
def setup():
    size(500, 500, P3D)
    rectMode(CENTER)
    
def draw():
    background(200)
    lights()
    translate(width / 2, height / 2)
    rotateX(radians(frameCount))
    stroke(255)
    fill(0, 200, 0)
    caixa(50, 50, 0, 20, 100, 50)
    fill(255, 0, 0)
    caixa(20, 20, -20, 20)
    fill(0, 0, 200)
    caixa(0, 20, 20, 20)
    stroke(0)
    line(0, 0, 0, 50, 50, 100)
    
    beginShape()
    vertex(0, 0, 0)
    vertex(100, 100, 100)
    vertex(100, -100, 50)
    endShape(CLOSE)
    
    # rotateY(QUARTER_PI + radians(frameCount))    
    translate(0, 0, 100)
    fill(255)
    rect(0, 0, 100, 100)    

def caixa(x, y, z, *tam):
    pushMatrix()
    translate(x, y, z)
    box(*tam)
    popMatrix()       
                                    
```

### Exemplo de caixa com furos (e outros)

https://github.com/villares/Paper-objects-with-Processing-and-Python

### Barra em 3D, orbit com PeasyCam

```python
add_library('peasycam')  # é preciso baixar/instalar pelo IDE

def setup():
    size(500, 500, P3D)
    cam = PeasyCam(this, 100)
    cam.setMinimumDistance(100)
    cam.setMaximumDistance(200)
    
def draw():
    background(200)
    bar(0, 0, 0, 20, 10, 30, 3)
    bar(50, 30, -30, 20, 10, 30, 3)
    bar(0, 0, 0, 50, 30, -30, 3)

def bar(x1, y1, z1, x2, y2, z2, weight=10):
    """Draw a box rotated in 3D like a bar/edge."""
    p1, p2 = PVector(x1, y1, z1), PVector(x2, y2, z2)
    v1 = p2 - p1
    rho = sqrt(v1.x ** 2 + v1.y ** 2 + v1.z ** 2)
    phi, the  = acos(v1.z / rho), atan2(v1.y, v1.x)
    v1.mult(0.5)
    pushMatrix()
    translate(x1 + v1.x, y1 + v1.y, z1 + v1.z)
    rotateZ(the)
    rotateY(phi)
    box(weight, weight, p1.dist(p2))
    popMatrix()
```

