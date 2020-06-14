## Compreensão de listas (*list comprehension*)



É muito comum usarmos um laço de repetição para produzir e acumular elementos  em uma estrutura de dados, vamos ver um exemplo genérico de um `for` que acrescenta itens em uma lista:

```.python
pontos = []
for i in range(10):
    x = i * 10
    y = random(-100, 100)
    ponto.append((x, y))  # os parenteses extra criam uma tupla
```

Existe um maneira alternativa de fazer isso usando a sintaxe chamada *compreensão de lista*, compare:

```python
pontos = [(i * 10, random(-100, 100)) for i in range(10)]
```

