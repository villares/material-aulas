# Funções beginShape, vertex e endShape

## Descrição

+ O uso das funções beginShape e endShape permite criar formulários mais complexos. O beginShape inicia a modulação das vértices para gerar uma forma e o endShape acrescentado ao fim da programação finaliza a mesma. 
+ O valor do parâmetro indica quais tipos de formas criar a partir dos vértices fornecidos. Sem o modo especificado, a forma pode ser qualquer polígono irregular. Os parâmetros disponíveis para beginShape são POINTS, LINES, TRIANGLES, TRIANGLE_FAN, TRIANGLE_STRIP, QUADS e QUAD_STRIP. 

## Passo a Passo

+ Após chamar a função beginShape, uma série de comandos vertex deve seguir. Para parar de desenhar a forma, chame endShape. A função vertex com dois parâmetros especifica uma posição em 2D e a função vertex com três parâmetros especifica uma posição em 3D. Cada forma será delineada com a cor do traçado atual e preenchida com a cor de preenchimento.

## Exemplo prático - Estrela 2D

```python
def setup():
    size(500, 500)
    desenha_retangulos(0, 0, 250, 50)
def setup():
    size(500, 500)
    
def draw():
    strokeWeight(5)
    background(82, 177, 214) #Mudar a cor do plano de fundo
    L, l = 150, 80 # Dimensões Ladomaior e Ladomenor . Vértices não adjacentes
    M, m = L / 2, l / 2
    translate(200, 200)
    beginShape() #iniciando a gravação as "vértices" da forma
    vertex(-M, -M)
    vertex(-m,  0)
    vertex(-M, +M)
    vertex( 0, +m)
    vertex(+M, +M)
    vertex( m, 0)
    vertex(+M, -M)
    vertex( 0, -m)
    endShape(CLOSE) #Fechamento da forma
```
### Observações

+ Transformações como translate, rotate e scale não funcionam dentro do bloco  beginShape/endShape. Também não é possível usar outras formas, como ellipse ou retângulo.
+ As configurações do renderizador P3D permitem que as configurações de traço e preenchimento sejam alteradas por vértice, mas o renderizador padrão não. (TO DO: checar no P2D) 
+ Configurações como strokeWeight, strokeCap e strokeJoin não podem ser alteradas enquanto  dentro de um bloco beginShape/endShape (devem ser aplicadas antes).

### Referência

https://py.processing.org/reference/beginShape.html
    
  
    
  


