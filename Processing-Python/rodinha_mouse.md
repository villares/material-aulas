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
    movimento_roda = event.getCount()
    global tamanho
    tamanho += movimento_roda
```
