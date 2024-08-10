# Primeiros passos de orientação a objetos: usando a classe Slider

No começo do curso os principais exemplos de código que vimos se valem, em geral, de estratégias de programação sem "Orientação a Objetos". Agora veremos como Python, assim como diversas outras linguagens, permite usar esta maneira de programar, pomposamente chamada de "paradigma de programação": a Orientação a objetos(__object Orientation_, por vezes abreviada OO). Python permite misturar elementos de diversos paradigmas.

Vamos começar apresentando os primeiros elementos e vocabulários da orientação a objetos.

## Ideias principais e vocabulário

### Classe (_class_), tipo (_type_) ou uma "categoria de objetos"

Tratando como equivalentes os termos classe e tipo, quando falamos sobre os valores manipulados pelo nosso programa é comum mencionarmos a categoria a que pertencem, isto é, de que tipo ou classe são. Os valores mais fundamentais, ditos primitivos, como os números que manipulamos, são em geral do tipo _float_(ponto flutuante) ou _int_(abreviação de _integer_, inteiros), já os textos são da classe _str_(abreviação de _string_, uma cadeia de caracteres). Estruturas como listas são objetos do tipo _list_ e assim por diante. Você pode não ter visto mas o Processing nos entrega os dados de imagens carregadas do disco na forma de um objeto `Py5Image`. Cada tipo de objeto pode ter propriedades e funcionalidades específicas(atributos e métodos) que os tornam mais úteis em determinados contextos.

Note que fora os tipos embutidos(acima mencionamos _int_, _float_, _str_ e _list_, mas há vários outros), as classes normalmente seguem a convenção de ter a primeira letra maiúscula no nome, com `Slider` que veremos mais à frente, e é especialmente recomendável seguir essa convençao para as classes que você criar.

### Atributos (propriedades ou campos)

Objetos tem "valores ou propriedades" chamadas de atributos, que podem ser consultados usando a "sintaxe do ponto" (`objeto.atributo`).
Por exemplo, quando carregamos uma imagem no Processing podemos consultar as dimensões dela nos atributos `.width` e `.height`:

```python
img = load_image('a.png')  # uma imagem PNG na pasta /data/
w = img.width  # largura em pixels
h = img.height  # altura em pixels
```

### Métodos (ou funções associadas aos objetos)

Objetos tem funções associadas, conhecidas como métodos, que podem ser invocadas com a "sintaxe do ponto" (`objeto.metodo()`).
Uma lista em Python, por exemplo, [possui diversos métodos](list_methods.md) e já vimos pelo menos um deles, o `.append()` que é chamado para incluir elementos na lista.

```python
frutas = ['uva', 'banana']
frutas.append('kiwi')
print(frutas)  # ['uva', 'banana', 'kiwi']
```

### Instanciar (criar uma nova instância de um objeto)

Fora casos especiais em que podemos criar objetos diretammente no código (como a lista de frutas que acabamos de ver) ou com uma função ajudante, no caso de `load_image(nome_arquivo)` que cria um objeto `Py5Image`, costumamos criar novos objetos *chamando* o nome da classe (usando os parênteses, como em uma chamada de funç, e isso pode ou não demandar argumentos. No exemplo que veremos a seguir vamos criar um slider.

```python
s1 = Slider(0, 90, 50, 'tamanho')  # mínimo, máximo, valor_inicial, etiqueta
```

## O que ficou de fora

Não vamos ver ainda neste momento em detalhes de como funciona a definição ou criação da classe(a parte que segue `class Slider: `), que codifica como ela produz e inicializa os objetos ou como são definidos os métodos, nem trataremos do assunto mais avançado "herança" em que uma classe é baseada em outra, recebendo desta parte das suas características.

## Exemplo de uso da classe `Slider`

Veja agora um exemplo comentado de como instanciar e usar objetos da classe `Slider` que vão servir de interface gráfica para modificar um desenho de uma àrvore.

Note que os objetos _slider_ tem os métodos `.position()` para locá-los na tela depois de terem sido criados, e o método `.update()`, que chamaremos dentro da função `draw()` para fazer o duplo trabalho de desenhar o slider na tela e obter o valor indicado pelo _slider_ naquele momento.

```python


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
    random_seed(seed)
    background(240, 240, 200)
    translate(250, 440)
    tamanho = s1.update()          # atualizando, desenha s1 na tela e obtem um valor
    angulo = radians(s2.update())
    rndvar = s3.update() / 10
    galho(tamanho)


def galho(tamanho):
    reducao = 0.75
    sw = tamanho / 10
    stroke_weight(sw)
    line(0, 0, 0, -tamanho)
    if tamanho > 5:
        push_matrix()
        translate(0, -tamanho)
        rotate(angulo)
        galho(tamanho * reducao - random(-sw, sw) * rndvar)
        rotate(-angulo * 2)
        galho(tamanho * reducao - random(-sw, sw) * rndvar)
        pop_matrix()

 # ...
 # Atenção: precisa colar aqui a definição da classe Slider que está mais abaixo nesta página.
 # ou colar em uma nova aba chamada slider.py e acrescentar `from slider
 # import Slider` no início do sketch
 ```
        
![slider](assets/slider.png) 
       
       
## Como é a definição da classe `Slider`? (a classe por dentro)       

> **Atenção: o código abaixo faz parte do exemplo acima.**
> Em projetos grandes, mais complexos, pode ser interessante separar as classes em outro arquivo para facilitar a manipulação e leitura do código. Para isso, crie um novo arquivo, que pode se chamar, por exemplo `slider.py`, vizinho ao seu arquivo principal. No arquivo principal é preciso usar a instrução `from slider import Slider` no começo do seu código. Se não quiser fazer isso, simplesmente cole-o no final do seu arquivo principal, após o código anterior`.
    
Veja uma primeira versão da classe Slider

```python
# PY5 IMPORTED MODE CODE

class Slider:

    def __init__(self, low, high, default, label=''):
        self.low , self.high = low, high
        self.value = default
        self.label = label
        self.w, self.h = 120, 20
        self.position(25, 25)  # default position

    def position(self, x, y):
        self.x, self.y = x, y
        self.rectx = self.x + remap(self.value, self.low, self.high, 0, self.w)

    def update(self):
        if is_mouse_pressed and dist(mouse_x, mouse_y, self.rectx, self.y) < self.h:
            self.rectx = mouse_x
        self.rectx = constrain(self.rectx, self.x, self.x + self.w)
        self.value = remap(self.rectx, self.x, self.x + self.w, self.low, self.high)
        self.display()
        return self.value
        
    def display(self):
        push()  # combina pushMatrix() and pushStyle()
        reset_matrix()
        camera()
        rect_mode(CENTER)
        stroke_weight(4)
        stroke(200)
        line(self.x, self.y, self.x + self.w, self.y)
        stroke_weight(1)
        stroke(0)
        line(self.x + self.w / 24, self.y, self.x + self.w - self.w / 24, self.y)
        fill(255)
        stroke(0)
        rect(self.rectx, self.y, self.w / 12, self.h)
        fill(0)
        text_align(CENTER, CENTER)
        text("{:.1f}".format(self.value), self.rectx, self.y + self.h)
        text(self.label, self.x + self.w / 2, self.y - self.h)
        pop()  # popStyle() and popMatrix
```
    
# Páginas relacionadas

- [Um botão com orientação a objetos](Processing-Python/botao_com_oo.md)
- [Uma classe de partículas simples](Processing-Python/particulas.md)
- [Introdução a orientação a objetos com bandeirinhas](https://abav.lugaralgum.com/mestrado/bandeirinhas/) (página externa)
    
## Extra: Uma segunda versão da classe `Slider`    
    
Acrescentando algumas funcionalidades extra e comentários à classe `Slider`.

```python
# PY5 IMPORTED MODE CODE

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
        self.position(25, 25)  # Pos default

    def position(self, x, y):
        """Define as coordenadas na tela, e calcula rectx, pos. do 'handle'"""
        self.x = x
        self.y = y
        # the position of the rect you slide:
        self.rectx = self.x + remap(self.value, self.low, self.high, 0, self.w)

    def update(self):
        """Atualiza o slider e devolve o valor (self.value). Chama display()"""
        # is_mouse_pressed moves slider
        if is_mouse_pressed and dist(mouse_x, mouse_y, self.rectx, self.y) < self.h:
            self.rectx = mouse_x
        # constrain rectangle
        self.rectx = constrain(self.rectx, self.x, self.x + self.w)
        self.value = remap(self.rectx,
                         self.x, self.x + self.w,
                         self.low, self.high)
        self.display()
        return self.value
        
    def display(self):
        """Desenha o slider na tela, usando coordenadas sem transformar"""
        push()         # Combina pushMatrix() e pushStyle()
        reset_matrix()  # push(), seguido de resetMatrix() e camera() permitem...
        camera()       # .maldino@fediscience.org.. desenhar o slider no sistema de coordenadas original
        rect_mode(CENTER)
        # Linha cinza sob o slider
        stroke_weight(4)
        stroke(200)
        line(self.x, self.y, self.x + self.w, self.y)
        # O retângulo, elemento principal da interface do slider
        stroke_weight(1)
        stroke(0)
        fill(255)
        translate(0, 0, 1)
        rect(self.rectx, self.y, self.w / 12, self.h)
        # Mostra o valor (value) atual
        fill(0)
        text_size(10)
        text_align(CENTER, CENTER)
        text(self.template.format(self.value), self.rectx, self.y + self.h)
        # draw label
        if self.label_align == LEFT:
            text_align(self.label_align)
            text(self.label, self.x, self.y - self.h)
        else:
            text(self.label, self.x + self.w / 2, self.y - self.h)
        pop()  # equivale a popStyle() and popMatrix()
```
