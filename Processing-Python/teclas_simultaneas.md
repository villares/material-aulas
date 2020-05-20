## Escutando teclas simultâneas

A questão de identificar teclas apertadas simultaneamente pode surgir quando estamos desenvolvendo um *sketch* interativo, e em especial se estamos criando um jogo, em que mais pessoas interagem simultaneamente usando o teclado, também sempre que a interface fica mais complexa e precisa de teclas em combinação. 

 Executando o código a seguir você vai notar que a variável `key` aponta para um valor que descreve a última tecla que foi pressionada (ou solta) no teclado.

Isso pode ser um problema se você precisar mostrar quando **a** e **b** estiverem apertadas simultaneamente.

 Não deixe de executar e experimentar você!

```python
def setup():
    size(256,256)
    textAlign(CENTER, CENTER)
    textSize(20)
    strokeWeight(3)
        
def draw():
    background(200, 200, 0)
    
    if key == 'a':
        fill(200, 0, 0) 
        rect(64, 96, 64, 64)
        fill(255)
        text('a', 96, 128)
        
    if key == 'b':
        fill(0, 0, 200) 
        rect(128, 96, 64, 64)
        fill(255)
        text('b', 160, 128)
        
```

![](assets/teclas_simultaneas_0.gif)

Uma modificação pode evitar que uma tecla seja 'indicada' no momento em que é solta e também que fique aparecendo quando já não está mais sendo apertada, mas isso ainda não resolve o problema das teclas simultâneas: 

```python
    if keyPressed and key == 'a':
        fill(200, 0, 0) 
        rect(64, 96, 64, 64)
        fill(255)
        text('a', 96, 128)
        
    if keyPressed and key == 'b':
        fill(0, 0, 200) 
        rect(128, 96, 64, 64)
        fill(255)
        text('b', 160, 128)
```

A verdadeira solução para esta questão é criar uma estrutura que  guarde o estado das teclas, e indique se a tecla está apertada naquele momento, sendo modificada pelos eventos de apertar ou soltar uma tecla.

Num primeiro momento, para este nosso exemplo, essa estrutura pode ser simplesmente um par de variáveis globais, usadas como indicadores (*flags*) do estado das teclas. 

```python

a_apertada = False
b_apertada = False

def setup():
    size(256,256)
    textAlign(CENTER, CENTER)
    textSize(20)
    strokeWeight(3)
        
def draw():
    background(0, 200, 200)
    
    if a_apertada:
        fill(200, 0, 0) 
        rect(64, 96, 64, 64)
        fill(255)
        text('a', 96, 128)
        
    if b_apertada:
        fill(0, 0, 200) 
        rect(128, 96, 64, 64)
        fill(255)
        text('b', 160, 128)
        
def keyPressed():
    global a_apertada, b_apertada
    if key == 'a':
        a_apertada = True
    if key == 'b':
        b_apertada = True        

def keyReleased():
    global a_apertada, b_apertada
    if key == 'a':
        a_apertada = False
    if key == 'b':
        b_apertada = False        
```

![](assets/teclas_simultaneas_1.gif)

Nas versões finais com teclado do [jogo PONG neste repositóro](../pong), usamos exatamente essa estratégia, de outra forma, e experiência de jogo ficaria muito prejudicada.

Por fim, gostaria de relembrar que algumas teclas são identificadas de maneira ligeiramente diferente, as ditas teclas *codificadas*. Quando `key == CODED` você precisa usar a variável `keyCode` para saber qual tecla foi apertada (ou solta), em geral comparando com uma constante numérica destas:

`UP DOWN LEFT RIGHT ALT CONTROL SHIFT`

E temos também teclas que não são codificadas, são identificáveis em `key`, mas precisam ser identificadas por constantes ou *strings* especiais:

```
BACKSPACE '\b'
TAB       '\t'
ENTER     '\n'
RETURN    '\r'
ESC       '\x1b'
DELETE    '\x7f'
```

### Um desafio um pouco maior

Mas e se o número de teclas for muito grande? Temos que fazer um montão de condicionais com `if` dentro do `keyPressed()` e do `keyReleased`?

Vamos explorar uma estratégia de guardar as teclas que foram apertadas em uma estrutura de dados chamada **conjunto** (*set*), removendo-as do conjunto quando forem soltas.

É bom notar que conjuntos não guardam a ordem em que seus itens foram adicionados, e os itens são únicos, um conjunto nunca tem itens duplicados. 

Em Python, podemos saber se um item existe dentro de uma coleção (como listas, tuplas, deques e conjuntos) com a palavra chave `in` usada como um operador, e isso é computacionalmente muito mais eficiente em um conjunto grande do que em uma lista ou tupla grande!

No exemplo abaixo, se `'b' in teclas_apertadas` for verdade, o fundo fica preto.

```python
teclas_apertadas = set()  # conjunto (set) vazio

def setup():
    size(512,256)
    textAlign(CENTER, CENTER)
    textSize(20)
    strokeWeight(3)
        
def draw():
    if 'b' in teclas_apertadas:
        background(0)
    else:
        background(100, 0, 200)
    
    for i, k in enumerate(teclas_apertadas):
        x = i * 64
        fill(0, x, 255 - i * 32) 
        rect(x, 96, 64, 64)
        fill(255)
        text(str(k), x + 32, 128)
    
def keyPressed():
    teclas_apertadas.add(key)    
    
def keyReleased():
    teclas_apertadas.discard(key)
```

![](assets/teclas_simultaneas_2.gif)

Você viu um `65535` no meio das teclas?

Significa que uma tecla *codificada* (`CODED`) foi pressionada, como `SHIFT`, por exemplo. 

`TAB`, `ENTER` e algumas outras teclas *não codificadas* não são mostradas direito também.

Vamos fazer alguns ajustes no código para identificar e mostrar de maneira mais elegante essas teclas!

Para isso vamos usar outra estrutura de dados chamada **dicionário** (*dict*).