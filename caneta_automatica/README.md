# Caneta automática	

### módulo caneta_automatica.pyi 

> Este módulo é uma tentativa de fazer com mínimos elementos uma ferramenta de desenho inspirada na tartatuga desenhadora da linguagem Logo. Leia mais sobre Logo em  <https://pt.wikipedia.org/wiki/Logo>.

O módulo *caneta_automatica.py*  deve estar na pasta do seu *sketch* e pode ser  importado e iniciado com as seguintes linhas: 

```pyde
form caneta_automatica import *

size(400, 400)  # área de desenho do Processing
inicie_caneta()
```
Você pode se quiser copiar e colar o conteúdo de [caneta_automatica.py]() mas vamos ver aqui passo a passo como ele é construído!

A função `inicie_caneta()`prepara o terreno cirando uma variável `caneta` que vai dizer se a caneta está no papel (abaixada, `True`) ou levantanda (`False`). Fazer com que ela comece abaixada e mudar as coordenadas do desenho para que o x=0 e y=0 sejam no meio da tela:

```pyde
def inicie_caneta():
    global caneta  # avisa que este é um nome global
    # vamos cria se não houver o nome 'caneta'
    caneta = True  # e apontar para o valor True 
    translate(width / 2, height / 2)  # muda o 0, 0 pro meio
    rotate(HALF_PI)  # vira o sistema de coordenadas 90 graus
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






