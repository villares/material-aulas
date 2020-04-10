# Transformando o sistema de coordenandas

Baseado em no tutorial [py.processing.org/tutorials/transform2d/](https://py.processing.org/tutorials/transform2d/)

### Um primeiro exemplo

Veja esta versão do código de uma função que desenha uma 'casinha' somando a posição `x, y` nas coordenadas dos objetos.

```pyde
def house(x, y):
    triangle(x + 15, y, x, y + 15, x + 30, y + 15)
    rect(x, y + 15, 30, 30)
    rect(x + 12, y + 30, 10, 15)

```

Compare agora com esta versão que usa o `translate()`. Neste caso o código desenha no mesmo lugar, no ponto (0, 0), e deixa a translação fazer o trabalho de mover o desenho para as coordenadas pedidas!

```pyde
def house(x, y):
    pushMatrix()
    translate(x, y)
    triangle(15, 0, 0, 15, 30, 15)
    rect(0, 15, 30, 30)
    rect(12, 30, 10, 15)
    popMatrix()

```

Note que para que isto funcione corretamente, é preciso usar `pushMatrix()` que 'guarda' o estado atual do sistema de coordenadas, e no final do desenho `popMatrix()`, que retoma o estado anterior.

