# Grades retangulares: filas e colunas de elementos

Para produzir uma grade retangular de elementos (filas e colunas) podemos utilizar laços de repetição 'encaixados' ou 'aninhados' (*nested*).

Vamos começar com uma fila de círculos:

```pyde
size(400, 40)
# deslocamento (offset) inicial: 20 - deslocamento horizontal de cada círculo: 40 
for x in range(20, 400, 40): # 10 números de 20 a 380, incluso, de 40 em 40
    ellipse(x, 20, 35, 35) # círculos de diâmetro 35
```

![](https://github.com/villares/material-aulas/blob/master/Processing-Python/assets/fila.png?raw=true)

Imagine que é possível escrever de forma parecida uma fila vertical, uma coluna de círculos... 

<details>
  <summary>clique para ver a resposta</summary>

```pyde
size(400, 400)
# deslocamento (offset) inicial: 20 - deslocamente vertical de cada círculo: 40 
for y in range(20, 400, 40): # 10 números de 20 a 380, incluso, de 40 em 40
    ellipse(20, y, 35, 35) # círculos de diâmetro 35
```
</details>

Em seguida, veremos que uma fila de colunas se torna uma grade de elementos:

```pyde
size(400, 400)
# deslocamento (offset) inicial: 20 - largura das colunas: 40 
for x in range(20, 400, 40): # 10 números de 20 a 380, de 40 em 40
  # deslocamento (offset) inicial: 20 - altura das filas: 40  
  for y in range(20, 400, 40): # 10 números de 20 a 380, de 40 em 40
    ellipse(x, y, 35, 35) # círculos de diâmetro 35
```

![](https://github.com/villares/material-aulas/blob/master/Processing-Python/assets/grade.png?raw=true)

É possível também fazer uma "coluna de filas", mudando só a ordem de desenho, mas não o resultado visual final.

Veja um exemplo, um pouco ampliado, em que a posição do elemento altera a cor e o tamanho:

```pyde
def setup():  
    size(400, 400)
    colorMode(HSB)

def draw():
    background(0)
    noStroke()
    colunas, filas = 10, 10    
    tam_coluna, tam_fila = width / colunas, height / filas  # largura coluna, altura fila
    offset_x, offset_y = tam_coluna / 2., tam_fila / 2.  # deslocamento de meio tamanho
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
![](https://github.com/villares/material-aulas/blob/master/Processing-Python/assets/sketch_2020_04_12b.png?raw=true)

### Usando um iterador (*iterator*) que devolve tuplas de coordenadas

A parte central da construção da grade, os laços encaixados produzindo as coordenadas, pode ser encapsulado em uma função separada. Neste exemplo `grid()` devove um objeto que a cada iteração devolve uma tupla (x, y) de uma grade com um certo número de filas e colunas, os dois últimos argumentos, opcionais, definem a largura da coluna e altura da fila.

```pyde
def setup():  
    size(400, 400)
    colorMode(HSB)

def draw():
    background(0)
    noStroke()
    colunas, filas = 10, 10    
    tam_coluna, tam_fila = width / colunas, height / filas  # largura coluna, altura fila
    offset_x, offset_y = tam_coluna / 2., tam_fila / 2.  # deslocamento de meio tamanho
    for x, y in grid(colunas, filas, tam_coluna, tam_fila):
        # desenho do elemento em x, y
        s = 25 + 15 * cos(radians(x + y))
        h = 128 + 128 * sin(x - y)
        c = color(h, 255, 200)
        fill(c)
        ellipse(x + offset_x, y + offset_y, s, s)

def grid(colunas, filas, tam_col=1, tam_fil=1):
    """
    Devolve um iterador que gera tuplas das coordenadas.
    Exemplo de uso:
    #    for x, y in grid(10, 10, 12, 12):
    #        rect(x, y, 10, 10)
    """
    range_filas = range(int(filas))
    range_colunas = range(int(colunas))
    for y in range_filas:
        for x in range_colunas:
            yield (x * tam_col, y * tam_fil)
```
![](https://github.com/villares/material-aulas/blob/master/Processing-Python/assets/sketch_2020_04_12a.png?raw=true)
