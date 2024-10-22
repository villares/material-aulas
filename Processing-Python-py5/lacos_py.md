# Repetição com laços `for`

É muito comum em programação pedir ao computador que repita uma ação várias vezes, possivelmente com variações. Para fazer isso frequentemente usamos os chamados laços de repetição (*loops*) e o processo de repetir operações também é por vezes chamado de iteração (note que não é i**n**teração, que é outra coisa).

Usando a estrutura `for` podemos fazer uma ação para cada item de uma coleção 'iterável', como as estruturas de dados que veremos depois, ou para cada item produzido por um gerador,  cada linha de um leitor de arquivos, ou ainda para cada número entregue por uma faixa de inteiros criada com `range()`.  

Em cada ciclo um item é atribuido a uma variável, cujo nome vem logo após o `for` e antes do `in`. No bloco indentado de código, também conhecido como o *corpo*, acontecem ações, quase sempre usando o valor do item atribuído à variável no início de cada ciclo. 

```python
for «variavel» in «iterável»:
    «corpo»
```
## Andando por uma coleção de elementos

Uma das estruturas de dados mais versáteis do Python são as listas, podemos criar uma lista no código envolvendo elementos separados por vírgulas em colchetes, como no exemplo abaixo uma lista de números chamada `tamanho`.

```python
size(200, 200)
no_fill()         # formas sem preenchimento
rect_mode(CENTER) # desenhar retângulos e quadrados pelo centro

tamanhos = [20, 40, 80, 160]
for t in tamanhos:
    square(100, 100, t)
```
![](assets/for_t_in_tamanhos.png)

## Produzindo sequências de inteiros com `range()`

### Você consegue imaginar o resultado do código a seguir?

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

A função embutida `range()` do Python produz um "objeto range", poderíamos talvez traduzir *range* como "faixa"; esses objetos especiais que são "faixas de números inteiros" podem ser usados nos laços `for`. Uma maneira de ver exatamente os números, exibindo com a função `print()`, é convertertendo estes objetos em listas com `list(range(n))`. Usando `range()` com o argumento 10, `range(10)`, no código abaixo, vamos obter uma lista de 10 números inteiros.

```python
print(list(range(10)))
```

#### Você consegue imaginar como é essa lista?
<details>
  <summary>clique para ver a resposta</summary>

<code>[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]</code>
</details>

#### Qual você acha que é o resultado de usar `range(1, 11)`?

```python
print(list(range(1, 11)))
```

<details>
  <summary>clique para ver a resposta</summary>

<code>[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]</code>

Podemos usar <code>range(parada)</code> ou <code>range(inicio, parada)</code>, o número início está incluso, o número de parada não está incluso. Há ainda a forma  <code>range(inicio, parada, passo)</code> que veremos mais adiante.

</details>


### Sobre os nomes das variáveis usadas no `for` e "repetições simples"

É tradicional usar certos nomes de variável `i`, `j` e `k`, por exemplo, para armazenar números de 'contadores' ou 'índices' que vão variando a cada volta do laço `for`.

![image](assets/for_i_in_range.png)

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

## Mais exemplos com `range()`

Veja a seguir mais alguns exemplos com o resultado oculto para você tentar resolver antes de olhar.

#### Linhas

Agora outro exemplo usando `range()` com efeito visual.

```python
for i in range(14):
    y = 10 + 5 * i
    line(30, y, 80, y)
```

#### Quais serão os valores de y e como fica o desenho das linhas?
<details>
  <summary>clique para ver os resultados</summary>

<img src= "assets/lines.png">

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

<img src="assets/verticais.png">
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

<img src="assets/verticais.png">
</details>


## Um pouco mais sobre listas e tuplas

A principal diferença, além do fato de que uma lista é construida com colchetes `[ ,]`, e uma tupla é construída com uma ou mais vírgulas apenas, se necessário em envolta em parenteses `( ,)`, é que uma lista permite que seus itens sejam alterados, itens podem ser adicionados, removidos, ou, como um todo, podem ser reordenados. Dizemos que uma lista é *mutável*. Já uma tupla não pode ter itens removidos, addicionados ou ser reordenada, dizemos que ela é *imutável* (mesmo se um item puder ter o seu conteúdo mais interno alterado). Se for necessária uma correção, podemos criar uma nova tupla com a alteração em substituição da original. 

```python
# Uma lista de nomes de frutas
frutas = ['uva', 'banana']
frutas.append('jaca')  # append acrescenta um item no final da lista
print(frutas) 
# Resutado exibido no console: ["uva", "banana", "jaca"]

frutas[0] = 'kiwi'  # 0 é o índice do primeiro item da lista
print(frutas) 
# Exibe: ['kiwi', 'banana', 'jaca']

# consultando um item pelo índice
print(frutas[1]) 
# Exibe: banana

del frutas[1]
print(frutas) 
# Exibe: ['kiwi', "jaca']

# Uma tupla de cantores sertanejos
cantores = 'Milionário', 'José Rico'
print(cantores)
# Exibe: ('Milionário', 'José Rico')

cantores.append('Zezé')
# Exibe: Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
# AttributeError: 'tuple' object has no attribute 'append'
```

As tuplas, em certos contextos computacionais, são mais eficientes que as listas, ocupam menos espaço na memória, por exemplo, não que você precise se preocupar com isso neste momento. É mais interessante, por enquanto, considerar que são bastante convenientes quando a ordem dos elementos tem significado, por exemplo, podemos fazer uma tupla com coordenadas x e y, a primeira posição 'significa' (a ordem indica) um valor no eixo X e a segunda posição indica um valor no eixo Y:

```python
posicao = (150, 50)  #  x: 150 y: 50

print(posicao[0])  # exibe 150
print(posicao[1])  # exibe 50
```

Um outro termo usado para se referir a uma coleção em que a ordem importa e não faz sentido reordenar é 'registro', se temos tuplas com nomes, emails e telefones, por exemplo, como uma linha em uma planilha.

Podemos 'desempacotar' uma tupla, atribuindo os seus valores a variáveis, desde que o número de variáveis seja igual ao número de itens:

```python
posicao = 250, 120  # ou posição = (250, 120) 
x, y = posicao # x passa a valer 250 e y passa a valer 120

# mais simples, mas com o mesmo resultado, do que escrever:
# x = posicao[0]  
# y = posicao[1]  
```

## Juntando as coisas

E é possível fazer tuplas com tuplas dentro, listas com listas dentro, listas com tuplas dentro e etc. Vamos experimentar fazer uma lista de tuplas representando as coordenadas de alguns pontos:

```python
pontos = [(10, 10), (100, 20), (200, 50), (50, 150)]
```

#### Qual é o resultado de `print(pontos[3])`?
<details>
  <summary>clique para ver a resposta</summary>

<code>(50, 150)</code>

</details>
 
### Iterando pelos dados

Finalmente vamos usar a estrutura de iteração, o *loop* `for`, para repetir a ação de desenhar um círculo, usando as coordenadas das tuplas de coordenadas na lista `pontos`:

```python
size(400, 400)
pontos = [(10, 10), (100, 20), (200, 50), (50, 150)]
for t in pontos:
    x, y = t # 'desempacotando' a tupla (x, y)
    circle(x, y, 15)
```

ou ainda podemos escrever abreviadamente assim:

```python
size(400, 400)
pontos = [(50, 50), (300, 370), (200, 50), (150, 150)]
for x, y in pontos:
    circle(x, y, 15)
```

![resultado](assets/for_lista_de_tuplas.png)

## Assuntos relacionados

#### Desenhando grades com laços "aninhados" 

[Grades retangulares: filas e colunas de elementos](grades.md)

```python
for x in range(5, 100, 10):  # x: 5, 15, 25, 35 ... 95
    for y in range(5, 100, 10):  # y: 5, 15, 25, 35 ... 95
        ellipse(x, y, 5, 5) 
```
![mini grade](assets/mini-grid.png)

#### Mais sobre sequências e fatias

[Tuplas e listas, mais sobre iterar sobre estruturas de dados e enumerar elementos](lacos_py.md)

#### Outra estrutura de repetição: `while`

[Laços de repetição com `while`](while.md) 

### Glossário

[**loop**](https://penseallen.github.io/PensePython2e/04-caso-interface.html#termo:loop) **(laço)** Parte de um programa que pode ser executada repetidamente.
