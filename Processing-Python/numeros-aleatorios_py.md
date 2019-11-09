# Números (pseudo)aleatórios

Cada vez que chamamos a função `random()` com um parâmetro, como em `sorteio = random(1);` um número entre zero e o parâmetro passado, o limite superior, é "sorteado" (não incluido este limite superior no sorteio).

![imagem_exemplo](assets/random1-10.png)

Se dois parâmetros forem usados, por exemplo `random (-5, 5)` serão sorteados números entre -5 (incluso) e 5 (não incluso).
E podemos obter números inteiros convertendo o valor usando `int()`, como em `sorteio_inteiro = int(random(1, 11))` que sorteia com igual probabilidades os números de 1 a 10.

**Atenção:** *Este é o `random()` do Processing, o random do Python é um pouquinho diferente*

### Exemplos
```python
# Produz um valor entre 0 e 10 (10 não incluso)
sorteio = random(10)

# números entre -5 e 5 (exemplo: 3.91, -2.23, -1.2, 4.25 …) 
faixa = random(-5, 5)

# Produz um valor entre 0 e 20 convertido em inteiro (0, 1, 2 … 19)
d20 = int(random(20)) 
```

### Pseudo-aleatoriedade

Os números produzidos por `random()` não são verdadeiramente aleatórios, eles são produzidos por algorítmos geradores determinísticos. É possível fixar um parâmetro inical, conhecido como semente (*seed*), para a geração de uma sequência fixa de números.

---
Este material é baseado no material do curso https://arteprog.space/programacao-criativa/

---
Texto e imagens / text and images: CC BY-NC-SA 4.0; Código / code: GNU GPL v3.0 exceto onde explicitamente indicado por questões de compatibilidade.
