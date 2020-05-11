## Arrastando círculos

![um círculo sendo arrastado](assets/arrastando_circulo.gif)

Neste exemplo vamos usar três funções que o Processing dispara pra nós em eventos do mouse (`mousePressed()`, `mouseReleased()` e `mouseDragged()`) para criar um elemento de interação interessante, um círculo que possa ser arrastado.

A ideia é que você possa adaptar este código para, por exemplo, arrastar pontos de controle de uma curva/polígono, ou então, outros 'elementos gráficos' do seu *sketch*. 

0. Vamos precisar de um indicador de estado (*flag*) parara saber se o arraste começou, para isso vamos usar a variável global `arrastando`, e vamos precisar também duas variáveis para a posição do círculo, `x_circulo` e `y_circulo`.

1. Dentro de `mousePressed()` vamos checar se o mouse está sobre o círculo. A estratégia escolhida foi usar a função `dist()` para comparar a distância do mouse até o centro do círculo com o raio do círculo (se a distância for menor que o raio, o mouse está sobre o círculo). Esse tipo de checagem é conhecida em programação de jogos e interfaces como "checagem de colisão".

    Neste caso estamos fazendo a checagem de colisão ponto-círculo (a posição do mouse é o ponto). Para outros casos, outros elementos gráficos, é preciso encontrar a estratégia de apropriada (veja por exemplo o exemplo do [botão simples](botao_simples.md) para ver como é uma checagem de colisão ponto-retângulo).

    Caso o mouse esteja dentro do círculo quando for apertado, mudamos `arrastando` de `False` para `True`.

2. Dentro de `mouseReleased()` vamos simplesmente mudar `arrastando` para `False`, isto é, sempre que um botão do mouse for solto vamos considerar que acaba qualquer gesto de arrastar o círculo que por ventura tem sido iniciado. Se não tinha nenhum gesto em andamento, nada muda.

3. Dentro de `mouseDragges()` caso o mouse seja movido apertado e o indicador `arrastando` seja `True`, vamos atualizar as variáveis globais `x_circulo` e `y_circulo` com o deslocamento do mouse neste evento de 'arraste' (*drag*). O deslocamento é obtido pela diferença da posição atual do mouse,`mouseX` e `mouseY`, para a posição imediatamente anterior (*previous*) que temos com`pmouseX` e `pmouseY`.

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
