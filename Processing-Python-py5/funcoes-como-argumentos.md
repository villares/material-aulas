# Funções como argumentos de outras funções
# Funções são valores/objetos e podem ser passadas ao se chamar outras funções

Pode passar despercebido no começo do aprendizado da linguagem Python que as funções embutidas, que já vem com a linguagem, bem com as que definimos ou até importamos, são também "objetos", são "valores" e podem ser passadas como argumentos na chamada de outras funções.

# O método `sort()` das listas e a função `filter()`

# `sort()` e o argumento nomeado `key`.

O método `sort()`, quando chamado em uma lista que contém números, põe os itens da lista em ordem crescente, já em listas contendo * strings * (texto) põe os itens em ordem alfabética:

```python
frutas = ['morango', 'abacaxi', 'uva', 'banana', 'caju']
frutas.sort()
print(frutas)  # ['abacaxi', 'banana', 'caju', 'morango', 'uva']
```

A função embutida `len()` do Python, quando aplicada a * strings * nos devolve o tamanho, número de caracteres:

```python
print(len('abacaxi'))  # exibe: 7
```
Se passarmos o nome da função `len()`, isto é `len` sem os parenteses, como o argumento nomeado(*keyword argument*) `key` do método `sort()` a lista vai ser ordenada pelo tamanho(crescente) das palavras!

```python
frutas = ['morango', 'abacaxi', 'uva', 'banana', 'caju']
frutas.sort(key=len)
print(frutas)  # ['uva', 'caju', 'banana', 'morango', 'abacaxi']
```
O ponto é que podemos passar uma função, isto é, uma referência a uma função, como argumento de outra função.

Veja este caso em que criamos uma função que nos dá a última letra de uma palavra:

```python


def ultima_letra(palavra):
    return palavra[-1]


frutas = ['morango', 'abacaxi', 'uva', 'banana', 'caju']
frutas.sort(key=ultima_letra)
print(frutas)  # ['uva', 'banana', 'abacaxi', 'morango', 'caju']
```

# Como selecionar valores de uma coleção, com um laço e com a função
# `filter()`.

Imagine que você tem uma coleção de valores, áreas, por exemplo, e gostaria de remover os zeros. Na verdade vamos produzir uma nova coleção só com os valores que nos interessam, sem zeros ou valores negativos. Uma primeira maneira de fazer isso seria por meio de um laço de repetição:

```python
areas = [10, 5, 13.2, 0, 12, 55, 2, 0, 3]

areas_filtradas = []
for v in areas:
    if v > 0:
        areas_filtradas.append(v)

print(areas_filtradas)  # exibe:  [10, 5, 13.2, 12, 55, 2, 3]
```

Uma segunda maneira seria usando uma * compreensão de lista*

```python
areas = [10, 5, 13.2, 0, 12, 55, 2, 0, 3]

areas_filtradas = [v for v in areas if v > 0]
```

Uma terceira maneira seria criar uma função que tem a regra(maior que zero) e usar a função embutida `filter()`

```python
areas = [10, 5, 13.2, 0, 12, 55, 2, 0, 3]


def maior_que_zero(n):
    return n > 0  # equivale a dizer if n > 0: return True


areas_filtradas = filter(maior_que_zero, areas)
```

# `lambda`, uma pequena função sem nome

A palavra chave `lambda` permite uma forma abreviada de definir funções. Com ela é possível criar funções anônimas(sem nome) no Python, que são úteis justamente quando precisamos de uma pequena função para passar como argumento de outra função!

Só para demonstrar a equivalência, no exemplo a seguir vamos criar a função `ultima_letra` usando a palavra chave `lambda` em vez de `def`, na verdade não é legal usar lambdas desta maneira, para criar uma função com nome é melhor usar a forma tradicional com `def`.

```python
def ultima_letra(p): return p[-1]


frutas = ['morango', 'abacaxi', 'uva', 'banana', 'caju']
frutas.sort(key=ultima_letra)
print(frutas)  # ['uva', 'banana', 'abacaxi', 'morango', 'caju']
```

Agora vejamos a forma mais idiomática, usando a expressão `lambda`, que acabamos de ver, no lugar onde iria o nome da função `ultima_letra`:

```python
frutas = ['morango', 'abacaxi', 'uva', 'banana', 'caju']
frutas.sort(key=lambda p: p[-1])
print(frutas)  # ['uva', 'banana', 'abacaxi', 'morango', 'caju']
```

Não abuse no uso de * lambdas*, na dúvida defina uma função com nome usando `def`, o código fica mais legível. As funções anônimas * lambda* têm também algumas restrições, seu corpo é uma só expressão(não pode ter várias linhas).

# Exercício

Você conseguiria escrever o exemplo de `filter()` usando uma função `lambda` ?

# Listas e dicionários de funções

Como as funções são também objetos/valores, podemos guardá-las em listas e dicionários.

```python


def draw():
    formas = [
        lambda x, y, lado: rect(x - lado / 2, y - lado / 2, lado, lado),
        lambda x, y, lado: ellipse(x, y, lado, lado/2)
        ]

    for func in formas:
        func(50, 50, 90)


```

ou

```python


def draw():
    formas = {
        'r': lambda x, y, lado: rect(x - lado / 2, y - lado / 2, lado, lado),
        'e': lambda x, y, lado: ellipse(x,  y, lado, lado/2)
        }

    formas['r'](50, 50, 80)
    formas['e'](50, 50, 80)

```

# A função embutida `map()`

Imagine que você tem uma lista de números que contém números `float`, números de ponto flutuante, e que precisa de números inteiros e com isso precisa converter todos em `int` (inteiros).

```python
angulos_para_arredondar = [15.0, 15.5, 40.2, 45.1, 60.8,  75.3]
```

A função `int()` faz essa conversão para um número de cada vez, desprezando a parte decimal. Já `round()` "empurra" números com a parte decimal maior que 0.5 para cima, veja um exemplo abaixo.

```python
print(int(10.8))   # exibe 10   (int)
print(round(10.8))  # exibe 11.0 (um resultado float!)
```

Uma primeira aproximação para o problema de arredondar ou converter em inteiros os números da lista pode ser criar um laço de repetição:

```python
angulos_para_arredondar = [15.0, 15.5, 40.2, 45.1, 60.8,  75.3]
angulos_inteiros = []
for a in angulos_para_arredondar:
    angulos_inteiros.append(int(a))
print(angulos_inteiros)
# Resultado:
# [15, 15, 40, 45, 60, 75]
```
Isso pode ser abreviado assim:

```python
angulos_para_arredondar = [15.0, 15.5, 40.2, 45.1, 60.8,  75.3]
angulos_inteiros = [int(a) for a in angulos_para_arredondar]
```

Uma outra estratégia que podemos usar é a função embutida `map()` do Python*

```python
angulos_para_arredondar = [15.0, 15.5, 40.2, 45.1, 60.8,  75.3]
# [15, 15, 40, 45, 60, 75]
angulos_inteiros = list(map(int, angulos_para_arredondar))
```

Repare que neste caso não estamos chamando a função `int()`, o que seria feito se usássemos os parenteses, estamos passando uma referência a ela como o primeiro argumento da chamada à `map()`. A função `map()` vai chamar `int()` para nós usando como argumento de `int()` cada valor da lista, e vai nos devolver o resultado. Em Python 2 é uma lista, em Python 3 é um objeto gerador que pode nos dar os itens um por vez ou ser convertido em uma lista.

Veja o mesmo exemplo, passando o nome da função `round()` como argumento:

```python
angulos_para_arredondar = [15.0, 15.5, 40.2, 45.1, 60.8,  75.3]
# [15.0, 16.0, 40.0, 45.0, 61.0, 75.0]
angulos_arredondados = list(map(round, angulos_para_arredondar))
```

>`*` A função `map()` do Python  é diferente da[função `map() ` do Processing](Processing-Python-py5/map_lerp.md), no py5 usamos `remap()` para ela...

