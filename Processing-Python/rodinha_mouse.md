### Usando a rodinha do mouse (*mouse wheel*)

Um exemplo de como usar a rodinha do mouse para controlar o desenho, por meio da função `mouseWheel(event)`.

![rodinha](assets/rodinha_mouse.gif)

```python
tamanho = 100

def setup():
    size(400, 400)
    strokeWeight(3)
    
def draw():
    background(0, 0, 200)
    if tamanho > 0:
        fill(255)
    else:
        fill(200, 0, 0)
    rect(100, 100, tamanho, tamanho)
    textSize(20)
    text("tamanho: {}".format(tamanho), 100, 370)
    
def mouseWheel(event):
    global tamanho
    movimento_roda = event.getCount()
    tamanho += movimento_roda
```

### Um exemplo mais extenso

![rodinha](assets/rodinha_mouse_2.gif)

O exemplo a seguir amplia o código de [arrastar círculos](arrastando_circulos.md) visto anteriormente, permitindo mudar o tamanho de cada círculo girando a rodinha do mouse com o cursor sobre ele.

```python
arrastando = -1  # -1 quer dizer nenhum círculo sendo arrastado
circulos = []  # lista com coordenadas e tamanhos dos círculos
NUM_CIRCULOS = 6

def setup():
    size(400, 400)
    strokeWeight(3)
    colorMode(HSB)
    sorteia_circulos(NUM_CIRCULOS)

def draw():
    background(200)
    # Queremos uma lista invertida da enumeração dos círculo
    i_circulos = list(enumerate(circulos))[::-1]
    # De forma a desenhar a lista do último para o primeiro
    for i, circulo in i_circulos:  
        x, y, d = circulo
        if i == arrastando:
            stroke(0)
        else:
            stroke(255)
        fill(d - 15, 255, 255, 200)    
        ellipse(x, y, d, d)

def keyPressed():
    if key == ' ':
        sorteia_circulos(NUM_CIRCULOS)

def mousePressed():  # quando um botão do mouse é apertado
    global arrastando
    for i, circulo in enumerate(circulos):
        x, y, d = circulo
        dist_mouse_circulo = dist(mouseX, mouseY, x, y)
        raio = d / 2
        if  dist_mouse_circulo < raio:
            arrastando = i
            break  # encerra o laço
    
def mouseReleased():  # quando um botão do mouse é solto
    global arrastando
    arrastando = -1
    
def mouseDragged():  # quando o mouse é movido apertado
    if arrastando >= 0:
        x, y, d = circulos[arrastando]
        x += mouseX - pmouseX
        y += mouseY - pmouseY
        circulos[arrastando] = (x, y, d)
        
def mouseWheel(event):
    movimento_roda = event.getCount()
    for i, circulo in enumerate(circulos):
        x, y, d = circulo
        dist_mouse_circulo = dist(mouseX, mouseY, x, y)
        raio = d / 2
        if  dist_mouse_circulo < raio:
            d += movimento_roda
            # Limitar o tamanho possível dos círculos
            if 15 < d < 270:
                circulos[i] = (x, y, d)
            # sem `break` todos sob o mouse seriam afetados
            break  # interrompe o laço `for` 
        
def sorteia_circulos(num):
    circulos[:] = []  # esvazia a lista
    for _ in range(num):  # vamos sortear `num` círculos
        d = 128
        x = random(d / 2, width - d / 2)
        y = random(d / 2, height - d / 2)
        circulos.append((x, y, d))
```
