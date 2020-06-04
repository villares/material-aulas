## *Perlin noise*
#### Ruído de Perlin

```python
def setup():
    size(600, 400)
    # noLoop()
    
def draw():
    background(200)
    for x in range(width):
        # y = random(height)
        escala = 0.004
        print("escala:{}".format(escala))
        n = noise((mouseX + x) * escala)
        y = height * n
        line(x, height, x, height - y)
        
```

```python
        
### NOISE 2D
def draw():
    background(200)
    for x in range(width):
        # y = random(height)
        escala = 0.004
        print("escala:{}".format(escala))
        n = noise((mouseX + x) * escala,
                  mouseY * escala)
        y = height * n
        line(x, height, x, height - y)
```

##### Campo de ruído

```python
escala = 0.003
z = 0 
def setup():
    size(600, 400)
    stroke(255)
    colorMode(HSB)
    # noLoop()
    
def draw():
    background(0)
    for x in range(0, width, 10):
        for y in range(0, height, 10):
            n = noise((mouseX + x) * escala,
                     (mouseY + y) * escala,
                     z * escala)
            pushMatrix()
            translate(x, y)
            rotate(TWO_PI * n)
            line(-5, 0, 5, 0)
            popMatrix()
        
def keyPressed():
    global z
    if keyCode == UP:
        z +=1
    if keyCode == DOWN:
        z -=1
```



#### Noise 3D
 
```python

"""
Exemplo de Perlin Noise em três dimensões 
"""

perlinScale = 0.1
z = 0

def setup():
    size(500, 500)  # define o tamanho da tela em pixels. Largura X Altura
    noStroke()
    colorMode(HSB)

def draw():
    background(0)
    cols = 50
    tam = width / cols
    for x in range(cols):
        for y in range(cols):
            n = noise((mouseX + x) * perlinScale, (mouseY + y) * perlinScale, z * perlinScale)
            fill(240 * n, 255, 255)
            ellipse(tam / 2 + x * tam, tam / 2 + y * tam,
                    tam - tam * n, tam - tam * n)
            
def keyPressed():
    global z
    if keyCode == UP:
        z +=1
    if keyCode == DOWN:
        z -=1
```

