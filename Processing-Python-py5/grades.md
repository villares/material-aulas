# Grades retangulares: filas e colunas de elementos

para produzir uma grade retangular de elementos(filas e colunas) podemos utilizar laços de repetição 'encaixados' ou 'aninhados' (*nested*).

vamos começar com uma fila de círculos:

```python
size(400, 40)
# deslocamento (offset) inicial: 20 - deslocamento horizontal de cada
# círculo: 40
for x in range(20, 400, 40):  # 10 números de 20 a 380, incluso, de 40 em 40
    ellipse(x, 20, 35, 35)  # círculos de diâmetro 35
```

![](assets/fila.png)

imagine que é possível escrever de forma parecida uma fila vertical, uma coluna de círculos...

    
<!-- summary> pense em como você escreveria o código e depois clique para a resposta </summary -->

```python
size(400, 400)
# deslocamento (offset) inicial: 20 - deslocamente vertical de cada círculo: 40
for y in range(20, 400, 40):  # 10 números de 20 a 380, incluso, de 40 em 40
    ellipse(20, y, 35, 35)  # círculos de diâmetro 35
```

Em seguida, veremos que uma fila de colunas se torna uma grade de elementos:

```python
size(400, 400)
# deslocamento (offset) inicial: 20 - largura das colunas: 40
for x in range(20, 400, 40):  # 10 números de 20 a 380, de 40 em 40
    # deslocamento (offset) inicial: 20 - altura das filas: 40
    for y in range(20, 400, 40):  # 10 números de 20 a 380, de 40 em 40
        ellipse(x, y, 35, 35)  # círculos de diâmetro 35
```

![](assets/grade.png)

É possível também fazer uma "coluna de filas", mudando só a ordem de desenho, mas não o resultado visual final. Veja um exemplo, um pouco ampliado, em que a posição do elemento altera a cor e o tamanho:

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
    for i in range(colunas):
        x = i * tam_coluna + offset_x
        for j in range(filas):
            y = j * tam_coluna + offset_y
            # desenho do elemento em x, y
            s = 10 + i + j
            h = (x + y) % 256
            c = color(h, 255, 200)
            fill(c)
            ellipse(x, y, s, s)
```

![](assets/sketch_2020_04_12b.png)

# Assuntos relacionados

- [Sequências e laços de repetição](lacos_py.md)
- [Cores com HSB(matiz, saturação e brilho)](cores_hsb.md)
- [Uma grade usando uma função geradora](grades2.md)
