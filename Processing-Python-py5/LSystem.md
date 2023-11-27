

# L-System - Sistema de Lindenmayer

L-Systems são as estruturas e procedimentos criados por Aristide Lindenmayer para estudar o crescimento de algas e plantas, por meio da manipulação de sequências de símbolos. As sequências são geradas por sucessivas iterações da aplicação de regras de substituição. 


A tradução computacional dessas estruturas foi discutida pela primeira vez na serie *Lecture Notes in Biomathematics* com o artigo [Lindenmayer Systems, Fractals, and Plants](https://link.springer.com/content/pdf/10.1007/978-1-4757-1428-9.pdf)  por Przemyslaw Prusinkiewcz e James Hanan (DOI: 10.1007/978-1-4757-1428-9).

> Mais referências:
>- [The Algorithmic Beauty of Plants](http://algorithmicbotany.org/papers/#abop) (+ diversos livros e artigos)
>- [Lindenmayer systems: Describing how things grow with strings of letters, bye Christopher G Jennings](https://www.cgjennings.ca/articles/l-systems/)
>- [L-System User Notes, by Paul Bourke](http://www.paulbourke.net/fractals/lsys/)
>- [Using Lindenmayer Systems to Introduce Computer Science Concepts](https://www.russellgordon.ca/cemc/2017/lindenmayer-systems/)
>- [Wikipedia: L-system](https://en.wikipedia.org/wiki/L-system)
         
## Um exemplo simples

![image](https://github.com/villares/material-aulas/assets/3694604/e0e6f78d-047c-4070-9218-4d1a7e91d183)

```python
axioma = "X"
regras = {"X": "F+[[X]-X]-F[-FX]+X",
          "F": "FF"
          }

tamanho = 10
angulo = 25
iteracoes = 4  # repeticoes (voltas na aplicação das regras)
xo, yo = 300, 500

def setup():
    size(600, 600)
    frase_inicial = axioma
    for i in range(iteracoes):
        frase = ""
        for simbolo in frase_inicial:
            substituicao = regras.get(simbolo, simbolo)
            frase = frase + substituicao
        frase_inicial = frase
    print(len(frase))

    background(240, 240, 200)
    translate(xo, yo)
    for simbolo in frase:
        if simbolo == "F":
            line(0, 0, 0, -tamanho)
            translate(0, -tamanho)
        if simbolo == "+":
            rotate(radians(angulo))
        if simbolo == "-":
            rotate(radians(-angulo))
        if simbolo == "[":
            push_matrix()
        if simbolo == "]":
            pop_matrix()
```

## Uma versão com interatividade

```python
axioma = "X"
regras = {"X": "F+[[X]-X]-F[-FX]+X",
          "F": "FF"
          }
tamanho = 10
angulo = 25
iteracoes = 4  # repeticoes (voltas na aplicação das regras)
xo, yo = 300, 500

def setup():
    global frase
    size(600, 600)
    frase = gerar_sistema(iteracoes, axioma, regras)
    print(len(frase))

def draw():
    background(240, 240, 200)
    translate(xo, yo)
    desenha_sistema(frase)

def gerar_sistema(num, axioma, regras):
    """
    Produz um sistema-L a partir da  frase `axioma`,
    repetindo `num` iterações, as substituições descritas
    nas pelo dicionário `regras`
    """
    frase_inicial = axioma
    for i in range(num):
        frase_nova = ""
        for simbolo in frase_inicial:
            substituicao = regras.get(simbolo, simbolo)
            frase_nova = frase_nova + substituicao
        frase_inicial = frase_nova
    return frase_nova

def desenha_sistema(simbolos):
    """
    Recebe uma frase e desenha de acordo com
    as "regras de desenho".
    """
    for simbolo in simbolos:
        if simbolo == "F":
            line(0, 0, 0, -tamanho)
            translate(0, -tamanho)
        if simbolo == "+":
            rotate(radians(angulo))
        if simbolo == "-":
            rotate(radians(-angulo))
        if simbolo == "[":
            push_matrix()
        if simbolo == "]":
            pop_matrix()

def key_pressed():
    global tamanho, angulo, iteracoes, frase
    if key == 'z':
        tamanho -= 1  # tamanho = tamanho - 1
    if key == 'x':
        tamanho += 1
    if key == 'a':
        angulo -= 1
    if key == 's':
        angulo += 1
    if key == 'q':
        iteracoes -= 1
        frase = gerar_sistema(iteracoes, axioma, regras)
        print(len(frase))
    if key == 'w':
        iteracoes += 1
        frase = gerar_sistema(iteracoes, axioma, regras)
        print(len(frase))
```

## Exemplo 3D

![animacao](assets/LSystem-3D.gif)

Exemplo usando `P3D` e adicionando `rotate_y()`

```python
axioma = 'X'
regras = {
    'X': 'F+[[X]-X]-F[-FX]+X',
    'F': 'FF',
    }
passo = 5
angulo = 25  # angulo em graus
iteracoes = 5

def setup():
    global frase_resultado
    size(900, 900, P3D)
    frase_inicial=axioma
    for _ in range(iteracoes):
        frase_resultado = ''
        for simbolo in frase_inicial:
            substituir = regras.get(simbolo, simbolo)
            frase_resultado = frase_resultado + substituir
        # print(frase_inicial, frase_resultado)
        frase_inicial=frase_resultado
    print(len(frase_resultado))

def draw():
    background(210, 210, 150)
    stroke_weight(3)
    angulo = 25
    # angulo = mouse_x / 70.0
    translate(width / 2, height * 0.8)
    rotate_y(frame_count / 100.0)
    for simbolo in frase_resultado:
        if simbolo == 'X':   # se simbolo for igual a 'X'
            pass
        elif simbolo == 'F':   # else if (senão se) o simbolo é F
                line(0, 0, 0, -passo)
                translate(0, -passo)
                rotate_y(radians(-angulo))
        elif simbolo == '+':
            rotate(radians(-angulo))  # + random(-5, 5)))
        elif simbolo == '-':
            rotate(radians(+angulo))  # + random(-5, 5)))
        elif simbolo == '[':
            push_matrix()
        elif simbolo == ']':
            pop_matrix()
```

