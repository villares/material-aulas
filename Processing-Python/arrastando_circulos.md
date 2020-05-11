## Arrastando círculo

Neste exemplo vamos usar três funções disparadas por eventos do mouse (`mousePressed()`, `mouseReleased()` e `mouseDragged`) para criar um elemento de interação muito interessante, um círculo que pode ser arrastado.

Você pode adaptar este código para arrastar, por exemplo pontos de controle de uma curva ou polígono, ou outros 'elementos gráficos' no seu sketch. 

Vamos precisar de um indicador de estado (*flag*) parara saber se o arraste começou, para isso vamos usar a variável global `arrastando`, e vamos precisar também atualizar a posição do círculo nas variáveis `x_circulo` e `y_circulo`.

```python
arrastando = False
x_circulo, y_circulo = 150, 150
D_CIRCULO = 100 # diâmetro do círculo

def setup():
    size(400, 400)
    strokeWeight(3)
    fill(0)

def draw():
    background(0, 0, 200)
    if arrastando:
        stroke(200, 0, 0)
    else:
        stroke(255)
    ellipse(x_circulo, y_circulo, D_CIRCULO, D_CIRCULO)

def mousePressed():  # quando um botão do mouse é apertado
    global arrastando
    dist_mouse_circulo = dist(mouseX, mouseY, x_circulo, y_circulo)
    raio = D_CIRCULO / 2
    if  dist_mouse_circulo < raio:
        arrastando = True

    
def mouseReleased():  # quando um botão do mouse é solto
    global arrastando
    arrastando = False
    
def mouseDragged():  # quando o mouse é movido apertado
    global x_circulo, y_circulo
    if arrastando:
        # mouseX - pmouseX é o que o mouse foi arrastado em X
        x_circulo += mouseX - pmouseX
        # mouseY - pmouseY é o que o mouse foi arrastado em Y
        y_circulo += mouseY - pmouseY    
```
