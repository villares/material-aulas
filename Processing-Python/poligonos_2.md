# Desenhando polígonos - II
### Mais sobre polígonos e PShape

Agora que já sabemos iterar por uma estrutura de dados, podemos usar as coordenadas das tuplas na lista que vimos anteriormente para desenhar um polígono ou mais genericamente um 'forma' PShape:

```python
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

**Note que é preciso que a direção dos pontos da forma interna, do furo, seja contrária a da forma externa.**

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

### Assuntos relacionados

- [Desenhando Polígonos - I](poligonos_1.md)
- [Sequências e laços de repetição](lacos_py.md)


### EXTRA: Funções para desenhar sequências de pontos em forma de polígono

**Desafio:** Você conseguiria encapsular em uma função a parte do código que faz o desenho do polígono?

<details>    
<summary>Resposta: Uma função que desenha polígonos a partir de sequências de pontos.</summary>

```python
def setup():
    size(400, 400)
    pontos_shape = [(20, 20), (330, 50), (300, 370)]
    draw_poly(pontos_shape)

def draw_poly(points, holes=None, closed=True):
    """
    Aceita como pontos sequencias de tuplas, lista ou vetores com (x, y) ou (x, y, z).
    Por default faz um polígono fechado.
    """
    beginShape()  # inicia o PShape
    for p in points:
        vertex(p[0], p[1])    
    # encerra o PShape
    if closed:
        endShape(CLOSE)
    else:
        endShape()
        
    # Para aceitar pontos em 2D ou 3D
    # for p in points:
    #     if len(p) == 2:
    #         vertex(p[0], p[1])
    #     else:
    #         vertex(*p)  # desempacota pontos em 3d
```

</details>   

**Avançado:** Agora imagine uma função que desenha um PShape com furos se mandarmos uma lista de pontos, mais uma lista de furos com polígonos dentro.

<details>    
<summary>Resposta: Uma função que desenha polígonos com furos.</summary>

```python
def setup():
    size(400, 400)

    pontos_shape = [(20, 20), (330, 50), (300, 370)]
    pontos_furo = [(290, 300), (300, 60), (100, 40)]

    poly_and_holes(pontos_shape, [pontos_furo])
    # poly_and_holes(pontos_shape, pontos_furo)  # tabém funciona

    saveFrame('contour_furo.png')

def poly_and_holes(points, holes=None, closed=True):
    """
    Aceita como pontos sequencias de tuplas, lista ou vetores com (x, y) ou (x, y, z).
    Note que `holes` espera uma sequencias de sequencias ou uma única sequencia de
    pontos. Por default faz um polígono fechado.
    """

    def depth(seq):
        """
        usada para checar se temos um furo ou vários
        devolve 2 para um só furo, 3 para vários furos
        """
        if (isinstance(seq, list) or
                isinstance(seq, tuple) or
                isinstance(seq, PVector)):
            return 1 + max(depth(item) for item in seq)
        else:
            return 0

    beginShape()  # inicia o PShape
    for p in points:
        if len(p) == 2:
            vertex(p[0], p[1])
        else:
            vertex(*p)  # desempacota pontos em 3d
    # tratamento dos furos, se houver           
    holes = holes or []  # equivale a: holes if holes else []
    if holes and depth(holes) == 2:  # sequência única de pontos
        holes = (holes,)     # envolve em um tupla
    for hole in holes:  # para cada furo
        beginContour()  # inicia o furo
        for p in hole:
            if len(p) == 2:
                vertex(p[0], p[1])
            else:
                vertex(*p)
        endContour()  # final e um furo
    # encerra o PShape
    if closed:
        endShape(CLOSE)
    else:
        endShape()
```        
</details>        


