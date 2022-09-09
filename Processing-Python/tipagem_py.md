
# Valores e seus tipos

Em computação existe uma classificação dos valores armazenados na memória do computador, dizemos que os valores tem um *tipo*.  Diferentes linguagens de programação tratam de como indicamos os tipos, ou de como reconhecemos e manipulamos valores de diferentes tipos, de maneiras diferentes.

Em Python, quando fazemos uma atribuição, criando ou alterando uma variável, por exemplo `i = 10`, o `i` é um nome que aponta para um valor na memória, `10`, um número **inteiro**, do tipo *integer* que é normalmente abreviado como `int`. 

Já `10.5`, `0.2` que tem uma parte fracionária, ou até mesmo `10.` (dez seguido de um ponto), são considerados **números de ponto flutuante**, *floating point* ou abreviadamente `float`. Valores numéricos em Python são, na maior parte das vezes, dos tipos ***inteiro***  ou  ***ponto flutuante***. Mas há também tipos como ***número complexo*** ([mais detalhes na documentação do Python](https://docs.python.org/pt-br/3/library/stdtypes.html#numeric-types-int-float-complex)), entre outros.

Textos, que aparecem entre aspas quando no meio do código de um programa, como por exemplo `'hello'` ou `"Eric Idle"`, são do tipo ***string*** (cadeia de caracteres em português) que abreviamos como `str`. Repare que `"1010"` é um *string* enquanto `1010` é um número inteiro, `int`, e `1010.0` é `float`. 

Outro tipo importante que já encontramos é o **booleano** (*boolean*), com apenas os dois valores `True` ou `False` (verdadeiro ou falso), é o tipo dos valores resultantes das operações lógicas (como `and`,  `or` e `not`), comparações (como `==`, `!=`,  `>`, `<`, `>=` e etc.) ou ainda valores que indicam um estado (como `mousePressed` é verdadeiro ou falso dependendo do estado dos botões do mouse)

### Objetos, tipos e classes

Em linguagens de programação que trabalham com a ideia de *orientação a objetos*, e especialmente em Python, os valores são *objetos* e usamos o termo *classe* e *tipo* de maneira mais ou menos intercambiável. A definição de uma classe estabelece as propriedades e comportamentos dos objetos de um certo tipo.

### Inspecionando os tipos dos valores

É comum dizer que em Python as variáveis não tem tipo (como em Java, por exemplo) mas sim os valores para os quais apontam. Podemos descobrir a classe/tipo de um objeto/valor usando a função embutida `type()`

```python
a = 1
print(type(a))
# resultado no console: <class 'int'>

a = "oi"
print(type(a))
# resultado no console <class 'str'>
```

## Conversão, tipos dos argumentos e dos valores devolvidos for funções

Os valores que usamos entre parênteses em uma chamada de função (argumentos, dentro da função são chamados parâmetros) frequentemente precisar ser de tipos específicos. Por exemplo `range()` só aceita como argumentos números inteiros. A função `text()`, precisa de um *string* e dois números (para as coordenadas): `text("Texto", x, y)`. 

É necessário então converter os dados de um tipo para outro, como por exemplo o número 'sorteado' pela função `random()` que é um `float` pode ser convertido em `int`, sendo truncado (encurtado) perdendo a parte não inteira. Números podem ser convertidos em texto (*string*) usando `str(num)` ou com `f'{num}'` (o `f` antes das aspas indica um *f-string*, que vai interpretar os valores entre chaves dentro).

```python
r = int(random(256))
print("Red: " + str(r))  # ou print(f"Red: {r}")
```
### Como saber os tipos dos argumentos

Para descobrir quais são os tipos dos argumentos que devemos usar com uma determinada função, precisamos ler a documentação (no caso de funções embutidas, pré-definidas, ou de bibliotecas externas) ou então olhar a definição da função. 

### Tipos dos valores devolvidos

Da mesma forma, é do nosso interesse saber o tipo dos valores devolvidos por uma função. Isso também pode ser descoberto lendo a documentação, a definição da função, ou ainda usando `print(type(valor))`.

Algumas funções executam operações mas não devolvem nenhum valor, como `setup()`, `draw()`, `noStroke()` e `rect()`, por exemplo. Sendo mais precisos, em Python, essas funções devolvem o valor especial [`None`](None.md) (que poderíamos imaginar como "nada" ou "nenhum").

Mas muitas funções devolvem algum valor como resultado. Além da função `random()` que devolve um número *float* como acabamos de comentar, `color()`, por exemplo, devolve um número que representa uma cor, e podemos nós também construir funções que devolvem valores:

```python
def cor_sorteada(alpha):
   r = int(random(256)
   g = int(random(256)
   b = int(random(256)
   return color(r, g, b, alpha)

minha_cor = cor_sorteada(255) # sorteia uma cor 
```

## Alguns tipos/classes de valores/objetos

Nesta tabela apresento apenas alguns dos tipos que vamos encontrar programando com Processing modo Python, vou marcar com *Py* os que são naturais do Python, mesmo que existam equivalentes no Processing modo Java, e *Py5* os que vem do Processing, e não existem no Python sozinho.

| tipo / classe | descrição | origem |
| ---      | --- | --- |
| `int`     | número inteiro, como `-5`, `0` ou `42`| Py |
| `float`  | número de ponto flutante, como `.5` `3.` ou `6.267` (note que o separador decimal é o ponto)| Py |
| `bool`| booleano é o tipo dos valores `True` ou `False`| Py |
| `string` | cadeia de caracteres, são sequencias de glifos, podem ser criados com aspas: `“texto”` ou `'maçã'` | Py |
| `list`   | lista, coleção ordenada de itens, construída com `list(itens)` ou com colchetes no código `[ ,]` | Py |
| `tuple`  | coleção ordenada e imutável de itens, construída com `tuple(itens)` ou com parenteses no código `( ,)` | Py |
| `set`    | conjunto não ordenado de itens 'hasheáveis', com `set(itens)` ou com chaves no código `{ ,}` | Py |
| `dict`   | dicionário um 'mapeamento' de chaves (*keys*) e valores, criado com `dict()` ou pares `{chave : valor,}` | Py |
| `None`   | o "nenhum" é de um tipo especial único `None`e é devolvido por funções que não devolvem nada  | Py |
| `PImage` | imagens raster/bitmap, podem ser criadas/carregadas na memória com `loadImage(arquivo_de_imagem)` | Py5 |
| `PShape` | contém formas vetorais, como as descritas num SVG, pode ser criado com `loadShape(arquivo)`| Py5 |
| `PVector`| vetor, usado geralmente para descrever posição, velocidade ou aceleração (em 2 ou 3 dimensões) | Py5 |
| `color`<sup>＊</sup>| uma cor é um `int` disfarçado, que pode ser construídao com `color(R,G,B)` ou `color(R,G,B,Alfa)`| Py5 |

> ＊ Preciso contar que a as cores não são um tipo 'de verdade', independente, são um jeito do Processing deixar as coisas mais elegantes pra nós, tem um termo em programação pra isso: 'açucar sintático' (*syntatic sugar*). Por baixo do capô as cores do Processing são apenas números inteiros grandes, com 4 bytes, para R, G, B e Alpha (opacidade) respectivamente, a função `color()` monta esse número grande pra nós. É útil (mais fácil) pensar em cores como um tipo especial de valores.

Existe uma discussão relativamente complexa mas na qual eu não vou entrar aqui, o tipo `bytes` do Processing lembra um *string* mas só com caracteres *ASCII*, e isso dá uma certa confusão os *strings*, pois não são texto *Unicode*, mas essa é uma questão avançada que eu queria evitar neste primeiro momento.


### Glossário

[**valor**](https://penseallen.github.io/PensePython2e/01-jornada.html#termo:valor) Uma das unidades básicas de dados, como um número ou *string*, que um programa manipula.

[**tipo**](https://penseallen.github.io/PensePython2e/01-jornada.html#termo:tipo) Uma categoria de valores. Alguns tipos que vimos por enquanto são números inteiros (tipo `int`), números de ponto flutuante (tipo `float`) e *strings* (tipo `str`).

[**inteiro**](https://penseallen.github.io/PensePython2e/01-jornada.html#termo:inteiro) Um tipo que representa números inteiros.

[**ponto flutuante**](https://penseallen.github.io/PensePython2e/01-jornada.html#termo:ponto%20flutuante) Um tipo que representa números com partes fracionárias.

[**string**](https://penseallen.github.io/PensePython2e/01-jornada.html#termo:string) Um tipo que representa sequências de caracteres.

---
Este material é baseado no mateMrial do curso https://arteprog.space/programacao-criativa/

---
Texto e imagens / text and images: CC BY-NC-SA 4.0; Código / code: GNU GPL v3.0 exceto onde explicitamente indicado por questões de compatibilidade.

