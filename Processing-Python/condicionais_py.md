# Condicionais

## As bifurcações no caminho de execução do código

Saindo de casa, se (`if`) está chovendo, a condição "chovendo" é verdadeira (`True`), então levo o guarda-chuva;

opcionalmente defino que, senão (`else`), quando a condição "chovendo" é falsa (`False`), levo óculos de sol.

## Sintaxe if/else e if

![condicional](https://arteprog.space/programacao-criativa/assets/imagens/condicional-com-else.jpg)

``` python
if chovendo:            # a condição "chovendo" é avaliada como True (verdadeiro) ou False (falso)
    levarGuardaChuva()  # se verdadeira a condição, então este bloco de código será executado
else:                   # termina o “se/então” e começa o “senão”
    levarOculos()       # este bloco será executado apenas quando "chovendo" é falso
                        # termina o bloco do “senão”, continua o passeio.
```

![condicional](https://arteprog.space/programacao-criativa/assets/imagens/condicional-sem-else.jpg)

``` python
if chovendo:            # a condição "chovendo" é avaliada como true (verdadeiro) ou false (falso)
    levarGuardaChuva()  # se verdadeira a condição, então este bloco de código será executado
                        # termina o bloco do “se/então”, continua o passeio.
```

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

## Comparações e operadores lógicos

Os valores `True` (verdadeiro) e `False` (falso) são o resultado das comparações e das chamadas operações lógicas **e** (`and`), **ou** (`or`) e **não** (`not`). Podem ser armazenados em variáveis do tipo *boolean* (Booleano, em homenagem a [George Boole](https:#pt.wikipedia.org/wiki/George_Boole)) definidas pela pessoa que criou o programa, representando um *estado*.

Da mesma forma, são os valores acessados quando usamos as variáveis de sistema *mousePressed* e *keyPressed*.
 
|operador | uso | descrição |
|:---:  |:---: |--- |
| `>` | `e1 > e2` |  verdadeiro se *e1* **maior** que *e2* |
| `>=` | `e1 >= e2` | verdadeiro se *e1* **maior ou igual** a *e2* |
| `<` | `e1 < e2` | verdadeiro se *e1* **menor** que *e2* |
| `<=` | `e1 <= e2` | verdadeiro se *e1* **menor ou igual** a *e2* |
| `==` | `e1 == e2` | verdadeiro se *e1* **igual** a *e2* |
| `!=` | `e1 != e2` | verdadeiro se *e1* **diferente** de *e2* |
| `and` | `e1 and e2` | verdadeiro se *e1* **e** *e2* forem ambos verdadeiros |
| `or` | `e1 or e2` | verrdadeiro se *e1* **ou** *e2* forem verdadeiros |
| `not` | `not e1` | **não** *e1* verdadeiro resulta falso, e **não** *e1* falso resulta verdadeiro |

## Condicionais aninhadas e outras estruturas

É comum encontraramos, além da composição das condições usando operadores lógicos, `ìf` dentro de um `ìf` ou de um `else`.

No caso de repetidos `if`, o 'else + if' é abreviado `elif`.

Confira também a abreviação de `if` + atribuições, o `A if C == True else B`

```python
a = 50 if keyPressed else 100
# a vai valer 50 se houver uma tecla pressionada
# senão, vai valer 100
```

---
Este material é baseado no material do curso https://arteprog.space/programacao-criativa/

---
Texto e imagens / text and images: CC BY-NC-SA 4.0; Código / code: GNU GPL v3.0 exceto onde explicitamente indicado por questões de compatibilidade.

