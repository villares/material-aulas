# Condicões aninhadas e outras estruturas condicionais

## Se, senão se, senão

É comum encontraramos, além da composição das condições usando operadores lógicos, `ìf` dentro de um `ìf` ou de um `else`.
No caso de repetidos `if`, o 'else + if' é abreviado `elif`.

```python
if a == 0:  # se `a` é igual a 0
    faz_isto()
elif a == 1:  # senão, se `a` é igual a  1
    faz_aquilo()
else:    # senão...
    faz_outra_coisa()
```

No contexto de um *sketch* com py5, é comum querer checar, por exemplo, qual tecla foi apertada.

```python
def key_pressed():
    if key == ' ':   # se a barra de espaço foi apertada
         background(200)  # limpe a tela de desenho com um fundo cinza
    elif key == 'a':  # tecla 'a'
         background(0, 0, 200)  # limpe a tela de desenho com azul
    elif key == 'v':  # tecla 'v'
         background(0, 200, 0)  # limpe a tela de desenho com verde
    else:  # se qualquer outra tecla foi apertada
         background(0)  # limpe a tela de desenho com preto
```

## Expressões condicionais e atribuição condicional

Muitas linguagens tem uma sintaxe conhecida como * operador condicional ternário * que permite escrever o que em Python é conhecido como uma * expressão condicional*. Esta forma de `if` é bastante usada para atribuições ou dentro de outras estruturas:

```python
n = x if cond else y
```

Isso equivale a:

```python
if cond:
    n = x
else:
    n = y
```

Veja um outro exemplo:

```python
a = 50 if is_key_pressed else 100
# A variável a passa a valer 50 se houver uma tecla pressionada
# senão, passa a valer 100
```

## Usando `or` para atribuição condicional

O operador lógico `or` retorna o valor do lado esquerdo caso este seja considerado algo 'verdadeiro', de outra forma, ele retorna o valor do lado direito(que pode ou não ser algo considerado 'falso').

Em Python `None`, `0` (o número zero), `""` (um *string* vazio) ou uma coleção vazia(lista, tupla, etc.) são considerados `False`. Outros valores são considerados `True`.

```python
print(0 or 10)  # exibe: 10
print(10 or 0)  # exibe: 10
print(None or 10)  # exibe: 10
print(10 or None)  # exibe: 10
print(None or 0)  # exibe: 0
print(0 or None)  # exibe: None
```

Por conta disso, você pode se deparar com a seguinte expressão:

```
a = a or b  # é o mesmo que: a = a if a else b
```

Essa forma é bastante usada em funções com parâmetros default:

```python
def quadrado(x, y, tamanho=None):
    tamanho = tamanho or 10
    # Isso significa que se tamanho for 0 ou `None` então tamanho deve passar a valer 10:
    # Equivalente a:
    # tamanho = tamanho if tamanho else 10
    rect(x, y, tamanho, tamanho)
```

Se `0` for um valor válido para o tamanho, o código anterior não serve,`0` é avaliado como `False` nesse contexto, melhor então usar assim:

```python
def quadrado(x, y, tamanho=None):
    tamanho = tamanho if tamanho is not None else 10
    rect(x, y, tamanho, tamanho)
```

ou, talvez mais legível:

```python
def quadrado(x, y, tamanho=None):
    if tamanho is None:
        tamanho = 10
    rect(x, y, tamanho, tamanho)
```
