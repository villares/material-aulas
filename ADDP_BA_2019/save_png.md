# Como exportar uma imagem PNG

O código abaixo exemplifica como salvar uma imagem PNG de um frame. Quando uma tecla é pressionada, é executada a função `keyPressed()` e se for identificada a tecla "s" (`key == 's'`) é execuatada a função `saveFrame()`, que grava uma imagem na pasta do *sketch*.

## Um exemplo bem simples

![frame.png](/assets/frame.png)

```python
def setup():
    size(500, 500)

def draw():
    background(0, 0, 200)
    x, y = random(width), random(height)
    circle(x, y, 100)

def keyPressed():
    if key == 's':
        saveFrame("frame.png")
```

## Um exememplo um pouco mais longo

```python
def setup():
    global seed
    seed = int(random(1000))
    print(seed)
    size(500, 500)
    
def draw(): 
    randomSeed(seed)
    background(240, 240, 200)
    translate(250, 300)
    galho(60)
          
def galho(tamanho): # definição do galho/árvore
    ang = radians(mouseX)
    reducao = .8
    strokeWeight(tamanho / 10)
    line(0, 0, 0, -tamanho)
    if tamanho > 5:
        pushMatrix()
        translate(0, -tamanho)
        rotate(ang)
        galho(tamanho * reducao - random(0, 2))
        rotate(-ang * 2)
        galho(tamanho * reducao - random(0, 2))
        popMatrix()
          
def keyPressed(): # executada quando uma tecla for precinada
    if keyCode == LEFT:
         seed = seed - 1
    if keyCode == RIGHT:
         seed = seed + 1
    if key == ' ':  # barra de espaço precionada, sorteia nova "seed"
        seed = int(random(100000))
        print(seed)
    if key == 's':  # tecla "s" precionada, salva a imagem PNG
        nome_arquivo = 'arvore-s{}-a{}.png'.format(seed, mouseX % 360)
        saveFrame(nome_arquivo)
        print("Salvando PNG")
```
