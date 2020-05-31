## Funções `map()`, `lerp()` e experimentando *easing*

### A função `map()` do Processing

> No Processing modo Python temos uma situação um pouco curiosa, por ser uma ferramenta híbrida com elementos de Processing e de Python. Essas duas linguagens tem funções de nome `map()` mas com comportamentos/significados totalmente distintos. Nesta página vamos explorar o comportamento do `map()` do Processing (mas é possível obter o comportamento de `map()` do Python também, que explicaremos em outra página).

A função `map()`, requer 5 argumentos e devolve um valor: `b = map(a, a0, a1, b0, b1)`

Ela recebe um número, que vamos chamar de **`a`**, e que está em uma faixa de origem de `a0`  a `a1` , e devolve um número **`b`**  na faixa de destino de `b0` a `b1`, de forma que 'mapeia' valores de uma faixa para outra. 

Veja uma animação que tenta mostrar como funciona essa conversão de valores de uma escala ou faixa para outra.

![](assets/map_2.gif)

Note que se você entregar um número **`a`** fora da faixa de origem indicada (entre `a0` e `a1`) vai receber um número 'para fora' da faixa de destino entre `b0` e `b1`.

Em um caso de uso bem simples, o `map()` podemos transformar o valor da posição horizontal do mouse, `mouseX`, que é um número entre **0** e a largura da área de desenho (`width`), em um valor para controlar elementos do desenho (na faixa que desejarmos).  No exemplo abaixo, cinzas entre preto e branco podem são criados com números na faixa entre **0** e **255**, e um círculo vai ser movido entre as posições **x**  de **100** a **300**.

![](assets/map_1.gif)

```python
def setup():
    size(400, 400)
    strokeWe
    
def draw():
    background(200)
    
    cinza = map(mouseX, 0, width, 0, 255)
    x = map(mouseX, 0, width, 100, 300)
    
    fill(cinza)
    circle(x, height / 2, 100)
```

### A função `lerp()`

O nome vem, de  <i>**l**inear int**erp**olation</i> (interpolação linear) e a função permite obter um número intermediário ente dois números `v0` e `v1` de maneira proporcional a um parâmetro **`t`**. Você pode interpretar **`t`** como uma porcentagem, **0** faz `lerp()` devolver o primeiro número, `v0`, e **1**  produz o segundo, `v1`.  Com o **`t`**  valendo  **0.5** (50%) o valor devolvido fica bem no meio do caminho entre os dois números (uma média aritmética).

Isso lembra o `map()` que acabamos de ver, mas com uma faixa de origem (para o **`t`**) predeterminada de  **0** a **1** , veja na animação abaixo.

![](assets/lerp_1.gif)

Note que assim como em `map()` valores fora da faixa esperada de origem (no caso entre **0** e **1**) produzem valores além dos limites fornecidos.


#### *Lerp* para cores

Podemos também obter cores intermediárias com a função `lerpColor()` 

![](assets/lerp_3.gif)

Veja um exemplo de uso abaixo.

```python
from __future__ import division

def setup():
    size(400, 400) 
    strokeWeight(3)
    noFill()
    
def draw():
    background(240)
    xa, ya = 100, 100
    xb, yb = 300, 300
    ca = color(200, 0, 0)
    cb = color(0, 0, 200)
    n = 1 + int(mouseX / 10) # ou 1 + int(map(mouseX, 0, width, 0, 40))
    for t in range(n + 1):
        xc = lerp(xa, xb, t / n)
        yc = lerp(ya, yb, t / n)
        cc = lerpColor(ca, cb, t / n)
        stroke(cc)    
        ellipse(xc, yc, 200, 200)
```
![](assets/lerp_3b.gif)

#### *Lerp* para vetores

Em Processing podemos usar objetos da classe `PVector` para armazenar pares ou triplas de valores, representando coordenadas e pontos ou vetores em duas ou três dimensões. Essa classe tem um método `lerp()` que pode ser muito útil, permitindo  fazer a interpolação linear de dois vetores ou pontos, isto é, encontrar vetores ou pontos intermediários.

![](assets/lerp_2.gif)

### O que é *easing*?

A ideia por trás de *easing* é a suavização da transição de um movimento, uma vez que, na natureza, os movimento tem variação de velocidade que raramente são instantâneas ou lineares. 

Um movimento pode iniciar rapidamente  e parar suavemente (*easing out*), iniciar suavemente (*ease in*) ou ainda iniciar e parar suavemente (*easing in and out*).

### Funções para suavização das transições

A estretégia mias comum é de se usar funções de *easing* que recebem um valor entre **0** e **1** e retornam um valor, grosso modo na mesma faixa, o pelo menos nos extremo (eventualmente passado um pouco para fora). Os valores podem ser usados em conjunto com `lerp()` ou simplesmente multiplicando um outro valor.

Em uma função `easing(p)` um `p = 0` devolve **0** e `p = 1` produz **1**, mas a variação intermediária acontece em velocidades diferentes. O *não-easing* é o crescimento linear, em que o valor devolvido é exatamente o mesmo recebido pela função.

Vejamos o exemplo que fizemos inicialmente com `map()` de um círculo que anda e vai de preto para branco, mas usando `lerp()` e uma função de *easing* exponencial, na saída e na chegada (*in* e *out*).

```python
def setup():
    size(400, 400)
    strokeWeight(3)
    
def draw():
    background(200)
    
    #  cinza = map(mouseX, 0, width, 0, 255)
    #  x = map(mouseX, 0, width, 100, 300)
    #  pode ser expresso em forma de t para usar lerp()
    t = map(mouseX, 0, width, 0, 1)    
    cinza = lerp(0, 255, t)
    x = lerp(100, 300, t)
    fill(cinza)
    circle(x, height * .33 , 100)

    # Aplicando 'easing' em 't'
    e = exponential_in_out(t)
    e_cinza = lerp(0, 255, e)  # ou 255 * e  
    e_x = lerp(100, 300, e) # ou 100 + 200 * e
    fill(e_cinza)
    circle(e_x, height * .66 , 100)

def exponential_in_out(p):
    if p == 0.0 or p == 1.0:
        return p
    if p < 0.5:
        return 0.5 * 2 ** ((20 * p) - 10)
    else:
        return -0.5 * 2 ** ((-20 * p) + 10) + 1
```

![](assets/easing_1b.gif)



#### Outros exemplos/métodos

![](assets/easing_2.gif)

```python
def linear(p):
    # sem easing, para comparação
    return p

def cubic_ease_in(p):
    return p ** 3

def quadratic_ease_in(p):
    return p ** 2

def sine_in_out(p):
    return -(cos(PI * p) - 1) / 2

def quadratic_ease_in_out(p):
    if p < 0.5:
        return 2 * p ** 2
    return -2 * p ** 2 + (4 * p) - 1

def cubic_ease_in_out(p):
    if p < 0.5:
        return 4 * p ** 3
    else:
        f = ((2 * p) - 2)
        return 0.5 * f ** 3 + 1

def exponential_in_out(p):
    if p == 0.0 or p == 1.0:
        return p
    if p < 0.5:
        r = 2 ** ((20 * p) - 10) / 2
    else:
        r = -0.5 * 2 ** ((-20 * p) + 10) + 1
    return r

def quadratic_ease_out(p):
    return -(p * (p - 2))

def cubic_ease_out(p):
    f = (p - 1)
    return f ** 3 + 1

def circular_ease_out(p):
    return sqrt((2 - p) * p)
```