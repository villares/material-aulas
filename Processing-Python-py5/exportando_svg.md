# Exportando SVG

from java.io import file
muito semelhante a exportação de PDF, para salvar um arquivo vetorial SVG, é necessário adicionar uma biblioteca de exportação, que já vem com o processing, acrescentando esta linha no início do * sketch*:

``` python
add_library('svg')
```
isso pode ser feito manualmente ou pelo menu * sketch * do processing IDE:
***sketch > importar biblioteca > SVG export***

# Usando um objeto PGraphics

A estratégia mostrada a seguir permite mostrar na tela o desenho mas salvar um arquivo ajustes especiais, como por exemplo dimensões escaladas.

![SVG](assets/arquivo.svg)

```python
"""
tecle 'e' para salvar um único frame e encerrar o sketch
"""

add_library('svg')

save_frame = False
fator_escala = 3.78  # 255px -> ~255mm


def setup():
    global svg_output
    size(255, 255)
    svg_output = create_graphics(int(width * fator_escala),
                                 int(height * fator_escala),
                                 SVG, "arquivo.svg")


def draw():
    background(200)  # antes do beginRecord() não sairá no SVG

    if save_frame:
        begin_record(svg_output)
        svg_output.stroke_weight(.33)  # linha mais fina ainda!
        svg_output.scale(fator_escala)
        # svg_output.background(200)  # sem background, fundo transparente no
        # SVG

    # desenhando aqui, sai na tela e no arquivo
    fill(255, 0, 0, 100)
    rect(50, 50, 100, 100)
    fill(0, mouse_x, mouse_y, 100)
    rect(100, 100, 100, 100)

    if save_frame:
        end_record()  # encerra a gravação do arquivo
        exit()  # encerra o sketch


def key_pressed():
    global save_frame
    if key == 'e':
        save_frame = True


```

# Permitindo que a pessoa escolha onde salvar

```python

add_library('svg')

save_frame = False
fator_escala = 3


def setup():
    size(400, 400)


def draw():
    global save_frame
    if (save_frame):
        begin_record(output)
        output.scale(fator_escala)

    # Desenho aqui
    background(200, 255, 255)
    rect(100, 100, 100, 100)

    if save_frame:
        end_record()
        save_frame = False


def salva_svg(selection, ):
    if selection is None:
        print("Salvar cancelado.")
    else:
        print("Salvando em: " + selection.get_absolute_path())
        output = create_graphics(int(width * fator_escala),
                                 int(height * fator_escala),
                                 SVG, selection.get_absolute_path())
        save_frame = True


def key_pressed():
    if key == 's':
        sugestao = file("exemplo.svg")
        select_output("Salvar:", "salvaSVG", sugestao)


```

# Limitações

O que não funciona quando exportamos em SVG?

- `blend_mode(MULTIPLY)`ou qualquer outra variante de `blend_mode()` não tem efeito no SVG(só na tela).

# Exportação de desenho 3D em arquivos vetoriais 2D

é possível exportar a geometria 3D em si para arquivos DXF ou ainda outros formatos apropriados, assunto que não vamos tratar neste momento.

no exemplo a seguir mostramos como exportar desenhos tridimensionais em formato vetorial 2D, o que pode ser feito tanto em SVG como em PDF, usando `begin_raw()` e `end_raw()`.

O resultado, infelizmente,  é  bastante limitado, como pode ser visto abaixo:

![a](assets/3_da.svg) ![b](assets/3_db.svg)


```python
"""
tecle 'e' para salvar um único frame e encerrar o sketch
"""

add_library('svg')
# add_library('pdf')

save_frame = False


def setup():
    global output
    size(500, 500, P3D)  # P3D para denhar em 3D
    output = create_graphics(width, height, SVG, "3D.svg")
    # output = createGraphics(width, height, PDF, "3D.pdf")
    text_mode(SHAPE)


def draw():
    if save_frame:
        begin_raw(output)  # com P3D é preciso gravar 'cru'/raw

    background(200)
    fill(0)
    if mouse_pressed:
        hint(ENABLE_DEPTH_SORT)
        text("ENABLE_DEPTH_SORT", 20, 20)
    else:
        hint(DISABLE_DEPTH_SORT)
        text("DISABLE_DEPTH_SORT", 20, 20)

    # lights()  # não funciona na exportação :(
    translate(250, 250)
    rotate_y(frame_count / 100.)
    stroke(0)
    fill(0, 0, 200)
    box(100, 100, 100)
    translate(0, 0, 100)
    # fill(200, 0, 0, 100)
    fill(200, 0, 0)
    box(50)

    if save_frame:
        end_raw()  # encerra a gravação do arquivo
        exit()  # encerra o sketch


def key_pressed():
    global save_frame
    if key == 'e':
        save_frame = True


```

# Assuntos relacionados:

- [exportando PDF](exportando_pdf.md)
