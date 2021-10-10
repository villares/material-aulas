# Ideias de orientação a objetos: primeiros passos, usando um slider

No começo do curso os principais exemplos de código que vimos se valem de estratégias de programação que são conhecidas pelos nomes, "Programação Procedural" ou "Programação Imperativa Estruturada". Agora, uma vez que Python, assim como diversas outras linguagens, permite usar uma maneira de programar chamada "Orientação a Objetos" (_Object Orientation_, por vezes abreviada OO), bem como misturar elementos de diversos paradigmas. 

Vamos aqui então apresentar os primeiros elementos e vocabulários da orientação a objetos.

## Vocabulário

### Classe (_class_), tipo (_type_) ou uma "categoria de objetos"

Tratando como equivalentes os termos classe e tipo, quando falamos sobre os valores manipulados pelo nosso programa é comum falarmos sobre a categoria a que pertencem, isto é, de que tipo ou classe são. Os valores mais fundamentais, ditos primitivos, como os números que manipulamos, são do tipo _float_ (ponto flutuante) ou _int_ (inteiros), já os textos são da classe _str_ (abreviação de _string_). Estruturas como listas são objetos do tipo _list_ e assim por diante. Você pode não ter visto mas o Processing nos entrega os dados de imagens carregadas do disco na forma de um objeto `PImage`. 

Por sinal note que fora os tipos embutidos (aqui mencionanmos _int_, _float_, _str_ e _list_), as classes mais comuns, e especialmente as que formos criar, seguem a convenção de ter a primeira letra maiúscula.

### Atributos, ou campos

Objetos tem "valores de estado interno", atributos que podem ser consultados, e em alguns casos modificados, usando a "sintaxe do ponto".
Por exemplo, quando carregamos uma imagem no Processing podemos consultar as dimensões dela:

```python
img = loadImage('a.png')  # uma imagem PNG na pasta /data/
w = img.width  # largura em pixels
h = img.height  # altura em pixels    
```

### Métodos, funções associadas aos objetos

Objetos tem funções associadas a eles, que chamamos de métodos.
Uma lista em Python possui diversos métodos, já vimos pelo menos um deles: `.append()` que inclui elementos na lista.

```python
frutas = ['uva', 'banana']
frutas.append('kiwi')   
print(frutas)  # ['uva', 'banana', 'kiwi']
```

### Instanciar, ou criar uma nova instância de um objeto

Fora casos especiais em que podemos criar objetos diretammente no código (como a lista de frutas que acabamos de ver) ou com uma função ajudante, no caso de `loadImage(nome_arquivo)`, que cria um objeto `PImage`, costumamos criar novos objetos chamando o nome da classe, e isso pode ou não demandar argumentos. No exemplo que veremos a seguir vamos criaremos um slider assim:

```python
s1 = Slider(0, 90, 50, 'tamanho')  # mínimo, máximo, valor_inicial, etiqueta
```

## Exemplo de uso da classe `Slider`

Veja um exemplo comentado de como instanciar e usar objetos da classe `Slider` que tem os métodos `.position()` para locá-los na tela, e o método `.update()` que faz o duplo papel de desenhar o slider na tela e obter o valor indicado por ele naquele momento.

```python
from __future__ import unicode_literals

def setup():
    global s1, s2, s3
    global seed
    seed = int(random(1000))
    print(seed)
    size(500, 500)
    s1 = Slider(0, 90, 50, 'tamanho')   # instanciando o slider s1
    s1.position(20, 30)                 # posicionando s1 em x:20 y:30
    s2 = Slider(0, 180, 45, 'ângulo')
    s2.position(190, 30)
    s3 = Slider(0, 10, 0, 'variação aleatória')
    s3.position(360, 30)    
                
def draw():
    global angulo, rndvar
    randomSeed(seed)
    background(240, 240, 200)
    translate(250, 440)    
    tamanho = s1.update()          # atualizando, desenha s1 na tela e obtem um valor
    angulo = radians(s2.update())
    rndvar = s3.update() / 10
    galho(tamanho)   
     
def galho(tamanho):
    reducao = 0.75
    sw = tamanho / 10
    strokeWeight(sw)
    line(0, 0, 0, -tamanho)
    if tamanho > 5:
        pushMatrix()
        translate(0, -tamanho)
        rotate(angulo)
        galho(tamanho * reducao - random(-sw, sw) * rndvar)
        rotate(-angulo * 2)
        galho(tamanho * reducao - random(-sw, sw) * rndvar)
        popMatrix()
        
 # ...       
 # ATENÇÃO: precisa colar aqui a definição da classe Slider que está mais abaixo nest página.
 # ou colar em uma nova aba chamada slider.py e acrescentar `from slider import Slider`
 ```
        
![slider](assets/slider.png) 
       
       
### Como é a classe `Slider` por dentro?       

> **Atenção: o código abaixo faz parte do exemplo acima.**
> Opcionalmente, é possível por este código separado em uma nova aba *slider*, que se torna um arquivo `slider.py`. Nesse caso é preciso usar a instrução `from slider import Slider` no começo do seu código. Se não quiser fazer isso, simplesmente cole-o na aba principal, após o código anterior`.
    
Veja uma primeira versão da classe Slider

```python
class Slider:

    def __init__(self, low, high, default, label=''):
        self.low , self.high = low, high
        self.value = default
        self.label = label
        self.w, self.h = 120, 20
        self.position(20, 20)  # default position

    def position(self, x, y):
        self.x, self.y = x, y
        self.rectx = self.x + map(self.value, self.low, self.high, 0, self.w)

    def update(self):
        if mousePressed and dist(mouseX, mouseY, self.rectx, self.y) < self.h:
            self.rectx = mouseX
        self.rectx = constrain(self.rectx, self.x, self.x + self.w)
        self.value = map(self.rectx, self.x, self.x + self.w, self.low, self.high)
        self.display()
        return self.value
        
    def display(self):
        push()  # combina pushMatrix() and pushStyle()
        resetMatrix()
        camera()
        rectMode(CENTER)
        strokeWeight(4)
        stroke(200)
        line(self.x, self.y, self.x + self.w, self.y)
        strokeWeight(1)
        # stroke(0)
        fill(255)
        stroke(0)
        rect(self.rectx, self.y, self.w / 12, self.h)
        fill(0)
        textAlign(CENTER, CENTER)
        text("{:.1f}".format(self.value), self.rectx, self.y + self.h)
        text(self.label, self.x + self.w / 2, self.y - self.h)
        pop()  # popStyle() and popMat
```
    
## Extra: Uma segunda versão da classe Slider    
    
Acrescentando alguns extras e comentários à classe Slider.

```python
class Slider:

    template = "{:.1f}"  # para formatar como mostra o valor
    label_align = CENTER

    def __init__(self, low, high, default, label=''):
        """
        Slider needs range from low to high
        and and a default value. Label is optional.
        """
        self.low = low
        self.high = high
        self.value = default
        self.label = label
        self.w, self.h = 120, 20
        self.position(20, 20)  # default position

    def position(self, x, y):
        """Set position on screen, and the rectx 'handle' position"""
        self.x = x
        self.y = y
        # the position of the rect you slide:
        self.rectx = self.x + map(self.value, self.low, self.high, 0, self.w)

    def update(self):
        """Updates the slider and returns value. Calls display()"""
        # mousePressed moves slider
        if mousePressed and dist(mouseX, mouseY, self.rectx, self.y) < self.h:
            self.rectx = mouseX
        # constrain rectangle
        self.rectx = constrain(self.rectx, self.x, self.x + self.w)
        self.value = map(self.rectx,
                         self.x, self.x + self.w,
                         self.low, self.high)
        self.display()
        return self.value
        
    def display(self):
        """Display sliner on screen, using orginal Processing coordinates."""
        push()  # combines pushMatrix() and pushStyle()
        resetMatrix()
        camera()
        rectMode(CENTER)
        # gray line behind slider
        strokeWeight(4)
        stroke(200)
        line(self.x, self.y, self.x + self.w, self.y)
        # draw rectangle
        strokeWeight(1)
        stroke(0)
        fill(255)
        translate(0, 0, 1)
        rect(self.rectx, self.y, self.w / 12, self.h)
        # draw value
        fill(0)
        textSize(10)
        textAlign(CENTER, CENTER)
        text(self.template.format(self.value), self.rectx, self.y + self.h)
        # draw label
        if self.label_align == LEFT:
            textAlign(self.label_align)
            text(self.label, self.x, self.y - self.h)
        else:
            text(self.label, self.x + self.w / 2, self.y - self.h)
        pop()  # popStyle() and popMat
```
