# Manipulações avançadas da janela

Os exemplos nesta página demonstram:
- Um *sketch* em 'tela cheia'
- Janela com dimensões calculadas
- Redimensionando da janela no meio da execução
<!--- Uso avançado de mais de uma janela -->

# Tela cheia

Se voce substituir a chamada de `size()` por `full_screen()` a janela do sketch toma toda a tela.

```python
def setup():
    full_screen()
    rect_mode(CENTER)

def draw():
    background(0)
    rect(width / 2, height / 2, width / 2, height / 2)
```

Note que é possível também usar a tela cheia com a indicação do * renderer * (como `full_screen(P3D)` para desenho em 3D, por exemplo).

```python
def setup():
    full_screen(P3D)

def draw():
    background(0)
    translate(width / 2, height / 2)
    rotate_y(frame_count / 100.0)
    box(height / 2)
```

# Variáveis no `size()`, usando `settings()`

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


# Mudando o tamanho da janela com o sketch em execução

Se você chamar `window_resizable(True)`, isso permite que as pessoas redimensionem manualmente a janela. Também é possível chamar `window_resize(largura, altura)` para mudar as dimensões pelo código do próprio programa. 

```python
def setup():
    size(400, 400)
    window_resizable(True)


def draw():
    background(255)
    line(100, 100, width-100, height-100)


def key_pressed():
    window_resize(int(random(200, 500)),
                  int(random(200, 500)))
```

<!---
# Um *sketch* com duas janelas

```python


def setup():
    size(200, 300)
    second_window = OtherWindow("2nd")


def draw():
    background(0)
    ellipse(mouse_x, mouse_y, 10, 10)


class OtherWindow(Sketch):

    def __init__(self, title=""):
        switches = ('--sketch-path=' + sketch_path(), '')
        PApplet.runSketch(switches, self)
        self.surface.set_title(title)

    def settings(self):
        self.size(300, 200)

    def draw(self):  # este é o draw pra a segunda janela
        self.background(255)
        self.fill(0)
        self.rect(self.mouse_x, self.mouse_y, 10, 10)


```
-->
