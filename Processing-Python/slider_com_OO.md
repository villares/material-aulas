# Ideias de orientação a objetos: um slider

### Como usar uma classe `Slider`

```python
from slider import Slider  # slider é o arquivo slider.py

def setup():
    global seed, t, a, ang
    seed = int(random(1000))
    print(seed)
    size(500, 500)
    t = Slider(10, 100, 50)
    t.position(10, 20)
    a = Slider(0, 360, 45)
    a.position(10, 60)
        
def draw():
    global ang
    randomSeed(seed)
    background(240, 240, 200)
    tamanho = t.value()
    ang = radians(a.value())
    translate(250, 300)
    galho(tamanho)   
     
def galho(tamanho):
    reducao = .8
    strokeWeight(tamanho / 10)
    line(0, 0, 0, -tamanho)
    if tamanho > 5:
        pushMatrix()
        translate(0, -tamanho)
        rotate(ang)
        # stroke(255, 0, 0)
        galho(tamanho * reducao - random(0, 2))
        rotate(-ang * 2)
        galho(tamanho * reducao - random(0, 2))
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
        self.clicked = False
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
        # draw label
        fill(0)
        textSize(10)
        textAlign(CENTER, CENTER)
        text(int(self.val), self.rectx, self.recty + self.h)
        # text label
        textAlign(LEFT, CENTER)
        text(self.label, self.x + self.w + self.h, self.y)
        popMatrix()
        popStyle()
        return self.val
```
