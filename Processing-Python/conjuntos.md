# Conjuntos

Conjuntos (*set*) são estruturas para guardar coleções de itens sem se preocupar com a ordem (por isso não nos referimos a eles como sequências como as tuplas e listas). 

- Converter uma coleção em conjunto garante que não temos repetição de itens (mas perderemos a ordem se originalmente tínhamos uma coleção ordenada, uma sequência)
- São super eficientes para a consulta de existência ou não de um item  (temos X neste conjunto?) assim como operações de subtração, união e intersecção de conjuntos. 

### Eliminando repetições com conjuntos

Uma das formas mais simples de se eliminar duplicações, items repetidos, em uma lista, é transformá-la em um conjunto e depois de volta em uma lista (perde-se a ordem dos elementos).

```python
frutas = ['banana', 'uva', 'uva', 'banana', 'kiwi', 'jaca', 'uva']

frutas_sem_repetir = list(set(frutas)) # resultado: ['banana', 'uva', 'kiwi', 'jaca']
```

### Operações com conjuntos e seus métodos

```python
conjunto_a = {"mar", "vento",}
conjunto_b = {"fogo", "vento"}

uniao = conjunto_a | conjunto_b                 # {"mar", "vento", "fogo"} 
interseccao = conjunto_a & conjunto_b           # {"vento"}
diferenca_simetrica = conjunto_a ^ conjunto_b   # {"mar", "fogo"} 
diferenca_a_menos_b = conjunto_a - conjunto_b   # {"mar"}
diferenca_b_menos_a = conjunto_b - conjunto_a   # {"fogo"}
```

#### Um exemplo visual, interativo

Execute o código abaixo e use o mouse para ligar e desligar, clicando na legenta, os diversos conjuntos de "pontos" calculados pelas operações de conjuntos, fazendo assim uma demonstração visual. Note que no código deste exemplo usamos uma tupla com dicionários dentro!

![conjuntos](assets/conjuntos.png)

```python
from __future__ import unicode_literals

def setup():
    global conjuntos
    size(900, 900)
    set1, set2 = set(), set()
    c1x, c1y, c2x, c2y = 300, 300, 600, 300
    textFont(createFont('Source Code Pro Bold', 24))
    for i in range(2000):
        x = random(width)
        y = random(height)
        if dist(x, y, c1x, c1y) < 270:
            set1.add((x, y))
        if dist(x, y, c2x, c2y) < 270:
            set2.add((x, y))
    conjuntos = (   # Atenção, `conjuntos` é uma tupla de dicionários! Contém conjuntos na chave 'set'
        {'set' : set1 - set2,'label' : 'set1 - set2 (diferença)',
        'visible': True, 'diameter': 20, 'color' : color(200, 0, 0)},                  
        {'set' : set2 - set1,'label' : 'set2 - set1 (diferença)',
        'visible': True, 'diameter': 20, 'color' : color(0, 0, 200)},                           
        {'set' : set1 | set2,'label' : 'set1 | set2 (união)',
        'visible': True, 'diameter': 18, 'color' : color(200, 200, 200)},           
        {'set' : set1, 'label' : 'set1',
        'visible': True, 'diameter': 14, 'color' : color(0, 200, 200)},
        {'set' : set2, 'label' : 'set2',
        'visible': True, 'diameter': 10, 'color' : color(200, 200, 0)},
        {'set' : set1 & set2, 'label' : 'set1 & set2 (intersecção)',
        'visible': True, 'diameter': 6, 'color' : color(0, 200, 0)},
        {'set' : set1 ^ set2, 'label' : 'set1 ^ set2 (diferença simétrica)',
        'visible': True, 'diameter': 6, 'color' : color(255, 0, 255)},
    )             
    
def draw():
    background(100)
    noStroke()
    textSize(24)
    for i, c in enumerate(conjuntos):
        fill(c['color'], 100 + 155 * c['visible'])
        text(c['label'], 30, 650 + i * 30)
        if c['visible']:
            for x, y in c['set']:
                circle(x, y, c['diameter'])        
    
def mouseClicked():
    for i, c in enumerate(conjuntos):
        y = 650 + i * 30 - 20
        if y < mouseY < y + 30 and 30 < mouseX < 30 + textWidth(c['label']):
            c['visible'] = not c['visible']
```

### Assuntos relacionados

- [Dicionários](dicionarios.md)
