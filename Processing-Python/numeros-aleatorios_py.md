# Números aleatórios

## Mais precisamente números pseudo-aleatórios

Computadores são máquinas determinísticas e não conseguem realmente 'sortear' um número, utilizamos algorítmos que produzem sequências de números praticamente indistinguíveis de sequências verdadeiramente aleatórias. Para certas aplicações de seguração, como gerar certos tipos de chaves criptográficas, é possível incluir 'fontes externas de entropia' de forma a tornar garantir resultados mais imprevisíveis.

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

Além de prover uma função `random()`, parecida com fornecida pelo Processing, da qual não vamos tratar aqui, o módulo `random` de Python nos oferece as funções `choice()` e `sample()`, que selecionam itens de uma coleção:

#### `elecionando um único item

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

```python
from random import sample

duas_Cores = sample

```

### Mais sobre pseudo-aleatoriedade, sementes.

Como os números produzidos por `random()` não são verdadeiramente aleatórios, e sim produzidos por algorítmos geradores determinísticos, é possível fixar um parâmetro inical, conhecido como semente (*seed*), o que permite reproduzir novamente a mesma sequência de números.

```
TODO:
- Exemplos visuais, caramba!
- Exemplo de randomSeed() e random.seed()
```

---
Este material é baseado no material do curso https://arteprog.space/programacao-criativa/

---
Texto e imagens / text and images: CC BY-NC-SA 4.0; Código / code: GNU GPL v3.0 exceto onde explicitamente indicado por questões de compatibilidade.
