# Instruções condicionais e operadores lógicos

## As bifurcações no caminho de execução do código

Imgine o seguinte cenário...

Saindo de casa, se (`if`) está chovendo, a condição "chovendo" é verdadeira (`True`), então levo o guarda-chuva;

Opcionalmente, podemos definir que, senão (`else`), quando a condição "chovendo" é falsa (`False`), devo levar óculos de sol.

## Sintaxe `if` e `if`/`else`

``` python
if chovendo:            # a condição "chovendo" é avaliada como true (verdadeiro) ou false (falso)
    levarGuardaChuva()  # se verdadeira a condição, então este bloco de código será executado
                        # termina o bloco do “se/então”, continua o passeio.
```
![condicional](https://arteprog.space/programacao-criativa/assets/imagens/condicional-sem-else.jpg)


``` python
if chovendo:            # a condição "chovendo" é avaliada como True (verdadeiro) ou False (falso)
    levarGuardaChuva()  # se verdadeira a condição, então este bloco de código será executado
else:                   # termina o “se/então” e começa o “senão”
    levarOculos()       # este bloco será executado apenas quando "chovendo" é falso
                        # termina o bloco do “senão”, continua o passeio.
```
![condicional](https://arteprog.space/programacao-criativa/assets/imagens/condicional-com-else.jpg)


## Exemplos

![exemplo1](https://arteprog.space//programacao-criativa/assets/imagens/condicional1.png)

``` python
def setup():
    size(200, 200)

def draw():
    if mouseY < 100:    # se a posição Y do mouse for menor que 100, o mouse estiver perto do topo da tela
        fill(255)       # então pede preenchimento branco (só executa quando mouseY é menor que 100)
    else:               # termina o bloco “se/então” e começa o do “senão”
        fill(100)       # preenchimento cinza 100 (só executa quando mouseY não é menor que 100)
                        # termina o bloco do “senão”    
    if mousePressed:                    # Se o mouse estiver pressionado
        ellipse(mouseX, mouseY, 10, 10) # Então desenha um círculo na posição do mouse
                                        # termina o bloco (repare que não faz nada se o mouse estiver solto)
    if keyPressed and key == 'a':    # Se uma tecla foi precionada E a tecla foi o caractere 'a'
        background(200)              # Apague a tela com um fundo cinza (só executa sob as condições acima)
```

## Comparações com operadores relacionais, operadores lógicos e utros casos 

Os valores `True` (verdadeiro) e `False` (falso) são o resultado de expressões booleanas (*boolean*, em homenagem a [George Boole](https:#pt.wikipedia.org/wiki/George_Boole)) como as comparações com operadores relacionais, `==` (igualdade), `>` (maior que) ou ainda operações lógicas **e** (`and`), **ou** (`or`) e **não** (`not`). 

Podem ser armazenados em variáveis, representando um *estado* no programa, e são os mesmos valores obtidos quando usamos as variáveis de sistema *mousePressed* e *keyPressed*, por exemplo.
 
|operador | uso | descrição |
|:---:  |:---: |--- |
| `>` | `a > b` |  verdadeiro se *a* **maior** que *b* |
| `>=` | `a >= b` | verdadeiro se *a* **maior ou igual** a *b* |
| `<` | `a < b` | verdadeiro se *a* **menor** que *b* |
| `<=` | `a <= b` | verdadeiro se *a* **menor ou igual** a *b* |
| `==` | `a == b` | verdadeiro se *a* **igual** a *b* |
| `!=` | `a != b` | verdadeiro se *a* **diferente** de *b* |
| `and` | `a and b` | verdadeiro se *a* **e** *b* forem ambos verdadeiros |
| `or` | `a or b` | verrdadeiro se *a* **ou** *b* forem verdadeiros |
| `not` | `not a` | **não** *a* verdadeiro resulta falso, e **não** *a* falso resulta verdadeiro |
| `in` | `a in b` | verdadeiro se elemento *a* **existe dentro** da coleção *b* |

## Extra: Condicionais aninhadas e outras estruturas

É comum encontraramos, além da composição das condições usando operadores lógicos, `ìf` dentro de um `ìf` ou de um `else`.
No caso de repetidos `if`, o 'else + if' é abreviado `elif`.

```python
if a == 0:
    faz_isto()
elif a == 1:
    faz_aquilo()
else:
    faz_outra_coisa()
```

Confira também a abreviação de `if` usada para atribuições ou dentro de outras expressões (conhecida em outras linguagens como 'operador condicional ternário'): 

```python
n = x if cond else y
```
Isso equivale a:

```python
if cond == True:
   n = x
else:
   n = y
```
Veja um outro exemplo:

```python
a = 50 if keyPressed else 100
# A variável a passa a valer 50 se houver uma tecla pressionada
# senão, passa a valer 100
```

Você pode ainda encontrar a seguinte expressão:

```
a = a or b # é o mesmo que: a = a if a else b
```

Essa forma é muito usada em funções com parâmetros default:

```python
def quadrado(x, y, tamanho=None):
    tamanho = tamanho or 10
    # Isso significa que se tamanho for 0 ou `None` então tamanho deve passar a valer 10:
    # Equivalente a:
    # tamanho = tamanho if tamanho else 10
    rect(x, y, tamanho, tamanho)
```

## Glossário

[**expressão booleana**](https://penseallen.github.io/PensePython2e/05-cond-recur.html#termo:expressão%20booleana) Uma expressão cujo valor é True (verdadeiro) ou False (falso).

[**operador relacional**](https://penseallen.github.io/PensePython2e/05-cond-recur.html#termo:operador%20relacional) Um destes operadores, que compara seus operandos: `==`, `!=`, `>`, `<`, `>=` e `<=`.

[**operador lógico**](https://penseallen.github.io/PensePython2e/05-cond-recur.html#termo:operador%20lógico) Um destes operadores, que combina expressões booleanas: `and` (e), `or` (ou) e `not` (não).

[**instrução condicional**](https://penseallen.github.io/PensePython2e/05-cond-recur.html#termo:instrução%20condicional) Uma instrução que controla o fluxo de execução, dependendo de alguma condição (como por exemplo o `if`).

[**condição**](https://penseallen.github.io/PensePython2e/05-cond-recur.html#termo:condição) A expressão booleana em uma instrução condicional que determina qual ramo deve ser executado.

---
Este material é baseado no material do curso https://arteprog.space/programacao-criativa/

---
Texto e imagens / text and images: CC BY-NC-SA 4.0; Código / code: GNU GPL v3.0 exceto onde explicitamente indicado por questões de compatibilidade.

