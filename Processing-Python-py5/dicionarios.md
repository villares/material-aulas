# Dicionários

Dicionários(*dict*), juntamente com as listas (*list*), tuplas (*tuple*) e conjuntos (*set*), são das mais importantes estruturas de dados de alto nível disponíveis embutidas em Python.

## Uma metáfora simplificadora para chaves e valores

Imagine um dicionário como uma tabela de duas colunas que permite que busquemos um item, que chamamos de **chave**, o procurando na coluna da esquerda. Se o encontrarmos podemos consultar na coluna da direita um **valor** correspondente. Um dicionário é feito de pares chave-valor.

Como regra simplificada, podemos usar como chaves objetos *imutáveis*, como números, texto (*strings*) ou tuplas cujos elementos internos também sejam imutáveis. Não podemos usar listas, uma vez que são *mutáveis*. Já os valores podem ser qualquer tipo de objeto/valor de Python, incluido listas e até mesmo outros dicionários!

> Uma explicação mais detalhadas sobre as limitações técnicas dos tipos que podemos usar nos dicionários não cabe neste texto introdutório, mas a sua curiosidade pode fazer você querer ler mais sobre eles em [Estruturas de dados (na documentação do Python)](https://docs.python.org/pt-br/3/tutorial/datastructures.html#dictionaries).

Vejamos um exemplo prático em que um dicionário serve para guardar uma paleta de cores nomeadas, os nomes das cores (*strings*) vão ser as chaves, e as cores produzidas pela função `color()` do py5 vão ser os valores (que podem no final das contas ser usados nas funções `fill()`, `stroke()` e `background()`, por exemplo).

| chaves(*keys*) | valores(*values*) |
| --------------- | ------------------ |
| "branco" | color(255) |
| "preto" | color(0) |
| "azul" | color(0, 0, 200) |
| "amarelo" | color(220, 220, 0) |
| "vermelho" | color(200, 0, 0) |

Em Python podemos definir um dicionário diretamente no código com a sintaxe `{chave: valor, }` ou apenas `{}` se quisermos um dicionário vazio para começar.

```python
cores = {
    "branco": color(255),
    "preto": color(0),
    "azul": color(0, 0, 200),
    "amarelo": color(220, 220, 0),
    "vermelho": color(200, 0, 0),
    }
```

Para consultar o valor atribuido a uma chave, acrescentar uma nova chave, ou modificar o valor dela usamos colchetes `[chave]`.

```python
cor_fundo = cores['azul']  # obtém a cor atribuida à chave 'azul'
background(cor_fundo)

cores['verde'] = color(0, 200, 0)  # acrescentar 'verde' ao dicionário
cores['amarelo'] = color(255, 255, 0)  # modifica valor de 'amarelo'
```

No caso da consulta, se não houver a chave no dicionário, teremos um erro! Se não temos certeza da existência da chave podemos usar uma segunda forma de consulta com `.get()`.

```python
cinza = cores['cinza']  # KeyError!

laranja = cores.get('laranja')  # Caso não haja 'laranja' obtemos `None`
if laranja:          # None é considerado semelhante-a-falso e neste caso
    fill(laranja)    # em um primeiro momento fill() não executa

# podemos também propor um resultado padrão quando a chave não está lá
roxo = cores.get('roxo', color(200))  # se não houver 'roxo' cinza claro
fill(roxo)  # enquanto não houver 'roxo' no dicionário teremos color(200)
```

## Removendo itens de um dicionário

O método `.pop(chave)` semelhante ao que existe nas listas, devolve o valor para uma determinada chave, ao mesmo tempo que a remove do dicionário. Mas, ao contrário das listas, não pode ser usado sem argumentos para se obter e remover o último item/valor.

```python
letras_chave = {'A': 1, 'B': 10, 'C': 100}
letras_chave.pop('B')
print(letras_chave)
# Exibe: {'A': 1, 'C': 100}

letras_chave.pop('D')  # KeyError!
```

Se temos certeza de que chave existe, e não estamos interessados no valor, podemos usar a instrução `del`, senão podemos usar o método `.pop()` com um segundo argumento `None`:

```python
del letras_chave['A']  # KeyError se não houver 'A'
letras_chave.pop('D', None) # Seguro, e devolve None se não houver a chave.
```

### Peças de um tabuleiro em um dicionário com tuplas como chaves

```python
"""
Um tabuleiro que permite acrescentar e remover peças com o clique do mouse
O botão da direita põe uma peça "D" e o da esquerda põe uma peça "E"
- Clicando sobre uma peça ela é removida
"""

tam_tabuleiro = 15
tam_casa = 35
meia_casa = tam_casa / 2
borda = 36
tabuleiro = {}  # cria um dicionário vazio
cores = {'E': color(200, 0, 0), 'D': color(0, 200, 0)}  # cores para as peças

def setup():
    size(600, 600)
    text_align(CENTER, CENTER)

def draw():
    background(200)
    for i in range(tam_tabuleiro):
        for j in range(tam_tabuleiro):
            c = tabuleiro.get((i, j))
            if c:
                fill(cores[c])
            else:
                fill(255)
            square(i * tam_casa + borda,
                   j * tam_casa + borda, tam_casa) 
            if c:
                fill(255)
                text(c,
                     i * tam_casa + borda + meia_casa,
                     j * tam_casa + borda + meia_casa)
    # Números nas bordas
    fill(0)
    for n in range(tam_tabuleiro):
        pos = n * tam_casa + borda + meia_casa
        text(n, meia_casa, pos)
        text(n, pos, height - meia_casa)

def mouse_to_tabuleiro(x, y):
    i = (x - borda) // tam_casa
    j = (y - borda) // tam_casa
    return i, j
    
def mouse_pressed():
    if (borda < mouse_x < width - borda and
        borda < mouse_y < height - borda):
        i, j = mouse_to_tabuleiro(mouse_x, mouse_y)

        if (i, j) in tabuleiro:
            del tabuleiro[i, j]
        else:
            tabuleiro[i, j] = 'E' if mouse_button == LEFT else 'D'
#       # Outra versão para remover e acrescentar peças
#       # remove peça se houver
#       if not tabuleiro.pop((i, j), None):  
#       # se não houver inclui peça
#           tabuleiro[i, j] = 'E' if mouse_button == LEFT else 'D'
```

![imagem do tabuleiro](assets/tabuleiro.png)


## `Counter` um objeto contador com interface de dicionário

A biblioteca padrão do Python vem com uma estrutura de dados muito interessante que podemos descrever como um "dicionário contador", [`collections.Counter`](https://docs.python.org/3/library/collections.html#collections.Counter).

### Um primeiro exemplo, contando números

Vamos imaginar como exemplo mínimo que queremos contar quantas vezes cada número aparece em uma lista:

```python
from collections import Counter

numeros = [1994, 1994, 1995, 1999, 1999, 1999, 1999, 2011, 2013, 2014, 2014, 2022, 2024]
contador = Counter(numeros)

print(contador)
# Resultado:
# Counter({1999: 4, 1994: 2, 2014: 2, 1995: 1, 2011: 1, 2013: 1, 2022: 1, 2024: 1})
```

Podemos obter a frequência de um item da coleção original com colchetes, como se fosse uma chave do dicionário criado por `Counter`, mas ao contrário de um dicionário comum, em vez de uma excessão `KeyError` se o item não existir, teremos 0.

```python
print(contador[1994])
# 2
print(contador[1996])
# 0
```

Podemos ainda obter uma sequência ordenada que começa pelos itens mais frequentes com o método `.most_common()`, é uma lista de tuplas (chave, contagem):

```python
for num, contagem in contador.most_common():
    print(f'{num}: {contagem}')
"""
Resultado:
1999: 4
1994: 2
2014: 2
1995: 1
2011: 1
2013: 1
2022: 1
2024: 1
"""
```

Podemos pedir uma espécie de fatia dos primeiros itens dessa lista passando um argumento `n` em `.most_comon(n)`. Repare que mesmo pedindo apenas um dos "itens mais comuns", teremos ainda uma lista de tuplas (nesse caso com uma única tupla dentro).

```python
print(contador.most_comon(2))
# [(1999, 4), (1994, 2)]
print(contador.most_comon(1))
# [(1999, 4)]
```

Isso pode produzir código um tanto desengonçado:

```python
num, contagem = contador.most_comon(1)[0]
```

### Contando outras coisas

Lembre que um *string* é um iterável, ou seja, pode ser interpretado como uma sequência de letras:

```python
print(Counter('abracadabra'))
# Counter({'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1})
```

<!-- Já para contar palavras, os liguistas costuma remover palavras muito frequentes e que acrescentam pouco conteúdo semântico como artigos, conectivos e etc., conhecidas em inglês como "stopwords".-->

## Exemplo de dicionário com dicionários dentro

Não é incomum termos como valores de um dicionário, outros dicionários. O formato de intercâmbio de infomações JSON (lê-se *djeizon*, vem de *JavaScript Object Notation*), é um tanto parecido com isto, em geral é quase uma lista com uma porção de dicionários aninhados dentro.

```python
# Fonte IBGE 2020

estados = {
    'MG': {'capital': 'Belo Horizonte', 'pop': 21292666},
    'AC': {'capital': 'Rio Branco', 'pop': 894470},
    'RJ': {'capital': 'Rio de Janeiro', 'pop': 17366189},
    'BH': {'capital': 'Salvador', 'pop': 14930634},
    'PR': {'capital': 'Curitiba', 'pop': 11516840},
    'AC': {'capital': 'Rio Branco', 'pop': 894470},
    'RS': {'capital': 'Porto Alegre', 'pop': 11422973},
    'PE': {'capital': 'Recife', 'pop': 9616621},
    'CE': {'capital': 'Fortaleza', 'pop': 9187103},
    'PA': {'capital': 'Belém', 'pop': 8690745},
    'SC': {'capital': 'Joinville', 'pop': 7252502},
    'MA': {'capital': 'São Luís', 'pop': 7114598},
    'GO': {'capital': 'Goiânia', 'pop': 7113540},
    'AM': {'capital': 'Manaus', 'pop': 4207714},
    'ES': {'capital': 'Vitória', 'pop': 4064052},
    'PB': {'capital': 'João Pessoa', 'pop': 4039277},
    'RN': {'capital': 'Natal', 'pop': 3534165},
    'MT': {'capital': 'Cuiabá', 'pop': 3526220},
    'AL': {'capital': 'Maceió', 'pop': 3351543},
    'TO': {'capital': 'Palmas', 'pop': 1607363},
    'MS': {'capital': 'Campo Grande', 'pop': 2839188},
    }

# Acrescenta estado, a chave é a sigla, o valor um outro dicionário
estados['SP'] = {'capital': 'São Paulo', 'pop': 46289333}

print(estados['ES']['capital'])  # exibe: Vitória
```

## A questão da ordem dos itens armazenados

Vale notar que até a versão 3.7 do Python, dicionários comuns não guardavam ou garantiam a ordem das chaves, assim como os conjuntos (*sets*), agora as chaves ficam na ordem em que foram foram criadas. Mas pode ser legal conhecer [`OrderedDict`](https://docs.python.org/3/library/collections.html#collections.OrderedDict), que foi criado especialmente para esses casos e tem mais métodos relacionados a reordenar os itens.

## Fazendo piadas sobre Python e os dicionários

Dicionários em especial são tão poderosos e flexíveis que são usados internamente para fazer funcionar muito da linguagem Python. Isso se reflete nesta piada sobre linguagens de programação:

> E se tudo fosse uma lista? LISP
>
> E se tudo fosse uma pilha (*stack*)? Forth
>
> E se tudo fosse um ponteiro? C
>
> E se tudo fosse um dicionário? Python!

Ou ainda este meme aqui:

![](https://pbs.twimg.com/media/EelzOpCX0AAIeYV?format=png&name=small)

## Assuntos relacionados

- [Conjuntos](conjuntos.md)
