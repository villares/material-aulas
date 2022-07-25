# O que é indentação?

A palavra * indentação * também significa  'recuo',  veja este exemplo de uma lista de compras relativamente organizada:

```
comes:
    pão
    cebola
    abacate
    alho

bebes:
    chá mate
    sucos:
        maçã
        uva
        laranja
    refrigerantes:
        água tônica
```
O espaço que faz os itens ficarem 'dentro' das categorias é a * indentação*. exatamente da mesma maneira, em python, criamos blocos de código que estão 'dentro' de estruturas. note os dois pontos(`: `) antes de um bloco indentado na lista de compras.

essa sintaxe com o espaço de indentação, e com `: `, vai ser usada em inúmeras estruturas de python, como `if`/`elif`/`else`,  nos laços de repetição `for` e `while`, na definição de novas funções com `def`, entre outras.

# Animando uma estrela com o movimento do mouse

vamos ver agora um exemplo que precisa de indentação, avançando um pouco em ideias cujos detalhes você pode retomar depois na página sobre[movimento](movimento_py.md).

# A função `setup()` e a função `draw()`

podemos reorganizar o código anterior mostrado no[primeiro contato com polígonos](poligonos_1.md) colocando os ajustes iniciais(*setup*), como  `size(200, 200)`, dentro da definição de função `def setup(): `, e a parte que desenha(*draw*) dentro de `def draw(): `.

A função `setup()` vai ser executada apenas uma vez no começo, e a função `draw()` fica repetindo sem parar, permitindo o movimento. repare como a indentação é o que determina  o que está dentro de cada função.

```python


def setup():
    size(400, 400)


def draw():
    background(0, 0, 200)  # para limpar a área de desenho
    x, y = width / 2, height / 2  # coordenadas do centro

    a = mouse_x / 4
    b = mouse_y / 4

    begin_shape()
    vertex(x - a, y - a)
    vertex(x - b, y)
    vertex(x - a, y + a)
    vertex(x, y + b)
    vertex(x + a, y + a)
    vertex(x + b, y)
    vertex(x + a, y - a)
    vertex(x, y - b)
    end_shape(CLOSE)


```

<div id = "iframe_DIV" > <img src = "assets/estrela_indentacao.gif" > </div >

<a id = "iframe_A" href = "https://abav.lugaralgum.com/material-aulas/Processing-Python/assets/indentacao/" > veja o resultado aqui < /a >

# Assuntos relacionados

- mais sobre[animações com `setup()` e `draw()`](movimento_py.md)
- estrelas de muitas pontas com[laços de repetição `while`](https: // github.com/villares/material-aulas/blob/master/processing-python/while.md)
- você pode ver usos mais avançados de `begin_shape()` na[referência](https: // py.processing.org/reference/begin_shape.html).
- você pode montar os vértices a partir de[estruturas de dados com laços de repetição ou fazer polígonos com furos](https: // github.com/villares/material-aulas/blob/master/processing-python/poligonos_2.md)
