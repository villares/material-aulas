# Movimento

# A estrutura `setup()` e `draw()`

Para produzir movimento nos valemos de uma ideia presente em todo tipo de animação, a ideia dos "quadros" (*frames*) que são as imagens mostradas em uma rápida sucessão. Usando py5, a geração dessas imagens acontece dentro de uma função que devemos definir chamada `draw()`. Tudo que é desenhado dentro de `draw()` é na verdade redesenhado cerca de 60 vezes por segundo (a taxa de atualizalção, também conhecida como *frame rate*). Para se obter o efeito de uma animação de elementos se deslocando na tela devemos "limpar" o quadro no começo de cada `draw()` frequentemente com a instrução `background()`. Se desenharmos sem essa "limpeza" da tela os elementos "acumulam" ou "deixam um rastro".

Antes do "laço principal de repetição", que é como costumamos descrever a execução do `draw()`, é executada uma função de preparo ou configuração chamada `setup()` que também devemos definir. Essas duas funções juntas são a forma mais comum de se estruturar um *sketch* (um "esboço", como chamamos os nossos programas, na tradição do Processing).

Resumindo: Dentro do `setup()` vai tudo aquilo que precisamos fazer apenas uma vez e no começo, como, por exemplo, definir a àrea de desenho com `size()`. Já no `draw()` vão principalmente as instruções de desenho propriamente ditas, em geral precedidas por uma limpeza da tela ou fundo, e são acionados os cálculos de atualização dos elementos da animação.

Note que no exemplo a seguir, a posição e velocidade do círculo é mantida em algumas variáveis, `px`, `py`, `vx` e `vy`, que precisam ser 'lembradas' entre os ciclos de repetição do `draw()` e dentro dele são modificadas. Isso é o que chamamamos de *variáveis globais*, em contraste com variáveis que fossem criadas dentro do `draw()` e que são *variáveis locais*. Leia mais sobre isso na página [Escopo: variáveis globais e locais](escopo_py.md).

# Círculo rebatendo nas bordas

![](assets/bola_rebate.gif)

```python
raio = 50  # tamanho do raio do círculo
vx = 2.5   # velocidade horizontal inicial
vy = -1.5  # velocidade vertical inicial


def setup():
    global px, py  # importante, permite criar variáveis globais dentro do setup!
    size(400, 400)
    no_stroke()  # desenhar sem traço de contorno
    # Define a posição inicial do círculo
    px, py = width / 2, height / 2  # meio do desenho


def draw():
    global px, py, vx, vy  # é o que permite modificar as variaveis globais no draw!
    background(0, 0, 200)  # limpa o frame com um fundo azul
    # Atualizar as variáveis da posição do círculo
    px = px + vx   # "posiçao x" passa a ser a "posição x" + "velocidade x"
    py = py + vy
    # Testar se o círculo está fora da tela, se estiver,
    # inverta a velocidade (de a ela o valor de -velocidade).
    if px > width - raio or px < raio:
        vx = -vx
    if py > height - raio or py < raio:
        vy = -vy
    # Desenha o círculo
    circle(px, py, raio * 2)


```
# Assuntos relacionados

- [Escopo: variáveis globais e locais](escopo_py.md)
- [Como exportar animações](exportar_animacoes.md)

