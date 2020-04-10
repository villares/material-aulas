# Números aleatórios

## Na verdade números pseudo-aleatórios

Computadores são máquinas determinísticas e não conseguem realmente 'sortear' um número, utilizamos na verdade algorítmos que produzem sequências de números praticamente indistinguíveis de sequências verdadeiramente aleatórias. Para certas aplicações é possível incluir 'fontes externas de entropia' para tornar ainda menos previsíveis os resultados.

### A função `random()` do Processing

Cada vez que chamamos a função `random()` com um parâmetro, como em `sorteio = random(1);` um número entre zero e o parâmetro passado, o limite superior, é "sorteado" (não incluido este limite superior no sorteio).

![imagem_exemplo](assets/random1-10.png)

Se dois parâmetros forem usados, por exemplo `random (-5, 5)` serão sorteados números entre -5 (incluso) e 5 (não incluso).
E podemos obter números inteiros convertendo o valor usando `int()`, como em `sorteio_inteiro = int(random(1, 11))` que sorteia com igual probabilidades os números de 1 a 10.

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

Além de prover uma função `random()`, parecida com fornecida pelo Processing, e que não vamos ver aqui, o módulo `random` de Python nos oferece a útil função `choice()` que sorteia itens de uma coleção:

```python
from random import choice

cores = (color(200, 0, 0), color(0, 200, 0), color(0, 0, 200))

def draw():
    c = choice(cores) # sorteia uma cor da tupla cores
    fill(c)
    rect(25, 25, 50, 50)
```

![random_choice](assets/random_choice.gif)

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
