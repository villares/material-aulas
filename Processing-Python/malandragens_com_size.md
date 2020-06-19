## Manipulações avançadas da janela

### Tela cheia, janela com o tamanho calculado, e redimensionando a janela no meio do caminho

#### Tela cheia

Se voce substituir a chamada de `size(..., ...)` por `fullScreen()` a janela do sketch toma toda a tela. É possível também usar com a indicação do *renderer* (como `fullScreen(P3D)` para desenho em 3D, por exemplo).

```
def setup():
    fullScreen(P3D)

def draw():
    background(0)
    translate(width / 2, height / 2)
    rotateY(frameCount / 10.)
    fill(255, 200, 200)
    box(200)
```


#### Variáveis no `size()`, usando `settings()`

Por questões de implementação do Processing, não é possível usar variáveis nos argumentos do size, quando este está, como de costume, no `setup()`. A solução é usar uma função chamada `settings()` que se for definida, o Processing chama, antes do `setup()`.

```python
def settings():
    img = loadImage('arquivo.jpg')
    size(img.width, img.height)
 
def draw():
    background(img) 
```
ou 

```python
def settings():
    img = loadImage('arquivo.jpg')
    size(img.width / 2, img.height / 2)
 
def draw():
    image(img, 0, 0, img.width / 2, img.height / 2) 
```


#### Mudando o tamanho da janela com o sketch executando

É preciso chamar `this.surface.setResizable(True)`, em geral no `setup()` e depois é posível usar `this.surface.setSize(largura, altura)`.

```python
def setup():
  size(400, 400);
  this.surface.setResizable(True)

def draw() :
  background(255);
  line(100, 100, width-100, height-100)

def keyPressed():
  this.surface.setSize(int(random(200, 500)),
                       int(random(200, 500)))
```

