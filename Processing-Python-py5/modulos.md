# Usando as abas no Thonny IDE e importando de outros módulos

Para organizar melhor um *sketch* mais longo é comum separar as definições de classes e outras funções em "arquivos secundários", e é comum também trabalhar com esses vários arquivos abertos em diferentes abas do Thoony. 

No Processing Java a integração entre arquivos é feita magicamente para você unindo todas as abas abertas do Processing IDE no modo Java, como se tudo fossem um só arquivo. Com o modo Python, e agora no Thonny IDE com py5, é diferente, você precisa pedir para o arquivo principal "importar" código dos outros, e aqui vamos ver um pouco sobre como isso funciona.

## Exemplos de importação de módulos em Python

Cada arquivo que escrevemos tem o potencial de conter código que se comporta da mesma maneira como um *módulo* da biblioteca padrão em Python, veja alguns exemplos de importação, as instruções que trazem os nomes de outros módulos para você usar no seu programa.

```
import random as rnd         # traga o módulo random da biblioteca padrão, com outro nome, usando o apelido rnd
from random import choice    # traga a função choice() do módulo random
from nome_arquivo import *   # traga todos os nomes de nome_arquivo.py (não é muito recomendado)
from nome_arquivo import uma_funcao, outra_funcao, Uma_classe, Outra_classe   # traga estes nomes no nome_arquivo.py
``` 

### Exemplo de importação da biblioteca padrão do Python

A instrução `import` e suas variantes são usadas para importar ferramentas da biblioteca padrão do Python, módulos que vem junto com o interpretador Python contendo diversas funções e classes, mas que só ficam disponíveis quando requisitados.

Vamos usar como exemplo aqui o módulo `random` de Python que tem uma função chamada `choice()`, que 'sorteia um item' (leia mais sobre[pseudo-aleatoriedade](aleatoriedade_1.md) e o [módulo `random`](aleatoriedade_2.md)) de uma coleção, que pode ser uma tupla, lista, conjunto..., e isso pode ser bastante útil na programação criativa.

Se fizermos `import random`, temos dois problemas, matamos a função `random()` do Processing e temos que usar a forma `sorteio = random.choice(colecao)` que é muito longa. A forma `from random import *` também mata o `random()` do Processing. Uma opção melhor pode ser fazer assim:

```python
from random import choice

colecao = ("A", "B", "C", "D")
sorteio = choice(colecao)
```

Um estilo muito comum, se você precisa de todos os métodos de `random`, mas não quer 'poluir' os nomes globais do Processing, é fazer assim:

```python
import random as rnd

colecao = ("A", "B", "C", "D")
sorteio = rnd.choice(colecao)
```

### Usando vários arquivos com o py5

As funções `setup()`, `draw()` assim como as que são acionadas por eventos, por exemplo, `mouse_dragged()` ou `key_pressed()`, precisam ficar no mesmo arquivo principal.

Saba também que, em princípio, quando está executando o código que está em um outro módulo, o Python não conhece o vocabulário da biblioteca py5, isso pode não ser um problema, mas também pode ser remediado com a extratégia [explicada na documentação do py5](http://py5coding.org/content/importing_py5_code.html) que consiste em adicionar um "comentário especial" para marcar arquivos secundários com código que queremos separar, e que use as funções do py5 no modo importado.

Arquivo principal `meu_sketch.py`:

```python
from pinceis import pincel_quadrado 

def setup():
    size(400, 400)

def draw():
    pincel_quadrado(random(10, 20))
```

Arquivo secundáro `pinceis.py`, o comentário especial `# PY5 IMPORTED MODE CODE` permite usar as funções de py5 aqui:

```python
# PY5 IMPORTED MODE CODE

def pincel_quadrado(tam):
    rect_mode(CENTER)
    square(mouse_x, mouse_y, tam)
```

# Glossário

- [módulo](https://penseallen.github.io/PensePython2e/03-funcoes.html#termo:módulo)
   Um arquivo que contém uma coleção de funções relacionadas e outras definições.

- [instrução de importação](https://penseallen.github.io/PensePython2e/03-funcoes.html#termo:instrução%20de%20importação)
   Uma instrução que lê um arquivo de módulo e cria um objeto de módulo.
