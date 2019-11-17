# Transformação do sistema de coordenadas

## Eixos X e Y

Ao iniciar um *sketch* com o sistema de coordenadas padrão, podemos identificar no 
Processing os eixos X e Y com origem (zero) no canto superior esquerdo da tela. O eixo X tem seus valores positivos crescendo em direção ao lado direito da tela, já o eixo Y cresce com valors positivos em direção à parte de baixo da tela, resultando em algo como:

![Coordenadas X e Y](assets/coordenadas.jpg)

## translate(x, y)

É possível alterar a posição de origem dos eixos, coordenadas (0, 0), utilizando `translate(x, y)` onde os argumentos (y, y) indicam as coordenadas atuais que se tornarão o novo (0, 0).

É importante entender que o efeito do `translate()` é cumulativo, um novo translate altera as coordenadas da origem a deslocando em relação a origem atual, e isso pode ser indesejado.

Mas saiba também que ao final da execução do `draw()`, um frame do Processing, o sistema de coordenadas original é restaurado.

## pushMatrix() e popMatrix()

Uma forma de lidar com os efeitos cumulativos do `translate()` é utilizando `pushMatrix()`, que permite salvar o sistema de coordenadas atual, e que deve ser mais tarde restaurarado  com `pophMatrix()`.

```python
def setup():
    size(500, 500)
    
def draw():
    triangulo(100, 100, 200, 100)
    triangulo(250, 100, 100, 100)

def triangulo(x, y, lado1 , lado2):
    pushMatrix() 
    translate(x, y)
    beginShape()
    vertex(0, 0)
    vertex(0, lado1)
    vertex(lado2, lado1)
    endShape(CLOSE) 
    popMatrix() 
```

