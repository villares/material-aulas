# L-System - Sistema de Lindenmayer

L-systems são as estruturas e procedimentos criados por aristide lindenmayer para estudar o crescimento de algas e plantas, por meio da manipulação de sequências de símbolos. as sequências são geradas por sucessivas iterações da aplicação de regras de substituição. A tradução computacional dessas estruturas foi discutida pela primeira vez em * lecture notes in biomathematics * por przemyslaw prusinkiewcz e james hanan.

referências externas:
- [the algorithmic beauty of plants](http: // algorithmicbotany.org/papers /  # abop) (+ diversos livros e artigos)
- https: // www.cgjennings.ca/articles/l-systems /
- http: // www.paulbourke.net/fractals/lsys /

# Um exemplo completo

```python
axioma="X"
regras={"X": "F+[[X]-X]-F[-FX]+X",
          "F": "FF"
          }
tamanho=10
angulo=25
iteracoes=4  # repeticoes (voltas na aplicação das regras)
xo, yo=300, 500

def setup():
    global frase
    size(600, 600)
    frase=gerar_sistema(iteracoes, aximoa, regras)
    print(len(frase))

def draw():
    background(240, 240, 200)
    translate(xo, yo)
    desenha_sistema(frase)

def gerar_sistema(num, axioma, regras):
    """
    produz um sistema-L a partir da  frase `axioma`,
    repetindo `num` iterações, as substituições descritas
    nas pelo dicionário `regras`
    """
    frase_inicial=axioma
    for i in range(num):
        frase_nova=""
        for simbolo in frase_inicial:
            substituicao=regras.get(simbolo, simbolo)
            frase_nova=frase_nova + substituicao
        frase_inicial=frase_nova
    return frase_nova

def desenha_sistema(simbolos):
    """
    recebe uma frase e desenha de acordo com
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
        frase=gerar_sistema(iteracoes, axioma, regras)
        print(len(frase))
    if key == 'w':
        iteracoes += 1
        frase=gerar_sistema(iteracoes, axioma, regras)
        print(len(frase))
```


# Exemplo 3D

exemplo usando `P3D` e adicionando `rotate_y()`

```python

axioma='X'
regras={
    'X': 'F+[[X]-X]-F[-FX]+X',
    'F': 'FF',
    }
passo=5
angulo=25  # angulo em graus
iteracoes=5

def setup():
    global frase_resultado
    size(900, 900, P3D)
    frase_inicial=axioma
    for _ in range(iteracoes):
        frase_resultado=''
        for simbolo in frase_inicial:
            substituir=regras.get(simbolo, simbolo)
            frase_resultado=frase_resultado + substituir
        # print(frase_inicial, frase_resultado)
        frase_inicial=frase_resultado
    print(len(frase_resultado))

def draw():
    background(210, 210, 150)
    stroke_weight(3)
    angulo=25
    # angulo = mouseX / 70.0
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

# Exemplo 3D

exemplo criando padroes animados usando `P3D` e `for _ in range(): `


```python

axioma='X'
regras={
    'X': 'F+[[X]-X]-F[-FX]+X',
    'F': 'FF',
    }
passo=5
angulo=25  # angulo em graus
iteracoes=5
tam=random(5, 10)


def setup():
    global frase_resultado
    size(900, 900, P3D)
    frase_inicial=axioma
    for _ in range(iteracoes):
        frase_resultado=''
        for simbolo in frase_inicial:
            substituir=regras.get(simbolo, simbolo)
            frase_resultado=frase_resultado + substituir
        # print(frase_inicial, frase_resultado)
        frase_inicial=frase_resultado
    print(len(frase_resultado))

def draw():
    background(200, 200, 150)
    random_seed(2)
    stroke_weight(1)
    for i in range(4):
        for j in range(4):
            if j % 2 == 0:
                x=200 + i * 200
            else:
                x=100 + i * 200
            y=200 + j * 200
            # plot(x, y, 5 + j * 10 -i * 3)
            plot(x, y + 50, random(10, 25))

def plot(x, y, angulo):
        push_matrix()
        translate(x, y)
        scale(0.5)
        # angulo = 25
        # angulo = mouseX / 70.0
        # translate(width / 2, height * 0.8)
        rotate_y(frame_count / 35.0)
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
        pop_matrix()

def key_pressed():
    if key == 's':
        save_frame('imagem###.png')

```
