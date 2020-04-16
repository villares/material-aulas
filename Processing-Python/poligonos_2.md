# Desenhando polígonos - II
### mais sobre polígonos e PShape

Agora que já sabemos iterar por uma estrutura de dados, podemos usar as coordenadas das tuplas na lista que vimos anteriormente para desenhar um polígono ou mais genericamente um 'forma' PShape:

```pyde
def setup():
    size(400, 400)
    
    pontos = [(50, 50), (300, 370), (200, 50), (150, 150)]
    
    beginShape()
    for x, y in pontos:
        vertex(x, y)
    endShape(CLOSE)
```

![poligono_2](assets/poligono_2.png)

### Formas com furos
    
    TODO

### Uma função para desenhar sequências de pontos em forma de polígono
Podemos inclusive encapsular em uma função a parte do código que faz o desenho do polígono:

```pyde
def setup():
    size(400, 400)
    
    pontos = [(50, 50), (300, 370), (200, 50), (150, 150)]
    poly(pontos)


def poly(sequencia):
    beginShape()
    for x, y in sequencia:
        vertex(x, y)
    endShape(CLOSE)
``` 
    
<details>    
<summary>Uma versão mais completa da função que desenha polígonos.</summary>

```pyde
def poly(points, closed=True):
    """
    Aceita uma sequencia de tuplas ou vetores
    tanto com (x, y) como com (x, y, z)
    por default faz um polígono fechado
    """
    beginShape()
    for p in points:
        if len(p) == 2 or p[2] == 0:
            vertex(p[0], p[1])
        else:
            vertex(*p)  # desempacota pontos em 3d
    if closed:
        endShape(CLOSE)
    else:
        endShape()
```        
</details>        

