# Uma função geradora (*generator*) que devolve tuplas de coordenadas

Em python, se usarmos a palavra chave `yield` no lugar de `return` dentro de um laço em uma função, isso produz um maquinário todo chamado * função geradora * que suspende a execução do laço a cada encontro com o `yield` e retorna quando um novo item é pedido para esse maquinário. A função, quando invocada não devolve um item ou mesmo uma lista de itens, devolve esse maquinário, na forma de um objeto gerador(ou * generator * em inglês) que pode ser iterado como uma lista(ou outro iterável qualquer).

A parte central da construção da grade, os laços encaixados produzindo as coordenadas, pode ser encapsulado em uma função separada. neste exemplo `grid()` devove um objeto que a cada iteração devolve uma tupla(x, y) de uma grade com um certo número de filas e colunas, os dois últimos argumentos, opcionais, definem a largura da coluna e altura da fila.

```python


def setup():
    size(400, 400)
    color_mode(HSB)


def draw():
    background(0)
    no_stroke()
    colunas, filas = 10, 10
    tam_coluna, tam_fila = width / colunas, height / \
        filas  # largura coluna, altura fila
    offset_x, offset_y = tam_coluna / 2., tam_fila / \
        2.  # deslocamento de meio tamanho
    for x, y in grid(colunas, filas, tam_coluna, tam_fila):
        # desenho do elemento em x, y
        s = 25 + 15 * cos(radians(x + y))
        h = 128 + 128 * sin(x - y)
        c = color(h, 255, 200)
        fill(c)
        ellipse(x + offset_x, y + offset_y, s, s)


def grid(colunas, filas, tam_col=1, tam_fil=1):
    """
    devolve um iterador que gera tuplas das coordenadas.
    exemplo de uso:
    #    for x, y in grid(10, 10, 12, 12):
    #        rect(x, y, 10, 10)
    """
    range_filas = range(int(filas))
    range_colunas = range(int(colunas))
    for y in range_filas:
        for x in range_colunas:
            # o yield no lugar de return muda tudo
            yield (x * tam_col, y * tam_fil)

    # faz essa função como um todo devolver um objeto gerador que por sua vez vai
    # produzindo os resultados conforme a necessidade. Dentro de um loop, por
    # exemplo.
```

![](assets/sketch_2020_04_12a.png)
