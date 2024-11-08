# Caneta automática

# módulo caneta_automatica.py

from caneta_automatica import *
> Este módulo é uma tentativa de fazer com mínimos elementos uma ferramenta de desenho inspirada na tartatuga desenhadora da linguagem Logo. Leia mais sobre Logo em < https://pt.wikipedia.org/wiki/Logo > . Você vai precisar do[Processing modo Python](https://abav.lugaralgum.com/como-instalar-o-processing-modo-python /) .

O módulo * caneta_automatica.py * deve ficar dentro da pasta do seu * sketch*, o que o torna uma aba do IDE. Baixe o arquivo ou copie e cole o conteúdo de[caneta_automatica.py](https://raw.githubusercontent.com/villares/material-aulas/master/caneta_automatica/caneta_automatica.py) em uma nova aba de nome 'caneta_automatica' (o Processing vai acrescentar '.py' no nome do arquivo para você).

Para importar e começar a usar a caneta você precisa das seguintes linhas:

```pyde

size(400, 400)  # área de desenho do Processing
inicie_caneta()  # precisa ser depois do 'size()'
```

# Exemplos de uso

# Desenhando um quadrado

Usando o laço de repetição `for`.

```pyde

size(400, 400)
inicie_caneta()

for i in range(4):  # repete 4 vezes:
    ande(100)       # anda e faz uma linha
    vire(90)        # viar 90 graus à esquerda
```

![quadrado](quadrado.png)

Equivalente, mas agora definindo mais funções.

```pyde


def setup():
    size(400, 400)
    inicie_caneta()
    quadrado(100)  # chama a função quadrado

    # save_frame("quadrado.png")


def quadrado(tamanho):
    for i in range(4):  # repete 4 vezes:
        ande(tamanho)   # anda e faz uma linha
        vire(90)        # viar 90 graus à esquerda


```

# Uma flor recursiva

Recursividade acontece quando durante a execução de uma função nós pedimos a execução da própria função. Esta função flor, chama a função flor se o tamanho dela for maior que 5.

```pyde


def setup():
    size(400, 400)
    inicie_caneta()

    suba_caneta()  # para andar sem desenhar
    ande(100)
    esquerda()  # equivale a 'vire(90)'
    baixe_caneta()  # para voltar a desenhar

    flor(5, 150)


def flor(n, tamanho):
    for i in range(n):
        ande(tamanho)
        vire(360 / n)
        if tamanho > 5:
            flor(n, tamanho / 3)


```
![flor](caneta_flor.png)


# Como o módulo `caneta_automatica.py` é feito por dentro?

A função `inicie_caneta()`prepara o terreno criando uma variável `caneta` que vai dizer se a caneta está no papel(abaixada, `True`) ou levantanda(`False`). Fazer com que ela comece abaixada e muda as coordenadas do  x = 0 e y = 0 para o meio da tela:

```pyde


def inicie_caneta():
    global caneta  # avisa que este é um nome global
    # cria se não houver o nome 'caneta'
    caneta = True  # e apontar para o valor True
    # zera transformações anteriores e põe a origim no meio
    reset_matrix()
    translate(width / 2, height / 2)  # muda o 0, 0
    rotate(HALF_PI)  # vira o sistema de coordenadas 90 graus

    # no estado inicial ande(n) faz translate(0, -n), para a direita
```

As funções `suba _caneta()` e  `baixe_caneta()` vão alterar o estado da caneta mudando a variável global, indicadora do estado da caneta, `caneta`:

```pyde


def suba_caneta():
    global caneta
    caneta = False


def baixe_caneta():
    global caneta
    caneta = True


```

Agora a parte mais bacana!

Se a caneta estiver abaixada(`True`) vamos desenhar uma linha da posição atual `0, 0` para a posição final `0, -n`, onde `n` é o valor da distância que recebemos para andar.

Por fim, vamos deslocar a origem(o x=0, y=0 do Processing)  para a posição final da caneta com `translate(0, -n`).

Note que é usado `- n`  por conta do sistema de coordenadas original ter sido girado 90 graus na função `inicie_caneta()`, e o Y do Processing cresce para cima... Deslocar`translate(0, -n)`na orientação inical, andar pra frente, é andar para a direita na tela.

```pyde


def ande(n):
    if caneta:
        line(0, -n, 0, 0)
    translate(0, -n)


```

Para virar, vamos converter o ângulo em graus para radianos com `radians()`e girar o sistema de coordenadas!

```pyde


def vire(a):
    rotate(radians(-a))  # ângulo positivo fica anti-hórario


def esquerda():
    vire(90)


def direita():
    vire(-90)


```
