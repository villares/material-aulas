# workshop 2019 de outubro - Senac

> Desenhos interativos com Processing Modo Python!

### Processing? Python? Sim!

Como instalar: https://abav.lugaralgum.com/como-instalar-o-processing-modo-python/
Outros exemplos do Alexandre: https://abav.lugaralgum.com/sketch-a-day

```python
h = 10
vh = 1
tam = 200
cor_fundo = color(200, 0, 200)

def setup():   # configuração inicial
    size(500, 500)  # tamanho da área de desenho

def draw():  # desenho do frame
    global h, vh
    background(cor_fundo)
    olho(h, 200, tam)
    olho(h + 100, 300, 50)
    # olho(h, mouseY, random(20, 100))

    h = h + vh
    if h > width:
        vh = -vh
    if h < -100:
        vh = -vh
    # print(h)

def keyPressed():
    global tam, cor_fundo
    if key == 'a':
        tam += 10 # tam = tam + 10
    if key == 'z':
        tam -= 10 # tam = tam - 10  
    if key == 'f':
        cor_fundo = color(random(255),
                          random(255), 
                          random(255))
    if key == 'p':
        saveFrame("olhos####.png")        

def olho(x, y, tamanho):
    metade = tamanho / 2
    noStroke()
    fill(255)
    ellipse(x, y, tamanho, metade)
    fill(255, 0, 0)
    circle(x, y, metade)
    fill(0)
    circle(x, y, metade / 3)
```

