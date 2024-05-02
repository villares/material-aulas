# Tipografia

## Trabalhando com fontes e outros ajustes do texto

Usamos `text('Lorem Ipsum dolor', x, y)` para escrever um texto na área de desenho. O tamanho pode ser controlado, em pontos, por `text_size()`. O alinhamento pode ser alterado por `text_align()`. A cor vem do `fill()`.

## Exemplo básico

```python
"""
Adaptado do tutorial https://py.processing.org/tutorials/typography/
"""

x, y = 33, 60


def setup():
    size(100, 100)
    text_size(12)
    # pode ser usado LEFT, RIGHT no primeiro parâmetro e CENTER ou TOP no
    # segundo
    text_align(CENTER, BOTTOM)
    no_stroke()


def draw():
    global x, y
    fill(204, 120)
    rect(0, 0, width, height)
    fill(0)
    # Se o mouse estiver sobre o texto, mova!
    if (x <= mouse_x <= x + 55 and
        y - 24 <= mouse_y <= y):
        x += random(-2, 2)
        y += random(-2, 2)

    text('Cócegas', x, y)


```

## Definindo a fonte

Se não indicarmos alguma, uma fonte padrão será usada, mas podemos criar uma nova fonte `Py5Font` e usar em `text_font()`,
a partir de uma fonte já instalada ou de um arquivo vetorial **.ttf** ou **.otf**, usualmente na pasta `data`:

```python
# para ver as fontes instaladas no seu computador
for font_name in Py5Font.list():
    print(font_name)
# para usar a fonte Vera Sans Mono no estilo negrito
f = create_font("Bitstream Vera Sans Mono Bold", 24)
text_font(f)
```

Especialmente no caso de não termos permissão para distribuir o arquivo vetorial da fonte, podemos criar uma fonte bitmap a partir da original e distribuir este novo arquivo **.vlw**, criado usando a ferramenta **Tool > Create Font...** no Processing IDE, produzimos o arquivo da fonte que pode ser carregado da seguinte maneira:

```python
font = load_font("LetterGothicStd-32.vlw")
```

## Uma grade de letras, símbolos, glifos!

![grade](https://raw.githubusercontent.com/arteprog/programacao-criativa/master/assets/imagens/typogrid.png)

Baixe o arquivo descompactado ***.otf*** da fonte [Garoa Hacker Clube Bold](https://garoa.net.br/wiki/Fonte_Garoa_Hacker_Clube_Bold).

```python
glifos = "ABCDEFGHIJKLMNOPQRSTUVWXYZ☂#$*&"
num_glifos = len(glifos)
passo = 25

def setup():
    global f
    size(640, 360)
    background(0)
    # Copie a fonte GaroaHackerClubeBold.otf na pasta /data e substitua o
    # "FreeSans Bold" abaixo
    f = create_font("FreeSans Bold", 24)
    text_font(f)
    text_align(CENTER, CENTER)  # Alinhamento horizontal e vertical
    text_size(24)               # Tamanho do texto
    no_loop()    # Este exemplo inicialmente desliga a repetiçao do draw()...


def draw():
    background(0)
    for y in range(12, height - 12, passo):
        for x in range(12, width - 12, passo):
            sorteio = int(random(num_glifos))
            glifo = glifos[sorteio]
            if (glifo == 'A' or glifo == 'E' or glifo == 'I' or
                    glifo == 'O' or glifo == 'U'):
                fill(255, 0, 255)
            else:
                fill(0, 255, 0)

            # Desenha a letra na tela
            text(glifo, x, y)

def mouse_pressed():
    loop()

def mouse_released():
    no_loop()
```
É possível desenhar texto no modo `P3D` (veja mais sobre isso na página sobre [Desenho em 3D](desenho-3D.md) )
Este exemplo mostra 23 linhas na tela, e anima a rolagem (scroll) com o giro da [rodinha do mouse](rodinha_mouse.md).

```python
zen = """\
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one—and preferably only one—obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than * right * now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea—let's do more of those!\
"""
pos = 0


def setup():
    global zen_lines
    size(900, 600, P3D)
    text_font(create_font("Inconsolata Bold", 21))
    zen_lines = ["\n"] * 22 + zen.split('\n')


def draw():
    translate(0, 200, -60)
    rotate_x(QUARTER_PI / 2,)
    translate(0, -250)
    background(0, 0, 100)
    x, y, lh = 75, 27, 27
    shown_lines = zen_lines[pos:(pos+22)]
    for a_line in shown_lines:
        text(a_line, x, y)
        y += lh


def mouse_wheel(e):
    global pos
    pos += e.get_count()
 ```
![grade](assets/zen.gif)

## Sugestão de leitutra

- Tutoriais em:
    - https://processing.org/tutorials/typography/ (Java)
    - https://py.processing.org/tutorials/text/ (Python)
