# Compreensão de listas (*list comprehension*)

é muito comum usarmos um laço de repetição para produzir e acumular elementos em uma estrutura de dados, vamos ver um exemplo meio bobinho de um `for` que acrescenta itens em uma lista. São pontos com um `x` que vai crescendo de 10 em 10 e o `y` produzido 'pseudo-aleatório', com a função embutidada do processing, `random()`:

```python
pontos = []
for i in range(10):
    x = i * 10
    y = random(-100, 100)
    ponto.append((x, y))  # os parenteses extra criam uma tupla
```

existe um maneira alternativa de fazer isso usando a sintaxe chamada * compreensão de lista*, compare:

```python
pontos = [(i * 10, random(-100, 100)) for i in range(10)]
```

veja se você consegue identificar, nos exemplos acima, os elementos do seguinte padrão geral, que usa um laço de repetição para construir a lista:

```python
lista_resultante = []
for «valor» in «iterável»:
      # o novo elemento é acrescentado
      lista_resultante.append(«novo_elemento»)
```

E a forma reescrita:

```python
lista_resultante = [«novo_elemento» for «valor» in «iterável»]
```

é possível ainda "filtrar", usar uma condição que permite ou não produzir novos elementos.

```python
lista_resultante = []
for «valor» in «iterável»:
    if «condição»:  # a condição depende do valor
        # o novo elemento é acrescentado
        lista_resultante.append(«novo_elemento»)
```
que pode ser reescrito assim:

```python
lista_resultante = [«novo_elemento» for «valor» in «iterável» if «condição»]
```

# Mais exemplos

sem "filtragem"

```python
dimensoes_retangulos = [(10, 20), (20, 30), (10, 30), (30, 30), (30, 10)]

areas = []
for a, b in dimensoes_retangulos:
    areas.append(a * b)

areas = [a * b for a, b in dimensoes_retangulos]
```

agora com "filtragem", ignorando quadrados!

```python
areas = []
for a, b in dimensoes_retangulos:
    if a != b:  # se `a` diferente de `b`, vai ignorar a == b
        areas.append(a * b)

areas = [a * b for a, b in dimensoes_retangulos if a != b]
```
# Expressões geradoras

se você não precisa dessa coleção de valores mais de uma vez, pode evitar que ela seja guardada na memória, usando expressões geradoras(*generator expressions*) substituindo os colchetes por parênteses, e até mesmo omitindo os parênteses se a expressão for posta como argumento de uma função:

```python
# soma os quadrados dos números pares entre 0 e 98 (o 100 não está incluso).
soma_quadrados = sum(n * n for n in range(100) if n % 2 == 0)  # 161700

```

# Compreensão de conjuntos e dicionários

```python
dimensoes_retangulos = [(10, 20), (20, 30), (10, 30),
                         (30, 30), (30, 10), (5, 40)]
areas_sem_repetir = {a * b for a, b in dimensoes_retangulos}
print(areas_sem_repetir)  # set([900, 200, 300, 600])
```

um dicionário "pré-calculado" das áreas

```
areas_dict = {(a, b): a * b for a, b in dimensoes_retangulos}
# {(30, 30): 900, (20, 30): 600, (10, 30): 300,
#  (10, 20): 200, (30, 10): 300, (5, 40): 200
# }
```


# Veja no livto Pense em Python

- [abrangência de listas](https: // github.com/villares/pense_python2e/blob/master/docs/19-extra.md  # 192---abrang%C3%AAncia-de-listas)
- [expressões geradoras](https: // github.com/villares/pense_python2e/blob/master/docs/19-extra.md  # 193---express%C3%B5es-geradoras)
