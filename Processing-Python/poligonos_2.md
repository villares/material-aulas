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
    
Podemos criar furos dentro de formas `PShape` pendindo uma sequência de vértices, com`vertex()`, entre as funções `beginContour()` e `endContour()`, que por sua vez precisam estar entre `beginShape()` e `endShape()`.
**Note que é preciso que a direção dos pontos da forma interna, do furo seja contrária a da forma externa.**

No exemplo a seguir vamos descrever com uma lista de tuplas 3 vértices em sentido horário, e os vértices do furo no mesmo sentido. Para funcionar corretamente o furo, no segundo laço `for` os pontos do furo tem sua ordem invertida com `pontos_furo[::-1]`. Experimente remover essa inversão para ver o resultado!
    
```python
def setup():
    size(400, 400)
    # fill(200, 100, 100)
    # rect(50, 50, 300, 300) # retângulo rosa pra destacar furo
    
    pontos_shape = [(20, 20), (330, 50), (300, 370)]
    pontos_furo = [(100, 40), (300, 60), (290, 300)]
    
    fill(255)
    beginShape()
    for x, y in pontos_shape:
        vertex(x, y)
    beginContour()
    for x, y in pontos_furo[::-1]:
        vertex(x, y)
    endContour()
    endShape(CLOSE)
```

![furo](assets/contour_furo.png)


### Uma função para desenhar sequências de pontos em forma de polígono

Você conseguiria encapsular em uma função a parte do código que faz o desenho do polígono?
    
<details>    
<summary>Resposta: Uma função que desenha polígonos a partir de sequências de pontos.</summary>

```python
def poly(points, holes=None, closed=True):
    """
    Aceita uma sequencia de tuplas ou vetores tanto com (x, y) como com (x, y, z).
    Note que `holes` espera um sequencias de sequencias, e não uma única sequencia.
    Por default faz um polígono fechado.
    """
    beginShape()
    for p in points:
        if len(p) == 2 or p[2] == 0:
            vertex(p[0], p[1])
        else:
            vertex(*p)  # desempacota pontos em 3d
    holes = holes or [] # holes if holes else []
    for hole in holes:
        beginContour()
        for p in hole:
           if len(p) == 2 or p[2] == 0:
                vertex(p[0], p[1])
        endContour()
    if closed:
        endShape(CLOSE)
    else:
        endShape()
```        
</details>        


