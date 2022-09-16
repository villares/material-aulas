# Mais sobre os atributos gráficos

Esta página tenta ampliar um pouco o assundo dos atributos gráficos, que são os ajustes que podemos fazer nas formas que desenhamos, mencionados desde os[primeiros passos](https://github.com/villares/material-aulas/blob/main/Processing-Python/desenho-basico_py.md) e também quando falamos[mais sobre as cores](https://github.com/villares/material-aulas/blob/main/Processing-Python/mais_sobre_cores.md).

## Quais são os ajustes que podemos fazer nos atributos gráficos das formas que desenhamos?

- Cor de preenchimento `fill()` ou não-preenchimento `no_fill()`, cor de traço `stroke()` e não-traço `no_stroke()`
- As cores podem ser indicadas como uma trinca de números de 0 a 255 (R, G, B) ou ainda com um quarto número que define o * alpha * ou opacidade(R, G, B, A) sendo que * alpha * 0 torna a cor totalmente transparente e 255 totalmente opaca. Se usarmos `color_mode(HSB)` podemos indicar matiz(*hue*), saturação(*saturation*) e Brilho(*brightness*), também com o quarto valor para o * alpha * opcional.
- Espessura de traço `stroke_weight()` (não pode ser menor que zero!)
- Junções e terminações dos traços[`stroke_join()`](https://py5coding.org/reference/sketch_stroke_join.html) e[`stroke_caps()`](https://py5coding.org/reference/sketch_stroke_cap.html)

## Preservando o estado atual dos atributos (fazendo modificações e depois voltando ao estado anterior)

As funções `push_style()` e `pop_style()` (ou `push()` e `pop()` que combinam os primeiros com `push_matrix`/`pop_matrix`) permitem alterar os atributos gráficos em uso para desenhar(dentro de uma função, por exemplo) e depois devolver os atributos ao que eram antes. Desta forma, uma função pode usar uma cor específica e outra que é a corrente, sem perturbar a segunda.

## Lendo o estado atual dos atributos de cor "ativos"

Uma carecterística pouco conhecida do Processing é o objeto **`g`** que é no fundo a superfície de tela em que estamos desenhando. Podemos consultar `._instance.fillColor` e `._instance.strokeColor` para saber as cores que estão atualmente em uso.

Veja um exemplo de uso, uma função que desenha uma pequena seta cuja cabeça é um triângulo preenchido com a mesma cor 'atual' do traço(_stroke_).

```python
def setup():
    size(400, 400)
    seta_vetor((100, 100), (200, 200))


def setup():
    size(400, 400)
    stroke(0, 150, 0)
    seta_vetor((100, 100), (200, 200))

def seta_vetor(v, origin=(0, 0), head_size=10):
    """
    Desenhe uma seta representando um vetor `v`, partindo da origem (0, 0)
    ou na posição informada com o argumentos opcional `origin`.
    """
    v = Py5Vector(*v)
    body = v.mag
    head_size = min(head_size, body / 2)
    xo, yo = origin
    xh = xo + v.x
    yh = yo + v.y
    ang = v.heading
    xha = xh + cos(ang + QUARTER_PI / 2 + PI) * head_size
    yha = yh + sin(ang + QUARTER_PI / 2 + PI) * head_size
    xhb = xh + cos(ang - QUARTER_PI / 2 + PI) * head_size
    yhb = yh + sin(ang - QUARTER_PI / 2 + PI) * head_size
    line(xo, yo, xh, yh)  # corpo com tamanho fixo
    with push():  # preserva os atributos gráficos atuais
        fill(g._instance.strokeColor)  # usa a cor de traço como preenchimento!
        no_stroke()
        with begin_closed_shape():
            vertex(xha, yha)
            vertex(xh, yh)
            vertex(xhb, yhb)
            end_shape(CLOSE)
```
