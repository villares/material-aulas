# Sequências e repetições

É muito comum em programação pedir ao computador que repita uma ação varias vezes, possivelmente com variações. Para fazer isso frequentemente usamos os chamados laços de repetição (*loops*) e o processo também pode ser chamado de iteração (note que não é i**n**teração, que é outra coisa).

Antes de chegar na execução das repetições com o laço `for`, propriamente, é útil saber como criar rapidamente sequências de valores. Existe uma função em Python que produz valores inteiros, o `range()`, que no Processing modo Python devolve uma lista (no Python 3 produz um 'iterador' que por sua vez devolve os valores, mas isso não importa agora).

## Produzindo sequências de inteiros com `range()`

Executando a função `range()` com o argumento 10, `range(10)`, vamos obter uma lista de 10 números inteiros.

#### Você consegue imaginar quais são?
<details>
  <summary>clique para ver a resposta</summary>

`[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]`
</details>

#### Qual você acha que é o resultado de `range(1, 11)`?
<details>
  <summary>clique para ver a resposta</summary>

`[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`

Podemos usar `range(parada)` ou `range(inicio, parada)`, o número início está incluso, o número de parada não é incluso.
</details>


## Laços de repetição com `for`

Usando a estrutura `for` podemos fazer uma ação para cada item de um 'iterável', o que inclui tuplas e listas. Em cada ciclo um item por vez da coleção é atribuido a uma variável, como neste exemplo:

```pyde
for n in range(10): # para cada número do range(10) 
    print(n)        # n vai ter um valor diferente a cada ciclo
```
<details>
  <summary>clique para ver o resutado no console</summary>

```
0
1
2
3
4
5
6
7
7
9
```
</details>

É tradicional usar certos nomes de variável `i`, `j` e `k`, por exemplo, para armazenar números de 'contadores' ou 'índices' que vão variando a cada volta do laço `for`.

Agora outro exemplo usando `range()` com efeito visual.
```pyde
for i in range(14):
    y = 10 + 5 * i
    line(30, y, 80, y)
```

#### Quais serão os valores de y e como fica o desenho das linhas?
<details>
  <summary>clique para ver os resultados</summary>

![linhas paralelas](https://raw.githubusercontent.com/villares/material-aulas/master/Processing-Python/assets/lines.png)
```
i: 0   y: 10 # início
i: 1   y: 15 # 10 + 5 * 1
i: 2   y: 20
i: 3   y: 25
...
i: 13  y: 75 # final
```
</details>

#### Você conseguiria escrever um `for` para desenhar as linhas na vertical?

> resultado mais à frente

### Repetições simples

Algumas vezes nem vamos usar os números! Só queremos repetir a operação, então em vez de guardar o número em uma variável nomeada com `x`, `y`, `n` ou `i` usamos uma variável com o curioso nome`_` (*underscore*, ou como muitos falam 'underline'). Isso é uma dica de quem está escrevendo o código de que o valor da variável vai ser desprezado. Exemplo:

```pyde
for _ in range(3): # repita 3 vezes!
   print("viva!")
```

<details>
  <summary>clique para ver o resutado no console</summary>

```
viva!
viva!
viva!
```
</details>

#### Você consegue imaginar um desenho usando esse tipo de repetição e números [pseudo-aleatórios](https://github.com/villares/material-aulas/blob/master/Processing-Python/numeros-aleatorios_py.md) com `random()`?

## Mais sobre o `range()`

A função `range()` aceita argumentos na forma `range(início, parada, passo)`, *início* será o primeiro número, e a sequência para antes do número *parada*, aumentando com o número do *passo*, veja este exemplo com resultado visual com linhas:

```pyde
for x in range(10, 80, 5): # x começa valendo 10 e termina valendo 75
    line(x, 30, x, 80)     # x aumenta de 5 em 5
```

#### Você consegue imaginar o resultado visual?
<details>
  <summary>clique para ver o resutado visual</summary>

![verticais](https://raw.githubusercontent.com/villares/material-aulas/master/Processing-Python/assets/verticais.png)
</details>

## Um pouco sobre listas e tuplas

Vamos ver agora duas estruturas de dados muito usadas em Python para guardar coleções ordenadas, ou sequências, de valores: tupla (*tuple*) e lista (*list*).

Exemplo de uma tupla:

`tupla_sertaneja = ("Maiara", "Maraisa")`

Exemplo de uma lista:

`meus_pockemons = ["Fomantis", "Eevee"]`

A principal difereça, além do fato de que a tupla foi construída com parenteses `( ,)`e a lista com colchetes `[ ,]`, é que **uma lista permite que seus itens sejam alterados**, itens sejam adicionados, itens podem ser removidos, ou, os itens como um todo podem ser reordenados.

Já **uma tupla não pode ter itens removidos, addicionados ou ser reordenada**, dizemos que ela é *imutável* (mesmo se um item puder ter o seu conteúdo mais interno alterado). Se for necessária uma correção, podemos criar uma nova tupla com a alteração em substituição da original.

Tuplas são mais 'econômicas' em termos computacionais e são bastante usadas quando a ordem dos elementos tem significado, por exemplo podemos fazer uma tupla com coordenadas x e y, o primeiro item 'significa' um valor no eixo X e o segundo um valor no eixo Y:

```pyde
posicao = (150, 50)  #  x: 150 y: 50
```

Podemos 'desempacotar' uma tupla, atribuindo os seus valores a variáveis, desde que o número de variáveis seja igual ao número de itens:

```pyde
posicao = (100, 150) 
x, y = posicao # x passa a valer 100 e y 150
```

E é possível fazer tuplas com tuplas dentro, listas com listas dentro, listas com tuplas dentro e etc. Vamos experimentar fazer uma lista de tuplas representando as coordenadas de alguns pontos:

```pyde
pontos = [(10, 10), (100, 20), (200, 50), (50, 150)]
```

### Iterando pelos dados

Finalmente vamos usar a estrutura de iteração, o loop `for`, para repetir a ação de desenhar um círculo, usando as coordenadas das tuplas de coordenadas na lista `pontos`:

```pyde
def setup():
    size(400, 400)
    pontos = [(10, 10), (100, 20), (200, 50), (50, 150)]
    for t in pontos:
        x, y = t # 'desempacotando' a tupla (x, y)
        ellipse(x, y, 15, 15)
```

ou ainda podemos escrever abreviadamente acliquessim:

```python
def setup():
    size(400, 400)
    pontos = [(50, 50), (300, 370), (200, 50), (150, 150)]
    for x, y in pontos:
        ellipse(x, y, 15, 15)
```

![resultado](https://i.imgur.com/TL0BBId.png)


### Enumerando os itens da sequência

Ao iterarmos por uma sequência, pode ser útil obter ao mesmo tempo que o item, o índice do item na sequência. Isso é chamado de enumeração, e usamos a função `enumerate()` como neste exemplo:

```pyde
def setup():
    size(400, 400)
    pontos = [(50, 50), (300, 370), (200, 50), (150, 150)]
    for i, (x, y) in enumerate(pontos):
        fill(255)
        ellipse(x, y, 5 + i * 5, 5 + i * 5)
        label = "{}: {}, {}".format(i, x, y)
        fill(0)
        text(label, x + 15, y)
```
![sketch_2020_04_10a](https://abav.lugaralgum.com/sketch-a-day/2020/sketch_2020_04_10a/enumerate.png)

## Assuntos relacionados

#### Grades de filas e colunas de elementos com laços "aninhados" 

```python
for x i

n range(5, 100, 10):  # x: 5, 15, 25, 35 ... 95
  for y in range(5, 100, 10):  # y: 5, 15, 25, 35 ... 95
    ellipse(x, y, 5, 5) 
```
![mini grade](https://raw.githubusercontent.com/villares/material-aulas/master/Processing-Python/assets/mini-grid.png)

Veja mais em: [Desenhando Grades](https://github.com/villares/material-aulas/blob/master/Processing-Python/grades.md)

#### Outra estrutura de repetição: `while`

[Laços de repetição com `while`](https://github.com/villares/material-aulas/blob/master/Processing-Python/while.md) 

#### Acessando e alterando itens de uma sequência

[Mais sobre sequências e fatias](https://github.com/villares/material-aulas/blob/master/Processing-Python/mais_sequencias.md)

### Glossário

[**loop**](https://penseallen.github.io/PensePython2e/04-caso-interface.html#termo:loop) **(laço)** Parte de um programa que pode ser executada repetidamente.

---
Este material é baseado no material do curso https://arteprog.space/programacao-criativa/

---
Texto e imagens / text and images: CC BY-NC-SA 4.0; Código / code: GNU GPL v3.0 exceto onde explicitamente indicado por questões de compatibilidade.
