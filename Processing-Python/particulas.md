# Particulas (Orientação a objetos)

> Adapatdo de: VILLARES, A. B. A.; MOREIRA, D. DE C.; GOMES, M. R. [Ensino de programação em um contexto de exploração gráfica com Processing modo Python](https://villares.github.io/mestrado/VILLARES_MOREIRA_GOMES_GRAPHICA_2017). In: Anais GRAPHICA 2017 - XII International Conference on Graphics Engineering for Arts and Design. Anais…Araçatuba(SP) UNIP, 2017.
> *Para executar [instale o Processing com o modo Python](http://villares.github.io/como-instalar-o-processing-modo-python/)*

Vamos ver aqui alguns conceitos introdutórios de orientação a objetos: 

- Definindo uma Classe e instanciando objetos
- Atributos (propriedades ou campos) e métodos de um um objeto

Não são abordadadas ainda questões de herança ou composição.

Prerequisitos para aproveitar melhor este material:
* Desenho básico no Processing:
* Declaração de variáveis e noções de tipagem;
* Métodos de desenho `rect`, `line`, `ellipse`;
* Controle de atributos gráficos `fill`, `stroke`, `noStroke`, `noFill`, `background`;
* Controle de fluxo de execução e laços (`if`, `else` e `for`);
* Declaração de funções com e sem parâmetros;

###  0. Começando sem orientação a objetos
#### Redesenhando formas e atualizando variáveis no laço principal do Processing

Para obter o efeito de movimento (animação de uma partícula) criaremos um par de variáveis globais `x` e `y`, que serão inicializadas no `setup()` com as coordenadas do meio da àrea de desenho. Note que o escopo global dessas variáveis precisa ser indicado com a palavra chave `global` quando pretendemos alterá-las.

O código que vai em `draw()` tem a execução repetida continuamente, é o "laço principal" do *sketch*. Neste bloco vamos inicialmente limpar a tela com `background()` e em seguida invocar a função de desenho `particula()` na posição indicada pelas variáveis `x` e `y`, atualizar as variáveis de posição e por fim checar se estas estão além de um certo limite e precisam ser redefinidas para um novo ciclo da animação.

```python
def setup():
    """ Código de configuração, executado no início pelo Processing """
    global x, y
    size(100, 100)  # área de desenho
    x, y = width / 2, height / 2   # coordenadas do meio da área de desenho

def draw():
    """ Laço principal de repetição do Processing """
    global x, y
    background(0)  # limpeza do frame, fundo preto
    circle(x, y, 10)  # desenha círculo
    x += 1  # incrementa o x
    y += 1  # incrementa o y
    if x > width + 25:
        x = -25
    if y > height + 25:
        y = -25
```
### 1. Primeira aproximação de uma classe
#### Definindo a classe Partícula

Vamos agora obter o mesmo comportamento usando um objeto da classe definida pelo bloco `class Particula():`.

A definição da classe começa com o método especial `__init__()` que inicializa os atributos de dados (campos) de posição e tamanho quando um novo objeto é criado.

O método `desenha()` é praticamente a função que escrevemos no passo inicial, não requer mais os parâmetros de posição e tamanho, uma vez que usa os atributos de posição e tamanho do próprio objeto (instância do objeto) quando executado.

O método `atualize()` contém o código anteriormente usado para atualizar a posição nas variáveis globais, agora atualiza os atribdutos de dados (campos ou variáveis de instância) de posição do objeto.

No bloco `setup()` criamos uma instância de particula no meio da àrea de desenho com a linha`particula = Particula(width / 2, height / 2)` e o bloco `draw()` vai repetidamente limpar a tela e chamar os métodos de desenho e atualização, `particula.desenha()` e `particula.atualize()` respectivamente. 

```python
def setup():
    """ Código de configuração, executado no início pelo Processing """
    global particula_0
    size(100, 100)  # área de desenho
    particula_0 = Particula(width / 2, height / 2)

def draw():
    """ Laço principal de repetição do Processing """
    background(0)  # atualização do desenho, fundo preto
    particula_0.desenha()
    particula_0.atualize()

class Particula():
    """ Classe Particula, com métodos de desenho e atualizaçao ('atualize') """

    def __init__(self, px, py, ptamanho=50):
        self.x = px
        self.y = py
        self.tamanho = ptamanho

    def desenha(self):
        """ Desenha círculo """
        circle(self.x, self.y, self.tamanho)

    def atualize(self):
        """ atualiza a posição do objeto """
        self.x += 1
        self.y += 1
        if self.x > width + 25:
            self.x = -25
        if self.y > height + 25:
            self.y = -25
```

### 2. Instanciando mais objetos
#### Criando algumas partículas

A vantagem da estruturação e encapsulamento de ter uma classe Particula pode começar a fazer sentido quando instanciamos mais de uma particula.

```python
def setup():
    """ Instancia três particulas """
    global particula_0, baindeira_1, particula_2
    size(100, 100)  # área de desenho (width, height)
    meia_largura, meia_altura = width / 2, height / 2
    particula_0 = Particula(meia_largura, meia_altura)
    particula_1 = Particula(80, 10, 30)
    particula_2 = Particula(10, 40, 20)

def draw():
    """ Limpa a tela, desenha e atualiza particulas """
    background(0)  # atualização do desenho, fundo preto
    particula_0.desenha()
    particula_0.atualize()
    particula_1.desenha()
    particula_1.atualize()
    particula_2.desenha()
    particula_2.atualize()
    
```
```
...o código continua com a classe Particula mostrada anteriormente
```
### 3. Ampliando a classe Particula
#### Mudando o comportamento e adicionando outras propriedades.

O passo seguinte é dado ampliando o código da classe Particula.

No método `__init__()`:
1. Sorteio do tamanho, caso nenhum tenha sido fornecido na expressão construtora;
2. Sorteio da velocidade, decomposta nos componentes horizontal `self.vx` e vertical `self.vy`;
3. Sorteio da cor, ligeiramente translúcida.

No método `desenha()`:
1. Remoção do contorno com `noStroke()`;
2. Aplicação da cor de preenchimento com `fill(self.cor)`.

No método `atualize()`:
1. Atualização da posição pela soma dos componentes de velocidade na posição;
2. Tratamento da saída do objeto da área de desenho por qualquer dos lados.

```python
class Particula():
    """ Classe Particula, cor sorteada, velocidade sorteada """

    def __init__(self, px, py, ptamanho=None):
        self.x = float(px)
        self.y = float(py)
        if ptamanho:
            self.tamanho = ptamanho
        else:
            self.tamanho = random(50, 200)
        self.vx = random(-1,1)
        self.vy = random(-1,1)
        self.cor = color(random(256),  # R
                         random(256),  # G
                         random(256),  # B
                         200)  # alpha

    def desenha(self):
	""" Desenha círculo """
        fill(self.cor)
        circle(self.x, self.y, self.tamanho)


    def atualize(self):
        """ atualiza a posição do objeto e devolve do lado oposto se sair """
        self.x += self.vx
        self.y += self.vy
        metade = self.tamanho / 2
        if self.x > width + metade:
            self.x = -metade
        if self.y > height + metade:
            self.y = -metade
        if self.x < -metade:
            self.x = width + metade
        if self.y < -metade:
            self.y = height + metade
```

### 4. Muitas partículas!
#### Uma lista de objetos

Uma estrutura de dados, no caso uma lista, pode de maneira muito simples conter referências para um grande número de objetos.
Aqui chegamos rapidamente a um comportamento visualmente interessante instanciando 50 particulas no `setup()` e em seguida no `draw()` iteramos por estas particulas de maneira bastante típica em Python com um laço `for `*`object`*` in `*`collection_of_objects`*`:` 

```python
particulas = []  # lista de objetos

def setup():
    """ Define área de desenho e popula lista de particulas """
    size(400, 400)  # área de desenho (width, height)
    meia_largura, meia_altura = width / 2, height / 2
    for _ in range(50):
        nova_particula = Particula(meia_largura, meia_altura)
        particulas.append(nova_particula)

def draw():
    """ Limpa a tela, desenha e atualiza particulas """
    background(0)  # atualização do desenho, fundo preto
    for particula in particulas:
        particula.desenha()
        particula.atualize()
```
```
...o código continua com a classe Particula mostrada anteriormente
```

