# Escopo: variáveis locais e globais

## Variáveis globais

Criamos variáveis globais quando  atribuímos um valor a um nome fora do corpo das funções do nosso programa (normalmente no começo do programa). 

Essas variáveis podem ser usadas ao longo de todo o programa. Se você desejar criar uma nova variável global, ou reatribuir (alterar) o valor de uma variável global de dentro de uma função, em Python, é necessário usar a instrução `global`. Exemplo:

### Exemplo de uma variável global

```python
x = 0  # x é uma variável global

def setup():
    size(500, 500)

def draw():
    # Podemos usar/ler o valor da variável global x.
    ellipse(x, height / 2, 10, 10)
    
def keyPressed():
    # Queremos alterar o valor da variável global x. 
    global x 
    x = x + 1
```

## Variáveis locais

Quando criamos uma variável dentro da definição de uma função (como a função `setup()`, por exemplo), dizemos que a variável tem *escopo local*, isto significa que somente o código dentro da função reconhece aquele nome e pode usar os valores a ela atribuídos.

Os parâmetros (os nomes que recebem os valores, também conhecidos como argumentos, usados na chamada de uma função), são declarados no cabeçalho da definição da função, e são nomes do escopo local da função.

### Exemplo de uma variável local

```python
def olho(x, y, tamanho):
    # tamanho é um parâmetro, um nome que funciona como uma variável local.
    metade = tamanho/2  # e metade é uma variável local.
    noStroke()
    fill(255)
    ellipse(x, y, tamanho, metade)
    fill(0)
    ellipse(x, y, metade-2, metade-2)
```

#### Recapitulando

Tradicionalmente criadas no início do *sketch*, e fora de qualquer função (incluindo `setup()` e `draw()`) as variáveis globais são conhecidas em qualquer parte do código. Variáveis criadas dentro de uma função e também os nomes dos parâmetros de uma função pertencem ao escopo local da função.

Para se criar uma variável global quando se está dentro de uma função (ou para poder alterar a atribição de uma variável global dentro de uma função) usamos a instrução `global` do Python.

#### Mais um exemplo, com variáveis globais e locais

```python
y = 100  # y é uma variável global, pode ser usada em qualquer ponto do programa.

def setup():
    global x # para criar uma variável global x aqui no setup()
    size(200, 200)
    x = width / 2

def draw():
    global x # necessário para poder alterar a variável global x aqui no draw()
    # repare que vamos 'ler' o valor de y, mas não vamos alterar
    background(0)
    tamanho = random(10, 50)  # tamanho é uma variável local
    ellipse(x, y, tamanho, tamanho) # x e y são variáveis globais
    x = x + 1
    if x > width:
        x = 0
```

É comum escutarmos que devemos usar variáveis globais com parcimônia, usadas descuidadamente, elas criam o risco de alterarmos inadvertidamente valores em pontos inesperados do programa.

O uso indicriminado de variáveis globais viola certos princípios da "boa engenharia de software", como o encapsulamento das funcionalidades em partes independentes. Em pequenos *sketches* você não deve se preocupar muito com isso!

#### Glossário

[**variável**](https://penseallen.github.io/PensePython2e/02-vars-expr-instr.html#termo:variável) Um nome que se refere a um valor.

[**variável local**](https://penseallen.github.io/PensePython2e/03-funcoes.html#termo:variável%20local) Uma variável definida dentro de uma função. Uma variável local só pode ser usada dentro da sua função.

[variável global](https://penseallen.github.io/PensePython2e/11-dicionarios.html#termo:variável%20global) Variável definida fora de uma função. As variáveis globais podem ser acessadas de qualquer função.

[instrução `global`](https://penseallen.github.io/PensePython2e/11-dicionarios.html#termo:instrução%20global) Instrução que declara um nome de variável global.

---
Este material é baseado no material do curso https://arteprog.space/programacao-criativa/

---
Texto e imagens / text and images: CC BY-NC-SA 4.0; Código / code: GNU GPL v3.0 exceto onde explicitamente indicado por questões de compatibilidade.
