
# Variáveis, parâmetros, valores e seus tipos

## Valores

Quando atribuimos um valor a uma variável, por exemplo `i = 10`, o `i` é um nome que aponta para um valor na memória do computador, `10`, e esse valor é de uma determinada categoria, de um *tipo*, neste caso, é um número inteiro, tipo *integer* que é normalmente abreviado como `int`.

Já `10.5`, `0.2` ou até mesmo `10.` (dez seguido de um ponto), são considerados números de ponto flutuante, *floating point* ou abreviadamente `float`.

Textos, que aparecem entre aspas quando no meio do código de um programa, como por exemplo `'hello'` ou `"Eric Idle"`, são do tipo `string` (cadeia de caracteres em português) que abreviamos como `str`. Repare que `"1010"` é um `string` enquanto `1010` é um número `int` e `1010.0` é um `float`. 

Outro tipo importante é o booleano (`boolean`), com apenas os dois valores `True` ou `False` (verdadeiro ou falso), é o tipo dos valores resultantes das operações lógicas (como `and`,  `or` e `not`), comparações (como `==`, `!=`,  `>`, `<`, `>=` e etc.) ou ainda valores que indicam um estado (como `mousePressed` é verdadeiro ou falso dependendo do estado dos botões do mouse).

## Conversão

É necessário por vezes converter os dados de um tipo para outro, como por exemplo o número sorteado por uma função `random()` que é um `float` pode ser convertido em `int`, sendo truncado (encurtado) se tiver uma parte não inteira. E números podem ser convertidos em texto (`string`).

```python
R = int(random(256))
println("Red: " + str(R))  # ou println("Red: {}".format(R))
```

### Alguns tipos de valores (classes de objetos)

| tipo / classe | descrição |
| ---      | --- |
|`int`     | número inteiro, como `-5`, `0` ou `42`|
| `float`  | número com ponto flutante, como `.5` `3.` ou `6.267` (note que o separador decimal é o ponto)|
| `boolean`| valores `True` ou `False`|
| `color`  | uma cor, que pode ser construída com `color(R,G,B)` ou `color(R,G,B,Alfa)`|
| `PImage` | imagens raster/bitmap, podem ser criadas/carregadas na memória com `loadImage(arquivo_de_imagem)` |
| `PShape` | contém formas vetorais, como as descritas num SVG, pode ser criado com `loadShape(arquivo)`| 
| `PVector`| vetor, usado geralmente para descrever posição, velocidade ou aceleração (em 2 ou 3 dimensões) |
| `string` | cadeia de caracteres, são sequencias de caracteres ou glifos, no código são criados com aspas: `“texto”` |
| `list`   | lista, coleção ordenada de itens, construída com `list(itens)` ou com colchetes no código `[ ,]` |
| `tuple`  | coleção ordenada e imutável de itens, construída com `tuple(itens)` ou com parenteses no código `( ,)` |
| `set`    | conjunto não ordenado de itens 'hasheáveis', com `set(itens)` ou com chaves no código `{ ,}` | 
| `dict`   | dicionário um 'mapeamento' de chaves (*keys*) e valores, criado com `dict()` ou pares `{chave : valor,}` |
| `None`   | o "nenhum" é de um tipo especial único `None`e é devolvido por funções que não devolvem nada  |

## Parâmetros e funções

Os valores que uma função recebe quando invocada podem precisar ser de tipos específicos, que podem ser descobertos na documentação (no caso de funções pré-definidas ou de bibliotecas externas) ou lendo a definição da função.
Da mesma forma os tipos dos valores devolvidos por uma função são do nosso interesse.

Algumas funções apenas executam operações mas não devolvem um valor, como `setup()`, `draw()`, `noStroke()` e `rect()`, por exemplo. Na verdade, sendo mais cuidadosos, veremos que em Pyhon essas funções retornam o valor especial `None` (que poderíamos imaginar como "nada" ou "nenhum").

Já outras funções devolvem um valor. A função `color()` do Processing, por exemplo, recebe como argumentos números inteiros e devolve uma cor:

`color minhaCor = color(255, 0, 0)  # A variável minhaCor aponta para uma cor vermelha na memória`

Podemos construir uma outra função que devolve uma cor também:

```python
cor_sorteada(alpha):
   R = int(random(256)
   G = int(random(256)
   B = int(random(256)
   return color(R, G, B, alpha)
```

### Glossário

[**valor**](https://penseallen.github.io/PensePython2e/01-jornada.html#termo:valor) Uma das unidades básicas de dados, como um número ou string, que um programa manipula.

[**tipo**](https://penseallen.github.io/PensePython2e/01-jornada.html#termo:tipo) Uma categoria de valores. Alguns tipos que vimos por enquanto são números inteiros (tipo int), números de ponto flutuante (tipo float) e strings (tipo str).

[**inteiro**](https://penseallen.github.io/PensePython2e/01-jornada.html#termo:inteiro) Um tipo que representa números inteiros.

[**ponto flutuante**](https://penseallen.github.io/PensePython2e/01-jornada.html#termo:ponto%20flutuante) Um tipo que representa números com partes fracionárias.

[**string**](https://penseallen.github.io/PensePython2e/01-jornada.html#termo:string) Um tipo que representa sequências de caracteres.

---
Este material é baseado no material do curso https://arteprog.space/programacao-criativa/

---
Texto e imagens / text and images: CC BY-NC-SA 4.0; Código / code: GNU GPL v3.0 exceto onde explicitamente indicado por questões de compatibilidade.

