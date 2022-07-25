# Python 2 e Python 3

from __future__ import unicode_literals
from __future__ import division
from __future__ import print_function
infelizmente o processing modo python depende de jython, uma implementação da linguagem python que está presa no python 2, que é um python do passado.

é possível trazer para o nosso uso alguns poucos comportamentos de python 3, o python do futuro, utilizando logo na primeira linha de um * sketch*, ou de um módulo `.py`, uma instrução na forma `from __future__ import ...`.

# Literais Unicode

para poder definir * strings * no código com texto entre aspas, chamadas literais * string*, contendo caracteres não-ASCII, como por exemplo caracteres acentuados, é preciso prefixá-las com `u` (indicando unicode) em python 2. como no exemplo: `fruta = u'maçã'`

python 3 considera por padrão * strings * definidas no corpo do código com texto entre aspas como sendo unicode:

```python

fruta = 'maçã'
```

# Divisão

no python 2:
```python
a = 3 / 2  # a = 1

# ou
a = 3 / 2.  # a = 1.5

```

no python 3:

```python

a = 3 / 2  # a = 1.5

# ou
a = 3 // 2  # a = 1
```

# Função print()

python 2:

```python
print a
```

python 3:

```python

print(a, end=' ')
```
