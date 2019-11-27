# Python 2 e Python 3

Infelizmente o Processing modo Python depende de Jython, uma implementação da linguagem Python que está presa no Python 2, é um Python do passado.

É possível trazer para o nosso uso alguns poucos comportamentos de Python 3, o Python do futuro, utilizando logo na primeira linha de um *sketch*, ou de um módulo `.py`, uma instrução na forma `from __future__ import ...`.

### Literais Unicode

Para poder usar *strings* cujo texto contém caracteres não-ASCII, em Python 2 é preciso prefixá-los com `u` (indicando Unicode). Como no exemplo:  `fruta = u'maçã'` 

O comportamento padrão em Python 3 é considerar os *strings* como sendo Unicode:

```python
from __future__ import unicode_literals

fruta = 'maça'
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
