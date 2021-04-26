É muito comum em Python ver  o seguinte padrão, que usa um laço de repetição para construir, ou popular, uma lista:

```python
nova_lista = []
for «valor» in «iterável»:
      resultado.append(«novo_elemento»)  # o novo elemento é calculado a partir do valor
```

É possível ainda "filtrar", usar uma condição que permite ou não produzir novos elementos.

```python
nova_lista = []
for «valor» in «iterável»:
    if  «condição»:  # a condição depende do valor
        resultado.append(«novo_elemento»)  # o novo elemento depende do valor
```

Isso pode ser reescrito da seguinte maneira:

```python
nova_lista = [«novo_elemento» for «valor» in «iterável» if «condição»]
# o primeiro padrão, sem a condição, é apenas [«novo_elemento» for «valor» in «iterável»]
```

Vamos ver alguns exemplos concretos!

```python
dimensoes_retangulos = [(10, 20), (20, 30), (10, 30), (30, 30), (30, 10)]
areas = []
for a, b in demensoes_retangulos:
    areas.append(a * b)

areas = [a * b for a, b in dimensoes]
```

Números divisíveis por 3

```python
divisivel_por_3 = []
for n in range(1000):
    if n % 3 == 0:
        divisivel_por_3.append(n)

divisivel_por_3 = [n for n in range(1000) if n % 3 == 0]
```

Se você não precisa dessa coleção de valores mais de uma vez, pode evitar que ela seja guardada na memória, usando expressões geradoras (generator expressions) substituindo os colchetes por parêntes:

```python
soma_quadrados = sum(n * n for n in range(100) if n % 2 == 0) # 161700

```

###### Veja no livto Pense em Python

- [Abrangência de listas](https://github.com/villares/PensePython2e/blob/master/docs/19-extra.md#192---abrang%C3%AAncia-de-listas)
- [Expressões geradoras](https://github.com/villares/PensePython2e/blob/master/docs/19-extra.md#193---express%C3%B5es-geradoras)




