# Escopo: variáveis locais e globais

## Variáveis locais e parâmetros nas definições de funções

Criando normalmente um variável dentro da definição de uma função (como `setup()`, por exemplo), dizemos que a variável tem *escopo local* e somente o código dentro da função reconhece aquele nome e enxerga os valores atribuidos neste escopo.
Os parâmetros ou argumentos de uma função funcionan no escopo local da função.

### exemplo de uma variável local

```python
def olho(x, y, tamanho):
    # tamanho é um parâmetro, só é conhecido aqui, como uma variável local.
    metade = tamanho/2  # e metade é uma variável local.
    noStroke()
    fill(255)
    ellipse(x, y, tamanho, metade)
    fill(0)
    ellipse(x, y, metade-2, metade-2)
```

## Variáveis globais

Traducionalmente criadas no início do *sketch*, e fora de qualquer função (incluindo `setup()` e `draw()`) as variveis globais são visíveis por qualquer parte do código. Para criar uma variável global estando dentro de uma função (ou para poder alterar a atribição de uma variável global) é preciso usar a instrução `global`.

### exemplo de uma variável global

```Python
y = 100  # y é uma variável global, pode ser usada em qualquer ponto do programa.

def setup():
    global x # para criar uma variável global x aqui no setup()
    size(200, 200)
    x = width / 2

def draw():
    global x # necessário para alterar a variável x
    background(0)
    circle(x, y, 10) # x e y são variáveis globais
    x = x + 1
    if x > width:
        x = 0
```

É comum escutarmos que devemos usar variáveis globais com parcimônia, usadas descuidadamente, elas criam o risco de alterarmos  inadvertidamente valores em pontos inesperados do programa. O uso indicriminado de variáveis globais viola certos princípios de "bom design de sofwtare", como o encapsulamento das funcionalidades em partes independentes. Em pequenos *sketches* você não deve se preocupar muito com isso!

---
Este material é baseado no material do curso https://arteprog.space/programacao-criativa/

---
Texto e imagens / text and images: CC BY-NC-SA 4.0; Código / code: GNU GPL v3.0 exceto onde explicitamente indicado por questões de compatibilidade.

