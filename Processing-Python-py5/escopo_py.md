# Escopo: variáveis locais e globais

Grosso modo, *escopo* é como nos referimos à região do código onde os nomes das variáveis, ou os nomes de parâmetros de uma função, estão associados a certos valores. Informalmente costumo dizer que é onde no programa uma variável é conhecida. Por exemplo, se você tenta usar uma variável que foi definida em um escopo local fora desse escopo vai obter um `NameError` e o seu programa será interrompido. Outros problemas também podem aparecer se você tentar criar ou modificar um nome global descuidademente.

## Variáveis locais

Quando criamos uma variável dentro da definição de uma função (como a função `setup()`, por exemplo), a variável tem *escopo local*, isto significa que somente o código dentro daquela função reconhece o nome e pode usar os valores a ele atribuídos.

Os parâmetros são os nomes que recebem os valores (argumentos), usados na chamada de uma função, são declarados no cabeçalho da definição da função, e também são nomes do escopo local da função.

### Exemplo de uma variável local

```python
def setup():
    size(256, 256)
    background(100, 0, 0)
    metade = 1  # `metade` é uma variável local, no escopo de setup()
     
    olho(128, 128, 200)  # Chama a função que desenha um olho com tamanho 200
    
    print(metade)   # Exibe 1 no console
    # Neste caso a variável `metade` só serve para demonstrar que é
    # diferente da variável local dentro do escopo de olho()

def olho(x, y, tamanho):  # parâmetros x, y, tamanho
    # 'tamanho' é um nome que funciona como uma variável local
    metade = tamanho / 2  # 'metade' variável local, no escopo de olho()
    no_stroke()
    fill(255)
    ellipse(x, y, tamanho, metade)
    fill(200, 200, 0)
    ellipse(x, y, metade - 5, metade - 5)
    fill(0)
    ellipse(x, y, tamanho * 0.2, tamanho * 0.2)
```

![olho](assets/escopo_olho.png)

O que acontece se você acrescentar `print(tamanho)` no final da função `setup()`?

## Variáveis globais

Criamos variáveis globais quando atribuímos um valor a um nome fora do corpo das funções do nosso programa (normalmente no começo do programa), também podemos dizer que a variável *tem escopo global*.

Essas variáveis podem ser usadas ao longo de todo o programa. Se você desejar criar uma nova variável global, ou reatribuir uma variável global (alterar o valor para o qual o nome da variável aponta) de dentro de uma função, em Python, é necessário usar a instrução `global`. Exemplo:

### Exemplo de uma variável global

```python
x = 0  # x é uma variável global

def setup():
    size(256, 256)
    background(0, 0, 200)  # fundo azul

def draw():
    # Podemos usar/ler o valor da variável global x.
    ellipse(x, height / 2, 100, 100)   # y é 128 e diâmetro 100

def key_pressed():
    # Queremos alterar o valor da variável global x.
    global x   # Sem esta instrução acontece um erro
    x = x + 1
    
def mouse_pressed():
    global x   # Sem esta instrução uma variável local x vai ser criada!
    background(0, 0, 200)  # limpa a tela com fundo azul
    x = 0
```

![key_pressed](assets/escopo_teclado.gif)

Sem a instrução `global x` dentro da função `key_pressed()` você verá o erro `UnboundLocalError: local variable 'x' referenced before assignment`. Pois o Python acredita que você está tentando alterar uma variável local `x` que ele não encontrou.

Sem a instrução `global x` dentro da função `mouse_pressed()` você não verá nenhuma mensagem de erro, mas o clique do mouse não vai fazer o círculo voltar para a posição 0, pois simplesmente será criada uma nova variável local `x` e a variável global `x` não será modificada. Experimente executar este código e fazer modificações para ver o que acontece!


## Recapitulando

- **Variáveis locais** - Criadas dentro de uma função, as variáveis locais são, assim como os nomes dos parâmetros, nomes que  pertencem ao escopo local da função em que foram criados. Se você tentar usar o nome de uma variável local fora do escopo em que ela foi criada, o programa será interrompido com `NameError`.

- **Variáveis globais** - Frequentemente criadas no início do *sketch*, e fora de qualquer função(incluindo `setup()` e `draw()`), as variáveis globais podem ser consultadas em qualquer parte do programa. É possível criar ou alterar uma variável global dentro de uma função, mas para isso é necessário incluir a instrução `global` antes!

### Mais um exemplo, com variáveis globais e locais

```python
# tamanho_maximo é uma variável global, pode ser usada em qualquer ponto do programa.
tamanho_maximo = 50

def setup():
    global x, y  # para criar variáveis globais x e y aqui dentro do setup()
    size(256, 256)
    y = height * 0.4
    x = tamanho_maximo / 2

def draw():
    global x  # para poder alterar a variável global x aqui no draw()
    # repare que vamos 'ler' o valor de y e de tamanho_maximo sem alterar
    background(0)
    tamanho = random(tamanho_maximo / 5, tamanho_maximo)  # tamanho é uma variável local
    ellipse(x, y, tamanho, tamanho)  # x e y são variáveis globais, assim como tamanho_maximo
    x = x + 1
    if x > width:
        x = tamanho_maximo / 2  
```
![vibrando](assets/escopo.gif)

## Conselhos sobre variáveis globais

É comum escutarmos que devemos usar variáveis globais com parcimônia, usadas descuidadamente, elas criam o risco de alterarmos inadvertidamente valores em pontos inesperados do programa.

Em projetos grandes, e com muitos programadores, o uso de variáveis globais é evitado, com o argumento de que seu uso viola certas "boas práticas" de engenharia de software. por exemplo, é considerado desejável o máximo encapsulamento das partes de um programa, e sendo elas independentes, com interfaces claras e adequadas para receber e devolver valores, não vão precisar de variáveis globais. mesmo assim, em certos contextos, variáveis globais são usadas.

Em *sketches*, programas raramente muito grandes e com propósitos visuais, você não deve se preocupar tanto com isso! Use variáveis globais quando precisar e só fique atento às suas modificações. Evite também criar propositalmente uma variável local de mesmo nome que uma global, para evitar confusões, principalmente, evite criar inadvertidamente uma variável local, quando queria reatribuir uma global, por esquecer de escrever a instrução `global` dentro de uma função (o que pode causar tanto erros gritantes como outros mais silenciosos).

## Glossário

[**variável**](https://Penseallen.github.io/PensePython2e/02-vars-expr-instr.html#termo:variável) Um nome que se refere a um valor.

[**variável local**](https://penseallen.github.io/PensePython2e/03-funcoes.html#termo:variável%20local) Uma variável definida dentro de uma função. Uma variável local só pode ser usada dentro da sua função.

[**variável global**](https://penseallen.github.io/PensePython2e/11-dicionarios.html#termo:variável%20global) Variável definida fora de uma função. As variáveis globais podem ser acessadas de qualquer função.

[**instrução `global`**](https://penseallen.github.io/PensePython2e/11-dicionarios.html#termo:instrução%20global) Instrução que declara um nome de variável global.

