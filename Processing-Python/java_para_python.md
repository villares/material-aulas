# Dicas para portar código de Processing modo Java para modo Python

> …e possivelmente vice-versa :)

![](assets/java_python.png) 

### Considerações gerais

- Comentários com `//` no Java viram comentários com `#` . Comentários de várias linhas com `/* … */ ` podem virar *docstrings*, com aspas triplas no Python, `""" … """`.

- Java é uma linguagem de *tipagem estática* e Python é uma linguagem de *tipagem dinâmica*  isso significa que vamos remover todas as declarações de tipo. Remova `int `, `float`, `String`, `color` , `boolean`  das declarações de variáveis. Por exemplo,  `int i = 0; ` se torna `i = 0`.

- Podemos também remover `void` ou  tipo na declaração de uma função e colocar no lugar o `def` do Python.  Depois remover a declaração de tipo dos parâmetros da função.

   **Java**
  ```java
  float media(float a, float b){
    return (a + b) / 2;
  }
  ```
  **Python**
  ```python
  def media(a, b):
      return (a + b) / 2
  ```
- É comum a indentação do Java estar refletindo a hierarquia dos blocos de instruções, mesmo isso não sendo obrigatório (no Java são as chaves `{}` que mandam), use a ferramenta de auto-formatação do IDE antes de começar! 
- As chaves precisam ser removidas, e você deve trocar cada `{ ` por `:` no começo de um bloco de instruções (isso só não vale para as definições de *arrays*, que tem chaves mas não definem um bloco de instruções, e viram uma lista ou uma tupla com `[ ]` ou` ( )` ). 
- Remova os `;` no final das linhas.

### `if`, `else` e seus amigos

Note que a condição do `if` no Python não tem os parênteses obrigatórios no Java. A combinação de um `else if` vira a contração `elif`.

**Java**

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
**Python**
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

Não existe `switch/case` no Python, você pode trocar por uma cadeia de `if/elif` ou, se for só para chamar diferentes funções, um dicionário de funções [TO DO página sobre isso].

### Variáveis globais

Se a variável for declarada e inicializada no começo do *sketch* basta remover a declaração de tipo

Mas como não há em Python a declaração de uma variável sem fazer uma atribuição, se a variável é só declarada (sem ser *inicializada*, isto é ter sua primeira atribuição) no começo do *sketch* precisamos ver onde ela é inicializada e acrescentar a instrução `global nome_da variável` no início da função. 

Na verdade, toda função que contém instruções que alteram a atribuição de variáveis globais precisam de instruções `global` com os nomes das variáveis que são modificadas. 

### Um quadro com equivalências para conversão

Os valores booleanos em Java são `true` e `false`, o que em Python fica `True` e `False`.  Vamos fazer um quadro com os operadores lógicos e outra equivalências. 

| Java                                             | Python                                     |
| ------------------------------------------------ | ------------------------------------------ |
| `true` e `false`                                 | `True` e `False`                           |
| ``a && b`` (**e** lógico)                        | `a and b`                                  |
| `a || b` (**ou** lógico)                         | `a or b`                                   |
| `!a` (**não** lógico)                            | `not a`                                    |
| `i++` (incremento de variável)                   | `i += 1`                                   |
| `i--`(decremento de variável)                    | `i -= 1`                                   |
| `a <= b && b < c`                                | `a <= b < c`                               |
| `for (int i=0; i < limite; i++){ … `             | `for i in range(limite): …`                |
| `for (int i=inicio; i < limite; i += passo){ … ` | `for i in range(inicio, limite, passo): …` |
| `for (Bola b : arrayListBolas){ …`               | `for b in listaBolas: …`                   |

E semelhante a `null` de Java temos o valor `None` em Python os usos não são totalmente equivalentes mas é um bom palpite fazer a substituição.



### Importando bibliotecas e as outras abas do sketch

No Processing modo Java as bibliotecas são importadas com `import` mas no modo Python essa instrução é mais usada para importar *módulos* da biblioteca padrão do Python, e arquivos **.py** como as outras abas do IDE, que ao contrário do modo Java não são automaticamente parte do *sketch*.

Use o comando do menu **Sketch > Importar Biblioteca.. ** (ou *Sketch > Import Library...* em inglês) para acrescrentar a linha com  `add_library()` com o argumento correto.

**Java**
```java
import com.hamoid.*; // biblioteca VideoExport
```

**Python**

```python
add_library('VideoExport')  # a mesma biblioteca Video Export
```

### Orientação a objetos

#### Obtendo uma instância e acessando métodos e atributos

Praticamente a única  diferença é que some a palavra chave `new` para criar uma instância de uma classe. O acesso a métodos e atributos é rigorosamente igual.

**Java**
```java
VideoExport videoExport;

void setup() {
  size(600, 600);
  videoExport = new VideoExport(this);
  videoExport.startMovie();
}
```

**Python**

```python
def  setup() :
    global videoExport
    size(600, 600)
    videoExport = VideoExport(this)
    videoExport.startMovie()
```

#### Declarando uma classe

Já as declarações de classe mudam um pouco, grosso modo, o método `__init__(self)` faz o papel do *construtor* da classe.  Veja a classe `MRect` do exemplo **Basics > Objects > Objects** que vem no IDE do Processing.

**Java**

```java
class MRect 
{
  int w; // single bar width
  float xpos; // rect xposition
  float h; // rect height
  float ypos ; // rect yposition
  float d; // single bar distance
  float t; // number of bars
 
  MRect(int iw, float ixp, float ih, float iyp, float id, float it) {
    w = iw;
    xpos = ixp;
    h = ih;
    ypos = iyp;
    d = id;
    t = it;
  }
 
  void move (float posX, float posY, float damping) {
    float dif = ypos - posY;
    if (abs(dif) > 1) {
      ypos -= dif/damping;
    }
    dif = xpos - posX;
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



**Python**

```python
class MRect:

    def __init__(self, iw, ixp, ih, iyp, id, it):
        self.w = iw  # single bar width
        self.xpos = ixp  # rect xposition
        self.h = ih  # rect height
        self.ypos = iyp  # rect yposition
        self.d = id  # single bar distance
        self.t = it  # number of bars

    def move(self, posX, posY, damping):
        self.dif = self.ypos - posY
        if abs(self.dif) > 1:
            self.ypos -= self.dif / damping

        self.dif = self.xpos - posX
        if abs(self.dif) > 1:
            self.xpos -= self.dif / damping

    def display(self):
        for i in range(self.t):
            rect(self.xpos + (i * (self.d + self.w)),
                 self.ypos, self.w, height * self.h)
```

