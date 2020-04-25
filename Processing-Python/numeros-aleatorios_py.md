# Números aleatórios

## Mais precisamente números pseudo-aleatórios

Computadores são máquinas determinísticas e não conseguem realmente 'sortear' um número, por isso usam algorítmos (receitas) que produzem e números praticamente indistinguíveis, para a maioria dos usos<sup>[*](#footnote1)</sup>, de sequências verdadeiramente aleatórias. Por conta disso ganham este nome tecnicamente mais preciso de *pseudo-aleatórios* (falsos aleatórios). 

### A função `random()` do Processing

Cada vez que chamamos a função `random()` com um valor como em `sorteio = random(1);` um número entre zero e o argumento passado, que serve de limite superior, mas não está nele incluso, é produzido. 

![imagem_exemplo](assets/random1-10.png)

Se dois valores forem usados, por exemplo `random (-5, 5)` serão produzidos números entre -5 (incluso) e 5 (não incluso).
E podemos obter números inteiros convertendo o valor usando `int()`, como em `sorteio_inteiro = int(random(1, 11))` que 'sorteia' com igual probabilidades os números de 1 a 10.

#### Exemplos
```python
# Produz um valor entre 0 e 10 (10 não incluso)
sorteio = random(10)

# números entre -5 e 5 (exemplo: 3.91, -2.23, -1.2, 4.25 …) 
faixa = random(-5, 5)

# Produz um valor entre 0 e 20 convertido em inteiro (0, 1, 2 … 19)
d20 = int(random(20)) 
```
**Atenção:** *Este é o `random()` do Processing, o random do Python é um pouquinho diferente*

### O módulo `random` da biblioteca padrão do Python

Além de prover uma função `random()`, parecida com fornecida pelo Processing, da qual não vamos tratar aqui, o módulo `random` de Python nos oferece as funções `choice()`, `sample()`, e `shuffle()`.

#### selecionando um único item

A função `choice(colection)` devolve um item de uma coleção (tupla, lista, conjunto).

```python
from random import choice

cores = (color(200, 0, 0), color(0, 200, 0), color(0, 0, 200))

def draw():um
    c = choice(cores) # sorteia uma cor da tupla cores
    fill(c)
    rect(25, 25, 50, 50)
```

![random_choice](assets/random_choice.gif)


#### selecionando uma amostra (sem repetição de itens)

*Sample* significa amostra, e usamos `sample(colection, k)` onde `k` é o tamanho da amostra (e não pode ser maior que tamanho da população) para obter uma lista com `k` itens.

```python
from random import sample

cores = (color(200, 0, 0),
         color(200, 200, 0),
         color(0, 200, 200),
         color(200, 0, 200),
         color(0, 200, 0),
         color(0, 0, 200))

# uma lista com duas cores
duas_cores = sample(cores, 2)

print(len(duas_cores))  # resultado: 2
```

#### Misturando a ordem de uma sequência mutável

Ao executar `shuffle(sequence)` fazemos com que `sequence`, que não pode ser uma sequência vazia, seja reordenada.

```python
from random import shuffle

letras = ['A', 'B', 'C', 'D', 'E']

shuffle(letras)

print(letras)

# a cada execução uma ordem diferente:
# ['C', 'B', 'D', 'A', 'E']
# ['D', 'C', 'E', 'B', 'A']
# ...
```
A coleção precisa ser ordenada e mutável, como uma lista, não pode ser uma tupla, que é imutável, ou um conjunto que não guarda a ordem dos elementos.

### Mais sobre pseudo-aleatoriedade, sementes.

Como os números produzidos por `random()` não são verdadeiramente aleatórios, e sim produzidos por algorítmos geradores determinísticos, é possível fixar um parâmetro inical, conhecido como semente (*seed*), o que permite reproduzir novamente a mesma sequência de números.

```
TODO:
- Exemplos mais visuais, caramba!
- Exemplo de randomSeed() e random.seed()
- noise() - merece uma página especial
```

---
<a name="myfootnote1">
* Para aplicações de seguraça da informação, como por exemplo gerar certos tipos de chaves criptográficas, é possível incluir 'fontes externas de entropia', de forma a garantir resultados mais imprevisíveis.

---
Este material é baseado no material do curso https://arteprog.space/programacao-criativa/

---
Texto e imagens / text and images: CC BY-NC-SA 4.0; Código / code: GNU GPL v3.0 exceto onde explicitamente indicado por questões de compatibilidade.
