# Mais sobre os atributos gráficos

Esta página tenta ampliar um pouco o assundo dos atributos gráficos, que são os ajustes que podemos fazer nas formas que desenhamos, mencionados desde os [primeiros passos](https://github.com/villares/material-aulas/blob/main/Processing-Python/desenho-basico_py.md) e também quando falamos [mais sobre as cores](https://github.com/villares/material-aulas/blob/main/Processing-Python/mais_sobre_cores.md).

### Quais são os ajustes que podemos fazer nos atributos gráficos das formas que desennhamos?

- Cor de preenchimento `fill()` ou não-preenchimento `noFill()`, cor de traço `stroke()` e não-traço `noStroke()`
    - As cores podem ser indicadas como uma trinca de números de 0 a 255 (R, G, B) ou ainda com um quarto número que define o *alpha* ou opacidade (R, G, B, A) sendo que *alpha* 0 torna a cor totalmente transparente e 255 totalmente opaca. Se usarmos `colorMode(HSB)` podemos indicar matiz (*hue*), saturação (*saturation*) e Brilho (*brightness*), também com o quarto valor para o *alpha* opcional.
- Espessura de traço `strokeWeight()` (não pode ser menor que zero!)
- Junções e terminações dos traços [`strokeJoin()`](https://py.processing.org/reference/strokeJoin.html) e [`strokeCaps()`](https://py.processing.org/reference/strokeCap.html)

### Preservando o estado atual dos atributos (fazendo modificações e depois voltando ao estado anterior)

As funções `pushStyle()` e `popStyle()` (ou `push()` e `pop()` que combinam os primeiros com `pushMatrix`/`popMatrix`) permitem alterar os atributos gráficos em uso para desenhar (dentro de uma função, por exemplo) e depois devolver os atributos ao que eram antes. Desta forma, uma função pode usar uma cor específica e outra que é a corrente, sem perturbar a segunda.

### Lendo o estado atual dos atributos de cor "ativos"

Uma carecterística pouco conhecida do Processing é o objeto **`g`** que é no fundo a superfície de tela em que estamos desenhando. Esse objeto mantém nos campos `.fillColor` e `.strokeColor` que podem ser consultados para saber as cores que estão atualmente em uso.

Veja um exemplo de uso, uma função que desenha uma pequena seta cuja cabeça é um triângulo preenchido com a mesma cor 'atual' do traço (_stroke_).

```python
def seta_vetor(v, xo=0, yo=0):
    """
    Desenhe uma seta representando um vetor v, partindo da origem (0, 0)
    ou na posição xo, yo informada como argumentos opcionais
    """
    body = v.mag()
    ang = v.heading()
    head_size = max(5, body / 5)
    xh = xo + cos(ang) * body
    yh = yo + sin(ang) * body
    line(xo, yo, xh, yh)  # corpo com tamanho fixo
    push()  # preserva os atributos gráficos atuais
    fill(g.strokeColor)  # usa a cor de traço como preenchimento!
    noStroke()
    beginShape()
    xha = xh + cos(ang + QUARTER_PI / 2 + PI) * head_size
    yha = yh + sin(ang + QUARTER_PI / 2 + PI) * head_size
    xhb = xh + cos(ang - QUARTER_PI / 2 + PI) * head_size
    yhb = yh + sin(ang - QUARTER_PI / 2 + PI) * head_size
    vertex(xha, yha)  
    vertex(xh, yh)
    vertex(xhb, yhb)
    endShape(CLOSE)
    pop()  # devolve os atributos ao que eram antes
```
