# Desenhando polígonos - II
# Mais sobre polígonos e outras "polilinhas"

<!-- para o thumbnail do sumário
![](assets/estrelas.png)
-->

## Uma forma alternativa ao `begin_shape()`/`close_shape()`

O Python tem uma estratégia especial, que é aproveitada por quem prepara as bibliotecas para nós, para quando é preciso "começar" uma operação e depois de um certo ponto do programa garantir que ela é "encerrada"; 

Nos exemplos iniciais de polígonos que vimos fizemos uso do par `begin_shape()` e `end_shape()` para produzir os desenhos abaixo.

![e4](assets/beginShape_endShape.png)

<!-- editor-pyp5js -->
```python
size(400, 200)

begin_shape()  # inicia o desenho do polígono da esquerda
vertex(10, 10)
vertex(50, 50)
vertex(190, 30)
vertex(90, 150)
vertex(30, 100)
end_shape()  # encerra o desenho de um polígono aberto

begin_shape()  # inicia o desenho do polígono da direita
vertex(210, 10)
vertex(250, 50)
vertex(390, 30)
vertex(290, 150)
vertex(230, 100)
end_shape(CLOSE)  # encerra o desenho de um polígono fechado
```

A nova  estratégia propõe que você crie um "contexto" em que a operação está acontecendo com a palavra chave `with`. É usado `with` e uma chamada para uma função que cria um *gerenciador de contexto*. Então você indica pela indentação do código as coisas que precisam acontecer naquele contexto, por exemplo enquanto o o `begin_shape()` está em ação. Quando a indentação acaba, o contexto se encerra, e, o *gerenciador de contexto*, cuida de encerrar o que tiver que ser encerrado. Veja como é possível desenhar os mesmos polígonos anteriores com essa estratégia.

<!-- editor-pyp5js -->
```python
size(400, 200)

with begin_shape():  # inicia o polígono aberto
    vertex(10, 10)
    vertex(50, 50)
    vertex(190, 30)
    vertex(90, 150)
    vertex(30, 100)
# acaba a indentação e terminou o desenho do polígono

with begin_closed_shape():  # inicia o polígono fechado
    vertex(210, 10)
    vertex(250, 50)
    vertex(390, 30)
    vertex(290, 150)
    vertex(230, 100)
# aqui já acabou o desenho do polígono
```

O resultado em desenho é exatamente o mesmo.

![image](https://user-images.githubusercontent.com/3694604/189493248-0bb81ba8-955a-43d8-8ba2-a077bda4c6f6.png)



## Calculando os pontos com um laço de repetição

Podemos calcular as coordenadas dos vértices dentro de um laço de repetição. Veja este exemplo de um função que desenha uma estrela.

<!-- editor-pyp5js -->
```python
def setup():
    size(500, 500)
    background(0)
    estrela(400, 100, 5, 50, 10)
    estrela(200, 200, 7, 150, 100)
    estrela(350, 400, 20, 80, 40)
        
def estrela(cx, cy, pontas, raio1, raio2):    
    passo = TWO_PI / pontas
    begin_shape() 
    for i in range(pontas): 
        angulo = i * passo 
        x = cx + raio1 * sin(angulo)
        y = cy + raio1 * cos(angulo)
        vertex(x, y)
        x = cx + raio2 * sin(angulo + passo / 2)
        y = cy + raio2 * cos(angulo + passo / 2)
        vertex(x, y) 
    end_shape(CLOSE)
```

![](assets/estrelas.png)


## Usando pontos de uma estrutura de dados

Sabendo iterar por uma estrutura de dados, podemos usar as coordenadas das tuplas na lista que vimos anteriormente para desenhar um polígono ou mais genericamente.

<!-- editor-pyp5js -->
```python
def setup():
    size(400, 400)

    pontos = [(50, 50), (300, 370), (200, 50), (150, 150)]

    begin_shape()
    for x, y in pontos:
        vertex(x, y)
    end_shape(CLOSE)
```

ou ainda mais sintético, se usarmos o gerenciador de contexto, com a forma `with begin_closed_shape()` e a função `vertices()` que aceita um iterável com os pontos dentro!

<!-- editor-pyp5js -->
```python
def setup():
    size(400, 400)

    pontos = [(50, 50), (300, 370), (200, 50), (150, 150)]

    with begin_closed_shape():
        vertices(pontos)
```

![poligono_2](assets/poligono_2.png)

## Formas com furos

Podemos criar furos dentro de formas `Py5Shape` pendindo uma sequência de vértices, com`vertex()`, entre as funções `begin_contour()` e `end_contour()`, que por sua vez precisam estar entre `begin_shape()` e `end_shape()`.

**Note que é preciso que a direção dos pontos da forma interna, do furo, seja contrária a da forma externa.**

No exemplo a seguir vamos descrever com uma lista de tuplas 3 vértices em sentido horário, e os vértices do furo no mesmo sentido. Para funcionar corretamente o furo, no segundo laço `for` os pontos do furo tem sua ordem invertida com `pontos_furo[::-1]`. Experimente remover essa inversão para ver o resultado!

<!-- editor-pyp5js -->
```python
def setup():
    size(400, 400)
    # fill(200, 100, 100)
    # rect(50, 50, 300, 300) # retângulo rosa pra destacar furo

    pontos_shape = [(20, 20), (330, 50), (300, 370)]
    pontos_furo = [(100, 40), (300, 60), (290, 300)]

    fill(255)
    begin_shape()
    for x, y in pontos_shape:
        vertex(x, y)
    begin_contour()
    for x, y in pontos_furo[::-1]:
        vertex(x, y)
    end_contour()
    end_shape(CLOSE)
```

![furo](assets/contour_furo.png)


### Uma função para desenhar polígonos com furos

Imagine uma função que desenha uma forma poligonal baseada em vértices (*Py5Shape*) com furos se mandarmos uma lista de pontos, mais uma lista de furos com listas de pontos dentro.

<!-- editor-pyp5js -->
```python
def setup():
    size(400, 400)

    pontos_shape = [(20, 20), (330, 50), (300, 370)]
    pontos_furo = [(290, 300), (300, 60), (100, 40)]

    poly_shape(pontos_shape, [pontos_furo])  # note os colchetes extra, uma lista com uma lista dentro

def poly_shape(pts, holes=None, closed=True):
    """
    Aceita como pontos sequencias de tuplas, listas ou vetores com (x, y) ou (x, y, z).
    Note que `holes` espera uma sequencias de sequencia de pontos, que precisam estar
    em sentido anti-horário. Por default faz um polígono fechado.
    """
    begin_shape()  # inicia o Py5Shape
    vertices(pts)
    if holes:
        for hole in holes:
            with begin_contour(): 
                vertices(hole)
    # encerra o Py5Shape
    if closed:
        end_shape(CLOSE)
    else:
        end_shape()
```

## Assuntos relacionados

- [Desenhando Polígonos - I](poligonos_1.md)
- [Sequências e laços de repetição](lacos_py.md)
