# Mais aleatoriedade

### A função `random()` do Processing

Vamos começar revisando a  função `random()` do Processing, uma vez que o *random* em Python é um pouquinho diferente, como veremos mais abaixo.

Cada vez que chamamos a função `random()` com um valor de argumento, como em `sorteio = random(1);` um número entre zero e o argumento passado (servindo de limite superior, mas não incluso) é produzido. 

![imagem_exemplo](assets/random1-10.png)

Se dois valores forem usados, por exemplo `random (-5, 5)` serão produzidos números entre -5 e 5 (não incluso).
E podemos obter números inteiros convertendo o valor usando `int()`, como em `sorteio_inteiro = int(random(1, 11))` que 'sorteia' com igual probabilidades os números de 1 a 10.

### O módulo `random` da biblioteca padrão do Python

No Python `random()` precisa ser importado do módulo `random` com a instrução `from random import random`, ela não recebe argumentos (isto é não vai nada dentro dos parênteses) e devolve o equivalente a `random(1)` no Processing, por isso não nos parece tão simpática e útil. 

Mas o módulo `random` de Python nos oferece outras funções muito simpáticas, quer dizer, interessantes: `choice()`, `sample()`, e `shuffle()`.

#### selecionando um único item

A função `choice(colection)` devolve um item de uma coleção (tupla, lista, conjunto). Para cada execução um item é escolhido (pseudo-)aleatoriamente.

```python
from random import choice

frutas = ("uva", "jaca", "melancia", "ubu", "pitanga")
sorteio = choice(frutas)
print(sorteio)
# Um resultado possível no console:
# jaca
```

Veja também outro exemplo, mais visual.

```python
from random import choice

cores = (color(200, 0, 0), color(0, 200, 0), color(0, 0, 200))

def draw():
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

Ao executar `shuffle(minha_sequencia)` fazemos com que `minha_sequencia`, que, atenção, não pode ser uma sequência vazia, seja reordenada 'aleatoriamente'.

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

###  Sementes dos geradores pseudo-aleatórios (*randomSeed*)

Como os números produzidos por `random()` não são verdadeiramente aleatórios, e sim produzidos por algorítmos geradores determinísticos, é possível fixar um parâmetro inical, conhecido como semente (*seed*), o que permite reproduzir novamente a mesma sequência de números.

Para fixar o início do gerador de `random()` no Processing usamos `randomSeed(numero_inteiro)`. 

Já para as funções do módulo `random` do Python:

```python
from random import seed
seed(numero_inteiro)
```

[ FALTA UM EXEMPLO LEGAL]

---
Texto e imagens / text and images: CC BY-NC-SA 4.0; Código / code: GNU GPL v3.0 exceto onde explicitamente indicado por questões de compatibilidade.
