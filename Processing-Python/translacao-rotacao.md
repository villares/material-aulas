# Transformando o sistema de coordenandas

Baseado no tutorial [py.processing.org/tutorials/transform2d/](https://py.processing.org/tutorials/transform2d/)

## Um primeiro exemplo de `translate()`

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

Note que para que funcione corretamente, é preciso usar `pushMatrix()`, que 'guarda' o estado atual do sistema de coordenadas, e no final do desenho `popMatrix()`, que retoma o estado anterior. O motivo é por conta do efeito de `translate()` ser cumulativo, um novo translate altera as coordenadas deslocando em relação a origem atual, o que pode ser indesejado. É preciso o cuidado de parear cada `pushMatrix()` com um `popMatrix()` equivalente ao final das etapas de desenho.

Saiba que ao final da execução do `draw()`, um frame do Processing, o sistema de coordenadas original é restaurado. E isso pode ser feito a qualquer momento também com `resetMatrix()`. 

## Rotação com `rotate()`

Além da translação que move a grade, é possível girar o sistema de coordenadas com a função `rotate()` com um ângulo em radianos. A função gira o sistema de coordenadas em torno da origem (0, 0) corrente, e por conta disso é em geral usada após e em conjunto com `pushMatrix()`, `translate()`, e sendo seguida por `popMatrix()` ao final do desenho.
