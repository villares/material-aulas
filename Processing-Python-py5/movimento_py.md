# Criando uma animação simples

## Redesenhando quadros com `draw()` e outras consideraçẽoes

Para produzir movimento nos valemos de uma ideia presente em todo tipo de animação, a ideia dos "quadros" (*frames*) que são as imagens mostradas em uma rápida sucessão. Usando py5, a geração dessas imagens acontece dentro de uma função que devemos definir chamada `draw()`. 

Tudo que é desenhado dentro de `draw()` é na verdade redesenhado cerca de 60 vezes por segundo, no máximo, essa é a taxa de atualização, também conhecida como *frame rate*. Essa taxa pode ser reduzida voluntariamente se usarmos a função `frame_rate()`, ou involutariamente, se fizermos coisas muito demoradas, isto é, custosas computacionalmente, dentro do `draw()`. Não é possível forçar um aumento da taxa de atualização.

Para se obter o efeito de uma animação de elementos se deslocando na tela é preciso ainda "limpar" o quadro no começo de cada `draw()` frequentemente com a instrução `background()`. Se desenharmos sem essa "limpeza" da tela os elementos "acumulam" ou "deixam um rastro".

## Círculo rebatendo nas bordas

No exemplo a seguir, usamos uma [execução condicional](condicionais_py.md), isto é uma estrutura com `if`, para executar as ações que fazem o círculo rebater nas bordas.

Repare também como a posição e velocidade do círculo é mantida em algumas variáveis, `px`, `py`, `vx` e `vy`, que precisam ser 'lembradas' entre os ciclos de repetição do `draw()` e dentro dele são modificadas. Isso é o que chamamamos de *variáveis globais*, em contraste com variáveis que fossem criadas dentro do `draw()` e que são *variáveis locais*. Leia mais sobre isso na página [Escopo: variáveis globais e locais](escopo_py.md). 


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

Experimente desligar por meio de um `#` tornando um comentário a linha do `background(0, 0, 200)` que limpa o frame, para ver a acumulação dos círculos.

# Assuntos relacionados

- [Condicionais(`if` e `else`)](condicionais_py.md(
- [Escopo: variáveis globais e locais](escopo_py.md)
- [Como exportar animações](exportar_animacoes.md)

