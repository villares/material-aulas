# Criando uma animação 

Vamos fazer uma animação clássica que é um elemento que se desloca e rebate nas bordas da tela, no nosso caso, um círculo branco em um fundo azul.

![](assets/bola_rebate.gif)

## Redesenhando quadros com `draw()` e outras considerações

Para produzir movimento nos valemos de uma ideia presente em todo tipo de animação, a ideia dos "quadros" (*frames*) que são as imagens mostradas em uma rápida sucessão. Usando py5, a geração dessas imagens acontece dentro de uma função que devemos definir chamada `draw()`. 

Tudo que é desenhado dentro de `draw()` é na verdade redesenhado cerca de 60 vezes por segundo, no máximo, essa é a taxa de atualização, também conhecida como *frame rate*. 

> Essa taxa de quadros por segundo pode ser reduzida voluntariamente se usarmos a função `frame_rate()`, ou involutariamente, quando fazemos coisas muito custosas computacionalmente, isto é, demoradas, dentro do `draw()`. Não é possível forçar um aumento da taxa de atualização, se o que estamos fazendo ficar demorado, isso acarreta em um limite, de outra forma, o limite são os 60 quadros por segundo. É possível saber uma média móvel da taxa de atualização om a função `get_frame_rate()`.

Para se obter o efeito de uma animação de elementos se deslocando na tela é preciso ainda "limpar" o quadro no começo de cada `draw()` frequentemente com a instrução `background()`. Se desenharmos sem essa "limpeza" da tela os elementos "acumulam" ou "deixam um rastro".

## Mantendo registro da posição e velocidade, e os atualizando

Repare como a posição e velocidade do círculo é mantida em algumas variáveis, `px`, `py`, `vx` e `vy`, que precisam ser 'lembradas' entre os ciclos de repetição do `draw()` e dentro de `draw()` são modificadas. Isso é o que chamamamos de *variáveis globais*, em contraste com variáveis que criadas dentro do `draw()`, que seriam. *variáveis locais*. Leia mais sobre isso na página [Escopo: variáveis globais e locais](escopo_py.md). 

E finalmente, no exemplo a seguir, usamos uma [execução condicional](condicionais_py.md), isto é uma estrutura com `if`, para executar as ações que fazem o círculo rebater nas bordas. 

Dá pra saber se o círculo está sainda a direta quando a posição `px` fica maior do que a largura da tela (`px > width`), mas nesse caso é o centro do círculo que está saindo, então `px > width - raio` é mais sofisticado. E para evitar uma saída do lado esquerdo também usamos então `px < raio` em vez de `px < 0`. A condição completa com o `if` fica `if px > width - raio or px < raio:` e dentro desse `if` invertemos o sentido da velocidade com `vx = -vx`. Uma estratégia equivalente é usada com `py`, a posição vertical do centro do círculo.

## O código completo


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

- [Condicionais(`if` e `else`)](condicionais_py.md)
- [Escopo: variáveis globais e locais](escopo_py.md)
- [Como exportar animações](exportar_animacoes.md)

