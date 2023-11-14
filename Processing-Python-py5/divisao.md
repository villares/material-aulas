<h1 id='toc'></h1>

# Divisão, números de ponto flutuante, inteiros, divisão por zero e o resto da divisão

## Divisão no Python 3 e os números inteiros

> #### Um pouco de contexto
>
> Em computação existem sistemas de classificação para valores armazenados na memória do computador, dizemos que os valores tem um *tipo*. Valores numéricos em Python são, na maior parte das vezes, dos tipos ***inteiro*** (abreviamos `int`), ***número de ponto flutuante*** (que tem uma parte fracionária, e abreviamos `float`) ou ***número complexo*** (`complex`, sendo `1j` a raiz quadrada de -1, que na escola costumamos chamar de *i*). Leia mais sobre isso em: [Tipos de valores(inteiros, números de ponto flutuante, texto(strings))](tipagem_py.md)

Veja este exemplo que mostra a divisão de dois números inteiros (*int*), `4` dividido por `10`. O resultado, `0.4`, é um número de ponto flutuante (*float*). Em programação a "vírgula" é um ponto.

```python
a = 4 / 10
print(a)
# resultado: 0.4
```

Antigamente, no Python 2, uma divisão entre dois números inteiros era forçada a responder com um inteiro, o que surpreendia algumas vezes, por exemplo, `4 / 10` resultava `0`. Agora no Python 3 o resultado pode ser um número de ponto flutuante, como vimos no exemplo anterior. Para obter o comportamento antigo, da divisão com resultado inteiro, use o operador `//` (*floor division*).

```python
a = 5 // 2
print(a)
# resultado: 2
```

> #### Conversão em inteiros
> 
> Certas situações em Python exigem números inteiros, como, por exemplo,  ao se usar `for n in range(inicio, parada):`. `inicio` e `parada` precisam ser números inteiros.
> A forma mais comum de converter um número de ponto flutuante (`float`) em inteiros (`int`) é usando a função embutida `int()`. Mas note que isso simplesmente joga fora a parte depois do ponto, e não é como outros tipos de "arredondamento". Experimente usar `round()` para ver o que acontece!
> 
> ```python
> a = int(10.654)  # Note que eum programação o separador decimal é um ponto (.)
> print(a)         # Exibe como resultado: 10
> b = round(10.654)
> print(b)         # Experimente e descubra!
> # resultado: ?
> # Experimente também print(round(10.5))...
> ```

## O problema dos números *float*

É uma coisa um pouco assustadora, mas, o Python, assim como a maior parte das linguagens de programação, fazem "arredondamentos estranhos" em valores que pra nós parecem perfeitamente "redondos", isto é, de representação finita. A causa do problema é que muitos números que tem uma representação finita em decimal, como `1 / 10`, isto é `0.1`, quando representados em binário na memória do computador, como *float*, não tem uma representação finita.

Isso é parecido com a dificuldade da representação decimal de certas frações, como `1 / 3`, por exemplo, que representamos "0.33333...". Dizemos que é uma "dízima periódica", e, ao interrompermos os infinitos 3 depois da vírgula, no caso do Python o ponto, estamos fazendo uma representação aproximada. Não dá pra escrever infinitos números 3, não dá pra representar de maneira finita como um número na base 10.

Veja o problema de forma mais explícita nesta soma e comparação de valores no Python.

```python
a = 0.1 + 0.1 + 0.1
b = 0.3
print(a == b)
# resultado: False
print(a)
# resultado: 0.30000000000000004
```

Existem maneiras um tanto elaboradas de contornar esse problema, usando os módulos `decimal` e `fraction` da biblioteca padrão do Python, mas no nosso contexto de desenho e geometria, em geral, é suficiente saber que não devemos contar com precisão absoluta, ou com o operador de igualdade (`==`) entre números *float*. O resultado de certas operações matemáticas com *float* que derivam de certos números é uma (muito boa) aproximação. 

Veja como usar a função `isclose()` do módulo `math` da biblioteca padrão, em vez de uma comparação de igualdade.

```python
from math import isclose

a = 0.1 + 0.1 + 0.1
b = 0.3
print(isclose(a, b))
# resultado: True
```

Você pode ler mais sobre os problemas causados pela representação interna dos números decimais em binário no computador em [Aritimética de ponto flutuante: problemas e limitações](https://docs.python.org/pt-br/3/tutorial/floatingpoint.html).

## O problema da divisão por zero (e um pouco sobre tratamento de exceções)

Provavelmente você se lembra que o resultaddo de dividir um número por zero é em geral considerado um valor "indefinido" na maior parte dos contextos matemáticos. Em Python se o seu programa for obrigado a avaliar essa conta ele vai parar tudo e "levantar uma exceção" chamada `ZeroDivisionError`.

> Exceções são um tipo de erro que é diferente dos erros de sintaxe, você também pode encontrá-as descritas como "erros em tempo de execução". Lidar com elas é às vezes inescapável, um procedimento conhecido como "captura" ou "tratamento" de exceções. Pra dar uma idea do que estamos falando, imagine que você pediu ao Python para gravar um arquivo no seu computador, mas o sistema operacional avisou que não foi possível (acabou o espaço, por exemplo, ou o caminho indicado da pasta não existe), acontecerá um `IOError`, e se o programa não foi preparado para tratar esse tipo de exceção graciosamente com um aviso para a pessoa que pediu a gravação, sua execução vai ser interrompida.

Voltando para a questão da divisão por zero, imagine que você tem no meio do seu programa uma divisão mas o número que divide, o denominador, é variável e de vez em quando ele pode ser zero, como se proteger da interupção do seu programa?

Isso pode acontecer, do denominador variar, por diversos motivos, por ele ser resultado de uma outra conta que varia, por depender de dados externos, da posição do mouse ou de uma resposta da pessoa usando o programa!

Uma maneira de resolver é testar antes de qualquer divisão cujo denominador varia se ele vale 0 (ou se não vale 0) e propor uma execução que não dependa dessa operação de divisão caso ele seja 0:

```python
if denomidador == 0:   # se denominador é igual a 0
    resultado = 1000000 
else:
    resultado = 10 / denominador
```
Ou o equivalente

```python
if denomidador != 0:   # se denominador não é igual a 0, != significa "é diferente de"
    resultado = 10 / denominador
else:
    resultado = 1000000
```

Uma outra maneira, talvez mais sofisticada, é usar uma estrutura para exceções do Python, que futuramente vai servir em casos como erros na manipulação de arquivos e outros em que você precisa "tentar" fazer a operação que pode não funcionar (que pode "levantar uma exceção"):

```python
try:
    resultado = 10 / denominador
except ZeroDivisionError:
    resultado = 1000000
```
### Uma outra maneira, malandra

Quando você sabe que os valores do denomidador nunca ficam negativos, e o resultado da divisão pode ser um número aproximado, é possível somar algum valor que apenas impeça o denomidador de ser zero.

```python
tangente_aproximada = dy / (0.01 + distancia)

fator_de_crescimento = 1 / (1 + mouse_x)  # o resultado é no mínimo 1 e sem divisão por zero pois mouse_x nunca fica negativo
```

## Agora a parte divertida! O resto da divisão

Em inglês a operação para obter o resto da divisão com inteiros tem o nome de *modulo* ou *modulus* o que pode causar uma grande confusão pois na matemática em português a palavra 'módulo' com a notação `|num|` é usada também para falar do valor absoluto (sem o sinal) de um número (em programação usamos `abs()` para isso), e em Python módulo é o nome de pedaço organizado de uma *biblioteca de funções de programação*, em geral um arquivo `.py`.

Mas estamos falando então aqui do resto da divisão com inteiros. "Quantas vezes o 3 cabe no 7? duas! e sobra quanto? 1".
O resto da divisão nos inteiros de 7 por 3 é 1. Em Python obtemos esse valor com o operador `%`.

```python
resto = 7 % 3
print(resto)  # exibe: 1
```
E essa operação é **extremamente útil**, para saber se um número é par ou ímpar, se é divisível por um certo número ou para produzir sequencias que se repetem!

##### Testando se um número é par
```python
if a % 2 == 0:
    print('a é par!')
else:
    print('a é impar!')
```
#### Testando se um número é divisível por outro
```python
if a % b == 0:
    print('a é divisível por b!')
else:
    print('a não é divisível por b!')
```
#### Mantendo os números circulando até um valor máximo

Para qualquer valor de **a**, o resultado da expressão **a % b** sempre é menor que **b**, e no máximo vale **b - 1**.
Podemos usar **n % max** em uma sequencia crescente de números **n** para obter uma sequência de números com repetição periódica da seguinte maneira:

```python
for n in range(10):  # pegue um n para cada número de 0 a 9
   print(n % 2)      # exiba no console o resto da divisão de n por 2
```
Resultado:
```
0
1
0
1
0
1
0
1
0
1
```
Outro exemplo.
```python
for n in range(100):  # pegue um n para cada número de 0 a 99
   print(n % 5)       # exiba no console o resto da divisão de n por 5
```
Resultado (truncado, seriam 100 números):
```
0
1
2
3
4
0
1
2
3
4
0
1
…
4
```

## Glossário

[**tipo**](https://penseallen.github.io/PensePython2e/01-jornada.html#termo:tipo) Uma categoria de valores. Alguns tipos que vimos por enquanto são números inteiros (tipo `int`), números de ponto flutuante (tipo `float`) e *strings* (tipo `str`).

[**inteiro**](https://penseallen.github.io/PensePython2e/01-jornada.html#termo:inteiro) Um tipo que representa números inteiros.

[**ponto flutuante**](https://penseallen.github.io/PensePython2e/01-jornada.html#termo:ponto%20flutuante) Um tipo que representa números com partes fracionárias.

## Assuntos relacionados

- [Valores e seus tipos](tipagem_py.md)


