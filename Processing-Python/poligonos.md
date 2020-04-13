# Desenhando polígonos


```pyde
def setup():
    size(500, 500)
    
def draw():
    strokeWeight(5)
    background(200, 0, 0)
    L, l = 150, 100
    M, m = L / 2, l / 2
    translate(200, 200)
    beginShape()
    vertex(-M, -M)
    vertex(-m,  0)
    vertex(-M, +M)
    vertex( 0, +m)
    vertex(+M, +M)
    vertex( m, 0)
    vertex(+M, -M)
    vertex( 0, -m)
    endShape(CLOSE)
```
