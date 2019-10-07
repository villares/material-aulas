
# Variáveis, parâmetros e seus tipos

## Valores

Quando atribuimos um valor a uma variável, por exemplo `i = 10`, o `i` aqui é um nome que vai apontar para um valor na memória do computador, `10`,  neste caso o tipo é `int`, um número inteiro.  

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
| None | o "nada" é devolvido por funções que não devolvem nada.
| `float`  | número com ponto flutante, como `.5` `3.` ou `6.267` (note que o separador decimal é o ponto)|
| `boolean` |  valores `true` ou `false`|
| `String`  | cadeia de caracteres, `“texto”` (
| `color`  |  armazena uma cor, que pode ser construída com `color(R,G,B)` ou `color(R,G,B,Alfa)`|


### Alguns tipos de objetos/classes 

| tipo/classe | descrição |
| --- | --- |
| `PImage` | imagens raster/bitmap
| `PShape` | formas vetorais, como as descritas num SVG
| `PVector` | vetor, usado geralmente para descrever posição, velocidade ou aceleração (em 2 ou 3 dimensões) |
