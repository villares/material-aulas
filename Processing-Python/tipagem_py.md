
# Variáveis, parâmetros e seus tipos

## Valores

Quando atribuimos um valor a uma variável, por exemplo `i = 10`, o `i` (um nome) apontar para um valor na memória do computador, `10`, e esse valor é de uma determinada categoria, tipo, neste caso, é um número inteiro que abreviamos como `int`.

Já `10.5`, `0.2` ou até mesmo `10.` (dez seguido de um ponto), são considerados números de ponto flutuantes, ou `float`.

Texto, que em geral aparece entre aspas quando no meio do código de um programa, como `'hello'` ou `"Eric Idle"`, são do tipo `String`.

Outro tipo curioso é o booleano (`boolean`) que pode ser apenas `True` ou `False` (verdadeiro ou falso).

## Conversão

É necessário por vezes converter os dados de um tipo para outro, como por exemplo o número sorteado por uma função `random()` que é um `float` pode ser convertido em `int`, sendo truncado (encurtado) se tiver uma parte não inteira. E números podem ser convertidos em texto (`String`).

```python
R = int(random(256))
println("Red: "+str(R))
```

## Parâmetros e funções

Os parâmetros ou argumentos que uma função recebe quando invocada tem tipos, que podem ser descobertos na documentação (no caso de funções pré-definidas ou de bibliotecas externas) ou na definição da função. Da mesma forma os dados retornados pela função tem um tipo. Algumas funções não retornan nada como `setup()`, `draw()`, `noStroke()` e `rect()`, por exemplo.

A função `color()` do Processing, por exemplo, recebe como argumentos números inteiros e devolve uma cor:

`color minhaCor = color(255, 0, 0)  # A variável minhaCor aponta para uma cor vermelha na memória`

Podemos construir uma função que retorna uma cor também:

```python
corSorteada(alpha):
   R = int(random(256)
   G = int(random(256)
   B = int(random(256)
   return color(R, G, B, alpha)
```

### Alguns tipos simples/primitivos

| tipo | descrição |
| --- | --- |
|`int`  |  número inteiro, como `-5`, `0` ou `42`|
| `float`  | número com ponto flutante, como `.5` `3.` ou `6.267` (note que o separador decimal é o ponto)|
| `boolean` |  valores `True` ou `False`|
| `String`  | cadeia de caracteres, `“texto”` (
| `None` | o "nenhum" é de um tipo especial único `None`e é devolvido por funções que não devolvem nada.


### Alguns tipos de objetos/classes 

| tipo/classe | descrição |
| --- | --- |
| `color`  |  armazena uma cor, que pode ser construída com `color(R,G,B)` ou `color(R,G,B,Alfa)`|
| `PImage` | imagens raster/bitmap
| `PShape` | formas vetorais, como as descritas num SVG
| `PVector` | vetor, usado geralmente para descrever posição, velocidade ou aceleração (em 2 ou 3 dimensões) |

---
Este material é baseado no material do curso https://arteprog.space/programacao-criativa/

---
Texto e imagens / text and images: CC BY-NC-SA 4.0; Código / code: GNU GPL v3.0 exceto onde explicitamente indicado por questões de compatibilidade.

