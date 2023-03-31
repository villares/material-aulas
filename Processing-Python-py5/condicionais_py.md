# Instruções condicionais e operadores lógicos
## As bifurcações no caminho de execução do código

<h1 id='toc'></h1>
<!--
###  Sumário

- [Sintaxe](#sintaxe-if-e-ifelse)
- [Comparações: operadores relacionais e operadores lógicos](#comparações-operadores-relacionais-e-operadores-lógicos)
   - [Um exemplo completo](#um-exemplo-completo)
- [Quadro de operadores](#quadro-de-operadores)
   - [Alguns exemplos e comentários](#alguns-exemplos-e-comentários)
- [Assuntos relacionados](#assuntos-relacionados)
-->

## Sintaxe `if` e `if`/`else`

```python 
if «condição»: #  se a condição for verdadeira, execute:
    «corpo» 
    
if «condição»: #  se a condição for verdadeira, execute:
    «corpo do `if`» 
else:          #  senão (se a condição é falsa) execute:
   «corpo do `else`»
```

### Imagine o seguinte cenário...

Saindo de casa, se (`if`) está chovendo, a condição "chovendo" é verdadeira (`True`), então levo o guarda-chuva;
Opcionalmente, podemos definir que, senão (`else`), quando a condição "chovendo" é falsa (`False`), devo levar óculos de sol.

``` python
# a condição "chovendo" é avaliada como True (verdadeiro) ou False (falso)
if chovendo:
    # se verdadeira a condição, então este bloco de código será executado
    levar_guarda_chuva()  
# termina o bloco do “se/então”, continua o passeio.
```
<img src="https://arteprog.space/programacao-criativa/assets/imagens/condicional-sem-else.jpg" title="Exemplo de if - desenho: Monica Rizzolli">

``` python
# a condição "chovendo" é avaliada como True (verdadeiro) ou False (falso)
if chovendo:
    # se verdadeira a condição, então este bloco de código será executado
    levar_guarda_chuva() 
else:               # termina o “se/então” e começa o “senão”
    levar_oculos()   # este bloco será executado apenas quando "chovendo" é falso
# termina o bloco do “senão”, continua o passeio.
```
<img src="https://arteprog.space/programacao-criativa/assets/imagens/condicional-com-else.jpg" title="Exemplo de if/else - desenho: Monica Rizzolli">

## Comparações: operadores relacionais e operadores lógicos

Os valores `True` (verdadeiro) e `False` (falso) são o resultado de expressões booleanas (*boolean*, em homenagem a [George Boole](https:#pt.wikipedia.org/wiki/George_Boole)) como as comparações com operadores relacionais, `==` (igualdade), `>` (maior que) ou ainda operações lógicas **e** (`and`), **ou** (`or`) e **não** (`not`). 

Valores `True` e `False` podem ser atribuidos a variáveis, muitas vezes representando um *estado* no programa, são os valores que obtemos quando usamos as variáveis de sistema *is_mouse_pressed* e *is_key_pressed*, por exemplo. É comum termos variáveis indicadoras (*flags*) que apontam para um estado da operação do programa: `gravando = True`,  `soma_concluida = False`.

### Um exemplo completo

No exemplo a abaixo usamos uma estrutura `if`/ `else` para escolher a cor de preenchimento dos círculos, como resultado da comparação `mouseY < 128`. Usamos o valor booleano de `mousePressed` (`True` ou `False`) em um `if` que determina se algum círculo yé desenhado ou não. Por fim usamos um `if` que combina dois valores usando `and`(**e**), `is_key_pressed` e a comparação de igualdade `==`, para decidir se deve apagar o desenho (`is_key_pressed and key == 'a'`).

``` python
def setup():
    size(256, 256)
    background(0, 100, 0)  # fundo verde

def draw():
    # se a posição Y do mouse for menor que 128 (mouse na metade de cima da tela)
    if mouse_y < 128:    
        fill(255)  # então pede preenchimento branco (se mouseY é menor que 128)
    else:          # termina o bloco “se/então” e começa o do “senão”
        fill(100)  # preenchimento cinza 100 (se mouseY não é menor que 128)
                   # termina o bloco do “senão”
                   
    # Se o mouse estiver pressionado
    if is_mouse_pressed:                    
        ellipse(mouse_x, mouse_y, 50, 50) # desenha um círculo na posição do mouse
    # termina o bloco (repare que não faz nada se o mouse estiver solto)
    
    # Se uma tecla foi precionada E a tecla foi o caractere 'a'
    if is_key_pressed and key == 'a':    
        background(0, 100, 0)  # apague a tela com um fundo verde
```
![exemplo condicional](assets/condicional.gif)

## Quadro de operadores 
 
|operador | uso | descrição |
|:---:  |:---: |--- |
| `>` | `a > b` |  verdadeiro se *a* **maior** que *b* |
| `>=` | `a >= b` | verdadeiro se *a* **maior ou igual** a *b* |
| `<` | `a < b` | verdadeiro se *a* **menor** que *b* |
| `<=` | `a <= b` | verdadeiro se *a* **menor ou igual** a *b* |
| `==` | `a == b` | verdadeiro se *a* **igual** a *b* |
| `!=` | `a != b` | verdadeiro se *a* **diferente** de *b* |
| `and` | `a and b` | verdadeiro se *a* **e** *b* forem ambos verdadeiros |
| `or` | `a or b` | verdadeiro se *a* **ou** *b* forem verdadeiros |
| `not` | `not a` | se *a* verdadeiro resulta falso, e sendo *a* falso resulta verdadeiro |
| `in` | `a in b` | verdadeiro se elemento *a* **existe dentro** da coleção *b* |
| `is` | `a is b` | verdadeiro se *a* **é o mesmo objeto** do que *b*, não bastando serem iguais |

### Alguns exemplos e comentários
```python
# maior que
n = 12
n_maior_que_10 = n > 10  # True
n = 5
n_maior_que_10 = n > 10  # False
# maior ou igual a
n = 10
n_maior_ou_ingual_a_10 = n >= 10  # True
# menor que / menor ou igual a
n = 5
n_menor_que_10 = n < 10 # True
n_menor_ou_igual_a_4 = n <= 4  # False

# igualdade e diferença
n, m = 10, 10.0    # n é int, m é float
numeros_iguais = n == m  # True  10 é igual a 10.0
numeros_diferentes = n != m  # False
numeros_diferentes = n != 11  # True, 10 não é igual a 11

# operador in (contido em, existe em)
contem_a = 'a' in 'abacaxi'  # True
contem_1 = 1 in [0, 1, 2, 3]  # True
nao_contem_4 = 4 not in [0, 1, 2, 3] # True
```

Para efeitos de operações lógicas, e no uso com `if`, por exemplo, os valores `0` (zero), `None`, `""` (string vazio), `[]` lista vazia, ou qualquer coleção vazia, são considerados como "falsos" (`False`), já qualquer outro número, texto (string) ou coleção com itens, são considerados "verdadeiros" (`True`). 

A função `bool()` converte valores ou expressões entre os parenteses em `True` ou `False` (os chamados valores booleanos) nos permitindo investigar como Python os interpreta! Note que se comparados diretamente entre si zero, `None`, um string vazio e uma lista vazia não são a mesma coisa, mas se convertidos com `bool()` são todos convertidos no valor `False`. Já `1`,`200` ou `"Unicamp"`, serão convertidos com `bool()` em `True`. 

```python
# Agradecimentos à Fabiana Costa que pegou um erro na versão anterior deste exemplo

texto = ""  # aspas sem nada dentro, também funcionaria com `texto = None`
print(bool(texto) == False)  # exibe True
if not texto:   # será acionado se o string texto for vazio ou None
   texto = "novo texto"
# mas...
print(texto == False)  # exibe False!
print(texto == True)  # exibe False!   
# curiosamente...
print(0 == False) # e também `print(1 == True)`, exibem True!
# Internamente verdadeiro e falso (True & False) são 1 e 0 no Python!
# isso permite certas malandragens como multiplicar algo por verdadeiro ou falso...
# resultando no próprio número ou 0 respectivamente.
   
# resumindo
print(bool(""))    # exibe False  (um string, texto, vazio)
print(bool("oi"))  # exibe True   (qualquer outro string)
print(bool(0))     # exibe False  (o número zero)
print(bool(2))     # exibe True   (qualquer outro número)
print(bool([]))    # exibe False  (uma lista vazia)
print(bool([0]))   # exibe True   (uma lista com um zero dentro)
```

Sobre o operador `is`, não acredito que você vá precisar dele tão cedo (na dúvida, não use!) mas já que ele estava no quadro, veja o exemplo a seguir, pois demonstra uma característica importante do Python chamada *aliasing*, ou "apelidamento".

```python
ponto_a = (10, 20)
ponto_b = (10, 20)
ponto_c = ponto_a  # ponto_c é um outro "apelido" (alias) para o objeto que chamamos de ponto_a

print(ponto_a == ponto_b)  # exibe True, as coordenadas são iguais
print(ponto_a is ponto_b)  # exibe False, são objetos diferentes na memória 
print(ponto_a is ponto_c)  # exibe True, são o mesmo objeto na memória
```

## Assuntos relacionados

* [Condições aninhadas e outras estruturas condicionais](condicionais_2.md)

## Glossário

[**expressão booleana**](https://penseallen.github.io/PensePython2e/05-cond-recur.html#termo:expressão%20booleana) Uma expressão cujo valor é True (verdadeiro) ou False (falso).

[**operador relacional**](https://penseallen.github.io/PensePython2e/05-cond-recur.html#termo:operador%20relacional) Um destes operadores, que compara seus operandos: `==`, `!=`, `>`, `<`, `>=` e `<=`.

[**operador lógico**](https://penseallen.github.io/PensePython2e/05-cond-recur.html#termo:operador%20lógico) Um destes operadores, que combina expressões booleanas: `and` (e), `or` (ou) e `not` (não).

[**instrução condicional**](https://penseallen.github.io/PensePython2e/05-cond-recur.html#termo:instrução%20condicional) Uma instrução que controla o fluxo de execução, dependendo de alguma condição (como por exemplo o `if`).

[**condição**](https://penseallen.github.io/PensePython2e/05-cond-recur.html#termo:condição) A expressão booleana em uma instrução condicional que determina qual ramo deve ser executado.

---

Este material é baseado no material do curso https://arteprog.space/programacao-criativa/ - Texto e imagens: CC BY-NC-SA 4.0; Código: GNU GPL v3.0 exceto onde explicitamente indicado por questões de compatibilidade.
