# Escopo: variáveis locais e globais

## Variáveis locais

Criando um variável dentro da definição de uma função (como `setup()`, por exemplo), dizemos que a variável tem *escopo local*, isto significa que somente o código dentro da função reconhece aquele nome e enxerga os valores a ela atríbuidos.

Os parâmetros que recebem os valores dos argumentos de uma função funcionan também como nomes no escopo local da função.

### Exemplo de uma variável local

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

Tradicionalmente criadas no início do *sketch*, e fora de qualquer função (incluindo `setup()` e `draw()`) as variveis globais são visíveis por qualquer parte do código.

Para se criar uma variável global quando se está dentro de uma função (ou para poder alterar a atribição de uma variável global dentro de uma função) é preciso usar a instrução `global`.

### Exemplo de uma variável global

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

#### Glossário

[**variável**](https://penseallen.github.io/PensePython2e/02-vars-expr-instr.html#termo:variável) Um nome que se refere a um valor.

[**variável local**](https://penseallen.github.io/PensePython2e/03-funcoes.html#termo:variável%20local) Uma variável definida dentro de uma função. Uma variável local só pode ser usada dentro da sua função.

[variável global](https://penseallen.github.io/PensePython2e/11-dicionarios.html#termo:variável%20global) Variável definida fora de uma função. As variáveis globais podem ser acessadas de qualquer função.

[instrução `global`](https://penseallen.github.io/PensePython2e/11-dicionarios.html#termo:instrução%20global) Instrução que declara um nome de variável global.

---
Este material é baseado no material do curso https://arteprog.space/programacao-criativa/

---
Texto e imagens / text and images: CC BY-NC-SA 4.0; Código / code: GNU GPL v3.0 exceto onde explicitamente indicado por questões de compatibilidade.
