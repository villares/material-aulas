# Uma função geradora (*generator*) 
## Devolve um objeto que produz tuplas de coordenadas

Neste exemplo, a parte central da construção da grade, os laços encaixados produzindo as coordenadas, foi encapsulada em uma função separada, a qual passamos um certo número de filas e colunas. Os dois últimos argumentos, opcionais, definem a largura da coluna e altura da fila.

Agora a grande diferença deste exemplo é que, se usarmos a palavra chave `yield` do Python no lugar de `return` dentro de um laço em uma função, isso produz uma *função geradora* que suspende a execução do laço a cada encontro com o `yield` e retorna em outro momento quando um novo item é pedido para o código que estava suspenso. A função, quando invocada não devolve um item ou mesmo uma lista de itens, devolve esse maquinário todo, na forma de um objeto gerador (ou *generator* em inglês) que pode ser iterado como uma lista (ou outro iterável qualquer).

Note que esse maquinário uma vez percorrido em um laço `for`, por exemplo, consumimndo os seus itens, é exaurido. Se você precisa iterar mais de uma vez pelos itens de um objeto gerador, pode convertê-lo primeiro em uma lista (para a qual você deve guardar uma referência, atribuindo a uma variável, por exemplo).

```python
def setup():
    size(400, 400)
    color_mode(HSB)

def draw():
    background(0)
    no_stroke()
    colunas, filas = 10, 10
    w_coluna = width / colunas # largura coluna
    h_fila =  height / filas  # altura fila
    for x, y in grid(colunas, filas, w_coluna, h_fila):
        # desenho do elemento em x, y
        d = 25 + 15 * cos(radians(x + y))
        matiz = 128 + 128 * sin(x - y)
        cor = color(matiz, 255, 200)
        fill(cor)
        circle(x + w_coluna / 2, y + h_fila / 2, d)


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
            # o yield no lugar de return muda tudo...
            yield (x * tam_col, y * tam_fil)

    # ...faz esta função como um todo devolver um objeto gerador que por sua vez vai
    # produzir os resultados conforme a necessidade, suspendendo a execução e depois
    # voltando. Podendo o objeto gerador ser consumido dentro de um loop, por exemplo.
```

### Assuntos relacionados

- [Cores com HSB (Matiz, Saturação e Brilho)](cores_HSB.md)


