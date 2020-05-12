### Usando a rodinha do mouse (*mouse wheel*)

Um exemplo de como usar a rodinha do mouse para controlar o desenho, por meio da função `mouseWheel(event)`.

```python
tamanho = 50

def setup():
    size(500, 500)
    
def draw():
    background(200)
    if tamanho > 0:
        fill(0, 0, 200)
    else:
        fill(200, 0, 0)
    square(width / 2, height / 2, tamanho)
    
def mouseWheel(event):
    movimento_roda = event.getCount()
    global tamanho
    tamanho += movimento_roda
```
