# Sequências e laços de repetição

É muito comum em programação pedir ao computador que repita uma ação várias vezes, possivelmente com variações. Para fazer isso frequentemente usamos os chamados laços de repetição (*loops*) e o processo também pode ser chamado de iteração (note que não é i**n**teração, que é outra coisa).

Antes de chegar na execução das repetições com o laço `for`, propriamente, é útil saber como criar rapidamente sequências de valores. Existe uma função em Python que produz valores inteiros, o `range()`, que no Processing modo Python devolve uma lista (no Python 3 produz um 'iterador' que por sua vez devolve os valores, mas isso não importa agora).

## Produzindo sequências de inteiros com `range()`

Executando a função `range()` com o argumento 10, `range(10)`, vamos obter uma lista de 10 números inteiros.

#### Você consegue imaginar quais são?
<details>
  <summary>clique para ver a resposta</summary>

<code>[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]</code>
</details>

#### Qual você acha que é o resultado de `range(1, 11)`?
<details>
  <summary>clique para ver a resposta</summary>

<code>[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]</code>

Podemos usar <code>range(parada)</code> ou <code>range(inicio, parada)</code>, o número início está incluso, o número de parada não está incluso. Há ainda a forma  <code>range(inicio, parada, passo)</code> que veremos mais adiante.

</details>

## Laços de repetição com `for`

Usando a estrutura `for` podemos fazer uma ação para cada item de uma coleção 'iterável', como as estruturas de dados que veremos depois, ou ainda para cada item produzido por um gerador (como uma linha de um leitor de arquivos, por exemplo) e para cada número produzido pelo `range()`. 

Em cada ciclo um item é atribuido a uma variável, cujo nome vem logo após o `for` e antes do `in`. No bloco indentado de código, também conhecido como o *corpo*, acontecem ações, quase sempre usando o valor do item atribuído à variável no início de cada ciclo. 

```python
for «variavel» in «iterável»:
    «corpo»
```

Você consegue imaginar o resultado do código a seguir?

```python
for n in range(10): # para cada número do range(10) 
    print(n)        # n vai ter um valor diferente a cada ciclo
```
<details>
  <summary>clique para ver o resutado no console</summary>

<pre>
0
1
2
3
4
5
6
7
8
9
</pre>
</details>

### Sobre os nomes das variáveis usadas no `for` e "repetições simples"

É tradicional usar certos nomes de variável `i`, `j` e `k`, por exemplo, para armazenar números de 'contadores' ou 'índices' que vão variando a cada volta do laço `for`.

![`for i in range(10):` ](assets/for_i.png)

Algumas vezes nem vamos usar os itens! Só queremos repetir a operação, então em vez de guardar o valor em uma variável nomeada com `x`, `y`, `n` ou `i` usamos uma variável com o curioso nome`_` (*underscore*, ou como muitos falam 'underline'). Isso é uma dica de quem está escrevendo o código de que o valor da variável vai ser desprezado. Exemplo:

```python
for _ in range(3): # repita 3 vezes!
   print("viva!")
```

<details>
  <summary>clique para ver o resutado no console</summary>

<pre>
viva!
viva!
viva!
</pre>
</details>

## Mais exemplos (com o resultado oculto para você tentar resolver antes de olhar)

Agora outro exemplo usando `range()` com efeito visual.

```python
for i in range(14):
    y = 10 + 5 * i
    line(30, y, 80, y)
```

#### Quais serão os valores de y e como fica o desenho das linhas?
<details>
  <summary>clique para ver os resultados</summary>

<img src= "https://raw.githubusercontent.com/villares/material-aulas/master/Processing-Python/assets/lines.png">

<pre>
i: 0   y: 10 # início
i: 1   y: 15 # 10 + 5 * 1
i: 2   y: 20
i: 3   y: 25
...
i: 13  y: 75 # final
</pre>
</details>

#### Você conseguiria escrever um `for` para desenhar as linhas na vertical?
<details>
  <summary>clique para ver a resposta</summary>

<pre>
for j in range(14):
    x = 10 + 5 * j
    line(x, 30, x, 80)
</pre>

<img src="https://raw.githubusercontent.com/villares/material-aulas/master/Processing-Python/assets/verticais.png">
</details>

#### Você consegue imaginar um desenho usando esse tipo de repetição e números [pseudo-aleatórios](aleatoriedade_1.md) com `random()`?

### Mais sobre o `range()`

![range(0, 10, 2)](assets/range_2.png)

> `range(0, 10, 2)` produz os números 0, 2, 4, 6, 8

A função `range()` aceita argumentos na forma `range(início, parada, passo)`, *início* será o primeiro número, e a sequência para antes do número *parada*, aumentando com o número do *passo*, veja este exemplo com resultado visual com linhas:

```python
for x in range(10, 80, 5): # x começa valendo 10 e termina valendo 75
    line(x, 30, x, 80)     # x aumenta de 5 em 5
```

#### Você consegue imaginar o resultado visual?
<details>
  <summary>clique para ver o resutado visual</summary>

<img src="https://raw.githubusercontent.com/villares/material-aulas/master/Processing-Python/assets/verticais.png">
</details>

## Um pouco sobre tuplas e listas

Vamos ver agora duas estruturas de dados muito usadas em Python para guardar coleções ordenadas, ou sequências, de valores: tupla (*tuple*) e lista (*list*).

Exemplo de uma tupla:

```python
tupla_sertaneja = ("Maiara", "Maraisa")
```

Exemplo de uma lista:

```python
meus_pokemon = ["Fomantis", "Eevee"]
```
A principal difereça, além do fato de que a tupla foi construída com parenteses `( ,)`e a lista com colchetes `[ ,]`, é que **uma lista permite que seus itens sejam alterados**, itens podem ser adicionados, removidos, ou, como um todo, podem ser reordenados.

```python
meus_pokemon = ["Fomantis", "Eevee"]
meus_pokemon.append("Luxray")
print(meus_pokemon) 
# Resutado: ["Fomantis", "Eevee", "Luxray"]

meus_pokemon[0] = "Bubasauro"  # 0 é o índice do primeiro item da lista
print(meus_pokemon) 
# Resutado: ["Bubasauro", "Eevee", "Luxray"]

del meus_pokemon[1]
print(meus_pokemon) 
# Resutado: ["Bubasauro", "Luxray"]
```

Já **uma tupla não pode ter itens removidos, addicionados ou ser reordenada**, dizemos que ela é *imutável* (mesmo se um item puder ter o seu conteúdo mais interno alterado). Se for necessária uma correção, podemos criar uma nova tupla com a alteração em substituição da original.

Tuplas são mais 'econômicas' em termos computacionais e são bastante usadas quando a ordem dos elementos tem significado, por exemplo podemos fazer uma tupla com coordenadas x e y, a primeira posição 'significa' (a ordem indica) um valor no eixo X e a segunda posição indica um valor no eixo Y:

```python
posicao = (150, 50)  #  x: 150 y: 50
```

Um outro termo usado para se referir a uma coleção em que a ordem importa e não faz sentido reordenar é 'registro', se temos tuplas com nomes, emails e telefones, por exemplo, como uma linha em uma planilha.

Podemos 'desempacotar' uma tupla, atribuindo os seus valores a variáveis, desde que o número de variáveis seja igual ao número de itens:

```python
posicao = (100, 150) 
x, y = posicao # x passa a valer 100 e y 150
```

E é possível fazer tuplas com tuplas dentro, listas com listas dentro, listas com tuplas dentro e etc. Vamos experimentar fazer uma lista de tuplas representando as coordenadas de alguns pontos:

```python
pontos = [(10, 10), (100, 20), (200, 50), (50, 150)]
```

### Iterando pelos dados

Finalmente vamos usar a estrutura de iteração, o *loop* `for`, para repetir a ação de desenhar um círculo, usando as coordenadas das tuplas de coordenadas na lista `pontos`:

```python
def setup():
    size(400, 400)
    pontos = [(10, 10), (100, 20), (200, 50), (50, 150)]
    for t in pontos:
        x, y = t # 'desempacotando' a tupla (x, y)
        ellipse(x, y, 15, 15)
```

ou ainda podemos escrever abreviadamente assim:

```python
def setup():
    size(400, 400)
    pontos = [(50, 50), (300, 370), (200, 50), (150, 150)]
    for x, y in pontos:
        ellipse(x, y, 15, 15)
```

![resultado](https://i.imgur.com/TL0BBId.png)


### Enumerando os itens da sequência

Ao iterarmos por uma sequência, pode ser útil obter ao mesmo tempo que o item, o índice da posição do item na sequência.
Isso é chamado de enumeração, e podemos usar a função `enumerate()`.

```python
for «variável_para_índice», «variável_para_item» in enumerate(«sequência»):
    «código do laço / corpo»
```

Veja usado no contexto do exemplo anterior.


```python
def setup():
    size(400, 400)
    pontos = [(50, 50), (300, 370), (200, 50), (150, 150)]
    for i, ponto in enumerate(pontos):
        # enumerate vai nos entregar uma sequência de tuplas:
        # (índice, item_da_coleção)
        x, y = ponto  
        fill(255)
        ellipse(x, y, 5 + i * 5, 5 + i * 5)
        # legenda em um string no formato «i:  x, y»
        legenda = str(i) + ": " + str(x) + ", " + str(y)  
        fill(0)
        text(legenda, x + 15, y)

# Você também pode encontrar escrito assim: «for i, (x, y) in enumerate(pontos):»
# E a construção «legenda = "{}: {}, {}".format(i, x, y)» para o formar texto
# o método .format() injeta valores passados como argumentos em posições marcadas com {} 
```
![sketch_2020_04_10a](https://abav.lugaralgum.com/sketch-a-day/2020/sketch_2020_04_10a/enumerate.png)

## Assuntos relacionados

#### Desenhando grades com laços "aninhados" 

```python
for x in range(5, 100, 10):  # x: 5, 15, 25, 35 ... 95
  for y in range(5, 100, 10):  # y: 5, 15, 25, 35 ... 95
    ellipse(x, y, 5, 5) 
```
![mini grade](https://raw.githubusercontent.com/villares/material-aulas/master/Processing-Python/assets/mini-grid.png)

Veja mais em: [Grades retangulares: filas e colunas de elementos](grades.md)

#### Outra estrutura de repetição: `while`

[Laços de repetição com `while`](while.md) 

#### Acessando e alterando itens de uma sequência

[Mais sobre sequências e fatias](mais_sequencias.md)

### Glossário

[**loop**](https://penseallen.github.io/PensePython2e/04-caso-interface.html#termo:loop) **(laço)** Parte de um programa que pode ser executada repetidamente.

---
Este material é baseado no material do curso https://arteprog.space/programacao-criativa/

---
Texto e imagens / text and images: CC BY-NC-SA 4.0; Código / code: GNU GPL v3.0 exceto onde explicitamente indicado por questões de compatibilidade.
