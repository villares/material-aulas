# Números inteiros (*int*) e de ponto flutuante (*float*)

Em computação existem sistemas de classificação para valores armazenados na memória do computador, dizemos que os valores tem um *tipo*. Valores numéricos em Python são, na maior parte das vezes, dos tipos ***inteiro*** (abreviamos `int`), ***número de ponto flutuante*** (que tem uma parte fracionária, e abreviamos `float`) ou ***número complexo*** (`complex`, sendo `1j` a raiz quadrada de -1, que na escola costumamos chamar de *i*). Leia mais sobre isso em: [Tipos de valores(inteiros, números de ponto flutuante, texto(strings))](tipagem_py.md)

Veja este exemplo que mostra a divisão de dois números inteiros (*int*), `4` dividido por `10`. O resultado, `0.4`, é um número de ponto flutuante (*float*). Em programação a "vírgula" é um ponto.

```python
a = 4 / 10
print(a)
# resultado: 0.4
# Note que em Python o separador decimal é um ponto (.)
```

### Conversão em inteiros

Certas situações em Python exigem números inteiros, como, por exemplo,  ao se usar `for n in range(inicio, parada):`, os valores de `inicio` e `parada` precisam ser números inteiros.

A forma mais comum de converter um número de ponto flutuante (`float`) em inteiros (`int`) é usando a função embutida `int()`. Mas note que `int()` simplesmente joga fora a parte depois do ponto, e não é como outros tipos de "arredondamento". Experimente usar a função embutida `round()`, que também devolve um número do tipo inteiro para ver o que acontece!

```python
a = int(10.654) 
print(a)
# resultado: 10

b = round(10.654)
print(b)         # Experimente e descubra!
# resultado: ?

# Experimente também...
print(round(10.5))
```

### A divisão no Python 3 e os números inteiros

Antigamente, no Python 2, uma divisão entre dois números inteiros era forçada a responder com um inteiro, o que surpreendia algumas vezes, por exemplo, `4 / 10` resultava `0`. Agora no Python 3 o resultado pode ser um número de ponto flutuante, como vimos ateriormente.

Para obter o comportamento próximo ao antigo é possível usar o operador `//` (*floor division*), se os operandos forem inteiros, o resultado será inteiro também, mas, se um deles for *float* o resultado, mesmo que "numericamente inteiro", será do tipo *float*. Uma outra solução, que garante um número do tipo *int*, pode ser converter o resultado da divisão usando `int()`.

```python
a = 5 // 2
print(a, type(a))
# resultado: 2 <class 'int'>

b = 5.0 // 2
print(b, type(b))
# resultado: 2.0 <class 'float'>

c = int(5 / 2)
print(c, type(c))
# resultado: 2 <class 'int'>
```

### O problema não muito visível dos números *float*

Pode parecer um pouco assustador o que você vai ler agora mas é bom saber que computadores, quando usamos Python e a maior parte das linguagens de programação, fazem "arredondamentos estranhos" ao armazenar na memória valores que pra nós parecem perfeitamente "redondos", isto é, de representação finita. A causa do problema é o fato de que muitos números que tem uma representação decimal finita (na base 10), como `1 / 10`, isto é, `0.1`, quando representados na memória do computador em binário (na base 2), usando *float* ([ponto flutuante](https://pt.wikipedia.org/wiki/V%C3%ADrgula_flutuante)), não tem uma representação finita equivalente.

Isso é parecido com a dificuldade da representação decimal de certas frações, como `1 / 3`, por exemplo, que representamos "0.33333...". Dizemos que é uma "dízima periódica", e, ao interrompermos os infinitos 3 depois da vírgula, no caso do Python o ponto, estamos fazendo uma representação aproximada. Não dá pra escrever infinitos números 3, não dá pra representar de maneira finita `1 / 3` como um número na base 10.

Veja o problema de forma mais explícita nesta soma e comparação de valores no Python.

```python
a = 0.1 + 0.1 + 0.1
b = 0.3
print(a == b)
# resultado: False
print(a)
# resultado: 0.30000000000000004
```

Não existem soluções simples para isso, mas, existem maneiras, um tanto elaboradas, de contornar o problema, usando os módulos [`decimal`](https://docs.python.org/pt-br/3.9/library/decimal.html) e [`fractions`](https://docs.python.org/pt-br/3.11/library/fractions.html) da biblioteca padrão do Python, só que não vamos discuti-las aqui.

No nosso contexto de desenho e geometria, em geral, é suficiente saber que não devemos contar com precisão absoluta, nem com o operador de igualdade (`==`) entre números *float*. O resultado de certas operações matemáticas com *float* que dependem de números de representação decimal finita, mas de representação binária *float* aproximada, torna-se uma (muito boa) aproximação. 

Veja como usar a função `isclose()` do módulo `math` da biblioteca padrão, em vez de uma comparação de igualdade.

```python
from math import isclose

a = 0.1 + 0.1 + 0.1
b = 0.3
print(isclose(a, b))
# resultado: True
```

Você pode ler mais sobre os problemas causados pela representação interna dos números decimais em binário no computador em [Aritimética de ponto flutuante: problemas e limitações](https://docs.python.org/pt-br/3/tutorial/floatingpoint.html).

## Glossário

[**tipo**](https://penseallen.github.io/PensePython2e/01-jornada.html#termo:tipo) Uma categoria de valores. Alguns tipos que vimos por enquanto são números inteiros (tipo `int`), números de ponto flutuante (tipo `float`) e *strings* (tipo `str`).

[**inteiro**](https://penseallen.github.io/PensePython2e/01-jornada.html#termo:inteiro) Um tipo que representa números inteiros.

[**ponto flutuante**](https://penseallen.github.io/PensePython2e/01-jornada.html#termo:ponto%20flutuante) Um tipo que representa números com partes fracionárias.

## Assuntos relacionados

- [Valores e seus tipos](tipagem_py.md)
- [Divisão por zero e o resto da divisão](divisao.md)
