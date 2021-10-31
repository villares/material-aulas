# Funções como argumentos de outras funções
## Funções são valores/objetos e podem ser passadas ao se chamar outras funções

Pode passar despercebido no começo do aprendizado da linguagem Python que as funções embutidas, que já vem com a linguagem, bem com as que definimos ou até importamos, são também "objetos", são "valores" e podem ser passadas como argumentos na chamada de outras funções. 

### Um primeiro caso, usando`map()`

Imagine que você tem uma lista de números que contém números `float`, números de ponto flutuante, e que precisa de números inteiros e com isso precisa converter todos em `int` (inteiros).

```python
angulos_para_arredondar = [15.0, 15.5, 40.2, 45.1, 60.8,  75.3]
```

A função `int()` faz essa conversão para um número de cada vez, desprezando a parte decimal. Já `round()` "empurra" números com a parte decimal maior que 0.5 para cima, veja um exemplo abaixo.

```python
print(int(10.8))   # exibe 10
print(round(10.8)) # exibe 11
```

Uma primeira aproximação para o problema de arredondar ou converter em inteiros os números da lista pode ser criar um laço de repetição:

```python
angulos_inteiros = []
for a in angulos_para_arredondar:
    angulos_inteiros.append(int(a))
print(angulos_inteiros)
# Resultado:
# [15, 15, 40, 45, 60, 75]
```

Mas uma outra estratégia muito legal que podemos usar é a função embutida `map()` do Python* 

```python
angulos_inteiros = list(map(int, angulos_para_arredondar))  # [15, 15, 40, 45, 60, 75]
```

Repare que não estamos chamando a função `int()`, com o s parenteses, estamos passando o nome dela para a função `map()` como o primeiro argumento.

>* A função `map()` do Python  é diferente da [função `map() ` do Processing](https://github.com/villares/material-aulas/blob/master/Processing-Python/map_lerp.md), no Processing modo Python temos as duas ao mesmo tempo, e isso é meio estranho..., o ambiente vê comforme os valores que você passou qual das funções vai usar.


### `sorted()` e funções anônimas com a palavra chave `lambda`

A palavra chave `lambda` permite uma forma abreviada de definir uma função, com algumas restrições, tem que ser um corpo em uma só expressão (não pode ter várias linhas). Como ela é possível criar funções sem nome no Python, que são úteis justamente quando precisamos de uma pequena função para passar como argumento de outra função! 

Veja este caso em que queremos uma função que nos dá a última letra de uma palavra:

```python
# esta definição de função normal
def ultima_letra(palavra):
    return palavra[-1]

# pode ser reescrita assim:
ultima_letra = lambda p : p[-1]
```
Agora podemos ordenar a nossa lista de frutas pela última letra!

```python
frutas = ['morango', 'abacaxi', 'uva', 'banana', 'caju']
print(sorted(frutas, key=lambda p : p[-1]))
```
### Listas e dicionários de funções

Como as funções são também objetos/valores, podemos guardá-las em listas e dicionários.

```python                        
def draw():
    formas = [lambda x, y, lado: rect(x - lado / 2, y - lado / 2, lado, lado),
              lambda x, y, lado: ellipse(x, y, lado, lado/2)
              ]
    
    for func in formas:
        func(100, 100, 100)
```

TO DO: 
 - *Decorators*: O que são? Onde vivem? Do que se alimentam?
