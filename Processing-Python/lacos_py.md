# Sequências e repetições

Uma das coisas mais comuns que fazemos em programção é pedir ao computador para repetir uma ação varias vezes. Para fazer isso usamos muitas vezes os chamados laços de repetição (*loops*) e o processo também é chamado de iteração (note que não é i**n**teração, que é outra coisa).

Mas antes de chegar nas repetições é útil saber como criar rapidamente sequências de valores. Existe uma função que produz valores inteiros, o `range()`, que no Processing modo Python devolve uma lista (no Python 3 devolve um 'iterador' mas isso não importa agora).

## Produzindo sequências de inteiros com `range()`

Executando a função `range()` com o argumento 10, `range(10)`, vamos obter uma lista de 10 números inteiros, você consegue imaginar quais são?

A resposta é `[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]`

Usando a estrutura `for` podemos fazer uma ação para cada item de um 'iterável', o que inclui tuplas e listas. Em cada ciclo um item por vez da coleção é atribuido a uma variável, como neste exemplo:

```python
for n in range(10): # para cada número do range(10) 
    print(n)        # n vai ter um valor diferente a cada ciclo

# Resutado no console:
# 0
# 1
# 2
# ... suprimi pra não ficar muito longo
# 8
# 9
```

É tradicional usar certos nomes de variável `i`, `j` e `k`, por exemplo, para armazenar números de 'contadores' ou 'índices' que vão variando a cada volta do laço `for`.

Agora outro exemplo usando `range()` com efeito visual. Veja se consegue imaginar os valores de y e a sequência em que as linhas são desenhadas):

```python
for i in range(14):
    y = 10 + 5 * i
    line(30, y, 80, y)
```

![linhas paralelas](https://raw.githubusercontent.com/villares/material-aulas/master/Processing-Python/assets/lines.png)

A função `range()` aceita também argumentos na forma `range(início, parada, passo)`, *início* é o primeiro número fornecido, e a sequência para antes do número *parada*, aumentando com o número *passo*, veja este exemplo com o mesmo resultado visual do código anterior:

```python
for y in range(10, 80, 5): # y começa valendo 10 e termina valendo 75
    line(30, y, 80, y)     # y aumenta de 5 em 5
```

   Você conseguiria escrever um `for` para desenhar algumas linhas na vertical?

## Repetições simples

Algumas vezes nem vamos usar os números! Só queremos repetir a operação, então em vez de guardar o número em uma variável nomeada com `x`, `y`, `n` ou `i` usamos uma variável com o curioso nome`_` (*underscore*, ou como muitos falam 'underline'). Isso é uma dica de quem está escrevendo o código de que o valor da variável vai ser desprezado. Exemplo:

```python
for _ in range(3): # repita 3 vezes!
   print("viva!")
   
# resultado no console:
# viva!
# viva!
# viva!
``` 

## Um pouco sobre listas e tuplas

Vamos estudar agora duas estruturas de dados muito usadas em Python para guardar coleções ordenadas, ou sequências de valores: tupla (*tuple*) e lista (*list*).

Exemplo de uma tupla:

`tupla_sertaneja = ("Maiara", "Maraisa")`

Exemplo de uma lista:

`meus_pockemons = ["Fomantis", "Eevee"]`

A principal difereça, além do fato de que a tupla foi construída com parenteses `( ,)`e a lista com colchetes `[ ,]`, é que **uma lista permite que seus itens sejam alterados**, itens sejam adicionados, itens podem ser removidos, ou, os itens como um todo podem ser reordenados.

Já **uma tupla não pode ter itens removidos, addicionados ou ser reordenada**, dizemos que ela é *imutável* (mesmo se um item puder ter o seu conteúdo mais interno alterado). Se for necessária uma correção, podemos criar uma nova tupla com a alteração em substituição da original.

Tuplas são mais 'econômicas' em termos computacionais e são bastante usadas quando a ordem dos elementos tem significado, por exemplo podemos fazer uma tupla com coordenadas x e y, o primeiro item 'significa' um valor no eixo X e o segundo um valor no eixo Y:

```python
posicao = (150, 50)  #  x: 150 y: 50
```

Podemos 'desempacotar' uma tupla, atribuindo os seus valores a variáveis, desde que o número de variáveis seja igual ao número de itens:

```python
posicao = (100, 150) 
x, y = posicao # x passa a valer 100 e y 150
```

E é possível fazer tuplas com tuplas dentro, listas com listas dentro, listas com tuplas dentro e etc. Vamos experimentar fazer uma lista de tuplas representando as coordenadas de alguns pontos:

```python
pontos = [(10, 10), (100, 20), (200, 50), (50, 150)]
```

Finalmente vamos usar a estrutura de iteração, o loop `for` para repetir a ação de desenhar um círculo, usando as coordenadas das tuplas:

```python
def setup():
    size(400, 400)
    pontos = [(10, 10), (100, 20), (200, 50), (50, 150)]
    for t in pontos:
        x, y = t # 'desempacotando' a tupla (x, y)
        ellipse(x, y, 15, 15)
```

ou ainda podemos escrever assim:

```python
def setup():
    size(400, 400)
    pontos = [(50, 50), (300, 370), (200, 50), (150, 150)]
    for x, y in pontos:
        ellipse(x, y, 15, 15)
```

![resultado](https://i.imgur.com/TL0BBId.png)

## Outras ideias

### Laços "aninhados" par fazer uma grade

```python
for x in range(0, 80, 10):
  for y in range(0, 80, 10): 
    ellipse(x, y, 5, 5) 
```

### Glossário

[**loop**](https://penseallen.github.io/PensePython2e/04-caso-interface.html#termo:loop) **(laço)** Parte de um programa que pode ser executada repetidamente.

---
Este material é baseado no material do curso https://arteprog.space/programacao-criativa/

---
Texto e imagens / text and images: CC BY-NC-SA 4.0; Código / code: GNU GPL v3.0 exceto onde explicitamente indicado por questões de compatibilidade.
