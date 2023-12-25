# Manipulações avançadas da janela

Os exemplos nesta página demonstram como executar um *sketch* em 'tela cheia', fazer uma janela com dimensões pré-calculadas permitir o redimensionando da janela no meio da execução, mover e redimenssionar a janela, e por fim um exemplo avançado de como criari mais de uma janela ao mesmo tempo.

## Tela cheia

Se voce substituir a chamada de `size()` por `full_screen()` a janela do sketch toma toda a tela.

```python
def setup():
    full_screen()
    rect_mode(CENTER)

def draw():
    background(0)
    rect(width / 2, height / 2, width / 2, height / 2)
```

Note que é possível também usar a tela cheia com a indicação do monitor, quando você tem mais de um monitor e o *renderer*, como `full_screen(P3D)` para desenho em 3D, por exemplo. Mais informações na documentação oficial de [`full_screen()`](https://py5coding.org/reference/sketch_full_screen.html).

```python
def setup():
    full_screen(P3D)

def draw():
    background(0)
    translate(width / 2, height / 2)
    rotate_y(frame_count / 100.0)
    box(height / 2)
```

## Variáveis no `size()`, usando `settings()`

Por questões de implementação do py5, e do Processing, não se deve usar variáveis nos argumentos do size, quando este está, como de costume, no `setup()`. A solução é usar uma função chamada `settings()` que se for definida, é executada antes do `setup()` e serve praticamente só para preparar a janela e o renderizador chamando `size()`.

```python
def settings():
    global img
    img = load_image('arquivo.jpg')
    size(img.width, img.height)

def draw():
    background(img)
```
ou

```python
def settings():
    global img
    img = load_image('arquivo.jpg')
    size(img.width / 2, img.height / 2)

def draw():
    image(img, 0, 0, img.width / 2, img.height / 2)
```

## Mudando o tamanho da janela com o *sketch* em execução

Se você chamar `window_resizable(True)`, isso permite que as pessoas redimensionem manualmente a janela. Também é possível chamar `window_resize(largura, altura)` para mudar as dimensões pelo código do próprio programa. A função `window_title()` permite mudar o texto-título da janela.


```python
def setup():
    size(400, 400)
    window_resizable(True)


def draw():
    background(255)
    line(100, 100, width - 100, height - 100)
    window_title(f'{width} x {height}')

def key_pressed():
    window_resize(int(random(200, 500)),
                  int(random(200, 500)))
```

![image](https://github.com/villares/material-aulas/assets/3694604/9464e498-c096-464b-b949-f34c75edabe5)
![image](https://github.com/villares/material-aulas/assets/3694604/81c7750f-d16a-4e6d-9e7b-cdf281ca4347)


## Mais possibilidades de manipulação da janela

### Desenho com proporções constantes

Este exemplo adaptado de [`window_ratio()`](https://py5coding.org/reference/sketch_window_ratio.html) mostra como fazer uma janela que pode ter o tamanho alterado, mas permite desenhar sempre na mesma proporção. Note o como o texto escala automaticamente, e uma posição do mouse "relativa" à proporção indicada pode ser obtida com `rmousex` e `rmousey`.

```python
def setup():
  size(400, 400)
  window_resizable(True)
  window_ratio(1280, 720)

  cursor(CROSS)
  stroke_weight(10)


def draw():
  background(255, 0, 0)
  fill(255)
  rect(0, 0, rwidth, rheight)

  fill(0)
  text_align(CENTER, CENTER)
  x, y = rwidth / 2, rheight / 2
  text_size(150)
  text(f'{rmouse_x}, {rmouse_y}', x, y - 150)
  text_size(70)
  text(f'sobra vertical:{int(ratio_top)}\n'
       f'sobra horizontal: {int(ratio_left)}\n'
       f'escala :{round(ratio_scale, 3)}', x, y + 100)
```

### Consultando e alterando a posição da janela na tela

É possivel consultar a posição da janela com `window_x` e `window_y` e movê-la com `window_move()`

## Um *sketch* com duas janelas

Esta técnica, que parte da infraestrutura para executar mais de um sketch simultaneamente, precisa do chamado [*class mode*](http://py5coding.org/content/py5_modes.html#class-mode). É provável que que este exemplo não funcione no Thonny no MacOS, mas deve funcionar usando Jupyter Notebooks no Mac. Agradeço quem puder comentar mais sobre isso (pode abrir uma issue).

```python
from py5 import Sketch

class SketchySketch(Sketch):
    def __init__(self, title="", other=None):
        self.other = other
        self.title = title
        self.clicked = False
        super().__init__()        

    def settings(self):
        self.size(300, 200)

    def setup(self):
        self.window_resizable(True)
        if self.title:
            self.window_title(self.title)
        if self.other:
            self.other.other = self

    def draw(self): 
        if self.title == 'A':
            self.background(255)
            self.fill(0)
        else:
            self.background(0)
            self.fill(255)
        self.rect(self.mouse_x, self.mouse_y, 10, 10)
        
        if self.clicked:
            w, h = self.width, self.height
            self.fill(128, 128)
            self.circle(w / 2, h / 2, min(w, h) * 0.8)
            
    def mouse_pressed(self):
        self.clicked = not self.clicked
        if self.other:
            self.other.clicked = self.clicked

a = SketchySketch('A')
a.run_sketch(block=False)
b = SketchySketch('B', a)
b.run_sketch(block=False)
```

![sketch_2022_09_05](https://user-images.githubusercontent.com/3694604/188527096-acefba92-7f85-4b20-9804-2392fa7f4d31.png)

