## Divisão com inteiros

### Um pouco de contexto

Em computação existem sistemas de classificação para valores armazenados na memória do computador, dizemos que os valores tem um *tipo*. Valores numéricos em Python são, na maior parte das vezes, dos tipos ***inteiro*** (abreviamos `int`), ***ponto flutuante*** (que tem uma parte fracionária, e abreviamos `float`) ou ***número complexo*** (`complex`, sendo `1j` a raiz quadrada de -1, que na escola costumamos chamar de *i*).

#### Conversão em inteiros

A forma mais comum de converter um número de ponto flutuante (`float`) em inteiros (`int`) é usando a função embutida `int()`. Mas note que isso simplesmente joga fora a parte depois da vírgula (que em programação é um ponto!) e não é como outros tipos de 'arredondamento' (experimente usar `round()` para ver o que acontece...).

```python
a = int(10.654)  # note que eum programação o separador decimal é um ponto (.)
print(a)         # exibe como resultado: 10
```

### O problema da divisão estranha no Processing modo Python

Em diferentes versões da linguagem Python (Python 2 e Python 3) temos um comportamento diferente para a divisão de dois números inteiros (`int`) e que pode ser  um tanto surpreendente!

Como o Processing modo Python é um Python 2, por padrão, vamos ter o seguinte resultado:

```python
a = 4 / 10
print(a)
# resultado: 0
```

Isso raramente é o que queremos, então, temos algumas estratégias para obter como resultado um número `float`. Primeiro, no caso dos números estarem diretamente no código é possível indicar que os valores são `float` com um ponto decimal (`4.0` ou `4.`)  e no caso de variáveis podemos pedir uma conversão usando `float()`:

```python
a = 4 / 10.0  # ou 4. / 10 ou 4. / 10. ou 4 / 10.
print(a)
# resultado: 0.4 
```
Se os números são o resultado de outras operações e vão ser referenciados por meios de variáveis.

```python
b = 10
a = 4 / float(b)
# resultado: 0.4 

d = float(n) / float(m)
# Para n = 5 e m = 20 o resultado é 0.25
```

Podemos também obter o comportamento de Python 3 para a divisão utilizando, **logo na primeira linha de um *sketch***, ou de um módulo (um arquivo `.py`), a  linha `from __future__ import division` . Note o duplo *underscore*, `_` antes e depois da palavra  *future*, e não pode haver outras instruções antes dessa linha (exceto comentários que não contam como instruções):

```
# Exemplo de como fazer a divisão ficar como no Python 3
from __future__ import division

a = 4 / 10
print(a)
# resultado: 0.4

# Para a divisão com resultado inteiro (floor division) use //
a = 5 // 2
print(a)
# resultado: 2
```

### O problema da divisão por zero (e um pouco sobre tratamento de exceções)

Provavelmente você se lembra que o resultaddo de dividir um número por zero é em geral considerado um valor "indefinido" na maior parte dos contextos matemáticos. Em Python se o seu programa for obrigado a avaliar essa conta ele vai parar tudo e "levantar uma exceção" chamada `ZeroDivisionError`.

> Exceções são um tipo de erro que é diferente dos erros de sintaxe, você também pode encontrá-as descritas como "erros em tempo de execução". Lidar com elas é às vezes inescapável, um procedimento conhecido como "captura" ou "tratamento" de exceções. Pra dar uma idea do que estamos falando, imagine que você pediu ao Python para gravar um arquivo no seu computador, mas o sistema operacional avisou que não foi possível (acabou o espaço, por exemplo, ou o caminho indicado da pasta não existe), acontecerá um `IOError`, e se o programa não foi preparado para tratar esse tipo de exceção graciosamente com um aviso para a pessoa que pediu a gravação, sua execução vai ser interrompida.

Voltando para a questão da divisão por zero, imagine que você tem no meio do seu programa uma divisão mas o número que divide, o denominador, é variável e de vez em quando ele pode ser zero, como se proteger da interupção do seu programa?

Isso pode acontecer, do denominador variar por diversos motivos, ele é resultado de uma outra conta que varia, ele depende de dados externos, da posição do mouse ou de uma resposta da pessoa usando o programa ou ainda de um sorteio, por exemplo.

Uma maneira de resolver é testar antes de qualquer divisão cujo denominador varia, se ele vale 0 (ou se não vale 0) e propor uma execução que não dependa dessa operação de divisão caso ele seja 0:

```
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

Uma outra maneira, talvez mais sofisticada, é usar uma extrutura para exceções do Python, que futuramente vai servir em casos como erros na manipulação de arquivos e outros em que você precisa "tentar" fazer a operação que pode não funcionar (que pode "levantar uma exceção"):

```python
try:
    resultado = 10 / denominador
except ZeroDivisionError:
    resultado = 1000000
```

### Agora a parte divertida! O resto da divisão

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
##### Testando se um número é divisível por outro
```python
if a % b == 0:
    print('a é divisível por b!')
else:
    print('a não é divisível por b!')
```
##### Mantendo os números circulando até um valor máximo

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
- Outras [diferenças entre Python 2 e Python 3](futuro.md)

#### faltando...

- Erros causados pela representação interna dos números decimais em binário no computador
