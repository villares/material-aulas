# Mais aleatoriedade

from random import random, choice, seed
from random import shuffle, seed
import random as rnd
from random import shuffle
from random import sample
from random import choice
from random import randint
from random import random
vamos começar revisando a  função `random()` do processing, que produz números pseudo-aleatórios e já vimos anteriormente, em seguida vamos ver um pouco do módulo * random * de python que pode ser * importado * (com a instrução `import` no início do código), que e tem uma função `random()` e algumas outras funções relacionadas.

# A função `random()` do Processing

cada vez que chamamos a função `random()` com um valor de argumento, como em `sorteio = random(1)
` um número entre zero e o argumento passado(servindo de limite superior, mas não incluso) é produzido.

![imagem_exemplo](assets/random1-10.png)

se dois valores forem usados, por exemplo `random(-5, 5)` serão produzidos números entre - 5 e 5 (não incluso). E podemos obter números inteiros convertendo o valor usando `int()`, como em `sorteio_inteiro = int(random(1, 11))` que 'sorteia' com igual probabilidades os números de 1 a 10.

# O módulo `random` da biblioteca padrão do Python

no python a funçao `random()` precisa ser importada do módulo `random` com a a seguinte  instrução:

```python
```

> mas, se fizermos isso "matamos" o `random()` do processing. uma alternativa, se quisermos manter as duas, é escrever: < /br >
> `from random import random as py_random` < /br >
> e aí usaremos o nome `py_random()`, uma outra opção ainda importar o módulo todo com outro nome < /br >
> `import random as rnd` < /br >
> e nesse caso usaremos `rnd.random()`, por exemplo. < /br >

A função `random()` em python não recebe argumentos(isto é não vai nada dentro dos parênteses) e devolve o equivalente a `random(1)` no processing, por esse motivo  não me  parece tão flexível e útil.

no entanto, o módulo `random` de python oferece outras funções muito simpáticas, quero dizer, interessantes: `choice()`, `sample()`, e `shuffle()`.

# Produzindo números inteiros com `randint()`

é comum querermos produzir números pseudo-aleatórios inteiros, em processing costumamos truncar, convertendo com `int()` como em `int(random(1, 6))`, mas em python podemos fazer assim:

```python

for _ in range(100):
    valor = randint(1, 5)  # 'sorteia' os números 1, 2, 3, 4, 5
    print(valor)

# Resultado: produz 100 valores de 1 a 5, INCLUI O 5!!!
```

# Selecionando um único item com `choice()`

A função `choice(colection)` devolve um item de uma coleção(tupla, lista, conjunto). para cada execução um item é escolhido(pseudo-)aleatoriamente.

```python

frutas = ("uva", "jaca", "melancia", "ubu", "pitanga")
sorteio = choice(frutas)  # 'sorteia' fruta da tupla de frutas
print(sorteio)
# Um resultado possível no console:
# jaca
```

veja também outro exemplo, mais visual.

```python

cores = [color(200, 0, 0), color(0, 200, 0), color(0, 0, 200)]


def draw():
    c = choice(cores)  # sorteia uma cor da lista de cores
    fill(c)
    rect(25, 25, 50, 50)


```

![random_choice](assets/random_choice.gif)

# Selecionando uma amostra (sem repetição de itens)

*sample * significa amostra, e usamos `sample(colection, k)` onde `k` é o tamanho da amostra(e não pode ser maior que tamanho da população) para obter uma lista com `k` itens.

```python

cores = (color(200, 0, 0),
         color(200, 200, 0),
         color(0, 200, 200),
         color(200, 0, 200),
         color(0, 200, 0),
         color(0, 0, 200))

# uma lista com duas cores
duas_cores = sample(cores, 2)

print(len(duas_cores))  # resultado: 2
```

# Misturando a ordem de uma sequência mutável

ao executar `shuffle(minha_sequencia)` fazemos com que `minha_sequencia`, que, atenção, não pode ser uma sequência vazia, seja reordenada 'aleatoriamente'.

```python

letras = ['A', 'B', 'C', 'D', 'E']
shuffle(letras)
print(letras)
# a cada execução uma ordem diferente:
# ['C', 'B', 'D', 'A', 'E']
# ['D', 'C', 'E', 'B', 'A']
# ...
```

A coleção precisa ser ordenada e mutável, como uma lista, não pode ser uma tupla, que é imutável, ou um conjunto que não guarda a ordem dos elementos.

veja um outro exemplo de `shuffle()`, embaralhando uma lista de tuplas que representam as posições em uma grade. as cores e os números são relativos à ordem dos elementos na lista(0, vermelho) é o primeiro quadrado da lista.

```python

tam = 80


def setup():
    size(400, 400)
    text_align(CENTER, CENTER)
    color_mode(HSB)  # matiz, saturacao, brilho
    frame_rate(1)


def draw():
    posicoes = []  # lista vazia
    for y in range(0, height, tam):
        for x in range(0, width, tam):
            posicoes.append((x, y))  # tupla (x, y)

    shuffle(posicoes)  # Embaralha a lista gerada

    for i, (x, y) in enumerate(posicoes):  # desenha os quadrados
        fill(i * 10, 200, 200)  # i influencia o matiz
        rect(x, y, tam, tam)
        fill(0)
        text(i, x + tam / 2, y + tam / 2)  # escrevendo o números


```

![random_choice](assets/shuffle.gif)

# Sementes dos geradores pseudo-aleatórios (*random seed*)

como os números produzidos por `random()` não são verdadeiramente aleatórios, e sim produzidos por algorítmos geradores determinísticos, é possível fixar um parâmetro inical, conhecido como semente(*seed*), o que permite reproduzir novamente a mesma sequência de números.

para fixar o início do gerador de `random()` no processing usamos `random_seed(numero_inteiro)`.

```python
random_seeed(numero_inteiro)  # ajusta a semente no Processing
s = random(10, 20)  # Função random() do Processing
```

Já para as funções do módulo `random` do python usamos a função `seed()` do módulo `random`.

```python

seed(numero_inteiro)
c = choice(('A', 'B', 'C'))
r = random() * 100  # random do Python sobrepôs o random do Processing
```

ou ainda

```python

rnd.seed(numero_inteiro)
c = rnd.choice(('A', 'B', 'C'))
r = rnd.random() * 100
```

# Um exemplo de uso do `random.seed()` do Python

modificando o exemplo anterior com `shuffle`.

```python

tam = 80


def setup():
    size(400, 400)
    text_align(CENTER, CENTER)
    color_mode(HSB)  # matiz, saturacao, brilho


def draw():
    seed(mouse_x)
    posicoes = []  # lista vazia
    for y in range(0, height, tam):
        for x in range(0, width, tam):
            posicoes.append((x, y))  # tupla (x, y)

    shuffle(posicoes)  # Embaralha a lista gerada

    for i, (x, y) in enumerate(posicoes):  # desenha os quadrados
        fill(i * 10, 200, 200)  # i influencia o matiz
        rect(x, y, tam, tam)
        fill(0)
        text(i, x + tam / 2, y + tam / 2)  # escrevendo o números


```


# Um exemplo do `randomSeed()` do Processing

neste exemplo abaixo usamos uma semente para manter 'congelados' os números gerados por `random()` entre frames do `draw()`, mantendo a interatividade de ajuste do ângulo da árvore com o mouse. quando uma imagem é exportada, o nome do arquivo contém a semente(_seed_) do gerador de números pseudo-aleatórios.

```python


def setup():
    global seed
    seed = int(random(1000))
    print(seed)
    size(500, 500)


def draw():
    random_seed(seed)
    background(240, 240, 200)
    translate(250, 300)
    galho(60)


def galho(tamanho):  # definição do galho/árvore
    ang = radians(mouse_x)
    reducao = .8
    stroke_weight(tamanho / 10)
    line(0, 0, 0, -tamanho)
    if tamanho > 5:
        push_matrix()
        translate(0, -tamanho)
        rotate(ang)
        galho(tamanho * reducao - random(0, 2))
        rotate(-ang * 2)
        galho(tamanho * reducao - random(0, 2))
        pop_matrix()


def key_pressed():  # executada quando uma tecla for precinada
    if key_code == LEFT:
        seed = seed - 1
    if key_code == RIGHT:
        seed = seed + 1
    if key == ' ':  # barra de espaço precionada, sorteia nova "seed"
        seed = int(random(100000))
        print(seed)
    if key == 's':  # tecla "s" precionada, salva a imagem PNG
        nome_arquivo = 'arvore-s{}-a{}.png'.format(seed, mouse_x % 360)
        save_frame(nome_arquivo)
        print("PNG salvo")


```

---

texto e imagens / text and images: CC BY-NC-SA 4.0
Código / code: GNU GPL v3.0 exceto onde explicitamente indicado por questões de compatibilidade.
