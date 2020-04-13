# Grades

Para produzir uma grade retangular de elementos (filas e colunas) podemos utilizar laços de repetição 'encaixados' ou 'aninhados' (*nested*).

```pyde
def setup():  
    size(400, 400)
    colorMode(HSB)

def draw():
    background(0)
    noStroke()
    colunas, filas = 10, 10    
    tam_coluna, tam_fila = width / colunas, height / filas
    offset_x, offset_y = tam_coluna / 2., tam_fila / 2. 
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

### Usando um iterador (*iterator*) que devolve tuplas de coordenadas

A parte central da construção da grade, os laços encaixados produzindo as coordenadas, pode ser encapsulado em uma função separada. Neste exemplo `grid()` a cada iteração devolve uma tupla (x, y) de uma grade com um certo número de filas e colunas, os dois últimos argumentos, opcionais, definem a largura da coluna e altura da fila.

```pyde
def setup():  
    size(400, 400)
    colorMode(HSB)

def draw():
    background(0)
    noStroke()
    offset_x, offset_y = 20, 20 
    for x, y in grid(10, 10, 40, 40):
        s = 25 + 15 * cos(radians(x + y))
        h = 128 + 128 * sin(x - y)
        c = color(h, 255, 200)
        fill(c)
        ellipse(x + offset_x, y + offset_y, s, s)

def grid(colunas, filas, tam_col=1, tam_fil=1):
    """
    Devolve um iterator tuplas das coordenadas.
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
