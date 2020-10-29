# Estruturas de dados

Coleção é o nome genérico para diversas estruturas de dados, as sequências são coleções preservam (guardam) a ordem dos itens, como uma lista (*list*) ou tupla (*tuple*). Outras coleções não são sequências, pois não guardam a ordem dos itens, como um conjunto (*set*) ou dicionário (*dict*).

### Listas

```python
frutas = ["manga", "manga", "morango", "abacaxi"]  # uma lista de frutas
```

Python usa `[ ]` colchetes (*square brackets*) para listas, sequências mutáveis e heterogêneas de itens (preservam a ordem, mas você pode trocar itens e reordenar). As listas Lembram um pouco *ArrayList* e *Array* em outras linguagens, só que em geral *arrays* só podem ter itens de um único tipo, sãoe struturas homogêneas, e podem ou não o seu tamanho alterado (em Python as listas podem ser aumentadas ou reduzidas).

Em Python moderno podemos usar a biblioteca *numpy* para obter estruturas sofisticadas como matrizes de muitas dimensões, para o nosso uso mais elementar, uma primeira aproximação destas estruturas pode ser feita usando listas de listas para representar matrizes!

```python
m = [[0, 12, 2, 3],
     [1, 22, 3, 4],
     [1, 10, 3, 4],
     [1, 22, 3, 4],
     ]
```

### Tuplas

```python    
ponto = (120, 34)
```
Tuplas são sequências imutáveis (preservam a ordem, mas não dá pra reordenar ou trocar itens). Uma tupla pode ser construída com `( )` parenteses, para fazer uma tupla de um item só precisamos acrescentar uma vírgula, assim: `(item, )`

### Conjuntos

```python
numeros_feios = {2342345, 3454674567, 2346234623463, 2473565656457}
```
Os conjuntos são estruturas muito interessantes, eliminam repetições de itens automáticamente! Um conjunto não preserva a ordem, e os itens tem que ser "hasheáveis", em geral, simplificando, isso significa itens imutáveis como números, *strings*, tuplas, *frozensets*, por exemplo. 

Use `s = set()` para produzir um conjunto vazio (no qual você pode acrescentar itens depois com `.add()`)

### Dicionários

```python
capitais = {"DF" : "Brasília", "RJ" : "Rio de Janeiro", "SP" : "São Paulo"}
```
Um dicionário pode ser criado com a forma  `{chave : valor} `
Apesar das chaves `}` não é um conjunto! Os dicionarios são conhecidos como mapeamentos ou *hash maps* em outras linguagens.
Não mantém a ordem, chave precisa ser hasheável (em geral imutável) números, strings, tuplas podem servir de chave (conjuntos e listas não!)

```python
d = {}  # cria um dicionário vazio    
d['a'] = 10   #  chave: 'a'  valor 10
```

### Outras estruturas para você pesquisar

- *deque*
- *frozenset*

### Assuntos relacionados

- [Mais sobre sequências e fatias em coleções ordenadas](mais_sequencias.md)

