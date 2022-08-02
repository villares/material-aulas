# Mais sobre os atributos gráficos

esta página tenta ampliar um pouco o assundo dos atributos gráficos, que são os ajustes que podemos fazer nas formas que desenhamos, mencionados desde os[primeiros passos](https: // github.com/villares/material-aulas/blob/main/processing-python/desenho-basico_py.md) e também quando falamos[mais sobre as cores](https: // github.com/villares/material-aulas/blob/main/processing-python/mais_sobre_cores.md).

# Quais são os ajustes que podemos fazer nos atributos gráficos das formas
# que desennhamos?

- cor de preenchimento `fill()` ou não-preenchimento `no_fill()`, cor de traço `stroke()` e não-traço `no_stroke()`
- as cores podem ser indicadas como uma trinca de números de 0 a 255 (R, G, B) ou ainda com um quarto número que define o * alpha * ou opacidade(R, G, B, A) sendo que * alpha * 0 torna a cor totalmente transparente e 255 totalmente opaca. se usarmos `color_mode(HSB)` podemos indicar matiz(*hue*), saturação(*saturation*) e brilho(*brightness*), também com o quarto valor para o * alpha * opcional.
- espessura de traço `stroke_weight()` (não pode ser menor que zero!)
- junções e terminações dos traços [`stroke_join()`](https://py5.ixora.io/reference/sketch_stroke_join.html) e [`stroke_caps()`](https://py5.ixora.io/reference/sketch_stroke_cap.html)

# Preservando o estado atual dos atributos (fazendo modificações e depois
# voltando ao estado anterior)

as funções `push_style()` e `pop_style()` (ou `push()` e `pop()` que combinam os primeiros com `push_matrix`/`pop_matrix`) permitem alterar os atributos gráficos em uso para desenhar(dentro de uma função, por exemplo) e depois devolver os atributos ao que eram antes. desta forma, uma função pode usar uma cor específica e outra que é a corrente, sem perturbar a segunda.

# Lendo o estado atual dos atributos de cor "ativos"

uma carecterística pouco conhecida do processing é o objeto **`g`** que é no fundo a superfície de tela em que estamos desenhando. esse objeto mantém nos campos `.fill_color` e `.stroke_color` que podem ser consultados para saber as cores que estão atualmente em uso.

veja um exemplo de uso, uma função que desenha uma pequena seta cuja cabeça é um triângulo preenchido com a mesma cor 'atual' do traço(_stroke_).

```python


def seta_vetor(v, xo=0, yo=0):
    """
    desenhe uma seta representando um vetor v, partindo da origem (0, 0)
    ou na posição xo, yo informada como argumentos opcionais
    """
    body = v.mag()
    ang = v.heading()
    head_size = max(5, body / 5)
    xh = xo + cos(ang) * body
    yh = yo + sin(ang) * body
    line(xo, yo, xh, yh)  # corpo com tamanho fixo
    push()  # preserva os atributos gráficos atuais
    fill(g.stroke_color)  # usa a cor de traço como preenchimento!
    no_stroke()
    begin_shape()
    xha = xh + cos(ang + QUARTER_PI / 2 + PI) * head_size
    yha = yh + sin(ang + QUARTER_PI / 2 + PI) * head_size
    xhb = xh + cos(ang - QUARTER_PI / 2 + PI) * head_size
    yhb = yh + sin(ang - QUARTER_PI / 2 + PI) * head_size
    vertex(xha, yha)
    vertex(xh, yh)
    vertex(xhb, yhb)
    end_shape(CLOSE)
    pop()  # devolve os atributos ao que eram antes


```
