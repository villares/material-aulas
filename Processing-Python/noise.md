## *Perlin noise*

### Ruído de Perlin

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

#### Noise 3D
https://github.com/villares/py.processing-play/blob/master/perlinNoise/perlinNoise.pyde

##### campo

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
