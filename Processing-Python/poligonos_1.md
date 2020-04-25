# Desenhando polígonos - I
### primeiro contato

Processing oferece funções para desenhar triângulos `triangle()` e quadriláteros `quad()` que são chamadas usando 3 e 4 pares de números, as coordenadas para 3 e 4 vértices, respectivamente. Veja o exemplo a seguir:

![triangulo e quadrilátero](assets/triangle_quad.png)

Mas e se quisermos desenhar um polígono com 5, 6 ou com um número arbitrário de vértices?

Neste caso usamos um conjuto de funções!

Tudo começa com `beguinShape()`, seguido da repetição da função `vertex()` para cada vértice, terminando com `endShape()`. Quando usado com a constante `CLOSE`, `endShape(CLOSE)`, produz polígonos fechados.

```pyde
def setup():
    size(400, 200)

    beginShape()  # inicia o polígono da esquerda
    vertex(10, 10)
    vertex(50, 50)
    vertex(190, 30)
    vertex(90, 150)
    vertex(30, 100)
    endShape()  # polígono aberto

    beginShape()  # inicia o polígono da direita
    vertex(210, 10)
    vertex(250, 50)
    vertex(390, 30)
    vertex(290, 150)
    vertex(230, 100)
    endShape(CLOSE)  # polígono fechado
```
![e4](assets/beginShape_endShape.png)

### Desenhando uma estrela de quatro pontas

Vejamos um exemplo que combina a estrutura que vimos antes com o uso de variáveis para calcular a posição dos vértices, formando um estrela!

```pyde
def setup():
    size(200, 200)
    
def draw():    
    x, y = 100, 100  # coordenadas do centro
    largura_total, largura_menor = 150, 100
    mm, m = largura_total / 2, largura_menor / 2
    beginShape()
    vertex(x - mm, y - mm)
    vertex(x - m, y)
    vertex(x - mm, y + mm)
    vertex(x, y + m)
    vertex(x + mm, y + mm)
    vertex(x + m, y)
    vertex(x + mm, y - mm)
    vertex(x, y - m)
    endShape(CLOSE)
```

![e4](assets/estrela_4_pontas.png)



### Assuntos relacionados

- Você pode ver [usos mais avançados de `beginShape()` na referência](https://py.processing.org/reference/beginShape.html).
- Você pode montar os vértices a partir de [estruturas de dados com laços de repetição ou fazer polígonos com furos](https://github.com/villares/material-aulas/blob/master/Processing-Python/poligonos_2.md)

- [Estrelas de muitas pontas com laços de repetição `while`](https://github.com/villares/material-aulas/blob/master/Processing-Python/while.md)

