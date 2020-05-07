
# Valores e seus tipos

## Valores

Quando atribuimos um valor a uma variável, por exemplo `i = 10`, o `i` é um nome que aponta para um valor na memória do computador, `10`, e esse valor é de uma determinada categoria, de um *tipo*, neste caso, é um número inteiro, tipo *integer* que é normalmente abreviado como `int`.

Já `10.5`, `0.2` ou até mesmo `10.` (dez seguido de um ponto), são considerados números de ponto flutuante, *floating point* ou abreviadamente `float`.

Textos, que aparecem entre aspas quando no meio do código de um programa, como por exemplo `'hello'` ou `"Eric Idle"`, são do tipo `string` (cadeia de caracteres em português) que abreviamos como `str`. Repare que `"1010"` é um `string` enquanto `1010` é um número `int` e `1010.0` é um `float`. 

Outro tipo importante é o booleano (`boolean`), com apenas os dois valores `True` ou `False` (verdadeiro ou falso), é o tipo dos valores resultantes das operações lógicas (como `and`,  `or` e `not`), comparações (como `==`, `!=`,  `>`, `<`, `>=` e etc.) ou ainda valores que indicam um estado (como `mousePressed` é verdadeiro ou falso dependendo do estado dos botões do mouse).

## Conversão

É necessário por vezes converter os dados de um tipo para outro, como por exemplo o número sorteado por uma função `random()` que é um `float` pode ser convertido em `int`, sendo truncado (encurtado) se tiver uma parte não inteira.

Números podem ser convertidos em texto (`string`) usando `str(num)` ou com `'{}'.format(num)`.

```python
R = int(random(256))
println("Red: " + str(R))  # ou println("Red: {}".format(R))
```

## Tipos dos argumentos e valores devolvidos for funções

Os valores que usamos entre parênteses em uma chamada de função (argumentos, dentro da função são chamados parâmetros) frequentemente precisar ser de tipos específicos. Por exemplo `range()` só aceita como argumentos números inteiros. A função `text()`, precisa de um *string* e dois números (para as coordenadas): `text("Texto", x, y)`. 

Para descobrir quais são os tipos dos argumentos que devemos usar com uma determinada função, precisamos ler a documentação (no caso de funções embutidas, pré-definidas, ou de bibliotecas externas) ou a definição da função. Da mesma forma é do nosso interesse saber os tipos dos valores devolvidos pelas funções.

Algumas funções executam operações mas não devolvem um valor, como `setup()`, `draw()`, `noStroke()` e `rect()`, por exemplo. Na verdade, sendo mais precisos, em Python, essas funções devolvem o valor especial `None` (que poderíamos imaginar como "nada" ou "nenhum").

Já outras funções, devolvem algum valor como resultado. A função `color()` do Processing, por exemplo, recebe como argumentos números e devolve uma cor:

`minha_cor = color(255, 0, 0)  # A variável minha_cor aponta para uma cor vermelha na memória`

Podemos construir uma função que devolve uma cor nós também:

```python
def cor_sorteada(alpha):
   r = int(random(256)
   g = int(random(256)
   b = int(random(256)
   return color(r, g, b, alpha)

minha_cor = cor_sorteada(255) # sorteia uma cor 
```

### Alguns tipos (classes de objetos)

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

### Glossário

[**valor**](https://penseallen.github.io/PensePython2e/01-jornada.html#termo:valor) Uma das unidades básicas de dados, como um número ou string, que um programa manipula.

[**tipo**](https://penseallen.github.io/PensePython2e/01-jornada.html#termo:tipo) Uma categoria de valores. Alguns tipos que vimos por enquanto são números inteiros (tipo `int`), números de ponto flutuante (tipo `float`) e *strings* (tipo `str`).

[**inteiro**](https://penseallen.github.io/PensePython2e/01-jornada.html#termo:inteiro) Um tipo que representa números inteiros.

[**ponto flutuante**](https://penseallen.github.io/PensePython2e/01-jornada.html#termo:ponto%20flutuante) Um tipo que representa números com partes fracionárias.

[**string**](https://penseallen.github.io/PensePython2e/01-jornada.html#termo:string) Um tipo que representa sequências de caracteres.

---
Este material é baseado no material do curso https://arteprog.space/programacao-criativa/

---
Texto e imagens / text and images: CC BY-NC-SA 4.0; Código / code: GNU GPL v3.0 exceto onde explicitamente indicado por questões de compatibilidade.

