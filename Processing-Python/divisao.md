## Divisão com inteiros no Processing modo Python

Em computação existe uma classificação dos valores armazenados na memória do computador, dizemos que os valores tem um *tipo*. Valores numéricos em Python são, na maior parte das vezes, dos tipos ***inteiro*** (abreviamos `int`), ***ponto flutuante*** (que tem uma parte fracionária, e abreviamos `float`) ou ***número complexo*** (`complex`, sendo `1j` a raiz quadrada de -1).

Em diferentes versões da linguagem Python (Python 2 e Python 3) temos um comportamento diferente para a divisão de dois números inteiros (`int`) e que pode ser  um tanto surpreendente!

Como o Processing modo Python é um Python 2, por padrão, vamos ter o seguinte resultado:

```python
a = 5 / 2
print(a)
# resultado: 2 
```

Isso raramente é o que queremos, então, temos algumas estratégias para obter como resultado um número *de ponto flutuante* (`float`) . Primeiro, no caso dos números estarem diretamente no código é possível indicar que os valores são `float` com um ponto decimal (`2.0` ou `2.`)  e no caso de variáveis podemos pedir uma conversão com `float()`:

```python
a = 5 / 2.0  # ou 5. / 2 ou 5. / 2. ou 5 / 2.
print(a)
# resultado: 2.5 

b = 2
a = 5 / float(b)
# resultado: 2.5 

```

Podemos também obter o comportamento de Python 3 para a divisão utilizando, **logo na primeira linha de um *sketch***, ou de um módulo `.py`, a  linha `from __future__ import division` . Note o duplo *underscore*, `_` antes e depois da palavra  *future*, e não pode haver outras instruções antes dessa linha (exceto comentários que não contam como instruções):

```
# Exemplo de como fazer a divisão ficar como no Python 3
from __future__ import division

a = 5 / 2
print(a)
# resultado: 2.5

# Para a divisão com resultado inteiro (floor division) use //
a = 5 // 2
print(a)
# resultado: 2
```

### Glossário

[**tipo**](https://penseallen.github.io/PensePython2e/01-jornada.html#termo:tipo) Uma categoria de valores. Alguns tipos que vimos por enquanto são números inteiros (tipo `int`), números de ponto flutuante (tipo `float`) e *strings* (tipo `str`).

[**inteiro**](https://penseallen.github.io/PensePython2e/01-jornada.html#termo:inteiro) Um tipo que representa números inteiros.

[**ponto flutuante**](https://penseallen.github.io/PensePython2e/01-jornada.html#termo:ponto%20flutuante) Um tipo que representa números com partes fracionárias.

## Assuntos relacionados

+ [Valores e seus tipos](tipagem_py.md)

- Outras [diferenças entre Python 2 e Python 3](futuro.md)

