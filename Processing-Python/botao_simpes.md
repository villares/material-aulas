## Um botão simples


Aqui um exemplo de um botão muito simplificado, baicamente uma função que desenha um retângulo com texto e retorna `True` caso o mouse esteja apertado sobre ele (e `False` caso contrário).

```python
fundo = color(0)

def setup():
    size(400, 400)

def draw():
    background(fundo)
    global fundo
    bv = botao(100, 100, 200, 50, "vermelho")
    if bv:
        fundo = color(255, 0, 0)

    bp = botao(100, 250, 200, 50, "preto")
    if bp:
        fundo = color(0)

def botao(x, y, w, h, _text):
    mouse_over = (x < mouseX < x + w and
                  y < mouseY < y + h)
    if mouse_over:
        fill(140)
    else:
        fill(240)
    rect(x, y, w, h, 5)
    fill(0)
    textAlign(CENTER, CENTER)
    text(_text, x + w / 2, y + h / 2)
    if mouse_over and mousePressed:
        return True
    else:
        return False

    ```
