# Os modos do py5

## Uma breve visão geral

A biblioteca **py5** pode ser usada de varias maneiras, estilos ou contextos de programação, que chamamos de "modos". Mais detalhes podem ser encontrados em [py5coding.org - The Four py5 Modes](http:// py5coding.org/content/py5_modes.html).

> ⚠️ **Se estiver em um Mac:**<br>
> Leia [Special Notes for OSX Users](http://py5coding.org/content/osx_users.html).

### Module mode (modo de módulo)

Este modo pode parecer familiar para alguns programadores Python. Você importa a biblioteca no começo do código e define algumas funções especiais que o py5 chama para você, como `setup()` (executa uma vez quando o sketch é iniciado), `draw()` (repete continuamente, usado para interação e animações ) e quem sabe algumas outras [funções de evento](http://py5coding.org/reference/sketch.html). No final você chama `py5.run_sketch()`.

O exemplo a seguir cria um pequeno sketch que desenha retângulos na posição atual do mouse:

```python
import py5

def setup():
    py5.size(300, 200)
    py5.rect_mode(py5.CENTER)

def draw():
    py5.rect(py5.mouse_x, py5.mouse_y, 10, 10)

py5.run_sketch()
```

![imagem](https://user-images.githubusercontent.com/3694604/201694987-f78a4856-1329-4693-a312-4ab3402fe689.png)

> ⚠️ **Cuidado:**<br>
> Não use `from py5 import *`, isso quebra muitas coisas! Se você quiser evitar os prefixos `py5.`, considere usar o *imported mode*.

> ℹ️ **Observação:**<br>
> Se você não definiu `settings()` (opcional neste modo), a função `setup()` será dividida em `setup()` e `settings()` para você sob o capô, de acordo com algumas regras, como `size()` precisa ficar em `settings()`, um requisito do Processing.

### Imported mode (modo importado)

Originalmente criado para programadores iniciantes, o *modo importado* é análogo ao modo como as pessoas programamam no Processing IDE. Você não precisa digitar `py5.` o tempo todo.

Para usar este modo, você precisa do *py5 Jupyter Notebook Kernel* ([instruções de instalação aqui](http://py5coding.org/content/install.html)) ou, se estiver usando outros editores de código, precisa executar o seu código a partir da ferramenta de linha de comando `run_sketch` (`$ run_sketch your_sketch.py`).

Outra opção é usar o *Thonny IDE* com o plug-in [thonny-py5mode](https://github.com/tabreturn/thonny-py5mode/) instalado, que cria um menu *py5* com a opção *Imported mode for py5*, que, quando estiver marcada, faz o Thonny executar a ferramenta `run_sketch` para você.

Este é o exemplo anterior escrito para *impoeted mode*:

``` python
def setup():
    size(300, 200)
    rect_mode(CENTER)

def draw():
    rect(mouse_x, mouse_y, 10, 10)

# Se você estiver usando um Jupyter Notebook, adicione isto:
run_sketch()
```

### Static mode (modo estático)

*Static mode* permite criar imagens estáticas usando código sem função. Ele é projetado para programadores iniciantes que estão dando seus primeiros passos na programação Python.

O código abaixo, escrito para *static mode*, criará uma imagem de 300 por 200 pixels com fundo cinza e 20 quadrados posicionados aleatoriamente:

``` python
size(300, 200)
rect_mode(CENTER)
for _ in range(20):
    rect(random_int(width), random_int(height), 10, 10)
```

![imagem](https://user-images.githubusercontent.com/3694604/201693378-ccce119a-29ca-4569-bebc-1a3ec2f4c4da.png)

Para usar o modo estático no Jupyter Lab, instale o *py5bot Kernel* conforme descrito na [página de instalação do py5](http://py5coding.org/content/install.html), depois inicie o Jupyter Lab usando `$ jupyter lab`. Você verá *py5bot* apresentado como uma opção no Launcher. Clique nele e coloque o código em uma célula do notebook.

Você também pode usar a ferramenta `run_sketch` ou o plug-in Thonny IDE conforme descrito para *modo importado*.

### Class mode (modo de classe)

Para usuários mais avançados que desejam executar vários esboços ao mesmo tempo, o *class mode* convida você a criar uma classe com um método `settings`, agora necessário, `setup`,`draw` e outros métodos desejados.

O primeiro exemplo de *module mode* convertido para *class mode* seria assim:

``` python
from py5 import Sketch


class TestSketch(Sketch):

    def settings(self):
        self.size(300, 200)

    def setup(self):
        self.rect_mode(self.CENTER)

    def draw(self):
        self.rect(self.mouse_x, self.mouse_y, 10, 10)


test = TestSketch()
test.run_sketch()
```

## Leitura adicional

Para mais detalhes, visite a **documentação do py5** completa em [py5coding.org](https://py5coding.org)
