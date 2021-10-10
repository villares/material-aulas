# Ideias de orientação a objetos: primeiros passos, usando um slider

No começo do curso os principais exemplos de código que vimos se valem de estratégias de programação que são conhecidas pelos nomes, "Programação Procedural" ou "Programação Imperativa Estruturada". Agora, uma vez que Python, assim como diversas outras linguagens, permite usar uma maneira de programar chamada "Orientação a Objetos" (_Object Orientation_, por vezes abreviada OO), bem como misturar elementos de diversos paradigmas. Vamos aqui então apresentar os primeiros elementos e vocabulários da orientação a objetos.

### Classe (_class_), tipo (_type_) ou uma "categoria de objetos"

Vamos aqui usar como equivalentes os termos classe e tipo, e quando falamos sobre os valores manipulados pela linguagem é comum falarmos sobre a que categoria pertencem, isto é, de que tipo ou classe são. Os valores mais simples como os números que manipulamos são objetos do tipo _float_ (ponto flutuante) ou _int_ (inteiros). E os textos são da classe _string_. Estruturas como listas são objetos do tipo _list_ e assim por diante. Você pode não ter percebido mas o Processing nos entrega os dados na forma de um objeto `PImage`. Por sinal fora os tipos embutidos essenciais, a maioria das classes, especialmente as que formos criar, seguem a conveção de ter a primeira letra maiúscula.

### Atributos e métodos

Objetos tem 


### Instanciar, ou criar uma nova instância de um objeto

Fora casos especiais em que uma função cria um novo objeto para nós (como `loadImage(nome_arquivo)` cria um objeto `PImage`) costumamos criar novos objetos chamando o nome da classe, e isso pode ou não demandar argumentos.

No exemplo que veremos a seguir vamos criar um slider assim:

```python
s1 = Slider(0, 90, 50, 'tamanho')  # mínimo, máximo, valor_inicial, etiqueta
```


## Exemplo de uso da classe `Slider`

```python
from __future__ import unicode_literals

def setup():
    global s1, s2, s3
    global seed
    seed = int(random(1000))
    print(seed)
    size(500, 500)
    s1 = Slider(0, 90, 50, 'tamanho')
    s1.position(20, 30)
    s2 = Slider(0, 180, 45, 'ângulo')
    s2.position(190, 30)
    s3 = Slider(0, 10, 0, 'variação aleatória')
    s3.position(360, 30)    
                
def draw():
    global angulo, rndvar
    randomSeed(seed)
    background(240, 240, 200)
    translate(250, 440)    
    tamanho = s1.update()
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
        
        
 # CONTINUA... precisa colar aqui a definição da classe Slider que está mais abaixo
 # ou colar em uma nova aba chamada slider.py e acrescentar `from slider import Slider`
 ```
        
![slider](assets/slider.png) 
        
### Como é a classe `Slider` por dentro?       
 
> Opcionalmente, é possível por o códio abaixo separado em uma nova aba *slider*, que se torna um arquivo `slider.py`. Nesse caso é preciso usar a instrução `from slider import Slider` no começo do seu código.
> Se não quiser fazer isso, simplesmente cole o código abaixo no final da aba principal.
    
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
    
    
### Uma segunda versão da classe Slider    
    
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
