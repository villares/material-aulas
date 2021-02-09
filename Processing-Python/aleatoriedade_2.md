# Mais aleatoriedade

Vamos começar revisando a  função `random()` do Processing, que produz números pseudo-aleatórios e já vimos anteriormente, em seguida vamos ver um pouco do módulo *random* de Python que pode ser *importado* (com a instrução `import` no início do código), que e tem uma função `random()` e algumas outras funções relacionadas.

### A função `random()` do Processing

Cada vez que chamamos a função `random()` com um valor de argumento, como em `sorteio = random(1);` um número entre zero e o argumento passado (servindo de limite superior, mas não incluso) é produzido. 

![imagem_exemplo](assets/random1-10.png)

Se dois valores forem usados, por exemplo `random (-5, 5)` serão produzidos números entre -5 e 5 (não incluso). E podemos obter números inteiros convertendo o valor usando `int()`, como em `sorteio_inteiro = int(random(1, 11))` que 'sorteia' com igual probabilidades os números de 1 a 10.

### O módulo `random` da biblioteca padrão do Python

No Python a funçao `random()` precisa ser importada do módulo `random` com a a seguinte  instrução:

```python
from random import random
```
> Mas, se fizermos isso "matamos" o `random()` do Processing. Uma alternativa, se quisermos manter as duas, é escrever:</br>
> `from random import random as py_random`</br>
> e aí usaremos o nome `py_random()`, uma outra opção ainda importar o módulo todo com outro nome</br>
> `import random as rnd`</br>
> e nesse caso usaremos `rnd.random()`, por exemplo.</br>

A função `random()` em Python não recebe argumentos (isto é não vai nada dentro dos parênteses) e devolve o equivalente a `random(1)` no Processing, por esse motivo  não me  parece tão flexível e útil. 

No entanto, o módulo `random` de Python oferece outras funções muito simpáticas, quero dizer, interessantes: `choice()`, `sample()`, e `shuffle()`.

#### Produzindo números inteiros com `randint()`

É comum querermos produzir números pseudo-aleatórios inteiros, em Processing costumamos truncar, convertendo com `int()` como em `int(random(1, 6))`, mas em Python podemos fazer assim:

```python
from random import randint

for _ in range(100):
    valor = randint(1, 5) # 'sorteia' os números 1, 2, 3, 4, 5
    print(valor)  

# Resultado: produz 100 valores de 1 a 5, INCLUI O 5!!!
```


#### Selecionando um único item com `choice()`

A função `choice(colection)` devolve um item de uma coleção (tupla, lista, conjunto). Para cada execução um item é escolhido (pseudo-)aleatoriamente.

```python
from random import choice

frutas = ("uva", "jaca", "melancia", "ubu", "pitanga")
sorteio = choice(frutas)  # 'sorteia' fruta da tupla de frutas
print(sorteio)
# Um resultado possível no console:
# jaca
```

Veja também outro exemplo, mais visual.

```python
from random import choice

cores = [color(200, 0, 0), color(0, 200, 0), color(0, 0, 200)]

def draw():
    c = choice(cores) # sorteia uma cor da lista de cores
    fill(c)
    rect(25, 25, 50, 50)
```

![random_choice](assets/random_choice.gif)

#### Selecionando uma amostra (sem repetição de itens)

*Sample* significa amostra, e usamos `sample(colection, k)` onde `k` é o tamanho da amostra (e não pode ser maior que tamanho da população) para obter uma lista com `k` itens.

```python
from random import sample

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

#### Misturando a ordem de uma sequência mutável

Ao executar `shuffle(minha_sequencia)` fazemos com que `minha_sequencia`, que, atenção, não pode ser uma sequência vazia, seja reordenada 'aleatoriamente'.

```python
from random import shuffle

letras = ['A', 'B', 'C', 'D', 'E']

shuffle(letras)

print(letras)

# a cada execução uma ordem diferente:
# ['C', 'B', 'D', 'A', 'E']
# ['D', 'C', 'E', 'B', 'A']
# ...
```
A coleção precisa ser ordenada e mutável, como uma lista, não pode ser uma tupla, que é imutável, ou um conjunto que não guarda a ordem dos elementos.

###  Sementes dos geradores pseudo-aleatórios (*randomSeed*)

Como os números produzidos por `random()` não são verdadeiramente aleatórios, e sim produzidos por algorítmos geradores determinísticos, é possível fixar um parâmetro inical, conhecido como semente (*seed*), o que permite reproduzir novamente a mesma sequência de números.

Para fixar o início do gerador de `random()` no Processing usamos `randomSeed(numero_inteiro)`. 

Já para as funções do módulo `random` do Python:

```python
from random import seed
seed(numero_inteiro)
```

Neste exemplo abaixo usamos uma semente para manter 'congelados' os números gerados por `random()` entre frames do `draw()`, mantendo a interatividade de ajuste do ângulo da árvore com o mouse. Quando uma imagem é exportada, o nome do arquivo contém a semente (_seed_) do gerador de números pseudo-aleatórios.

```python
def setup():
    global seed
    seed = int(random(1000))
    print(seed)
    size(500, 500)
    
def draw(): 
    randomSeed(seed)
    background(240, 240, 200)
    translate(250, 300)
    galho(60)
          
def galho(tamanho): # definição do galho/árvore
    ang = radians(mouseX)
    reducao = .8
    strokeWeight(tamanho / 10)
    line(0, 0, 0, -tamanho)
    if tamanho > 5:
        pushMatrix()
        translate(0, -tamanho)
        rotate(ang)
        galho(tamanho * reducao - random(0, 2))
        rotate(-ang * 2)
        galho(tamanho * reducao - random(0, 2))
        popMatrix()
          
def keyPressed(): # executada quando uma tecla for precinada
    if keyCode == LEFT:
         seed = seed - 1
    if keyCode == RIGHT:
         seed = seed + 1
    if key == ' ':  # barra de espaço precionada, sorteia nova "seed"
        seed = int(random(100000))
        print(seed)
    if key == 's':  # tecla "s" precionada, salva a imagem PNG
        nome_arquivo = 'arvore-s{}-a{}.png'.format(seed, mouseX % 360)
        saveFrame(nome_arquivo)
        print("PNG salvo")
```

---
Texto e imagens / text and images: CC BY-NC-SA 4.0; Código / code: GNU GPL v3.0 exceto onde explicitamente indicado por questões de compatibilidade.
