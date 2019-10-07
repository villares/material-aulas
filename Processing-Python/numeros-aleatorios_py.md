# Números (pseudo)aleatórios

Cada vez que chamamos a função `random()` com um parâmetro, como em `sorteio = random(1);` um número entre zero e o parâmetro passado, o limite superior, é "sorteado" (não incluido este limite superior no sorteio).

Se dois parâmetros forem usados, por exemplo `random (-5, 5)` serão sorteados números entre -5 (incluso) e 5 (não incluso).
E podemos obter números inteiros convertendo o valor usando `int()`, como em `sorteio_inteiro = int(random(1, 11))` que sorteia com igual probabilidades os números de 1 a 10.


### Exemplos
```python
# Produz um valor entre 0 e 10 (10 não incluso)
sorteio = random(10)

# números entre -5 e 5 (exemplo: 3.91, -2.23, -1.2, 4.25 …) 
faixa = random(-5, 5)

# Produz um valor entre 0 e 20 convertido em inteiro (0, 1, 2 … 19)
d20 = int(random(20)) 
```

---
Este material é baseado no material do curso https://arteprog.space/programacao-criativa/

---
Texto e imagens / text and images: CC BY-NC-SA 4.0; Código / code: GNU GPL v3.0 exceto onde explicitamente indicado por questões de compatibilidade.
