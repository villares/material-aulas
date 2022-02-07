# Dicas para portar código de Processing modo Java para modo Python

> …e possivelmente vice-versa: )

![](assets/java_python.png)

# Considerações gerais

- como você provavelmente sabe, em python o que conta para saber se uma linha de código está 'dentro' de uma função ou de outra estrutura qualquer, como um `if`, é a indentação. no java são as chaves `{}` que mandam, mas é comum a indentação refletir a hierarquia, mesmo isso não sendo obrigatório. por isso, use a ferramenta de auto-formatação do IDE antes de começar e avance com cuidado!
- as chaves precisam ser removidas, e você deve trocar cada `{` por `: ` no começo de um bloco de instruções(isso só não vale para as definições de * arrays*, que tem chaves mas não definem um bloco de instruções, e viram uma lista ou uma tupla com `[]` ou` ()`).
- remova os `; ` no final das linhas.
- comentários com `//` no java viram comentários com `  # `. Comentários de várias linhas com `/* … */ ` podem virar *docstrings*, com aspas triplas no Python, `""" … """`.
- java é uma linguagem de * tipagem estática * e python é uma linguagem de * tipagem dinâmica * isso significa que vamos remover todas as declarações de tipo. remova `int `, `float`, `string`, `color`, `boolean`  das declarações de variáveis. por exemplo,  `int i = 0; ` se torna `i = 0`.
- podemos também remover `void` ou  tipo na declaração de uma função e colocar no lugar o `def` do python.  depois remover a declaração de tipo dos parâmetros da função.

   **java**

  ```java
  float media(float a, float b){
    return (a + b) / 2;
  }
  ```
  **python**
  
  ```python
  def media(a, b):
      return (a + b) / 2
  ```

# Um quadro com equivalências para conversão

os valores booleanos em java são `true` e `false`, o que em python fica `True` e `False`.  vamos fazer um quadro com os operadores lógicos e algumas outras equivalências. 

| java                                             | python                                     |
| ------------------------------------------------ | ------------------------------------------ |
| `void func() { … }`                              | `def func(): …`                            |
| **`true`** e **`false`**                         | **`True`** e **`False`**                   |
|  <code>a <b>&&</b> b</code> (E lógico)           | `a `**`and`**` b`                          |
| <code>a <b>&#x7C;&#x7C;</b> b</code> (OU lógico) | `a `**`or`**` b`                           |
| **`!`**`a` (NãO lógico)                          | **`not`**` a`                              |
| `i++` (incremento)                               | `i += 1`                                   |
| `i--`(decremento)                                | `i -= 1`                                   |
| `a <= b && b < c`                                | `a <= b < c`                               |
| `for (int i=0; i < limite; i++){ … `             | `for i in range(limite): …`                |
| `for (int i=inicio; i < limite; i += passo){ … ` | `for i in range(inicio, limite, passo): …` |
| `for (bola b : array_list_bolas){ …`               | `for b in lista_bolas: …`                   |
| `for (bola b : array_list_bolas){ …`               | `for b in lista_bolas: …`                   |
| `fill(#FFCC00) // cor em notação hexadecimal  `  | `fill("#FFCC00") # precisa aspas e não funciona com `color()` |

E semelhante a `null` de java temos o valor `None` em python os usos não são totalmente equivalentes mas é um bom palpite fazer a substituição.

# Loops `for`

O caso mais simples é um `for` baseado em um contador qualquer, como `for (int i=0; i < limite; i++){ … `  e a tradução é `for i in range(limite): …`

O chamado *for each*, mostrado no quadro, também é muito direto, mas se você encontrar um loop `for` no java com um passo não inteiro (*float*), como a construção baseada em `range()` no  python só funciona com números inteiros, você vai ter que implementar um range 'especia', como mostrado abaixo com `frange()` ou então convertê-lo em um loop `while`:

**java**

```java
float passo = TWO_PI / 18
for (float angulo=0; angulo < TWO_PI; angulo += passo){ 
    …
}
```

**python**

```python
passo = TWO_PI / 18
angulo = 0
while angulo < TWO_PI:
    …
    angulo += passo
```

# Implementando um range com passos não inteiros:

```python
def frange(start, stop, step):
    from itertools import count, takewhile
    return takewhile(lambda x: x < stop, count(start, step))

# em uso no exemplo...
passo = TWO_PI / 18
for angulo in frange(0, TWO_PI, passo):
    …    

```

aqui um exemplo de laço é feito apenas para pegar objetos de uma estrutura de dados:


```java
for (int i = 0;  i < meu_array.length; i++) {
  fazendo_algo(i, meu_array[i]);
}
```

**python**

```python
for item in minha_lista:
    fazendo_algo(item)
```
ou

```python
for i, item in enumerate(minha_lista):
    fazendo_algo(i, item)
```

veja uma iteração invertida para remover itens de um *array_list* no java, uma lista no python:

**java**

```java
for (int i = particles.size()-1; i >= 0; i--) {
  particle p = particles.get(i);
  p.run();
  if (p.is_dead()) {
    particles.remove(i);
  }
}
```

**python**

```python
for p in reversed(particles):
    p.run()
    if p.is_dead():
        del p
```

ou, se você precisar o índice:

```python
for i in reversed(range(len(particles))):
    p = particles[i]
    p.run()
    if p.is_dead():
        del particles[i]
```

ou ainda:

```python
for i, p in reversed(list(enumerate(self.particles))):
    p.run()
    if p.is_dead():
        del p # ou del self.particles[i]
```



# `if`, `else` e seus amigos

note que a condição do `if` no python não tem os parênteses obrigatórios no java. A combinação de um `else if` vira a contração `elif`.

**java**

```java
for (int i = 2; i < width-2; i += 2) {
  if ((i % 20) == 0) {
    stroke(255);
    line(i, 80, i, height/2);
  } else if ((i % 10) == 0) {
    stroke(153);
    line(i, 20, i, 180); 
  } else {  
    stroke(102);
    line(i, height/2, i, height-20);
  }
}
```
**python**

```python
for i in range(2, width - 2, 2):
    # If 'i' divides by 20 with no remainder
    if i % 20 == 0:
        stroke(255)
        line(i, 80, i, height / 2)
    elif i % 10 == 0:
        stroke(153)
        line(i, 20, i, 180)
    else:
        stroke(102)
        line(i, height / 2, i, height - 20)
```

# Operador ternário

**java**

```java
resultado = cond ? a : b 
```
**python**

```python
 resultado = a if cond else  b 
```

# switch & case

Não existe `switch/case` no python, você pode trocar por uma cadeia de `if/elif` ou, se for só para chamar diferentes funções, um dicionário de funções [TO DO página sobre isso].
**java**
```java
char letter = 'b';

switch(letter) {
  case 'a':
  case 'A': 
    print("Alpha");  // does not execute in this example
    break;
  case 'b':
  case 'B': 
    print("Bravo");  // prints "Bravo"
    break;
  default:            // default is optional
    print("Not found");  
    break;
}
```

**python**
```python
letter = 'b'

if letter == 'a' or letter == 'A':
    print("Alpha")  # Does not execute in this example
elif letter in ('b', 'B'):
    print("Bravo")  # Prints "Bravo"
else:
    print("Not found")  
```

# Variáveis globais

se a variável for *declarada e inicializada* (definido o tipo e o valor) no começo do *sketch* basta remover a declaração de tipo.

mas como não há em python a declaração de uma variável sem fazer uma atribuição, quando a variável é só declarada (é indicado um tipo sem a *inicialização*, isto é ter sua primeira atribuição) no começo do *sketch* precisamos ver onde ela é calculada a primeira vez e acrescentar, no início da função, a instrução `global nome_da variável`. 

na verdade, toda função que altera a atribuição de variáveis globais em seu corpo precisa da instrução `global` com os nomes das variáveis que são modificadas. 

veja um exemplo:

**java**
```java
int rad = 60;        // width of the shape
float xpos, ypos;    // starting position of shape    
float xspeed = 2.8;  // speed of the shape
float yspeed = 2.2;  // speed of the shape
int xdirection = 1;  // left or right
int ydirection = 1;  // top to bottom

void setup() 
{
  size(600, 300);
  // set the starting position of the shape
  xpos = width/2;
  ypos = height/2;
}

void draw() 
{
  background(102);
  xpos = xpos + ( xspeed * xdirection );
  ypos = ypos + ( yspeed * ydirection );
    
  if (xpos > width-rad || xpos < rad) {
    xdirection *= -1;
  }
  if (ypos > height-rad || ypos < rad) {
    ydirection *= -1;
  }

  ellipse(xpos, ypos, rad * 2, rad * 2);
}
```
**python**

```python

rad = 60;        # Width of the shape
# No original tinha: float xpos, ypos; // Starting position of shape    
xspeed = 2.8;    # Speed of the shape
yspeed = 2.2;    # Speed of the shape
xdirection = 1;  # Left or Right
ydirection = 1;  # Top to Bottom

def setup():**python**
    size(600, 300)
    global xpos, ypos  #  xpos, ypos são globais criadas no setup
    no_stroke()
    xpos = width / 2
    ypos = height / 2

def draw():
    global xpos, ypos, xdirection, ydirection  # vão ser alteradas!
    background(102)   
    xpos += xspeed * xdirection
    ypos += yspeed * ydirection
    
    if xpos < rad or width - rad < xpos:  # note que rad não é alterada
        xdirection *= -1
    if ypos < rad or height - rad < ypos:
        ydirection *= -1
    ellipse(xpos, ypos, rad * 2, rad * 2)
```

# Strings


se o código contiver strings com caracteres *não-ASCII* (como letras acentuadas ou emojis) pode ser uma boa ideia iniciar o *sketch* com a seguinte linha:

```python
from __future__ import unicode_literals
```

de outra forma você terá que preceder cada string com `u` da seguinte maneira:  `u"maçã"`.

**tipo *char* em java**

java tem uma tipo especial para caracteres, *char* que são representados no código com aspas simples, python não tem essa distinção, usa-se *strings* de um só caractere, e aspas simples ou duplas para *strings*. 

para obter um caractere em determinada posição de *string* em java é preciso fazer isto:
 
```java
string palavra = "amor";
char c = palavra.char_at(1); // c = 'm'
```
O equivalente em python, continua sendo *string*:

```python
palavra = 'amor'
c = palavra[1] # c = 'm'
```

**comparando *strings* em java**

```java
string str1 = "amor";
string str2 = "amor";
// testa se str1 é igual a str2
if (str1.equals(str2)) {
  print("iguais"); } else {
  print("diferentes"); 
}
```
**comparando *strings* em python**

```python
str1 = "amor"
str2 = "amor"
# Testa se str1 é igual a str2
if str1 == str2:
  print("iguais")
else:
  print("diferentes")
```


# Importando bibliotecas e as outras abas do sketch

no processing modo java as bibliotecas são importadas com `import` mas no modo python essa instrução é mais usada para importar *módulos* da biblioteca padrão do python, e arquivos **.py** das outras abas do IDE, que ao contrário do modo java não são automaticamente parte do *sketch*.

para bibliotecas de terceiros, use o comando do menu **sketch > importar biblioteca...** (ou *sketch > import library...* em inglês) para acrescentar a linha com  `add_library()` e o argumento correto.

**java**

```java
import com.hamoid.*; // importa biblioteca video_export no modo java
```

**python**

```python
add_library('VideoExport')  # a mesma biblioteca no modo Python
```

para usar múltiplas abas no modo python, é preciso tratá-las como módulos e trazer classes ou funções com `import`. Há mais de uma maneira de fazer isso.

```python
from outra_aba import *  # importa código do arquivo outra_aba.py
```

se as outras abas contiverem caracteres *não-ASCII*  é necessário acrescentar como primeira linha este comentário especial:

```python
# -*- coding: utf-8 -*-
```

# Orientação a objetos

# Obtendo uma instância e acessando métodos e atributos

java precisa da palavra chave **`new`** para criar uma instância de uma classe, é só removê-la! O acesso a métodos e atributos é exatamente igual.

**java**

```java
video_export video_export;

void setup() {
  size(600, 600);
  video_export = new video_export(this);
  video_export.start_movie();
}
```

**python**

```python
def  setup() :
    global video_export
    size(600, 600)
    video_export = video_export(this)
    video_export.start_movie()
```

# Declarando uma classe

Já as declarações de classe mudam um pouco, grosso modo, o método `__init__()` faz o papel do *construtor* (a definição de método que em java tem o mesmo nome da classe e faz a inicialização de uma instância do objeto).

você vai ter o trabalho de acrescentar `self` como primeiro parâmetro de todos os métodos, e vai ter que usar `self.` para acessar atributos e membros da classe.

veja a classe `m_rect` do exemplo **basics > objects > objects** que vem no IDE do processing.

**java**

```java
class m_rect 
{
  int w; // single bar width
  float xpos; // rect xposition
  float h; // rect height
  float ypos ; // rect yposition
  float d; // single bar distance
  float t; // number of bars
 
  m_rect(int iw, float ixp, float ih, float iyp, float id, float it) {
    w = iw;
    xpos = ixp;
    h = ih;
    ypos = iyp;
    d = id;
    t = it;
  }
 
  void move (float pos_x, float pos_y, float damping) {
    float dif = ypos - pos_y;
    if (abs(dif) > 1) {
      ypos -= dif/damping;
    }
    dif = xpos - pos_x;
    if (abs(dif) > 1) {
      xpos -= dif/damping;
    }
  }
 
  void display() {
    for (int i=0; i<t; i++) {
      rect(xpos+(i*(d+w)), ypos, w, height*h);
    }
  }
}
```

**python**

```python
class m_rect:

    def __init__(self, iw, ixp, ih, iyp, id, it):
        self.w = iw  # single bar width
        self.xpos = ixp  # rect xposition
        self.h = ih  # rect height
        self.ypos = iyp  # rect yposition
        self.d = id  # single bar distance
        self.t = it  # number of bars

    def move(self, pos_x, pos_y, damping):
        self.dif = self.ypos - pos_y
        if abs(self.dif) > 1:
            self.ypos -= self.dif / damping

        self.dif = self.xpos - pos_x
        if abs(self.dif) > 1:
            self.xpos -= self.dif / damping

    def display(self):
        for i in range(self.t):
            rect(self.xpos + (i * (self.d + self.w)),
                 self.ypos, self.w, height * self.h)
```

# Estruturas de dados

arrays como `int[]`, `float[]` ou `p_vector[]` podem virar listas em python (ou quem sabe tuplas, se forem criadas e deixadas quietas). um *array_list* é muito parecido com uma lista:

**java**
```java
array_list<bandeirinha> bandeirinhas; // uma lista de objetos da classe bandeirinha

void setup() {
  size(400, 400); 
  bandeirinhas = new array_list<bandeirinha>();
  for (int i=0; i <50; i++) {
    bandeirinhas.add(new bandeirinha(100, 100, 12));
  }
}
```

**python**
```python
bandeirinhas = []  # uma lista de objetos Bandeirinha
def setup():
    size(400, 400); 
    for i in range(50):
        bandeirinhas.append(bandeirinha(100, 100, 12))
```

ou

```python
def setup():
    global bandeirinhas
    size(400, 400); 
    bandeirinhas = [bandeirinha(100, 100, 12) for i in range(50)]  # uma compreensão de lista de objetos Bandeirinha
```


# Arrays 2D 

parar traduzir, arrays de duas dimensões em java, faça uma lista de listas (não, você não pode usar numpy).

**java**
```java
int[][] board;
board = new int[grid_w][grid_h]
```
**python**
```python
board = [[0] * grid_w for _ in range(grid_h)]
```

em vez do `0` você pode usar outro valor calculado ou `None` como 'segurador de lugar' (*placeholder*) caso a estrutura vá servir para outros tipos de dados.

---

trabalho em andamento...
