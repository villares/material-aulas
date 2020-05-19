
# Valores e seus tipos

## Valores

Quando fazemos uma atribuição, criando ou alterando uma variável, por exemplo `i = 10`, o `i` é um nome que aponta para um valor na memória do computador, `10`, e esse valor é de uma determinada categoria, de um *tipo*, neste caso, é um número inteiro, tipo *integer* que é normalmente abreviado como `int`. 

Já `10.5`, `0.2` ou até mesmo `10.` (dez seguido de um ponto), são considerados números de ponto flutuante, *floating point* ou abreviadamente `float`.

Textos, que aparecem entre aspas quando no meio do código de um programa, como por exemplo `'hello'` ou `"Eric Idle"`, são do tipo *string* (cadeia de caracteres em português) que abreviamos como `str`. Repare que `"1010"` é um *string* enquanto `1010` é um número inteiro, `int`, e `1010.0` é `float`. 

Outro tipo importante que já encontramos é o booleano (*boolean*), com apenas os dois valores `True` ou `False` (verdadeiro ou falso), é o tipo dos valores resultantes das operações lógicas (como `and`,  `or` e `not`), comparações (como `==`, `!=`,  `>`, `<`, `>=` e etc.) ou ainda valores que indicam um estado (como `mousePressed` é verdadeiro ou falso dependendo do estado dos botões do mouse)

### valores, objetos, tipos e classes

Em linguagens de programação que trabalham com a ideia de *orientação a objetos*, e especialmente em Python, os valores são *objetos* e usamos o termo *classe* e *tipo* de maneira mais ou menos intercambiável. Um definição de uma classe estabelece as propriedades e comportamentos dos objetos de um certo tipo.

### Inspecionando os tipos dos valores

É comum dizer que em Python as variáveis não tem tipo (como em Java, por exemplo) mas sim os valores para os quais apontam. Podemos descobrir a classe/tipo de um objeto/valor usando a função embutida `type()`

```python
a = 1
print(type(a))
# resultado no console: <type 'int'>

a = "oi"
print(type(a))
# resultado no consol<type 'str'>
```

## Conversão, tipos dos argumentos e dos valores devolvidos for funções

Os valores que usamos entre parênteses em uma chamada de função (argumentos, dentro da função são chamados parâmetros) frequentemente precisar ser de tipos específicos. Por exemplo `range()` só aceita como argumentos números inteiros. A função `text()`, precisa de um *string* e dois números (para as coordenadas): `text("Texto", x, y)`. 

É necessário então converter os dados de um tipo para outro, como por exemplo o número 'sorteado' pela função `random()` que é um `float` pode ser convertido em `int`, sendo truncado (encurtado) perdendo a parte não inteira. Números podem ser convertidos em texto (`string`) usando `str(num)` ou com `'{}'.format(num)`.

```python
R = int(random(256))
println("Red: " + str(R))  # ou println("Red: {}".format(R))
```
### Como saber os tipos dos argumentos

Para descobrir quais são os tipos dos argumentos que devemos usar com uma determinada função, precisamos ler a documentação (no caso de funções embutidas, pré-definidas, ou de bibliotecas externas) ou então olhar a definição da função. 

### Tipos dos valores devolvidos por uma função

Da mesma forma, é do nosso interesse saber o tipo dos valores devolvidos por uma função. Isso também pode ser descoberto lendo a documentação, a definição da função, ou ainda usando `print(type(valor))`.

Algumas funções executam operações mas não devolvem nenhum valor, como `setup()`, `draw()`, `noStroke()` e `rect()`, por exemplo. Sendo mais precisos, em Python, essas funções devolvem o valor especial `None` (que poderíamos imaginar como "nada" ou "nenhum").

Mas muitas funções, devolvem um valor como resultado. Além da função `random()` que devolve um número *float* como acabamos de comentar, `color()`, por exemplo, devolve um número que representa uma cor, e podemos construir funções que devolvem valores para nós também:

```python
def cor_sorteada(alpha):
   r = int(random(256)
   g = int(random(256)
   b = int(random(256)
   return color(r, g, b, alpha)

minha_cor = cor_sorteada(255) # sorteia uma cor 
```

## Alguns tipos/classes de valores/objetos

Nesta tabela, alguns dos tipos que vamos encontrar programando com Processing modo Python, vou marcar com "Py" as que são naturais do Python, mesmo que existam equivalentes no Processing modo Java, e "P5" as que vem do Processing, e não existem no Python sozinho.

| tipo / classe | descrição | origem |
| ---      | --- | --- |
| `int`     | número inteiro, como `-5`, `0` ou `42`| Py |
| `float`  | número com ponto flutante, como `.5` `3.` ou `6.267` (note que o separador decimal é o ponto)| Py |
| `boolean`| valores `True` ou `False`| Py |
| `PImage` | imagens raster/bitmap, podem ser criadas/carregadas na memória com `loadImage(arquivo_de_imagem)` | P5 |
| `PShape` | contém formas vetorais, como as descritas num SVG, pode ser criado com `loadShape(arquivo)`| P5 |
| `PVector`| vetor, usado geralmente para descrever posição, velocidade ou aceleração (em 2 ou 3 dimensões) | P5 |
| `string` | cadeia de caracteres, são sequencias de caracteres ou glifos, no código são criados com aspas: `“texto”` | Py |
| `list`   | lista, coleção ordenada de itens, construída com `list(itens)` ou com colchetes no código `[ ,]` | Py |
| `tuple`  | coleção ordenada e imutável de itens, construída com `tuple(itens)` ou com parenteses no código `( ,)` | Py |
| `set`    | conjunto não ordenado de itens 'hasheáveis', com `set(itens)` ou com chaves no código `{ ,}` | Py |
| `dict`   | dicionário um 'mapeamento' de chaves (*keys*) e valores, criado com `dict()` ou pares `{chave : valor,}` | Py |
| `None`   | o "nenhum" é de um tipo especial único `None`e é devolvido por funções que não devolvem nada  | Py |
| `color`<sup>＊</sup>| uma cor é um `int` disfarçado, que pode ser construídao com `color(R,G,B)` ou `color(R,G,B,Alfa)`| P5 |

> ＊ Preciso contar que a as cores não são um tipo 'de verdade', independente, são um jeito do Processing deixar as coisas mais elegantes pra nós, tem um termo em programação pra isso: 'açucar sintático' (*syntatic sugar*). Por baixo do capô as cores do Processing são apenas números inteiros grandes, com 4 býtes, para R, G, B e A (tansparência) respectivamente, a função `color()` monta esse número grande pra nós. É útil (mais fácil) pensar em cores como um tipo especial de valores, no Processing modo Java você declara o tipo `color` para variáveis e funções e parâmetros que vão trabalhar com cores.

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

