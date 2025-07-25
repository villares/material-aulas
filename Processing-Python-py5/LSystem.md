# L-System - Sistema de Lindenmayer

<!-- 
![image](https://github.com/villares/material-aulas/assets/3694604/e0e6f78d-047c-4070-9218-4d1a7e91d183)
-->

L-Systems são as estruturas e procedimentos criados por Aristide Lindenmayer para estudar o crescimento de algas e plantas, por meio da manipulação de sequências de símbolos. As sequências são geradas por sucessivas iterações da aplicação de regras de substituição. 

A tradução computacional dessas estruturas foi discutida pela primeira vez na serie *Lecture Notes in Biomathematics* com o artigo [Lindenmayer Systems, Fractals, and Plants](https://link.springer.com/content/pdf/10.1007/978-1-4757-1428-9.pdf)  por Przemyslaw Prusinkiewcz e James Hanan (DOI: 10.1007/978-1-4757-1428-9).

> Mais referências:
> 
> - [The Algorithmic Beauty of Plants](http://algorithmicbotany.org/papers/#abop) (+ diversos livros e artigos)
> - [Lindenmayer systems: Describing how things grow with strings of letters, bye Christopher G Jennings](https://www.cgjennings.ca/articles/l-systems/)
> - [L-System User Notes, by Paul Bourke](http://www.paulbourke.net/fractals/lsys/)
> - [Using Lindenmayer Systems to Introduce Computer Science Concepts](https://www.russellgordon.ca/cemc/2017/lindenmayer-systems/)
> - [Wikipedia: L-system](https://en.wikipedia.org/wiki/L-system)


## Pré-requisitos

Para entender os exemplos apresentados mais à frente, é preciso familiaridade com algumas ideias do Python e da biblioteca py5:
- É possível percorrer os caracteres (letras ou símbolos) de uma cadeia de caracteres (*string*) e podemos compor uma nova concatenando elementos;
- A estrutura de dados [dicionário (*dict*)](dicionario.md) pode ser usada para armazenar regras de substiruição;
- Se desenharamos linhas ao mesmo tempo que [modificamos o sistema de coordenadas](transformacoes_coordenadas) a cada passo, podemos mudar de direção e também voltar a pontos anteriores do desenho.

### Percorrendo e concatenando *strings*

Podemos percorrer uma palavra com um laço `for`.
```python
>>> for letra in 'aeiou':
       print(letra)
a
e
i
o
u
```

Podemos concatenar novas palavras com o operador `+`. Um *string* vazio com `''` pode ser concatenado sem alterar o resultado.

```python
>>> 'a' + 'e' + 'i' + 'o' + 'u'
'aeiou'

>>> '' + 'a'
'a'  
```

### Usando dicionários para fazer substituições em *strings*

Um dicionário é uma estrutura que guarda pares *chave-valor*. Os *valores* podem ser pesquisados na estrutura a partir de uma *chave*. Quando consultamos o dicionário com a sintaxe dos colchetes `dicionario[chave]`, ele entrega o o valor, e se não houver a chave ocorre uma exceção `KeyError`. Usando o método `.get(chave)` é possível evitar essa excessãom e o valor especial `None` é devolvido, mas e usarmos a forma `.get(chave, valor_para_chave_faltando)` é possível escolher o que o dicionário devolve caso a chave não seja encontrada. 

```python
>>> ingles = {'maçã': 'apple', 'pêra': 'pear'}

>>> ingles['maçã']
'apple'

>>> fruta = 'cupuaçu'  # não tem 'cupuaçu' no dicionário

>>> ingles[fruta]   # a fruta é 'cupuaçu'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'cupuaçu'

>>> ingles.get(fruta, 'não sei') # .get() evita o erro
'não sei'

>>> ingles.get(fruta, fruta)  
'cupuaçu'
```

Como pode ser observado no exemplo acima, se usarmos a forma `.get(chave, chave)`, obtemos a própria chave caso ela não seja encontrada no dicionário, e isso se mostra muito útil quando usamos o dicionário para indicar regras de substituição: a falta da chave indica que a própria chave deve ser usada sem nenhuma substituição.

No exemplo abaixo vamos armazenar algumas letras como chaves associadas a uma sequência de letras como valor para cada uma delas, usaremos o valores para substituir as letras das chaves encontradas em um laço `for`.

```python
vogais = {'a': 'aaa', 'e': 'eeê', 'i': 'iih', 'o': 'oôo', 'u': 'üüü'}
palavra = 'anticonstitucionalissimamente'
nova_palavra = ''
for letra in palavra:
    nova_palavra = nova_palavra + vogais.get(letra, letra)
print(nova_palavra)
```
Resultado: **`aaantiihcoôonstiihtüüüciihoôonaaaliihssiihmaaameeênteeê`**

### Desenhando linhas, como se arrastando uma caneta

Para simular o movimento de uma "caneta" fazendo linhas sucessivas, podemos mover a origem do sistema de coordenadas como `translate()`  desenhar uma linha e em seguida mover a origem para o final da linha, para mudar a orientação dos traços é possível "girar o papel" em torno da origem com `rotate()`. Se salvarmos o estado do sistema de coordenadas com `push_matrix()` podemos desfazer transformações posteriores com `pop_matrix()`, trazendo a "caneta" para um ponto e orientação anterior.

Veja abaixo um exemplo e o resultado que gera.

<!-- editor-pyp5js -->
```python
def setup():
    size(400, 400)
    translate(200, 350)  # move a origem para um ponto mais abaixo do que o meio da tela (posição 0)
    
    line(0, 0, 0, -100)  # uma linha de tamanho 100 para cima
    translate(0, -100)   # muda a origem para o final da linha (posição 1)
    
    rotate(radians(45))  # gira o papel 45 graus
    
    line(0, 0, 0, -100)  # uma linha de tamanho 100 para cima
    translate(0, -100)   # muda a origem para o final da linha (posição 2)

    push_matrix()        # guarda o sistema de coordenadas (posição 2)
    
    rotate(radians(45))  # "gira o papel" 45 graus para a esquerda
    
    line(0, 0, 0, -100)  # uma linha de tamanho 100 para cima
    translate(0, -100)   # muda a origem para o final dalinha (posição 3)
    
    pop_matrix()         # vota ao sistema de coordenadas (posição 2)
    
    rotate(radians(-45))  # "gira o papel" 45 graus para a direita
        
    line(0, 0, 0, -100)  # uma linha de tamanho 100 para cima
    translate(0, -100)   # muda a origem para o final dalinha (posição 4)
```

![turtle-move](https://github.com/user-attachments/assets/c40ca77b-0a90-43fc-9b19-9807b6512314)

## Um exemplo inicial de L-System

Estudados os pré-requisitos podemos finalmente construir um exemplo de L-System.

Partindo de regras de substição aplicadas à uma frase inicial (axioma) é possível produzir desenhos que se aproximam de plantas e fractais com autosimilaridade em várias escalas. Para isso parte dos símbolos (letras) são interpretados como uma ação de desenho, tal como andar com uma caneta para frente, virar para direita ou para esquerda um certo ângulo, ou ainda, volar a uma posição anterior armazenada em uma pilha de estados do sistema de coordenadas.

![image](https://github.com/villares/material-aulas/assets/3694604/e0e6f78d-047c-4070-9218-4d1a7e91d183)

<!-- editor-pyp5js -->
```python
axioma = "X"
regras = {"X": "F+[[X]-X]-F[-FX]+X",
          "F": "FF"
          }

passo = 10
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
            line(0, 0, 0, -passo)  # desenha uma linha
            translate(0, -passo)   # move a origem 
        if simbolo == "+":
            rotate(radians(angulo)) 
        if simbolo == "-":
            rotate(radians(-angulo))  
        if simbolo == "[":
            push_matrix()  # grava o estado (posição e ângulo)
        if simbolo == "]":
            pop_matrix()   # volta ao último estado gravado
```

## Uma versão com interatividade

Esta versão permite controlar com o teclado o tamnaho das linhas (passo), ângulo e número de iterações (cuidado que muitas iterações podem tornar o sketch muito lento)>

<!-- editor-pyp5js -->
```python
axioma = "X"
regras = {"X": "F+[[X]-X]-F[-FX]+X",
          "F": "FF"
          }
passo = 10
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
            line(0, 0, 0, -passo)
            translate(0, -passo)
        if simbolo == "+":
            rotate(radians(angulo))
        if simbolo == "-":
            rotate(radians(-angulo))
        if simbolo == "[":
            push_matrix()
        if simbolo == "]":
            pop_matrix()

def key_pressed():
    global passo, angulo, iteracoes, frase
    if key == 'z':
        passo -= 1  # passo = passo - 1
    if key == 'x':
        passo += 1
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
> Esta última versão com 3D precisa modificações no editor online do pyp5js pois o p5.js tem a origem no centro da tela quando em 3D... esperimente este link com o [código modificado](https://abav.lugaralgum.com/material-aulas/pyp5js/py5mode/?sketch=YXhpb21hJTIwJTNEJTIwJ1gnJTBBcmVncmFzJTIwJTNEJTIwJTdCJTBBJTIwJTIwJTIwJTIwJ1gnJTNBJTIwJ0YlMkIlNUIlNUJYJTVELVglNUQtRiU1Qi1GWCU1RCUyQlgnJTJDJTBBJTIwJTIwJTIwJTIwJ0YnJTNBJTIwJ0ZGJyUyQyUwQSUyMCUyMCUyMCUyMCU3RCUwQXBhc3NvJTIwJTNEJTIwNSUwQWFuZ3VsbyUyMCUzRCUyMDI1JTIwJTIwJTIzJTIwYW5ndWxvJTIwZW0lMjBncmF1cyUwQWl0ZXJhY29lcyUyMCUzRCUyMDUlMEElMEFkZWYlMjBzZXR1cCgpJTNBJTBBJTIwJTIwJTIwJTIwZ2xvYmFsJTIwZnJhc2VfcmVzdWx0YWRvJTBBJTIwJTIwJTIwJTIwc2l6ZSg5MDAlMkMlMjA5MDAlMkMlMjBQM0QpJTBBJTIwJTIwJTIwJTIwZnJhc2VfaW5pY2lhbCUzRGF4aW9tYSUwQSUyMCUyMCUyMCUyMGZvciUyMF8lMjBpbiUyMHJhbmdlKGl0ZXJhY29lcyklM0ElMEElMjAlMjAlMjAlMjAlMjAlMjAlMjAlMjBmcmFzZV9yZXN1bHRhZG8lMjAlM0QlMjAnJyUwQSUyMCUyMCUyMCUyMCUyMCUyMCUyMCUyMGZvciUyMHNpbWJvbG8lMjBpbiUyMGZyYXNlX2luaWNpYWwlM0ElMEElMjAlMjAlMjAlMjAlMjAlMjAlMjAlMjAlMjAlMjAlMjAlMjBzdWJzdGl0dWlyJTIwJTNEJTIwcmVncmFzLmdldChzaW1ib2xvJTJDJTIwc2ltYm9sbyklMEElMjAlMjAlMjAlMjAlMjAlMjAlMjAlMjAlMjAlMjAlMjAlMjBmcmFzZV9yZXN1bHRhZG8lMjAlM0QlMjBmcmFzZV9yZXN1bHRhZG8lMjAlMkIlMjBzdWJzdGl0dWlyJTBBJTIwJTIwJTIwJTIwJTIwJTIwJTIwJTIwJTIzJTIwcHJpbnQoZnJhc2VfaW5pY2lhbCUyQyUyMGZyYXNlX3Jlc3VsdGFkbyklMEElMjAlMjAlMjAlMjAlMjAlMjAlMjAlMjBmcmFzZV9pbmljaWFsJTNEZnJhc2VfcmVzdWx0YWRvJTBBJTIwJTIwJTIwJTIwcHJpbnQobGVuKGZyYXNlX3Jlc3VsdGFkbykpJTBBJTBBZGVmJTIwZHJhdygpJTNBJTBBJTIwJTIwJTIwJTIwYmFja2dyb3VuZCgyMTAlMkMlMjAyMTAlMkMlMjAxNTApJTBBJTIwJTIwJTIwJTIwdHJhbnNsYXRlKC13aWR0aCUyMCUyRiUyMDIlMkMlMjAtaGVpZ2h0JTIwJTJGJTIwMiklMEElMjAlMjAlMjAlMjBzdHJva2Vfd2VpZ2h0KDMpJTBBJTIwJTIwJTIwJTIwYW5ndWxvJTIwJTNEJTIwMjUlMEElMjAlMjAlMjAlMjAlMjMlMjBhbmd1bG8lMjAlM0QlMjBtb3VzZV94JTIwJTJGJTIwNzAuMCUwQSUyMCUyMCUyMCUyMHRyYW5zbGF0ZSh3aWR0aCUyMCUyRiUyMDIlMkMlMjBoZWlnaHQlMjAqJTIwMC44KSUwQSUyMCUyMCUyMCUyMHJvdGF0ZV95KGZyYW1lX2NvdW50JTIwJTJGJTIwMTAwLjApJTBBJTIwJTIwJTIwJTIwZm9yJTIwc2ltYm9sbyUyMGluJTIwZnJhc2VfcmVzdWx0YWRvJTNBJTBBJTIwJTIwJTIwJTIwJTIwJTIwJTIwJTIwaWYlMjBzaW1ib2xvJTIwJTNEJTNEJTIwJ1gnJTNBJTIwJTIwJTIwJTIzJTIwc2UlMjBzaW1ib2xvJTIwZm9yJTIwaWd1YWwlMjBhJTIwJ1gnJTBBJTIwJTIwJTIwJTIwJTIwJTIwJTIwJTIwJTIwJTIwJTIwJTIwcGFzcyUwQSUyMCUyMCUyMCUyMCUyMCUyMCUyMCUyMGVsaWYlMjBzaW1ib2xvJTIwJTNEJTNEJTIwJ0YnJTNBJTIwJTIwJTIwJTIzJTIwZWxzZSUyMGlmJTIwKHNlbiVDMyVBM28lMjBzZSklMjBvJTIwc2ltYm9sbyUyMCVDMyVBOSUyMEYlMEElMjAlMjAlMjAlMjAlMjAlMjAlMjAlMjAlMjAlMjAlMjAlMjAlMjAlMjAlMjAlMjBsaW5lKDAlMkMlMjAwJTJDJTIwMCUyQyUyMC1wYXNzbyklMEElMjAlMjAlMjAlMjAlMjAlMjAlMjAlMjAlMjAlMjAlMjAlMjAlMjAlMjAlMjAlMjB0cmFuc2xhdGUoMCUyQyUyMC1wYXNzbyklMEElMjAlMjAlMjAlMjAlMjAlMjAlMjAlMjAlMjAlMjAlMjAlMjAlMjAlMjAlMjAlMjByb3RhdGVfeShyYWRpYW5zKC1hbmd1bG8pKSUwQSUyMCUyMCUyMCUyMCUyMCUyMCUyMCUyMGVsaWYlMjBzaW1ib2xvJTIwJTNEJTNEJTIwJyUyQiclM0ElMEElMjAlMjAlMjAlMjAlMjAlMjAlMjAlMjAlMjAlMjAlMjAlMjByb3RhdGUocmFkaWFucygtYW5ndWxvKSklMjAlMjAlMjMlMjAlMkIlMjByYW5kb20oLTUlMkMlMjA1KSkpJTBBJTIwJTIwJTIwJTIwJTIwJTIwJTIwJTIwZWxpZiUyMHNpbWJvbG8lMjAlM0QlM0QlMjAnLSclM0ElMEElMjAlMjAlMjAlMjAlMjAlMjAlMjAlMjAlMjAlMjAlMjAlMjByb3RhdGUocmFkaWFucyglMkJhbmd1bG8pKSUyMCUyMCUyMyUyMCUyQiUyMHJhbmRvbSgtNSUyQyUyMDUpKSklMEElMjAlMjAlMjAlMjAlMjAlMjAlMjAlMjBlbGlmJTIwc2ltYm9sbyUyMCUzRCUzRCUyMCclNUInJTNBJTBBJTIwJTIwJTIwJTIwJTIwJTIwJTIwJTIwJTIwJTIwJTIwJTIwcHVzaF9tYXRyaXgoKSUwQSUyMCUyMCUyMCUyMCUyMCUyMCUyMCUyMGVsaWYlMjBzaW1ib2xvJTIwJTNEJTNEJTIwJyU1RCclM0ElMEElMjAlMjAlMjAlMjAlMjAlMjAlMjAlMjAlMjAlMjAlMjAlMjBwb3BfbWF0cml4KCk%3D)
