# Ideias de orientação a objetos: um slider

### Como usar uma classe `Slider`

```python
from __future__ import unicode_literals
from slider import Slider  # slider é o arquivo slider.py


def setup():
    global s1, s2, s3
    global seed
    seed = int(random(1000))
    print(seed)
    size(500, 500)
    s1 = Slider(0, 90, 50, 'tamanho')
    s1.position(20, 30)
    s2 = Slider(0, 180, 45, 'ângulo')
    s2.position(190, 30)
    s3 = Slider(0, 10, 0, 'variação aleatória')
    s3.position(360, 30)    
                
def draw():
    global angulo, rndvar
    randomSeed(seed)
    background(240, 240, 200)
    
    tamanho = s1.update()
    angulo = radians(s2.update())
    rndvar = s3.update() / 10

    translate(250, 440)
    galho(tamanho)   
     
def galho(tamanho):
    reducao = 0.75
    sw = tamanho / 10
    strokeWeight(sw)
    line(0, 0, 0, -tamanho)
    if tamanho > 5:
        pushMatrix()
        translate(0, -tamanho)
        rotate(angulo)
        galho(tamanho * reducao - random(-sw, sw) * rndvar)
        rotate(-angulo * 2)
        galho(tamanho * reducao - random(-sw, sw) * rndvar)
        popMatrix()
 ```
        
 ### Como é a classe `Slider` por dentro?       
 
Uma aba **slider** é um arquivo `slider.py`
        
```python
class Slider:

    def __init__(self, low, high, default):
        """
        slider has range from low to high
        and is set to default
        """
        self.low = low
        self.high = high
        self.val = default
        self.label = ''  # blank label
        self.w, self.h = 120, 20

    def position(self, x, y):
        """slider's position on screen"""
        self.x = x
        self.y = y
        # the position of the rect you slide:
        self.rectx = self.x + map(self.val, self.low, self.high, 0, self.w)
        self.recty = self.y

    def value(self):
        """updates the slider and returns value"""
        pushStyle()
        pushMatrix()
        resetMatrix()
        rectMode(CENTER)
        # gray line behind slider
        strokeWeight(4)
        stroke(200)
        line(self.x, self.y, self.x + 120, self.y)
        # press mouse to move slider
        if mousePressed and dist(mouseX, mouseY, self.rectx, self.recty) < self.h:
            self.rectx = mouseX
        # constrain rectangle
        self.rectx = constrain(self.rectx, self.x, self.x + self.w)
        # draw rectangle
        strokeWeight(1)
        stroke(0)
        fill(255)
        rect(self.rectx, self.recty, self.w / 12, self.h)
        self.val = map(
            self.rectx, self.x, self.x + self.w, self.low, self.high)
        # draw value
        fill(0)
        textSize(10)
        textAlign(CENTER, CENTER)
        text(int(self.val), self.rectx, self.recty + self.h)
        # text label
        text(self.label, self.x + self.w / 2, self.y - self.h)
        popMatrix()
        popStyle()
        return self.val
```
