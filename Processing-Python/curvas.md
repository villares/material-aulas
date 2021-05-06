
# Desenhando curvas - I

Agora que já sabemos desenhar um polígonos com `beginShape()` e `endShape()` ou `endShape(CLOSE)` podemos experimentar formas curvas.

## Sumário
[Assunto anterior: desenhando polígonos (beginShape e endShape)](poligonos_2)

[Curvas Bezier com bezierVertex()](curvas.html#curvas-bezier-com-beziervertex)
- [Exemplo 1](curvas.html#curvas-bezier-com-beziervertex#exemplo-1)

[Curvas com curveVertex()](curvas.html#curvas-com-curvevertex)
- [Exemplo 1](curvas.html#curvas-com-curvevertex#exemplo-1)
- [Exemplo 2](curvas.html#curvas-com-curvevertex#exemplo-2)
- [Exemplo 3](curvas.html#curvas-com-curvevertex#exemplo-3)
- [Exemplo 4](curvas.html#curvas-com-curvevertex#exemplo-4)
- [Exemplo 5](curvas.html#curvas-com-curvevertex#exemplo-5)

[Simulando arcos e filetes com Bezier](curvas.html#simulando-arcos-e-filetes-com-bezier)

[Assuntos relacionados](curvas.html#assuntos-relacionados)

[Extra: Um testador de curvas interativo](curvas.html#extra-um-testador-de-curvas-interativo)



## Curvas Bezier com `bezierVertex()`

As famosas curvas Bezier levam o nome de Pierre Bézier, que as desenvolveu em seus trabalhos na década de 1960 na indústria automotiva, elas descrevem curvas a partir das coordenadas de pontos, ou âncoras, que delimitam o início e o fim de uma curva, mas também precisam de "pontos de controle" que em geral ficam fora da curva, mas controlam o seu comportamento.

Você pode usar um ou mais vértices *Bezier* entre o `beginShape()` e o `endShape()`, e ela pode ser aberta ou fechada (com `endShape(CLOSE)`), mas antes de cada `bezierVertex()` é preciso que haja algum outro vértice, um ponto âncora, que marca o início e que pode ser feito com `vertex()`, como neste exemplo a seguir.

No `bezierVertex()` propriamente dito, os quatro primeiros argumentos são as cordenadas de dois pontos de controle e os últimos dois são as coordenadas do vértice (que pode servir de âncora inicial para um próximo vértice Bezier).

### Exemplo 1

```
 beginShape()
    vertex(100, 50)         # 0: âncora inicial 
    bezierVertex(150, 150,  # 1: primeiro ponto de controle do primeiro vértice
                 250, 100,  # 2: segundo ponto de controle do primeiro vértice
                 250, 200), # 3: vértice final da primeira curva, âncora da segunda
    bezierVertex(150, 250,  # 4: primeiro ponto de controle do segundo vértice
                 50, 200,   # 5: segundo ponto de controle do segundo vértice
                 50, 100)   # 6: segundo vértice bezier (final)
    endShape(),
```

![errada](assets/curve_bezier.png)

<details>
<summary>Código completo</summary>
<pre>

pontos = [
    (100, 50),          
    (150, 150),
    (250, 100),
    (250, 200),
    (150, 250),
    (50, 200),
    (50, 100),
    ] 

 def setup():
    size(300, 300)

def draw():
    background(100)
    strokeWeight(3)
    stroke(0)
    noFill()
    
    beginShape()
    vertex(100, 50)          
    bezierVertex(150, 150,  
                    250, 100,  
                    250, 200), 
    bezierVertex(150, 250,  
                    50, 200,   
                    50, 100)
    endShape()
    strokeWeight(1)
    for i, ponto in enumerate(pontos):
        x, y = ponto
        fill(255)
        ellipse(x, y, 5, 5)
        t = "{}: {:03}, {:03}".format(i, x, y) 
        text(t, x+5, y-5) 

</pre>
</details> 

## Curvas com `curveVertex()`

Agora que já sabemos iterar por uma estrutura de dados, e como usar as coordenadas das tuplas para desenhar um polígono, podemos experimentar a mesma estratégia com outros típos de vértice. 

Agora veremos o `curveVertex()`,que não tem pontos de controle como Bezier, mas tem a curiosa propriedade de ser influenciado pelos pontos que vem antes e depois dele.

Considere esta lista de pontos:


```python
pontos = [
    (100, 50),          
    (150, 100),
    (250, 100),
    (250, 200),
    (150, 200),
    (50, 200),
    (50, 100),
    ]  
```

### Exemplo 1

Se chamarmos uma vez `curveVertex()` para cada vértice dentro de um contexto de `beginShape()` e `endShape(CLOSE)`obteremos o seguinte resultado, esquisito (estou aqui omitindo parte do código que controla os atributos gráficos e mostra os texto com os índices dos pontos):

```python
beginShape()
for x, y in pontos:
    curveVertex(x, y)
endShape(CLOSE)
```

![errada](assets/curve_wrong.png)

<details>
<summary>Código completo</summary>
 
 <pre>
 pontos = [
    (100, 50),          
    (150, 100),
    (250, 100),
    (250, 200),
    (150, 200),
    (50, 200),
    (50, 100),
    ]

def setup():
    size(300, 300)
    
def draw():
    background(100)
    strokeWeight(3)
    stroke(0)
    noFill()
    
    beginShape()
    for x, y in pontos:
        curveVertex(x, y)
    endShape(CLOSE)
    strokeWeight(1)
    for i, ponto in enumerate(pontos):
        x, y = ponto
        fill(255)
        ellipse(x, y, 5, 5)
        text(i, x+5, y-5)
</pre>
</details>

### Exemplo 2

Para obter o resultado esperado (ou, caro leitor, pelo menos o que eu esperava) temos que acrescentar uma chamada com as coordenadas do último vértice antes do primeiro, e do primeiro vértice depois do último! Diga lá se não é estranho isso!

```python
curveVertex(pontos[-1][0], pontos[-1][1])
for x, y in pontos:
    curveVertex(x, y)
curveVertex(pontos[0][0], pontos[0][1])
endShape(CLOSE)
```

![fechada](assets/curve_closed_smooth.png)

<details>
<summary>Código completo</summary>
 
 <pre>
pontos = [
    (100, 50),          
    (150, 100),
    (250, 100),
    (250, 200),
    (150, 200),
    (50, 200),
    (50, 100),
    ] 

def setup():
    size(300, 300)
    
def draw():
    background(100)
    strokeWeight(3)
    stroke(0)
    noFill()

    beginShape()
    curveVertex(pontos[-1][0], pontos[-1][1])
    for x, y in pontos:
        curveVertex(x, y)
    curveVertex(pontos[0][0], pontos[0][1])
    endShape(CLOSE)
    strokeWeight(1)
    for i, ponto in enumerate(pontos):
        x, y = ponto
        fill(255)
        ellipse(x, y, 5, 5)
        text(i, x+5, y-5)

</pre>
</details>

### Exemplo 3

É possível fazer uma curva aberta com os mesmo pontos e a mesma influência do último ponto no primeiro, e do primeiro no último, omitindo o `CLOSE`:

```python
curveVertex(pontos[-1][0], pontos[-1][1])
for x, y in pontos:
    curveVertex(x, y)
curveVertex(pontos[0][0], pontos[0][1])
endShape()
```

![aberta com a forma da fechada](assets/curve_smooth.png)

<details>
<summary>Código completo</summary>
<pre>
pontos = [
    (100, 50),          
    (150, 100),
    (250, 100),
    (250, 200),
    (150, 200),
    (50, 200),
    (50, 100),
    ] 

def setup():
    size(600, 600)
    
def draw():
    background(100)
    strokeWeight(3)
    stroke(0)
    noFill()

    beginShape()
    curveVertex(pontos[-1][0], pontos[-1][1])
    for x, y in pontos:
        curveVertex(x, y)
    curveVertex(pontos[0][0], pontos[0][1])
    endShape()
    strokeWeight(1)
    for i, ponto in enumerate(pontos):
        x, y = ponto
        fill(255)
        ellipse(x, y, 5, 5)
        text(i, x+5, y-5)
        
</pre>
</details>
 


### Exemplo 4

Agora se não queremos essa influência da curva fechada, é preciso repetir o primeiro e o último vértice.

```python
beginShape()
curveVertex(pontos[0][0], pontos[0][1])   
for x, y in pontos:
    curveVertex(x, y)
curveVertex(pontos[-1][0], pontos[-1][1])
endShape()
```

![aberta normal](assets/curve.png)

<details>
<summary>Código completo</summary>
<pre>
pontos = [
    (100, 50),          
    (150, 100),
    (250, 100),
    (250, 200),
    (150, 200),
    (50, 200),
    (50, 100),
    ] 

def setup():
    size(600, 600)
    
def draw():
    background(100)
    strokeWeight(3)
    stroke(0)
    noFill()

    beginShape()
    curveVertex(pontos[0][0], pontos[0][1])
    for x, y in pontos:
        curveVertex(x, y)
    curveVertex(pontos[-1][0], pontos[-1][1])
    endShape()
    strokeWeight(1)
    for i, ponto in enumerate(pontos):
        x, y = ponto
        fill(255)
        ellipse(x, y, 5, 5)
        text(i, x+5, y-5)
</pre>
</details>

### Exemplo 5

Veja como ficaria acrescentando-se o `CLOSE` em `endShape(CLOSE)`

![aberta normal](assets/curve_closed.png)

<details>
<summary>Código completo</summary>
<pre>
pontos = [
    (100, 50),          
    (150, 100),
    (250, 100),
    (250, 200),
    (150, 200),
    (50, 200),
    (50, 100),
    ] 

def setup():
    size(600, 600)
    
def draw():
    background(100)
    strokeWeight(3)
    stroke(0)
    noFill()

    beginShape()
    curveVertex(pontos[0][0], pontos[0][1])
    for x, y in pontos:
        curveVertex(x, y)
    curveVertex(pontos[-1][0], pontos[-1][1])
    endShape(CLOSE)
    strokeWeight(1)
    for i, ponto in enumerate(pontos):
        x, y = ponto
        fill(255)
        ellipse(x, y, 5, 5)
        text(i, x+5, y-5)
</pre>
</details>

### Assuntos relacionados

- [Desenhando Polígonos - I](poligonos_1.md)
- [Desenhando Polígonos - II](poligonos_2.md)
- [Sequências e laços de repetição](lacos_py.md)

### EXTRA: Um testador de curvas interativo

**Desafio:** Você conseguiria escrever o código que permite testar as curvas arrastando os pontos com o mouse?

![errada](assets/curves_animate.gif)

<details>    
<summary>Resposta: Usando a mesma estratégia de "arrastar círculos".</summary>
<pre>
arrastando = None

pontos = [ 
    (100, 50),
    (150, 100), 
    (250, 100),
    (250, 200), 
    (150, 200), 
    (50, 200), 
    (50, 100)] 
    
def setup(): 
    size(300, 300) 

def draw(): 
    background(100) 
    strokeWeight(3) 
    stroke(0) 
    noFill() 
    
    beginShape() 
    global pontos
    global arrastando
    curveVertex(pontos[-1][0], pontos[-1][1])
    for x, y in pontos: 
        curveVertex(x, y) 
    curveVertex(pontos[0][0], pontos[0][1]) 
    endShape(CLOSE) 
    strokeWeight(1) 
    for i, ponto in enumerate(pontos): 
        x, y = ponto 
        if i == arrastando: 
            fill(200, 0, 0)             
        else:
            fill(255)
        ellipse(x, y, 5, 5) 
        t = "{}: {:03}, {:03}".format(i, x, y)
        text(t, x + 5, y - 5) 
    
def mousePressed():            # quando um botão do mouse é apertado 
    global arrastando 
    for i, ponto in enumerate(pontos): 
        x, y = ponto
        dist_mouse_ponto = dist(mouseX, mouseY, x, y) 
        if dist_mouse_ponto < 10: 
            arrastando = i 
            break # encerra o laço 

def mouseReleased(): 
    # quando um botão do mouse é solto 
    global arrastando 
    arrastando = None 
        
def mouseDragged():
     # quando o mouse é movido apertado 
     global pontos
     global arrastando
     if arrastando is not None: 
        x, y = pontos[arrastando] 
        x += mouseX - pmouseX 
        y += mouseY - pmouseY 
        pontos[arrastando] = (x, y)

</pre>
</details>
