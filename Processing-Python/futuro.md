# Python 2 e Python 3

Infelizmente o Processing modo Python depende de Jython, uma implementação da linguagem Python que está presa no Python 2, é um Python do passado.

É possível trazer para o nosso uso alguns poucos comportamentos de Python 3, o Python do futuro, utilizando logo na primeira linha de um *sketch*, ou de um módulo `.py`, uma instrução na forma `from __future__ impor ...`.

### Literais Unicode

Para poder usar *strings* cujo texto contém caracteres não-ASCII, em Python 2 é preciso prefixá-los com `u`. Como no exemplo:  `fruta = u"maçã"`

Ou, para evitar essa necessidade:

```python
from __future__ import unicode_literals

fruta = 'maça'
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
 