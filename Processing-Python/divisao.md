## Divisão com inteiros no Processing modo Python

Python 2 e Python 3 tem um comportamento padrão um pouco diferente para divisão de dois números inteiros (valores do tipo `int`), o que pode ser um tanto surpreendente!

Como o Processing modo Python é um Python 2 por padrão vamos ter o seguinte resultado:

```python
a = 5 / 2
print(a)
# resultado: 2 
```

Pasta contornar isso temos algumas estratégias. A primeira, no caso dos números estarem diretamente no código é indicar que os valores são `float` com um ponto decimal: `2.0` ou `2.`:

```python
a = 5 / 2.0  # ou 5. / 2 entre outros
print(a)
# resultado: 2.5 
```



É possível trazer para o nosso uso alguns poucos comportamentos de Python 3, o Python do futuro, utilizando logo na primeira linha de um *sketch*, ou de um módulo `.py`, uma instrução na forma `from __future__ import ...`.

### Literais Unicode

Para poder definir *strings* no código com texto entre aspas, chamadas literais *string*, contendo caracteres não-ASCII, como por exemplo caracteres acentuados, é preciso prefixá-las com `u` (indicando Unicode) em Python 2. Como no exemplo: `fruta = u'maçã'` 

Python 3 considera por padrão *strings* definidas no corpo do código com texto entre aspas como sendo Unicode:

```python
from __future__ import unicode_literals

fruta = 'maçã'
```

### Divisão 

No Python 2:
```python
a = 3 / 2  # a = 1

# ou
a = 3 / 2. # a = 1.5

```

No Python 3:

```python
from __future__ import division

a = 3 / 2  # a = 1.5

# ou
a = 3 // 2  # a = 1
```

### Função print()

Python 2:

```python
print a
```

Python 3:

```python
from __future__ import print_function

print(a, end = ' ')
```
