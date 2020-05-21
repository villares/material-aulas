## Escutando teclas simultâneas

A questão de identificar teclas apertadas simultaneamente pode surgir quando estamos desenvolvendo um *sketch* interativo, e em especial se estamos criando um jogo, em que mais pessoas interagem simultaneamente usando o teclado, também sempre que a interface fica mais complexa e precisa de teclas em combinação. 

Executando o código a seguir você vai notar que a variável `key` aponta para um valor que descreve a última tecla que foi pressionada (ou solta) no teclado. Isso pode ser um problema se você precisar mostrar quando **a** e **b** estiverem apertadas simultaneamente.

 Não deixe de executar e experimentar!

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

Uma modificação pode evitar que uma tecla seja indicada no momento em que é solta e também que fique aparecendo quando já não está mais sendo apertada, mas isso ainda não resolve o problema das teclas simultâneas: 

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

A solução para esta questão é criar uma estrutura que  guarde o estado das teclas, e indique se a tecla está apertada naquele momento, sendo modificada pelos eventos de apertar ou soltar uma tecla. Em um primeiro momento, para este nosso exemplo, a estrutura pode ser simplesmente um par de variáveis globais, usadas como indicadores (*flags*) do estado das teclas, `a_apertada` e `b_apertada`. 

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

#### Notas

- Se você soltar uma tecla quando o *foco* do seu sistema operacional não estiver na janela do *sketch* o evento `keyReleased()` não será acionado, e o *sketch* não fica sabendo que a tecla foi solta!

- Nas versões finais com teclado do [jogo PONG neste repositóro](../pong), usamos exatamente essa estratégia, sem isso a experiência de jogo fica muito prejudicada.

É interessante lembrar que algumas teclas são identificadas de maneira ligeiramente diferente, as ditas teclas *codificadas*. Quando `key == CODED` você precisa usar a variável `keyCode` para saber qual tecla foi apertada (ou solta), em geral comparando com uma constante numérica destas aqui:

`UP DOWN LEFT RIGHT ALT CONTROL SHIFT`

Temos também teclas que não são codificadas, são identificáveis em `key` mesmo, mas precisam ser identificadas por constantes ou *strings* especiais:

```
BACKSPACE '\b'
TAB       '\t'
ENTER     '\n'
RETURN    '\r'
ESC       '\x1b'
DELETE    '\x7f'
```

### Um desafio um pouco maior

Mas como fazer  se o número de teclas que queremos identificar for muito grande? Temos que fazer um monte variáveis globais e um monte de condicionais com `if` dentro do `keyPressed()` e do `keyReleased`? Isso não parece muito elegante!

Vamos então explorar uma estratégia de guardar as teclas que foram apertadas em uma estrutura de dados chamada **conjunto** (*set*), removendo-as do conjunto quando forem soltas. É bom notar que conjuntos não guardam a ordem em que seus itens foram adicionados, e os itens são únicos, um conjunto nunca tem itens duplicados. 

Para acrescentar um item em um conjunto usamos `conjunto.add(item)`, e para remover `conjunto.discard(item)`. Essa última operação, *discard*, não faz nada se o item não existir no conjunto.

Em Python, podemos saber se um item existe dentro de uma coleção (como listas, tuplas, deques e conjuntos) com a palavra chave `in` usada como um operador, e isso é computacionalmente muito mais eficiente em um conjunto grande do que em uma lista ou tupla grande! No exemplo abaixo, se `'b' in teclas_apertadas` for verdade, o fundo fica preto.

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

Significa que uma tecla *codificada* (`CODED`) foi pressionada, como `SHIFT`, por exemplo. `TAB`, `ENTER` e algumas outras teclas *não codificadas* também não são mostradas direito.

Vamos fazer alguns ajustes no código para identificar e mostrar de maneira mais elegante essas teclas!

Para isso vamos usar outra estrutura de dados chamada **dicionário** (*dict*). Que mapeias chaves (*keys*) e valores (*values*). É muito rápido consultar um valor atrelado a uma chave em um dicionário. 

Se você sabe que a chave existe no dicionário, pode consultar com a forma `dicionario[chave]` (que dá erro se a chave não existir no dicionário). Quando não se tem certeza se a chave está lá, ou é parte da  estratégia  procurar chaves que podem não estar lá, então se usa `dicionario.get(chave, valor_se_nao_tem_a_chave)`.

```python
from __future__ import unicode_literals

teclas_apertadas = set()  # conjunto (set) vazio
# dicionário {tecla: 'nome para mostrar'}
nomes = {UP: '↑',
         DOWN: '↓',
         LEFT: '←',
         RIGHT: '→',
         ALT: 'Alt',
         CONTROL: 'Ctrl',
         SHIFT: 'Shift',
         BACKSPACE: 'Bcksp',
         TAB: 'Tab',
         ENTER: 'Enter',
         RETURN: 'Return',
         ESC: 'Esc',
         DELETE: 'Del',
         524: 'Meta',
         525: 'Menu',
         65406: 'AltGr',
         155: 'Insert',
         36: 'Home',
         35: 'End',
         33: 'PgUp',
         34: 'PgDwn',
         144: 'NumLk',
         ' ': 'espaço',
         }

def setup():
    size(512, 256)
    textAlign(CENTER, CENTER)
    textSize(15)
    strokeWeight(3)

def draw():
    # em vez de 'b' agora o espaço deixa o fundo preto
    if ' ' in teclas_apertadas:
        background(0)
    else:
        background(50, 200, 50)
    
    for i, tecla in enumerate(sorted(teclas_apertadas)):
        # tendo `tecla` no dicionário pega o 'nome para mostrar'
        n = nomes.get(tecla, tecla)  # se não tiver, devolve `tecla` mesmo!   
        x = i * 64
        fill(0, x / 2, 200)
        rect(x, 96, 64, 64)
        fill(255)
        text(n, x + 32, 128)

def keyPressed():
    if key != CODED:
        teclas_apertadas.add(key)
    else:
        teclas_apertadas.add(keyCode)

    # Impeça que o sketch seja encerrado com ESC!
    if key == ESC:
        this.key = ' '

def keyReleased():
    if key != CODED:
        teclas_apertadas.discard(key)
    else:
        teclas_apertadas.discard(keyCode)
```
![](assets/teclas_simultaneas_3.gif)

#### Notas

* Uma vez que certas teclas modificam o efeito de outras, por exemplo, `SHIFT` faz a tecla `1`  aparecer como `!`, então certas sequências podem trazer resultados estranhos:

  Apertar`SHIFT`, depois `1 `, soltar `SHIFT`e por fim soltar `1`. faz o sketch ficar sem ver a tecla `!` ser 'solta'. 
  Uma solução possível é manter registro só do `keyCode` das teclas que permanece sempre o mesmo, o convertendo em algo mais legível com `chr()`:

  ```python
  def keyPressed():
      if key != CODED:
          teclas_apertadas.add(chr(keyCode))
      else:
          teclas_apertadas.add(keyCode)

  def keyReleased():
      if key != CODED:
          teclas_apertadas.discard(chr(keyCode))
      else:
          teclas_apertadas.discard(keyCode) 
  ```
  Mas fique atento e teste para evitar surpresas! No meu computador o `keyCode` do `+` e `-` do teclado numérico lateral, por exemplo, aparecem como `k` e `m`.
- Foi usada `sorted()` para obter uma lista ordenada a partir do conjunto `teclas_apertadas`
- Dentro do `keyPressed()` tem um pequeno truque que impede o *sketch*  de ser interrompido pela tecla `ESC`.
- No dicionário acrescentei alguns códigos que vi, estando no Linux, os códigos e nomes das teclas podem variar dependendo do seu sistema operacional.