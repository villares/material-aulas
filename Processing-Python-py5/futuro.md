# Python 2 e Python 3




Infelizmente o Processing modo Python depende de Jython, uma implementação da linguagem Python que está presa no Python 2, que é um Python do passado.

É possível trazer para o nosso uso alguns poucos comportamentos de Python 3, o Python do futuro, utilizando logo na primeira linha de um * sketch*, ou de um módulo `.py`, uma instrução na forma `

# Literais Unicode

Para poder definir * strings * no código com texto entre aspas, chamadas literais * string*, contendo caracteres não-ASCII, como por exemplo caracteres acentuados, é preciso prefixá-las com `u` (indicando Unicode) em Python 2. Como no exemplo: `fruta = u'maçã'`

Python 3 considera por padrão * strings * definidas no corpo do código com texto entre aspas como sendo Unicode:

```python

fruta = 'maçã'
```

# Divisão

No Python 2:
```python
a = 3 / 2  # a = 1

# ou
a = 3 / 2.  # a = 1.5

```

No Python 3:

```python

a = 3 / 2  # a = 1.5

# ou
a = 3 // 2  # a = 1
```

# Função print()

Python 2:

```python
print a
```

Python 3:

```python

print(a, end=' ')
```
