# Manipulações avançadas da janela

os exemplos nesta página demonstram:
- um * sketch * em 'tela cheia'
- janela com dimensões calculadas
- redimensionando da janela no meio da execução
- uso avançado de mais de uma janela

# Tela cheia

se voce substituir a chamada de `size()` por `full_screen()` a janela do sketch toma toda a tela.

```python


def setup():
    full_screen()
    rect_mode(CENTER)


def draw():
    background(0)
    rect(width / 2, height / 2, width / 2, height / 2)


```

note que é possível também usar a tela cheia com a indicação do * renderer * (como `full_screen(P3D)` para desenho em 3D, por exemplo).

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

por questões de implementação do processing, não é recomendado usar variáveis nos argumentos do size, quando este está, como de costume, no `setup()` (as vezes até funciona!). A solução é usar uma função chamada `settings()` que se for definida, o processing chama, antes do `setup()`.

```python


def settings():
    img = load_image('arquivo.jpg')
    size(img.width, img.height)


def draw():
    background(img)


```
ou

```python


def settings():
    img = load_image('arquivo.jpg')
    size(img.width / 2, img.height / 2)


def draw():
    image(img, 0, 0, img.width / 2, img.height / 2)


```


# Mudando o tamanho da janela com o sketch em execução

é preciso chamar `this.surface.set_resizable(True)`, em geral no `setup()`, o que permite também que a pessoa redimensione manualmente a janela, e depois, é posível usar `this.surface.set_size(largura, altura)` para mudar as dimensões pelo código do próprio programa.

```python


def setup():
    size(400, 400)
    this.surface.set_resizable(True)


def draw():
    background(255)
    line(100, 100, width-100, height-100)


def key_pressed():
    this.surface.set_size(int(random(200, 500)),
                          int(random(200, 500)))


```

# Um *sketch* com duas janelas

```python


def setup():
    size(200, 300)
    second_window = other_window("2nd")


def draw():
    background(0)
    ellipse(mouse_x, mouse_y, 10, 10)


class other_window(Sketch):

    def __init__(self, title=""):
        switches = ('--sketch-path=' + sketch_path(), '')
        p_applet.run_sketch(switches, self)
        self.surface.set_title(title)

    def settings(self):
        self.size(300, 200)

    def draw(self):  # este é o draw pra a segunda janela
        self.background(255)
        self.fill(0)
        self.rect(self.mouse_x, self.mouse_y, 10, 10)


```
