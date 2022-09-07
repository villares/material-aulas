# Usando as abas no Thonny IDE
## TL:DR; As abas se comportam como *módulos* de Python

```
from nome_aba import *
import random as rnd
from random import choice`
from nome_aba import uma_funcao, outra_funcao, Uma_classe, Outra_classe
``` 


Múltiplas abas são utilizadas para organizar melhor um *sketch* mais longo. É comum separar as definições de classes e outras funções em abas "secundárias".

**As funções `setup()`,  `draw()` assim como as que são acionadas por eventos, por exemplo, `mouse_dragged()` ou `key_pressed()`, precisam ficar na primeira aba.**

Em princípio quando está executando o código de um outro módulo o Pyrhon não conhece o vocabulário da biblioteca py5.


## Exemplo de importação da biblioteca padrão do Python

A instrução `import` e suas variantes são usadas para importar ferramentas da biblioteca padrão do Python, módulos que vem junto com o interpretador Python contendo diversas funções e classes, mas que só ficam disponíveis quando requisitados.

Vamos usar como exemplo aqui o módulo `random` de Python que tem uma função chamada `choice()`, que 'sorteia um item' (leia mais sobre[pseudo-aleatoriedade](aleatoriedade_1.md) e o[módulo `random`](aleatoriedade_2.md)) de uma coleção, que pode ser uma tupla, lista, conjunto..., e isso pode ser bastante útil na programação criativa.

Se fizermos `import random`, temos dois problemas, matamos a função `random()` do Processing e temos que usar a forma `sorteio = random.choice(colecao)` que é muito longa. A forma `from random import *` também mata o `random()` do Processing. Uma opção melhor pode ser fazer assim:

```python

colecao = ("A", "B", "C", "D")
sorteio = choice(colecao)
```

Um estilo muito comum, se você precisa de todos os métodos de `random`, mas não quer 'poluir' os nomes globais do Processing, é fazer assim:

```python

colecao = ("A", "B", "C", "D")
sorteio = rnd.choice(colecao)
```

# Glossário

[módulo](https://penseallen.github.io/PensePython2e/03-funcoes.html  # termo:m%C3%B3dulo)

Um arquivo que contém uma coleção de funções relacionadas e outras definições.

[instrução de importação](https://penseallen.github.io/PensePython2e/03-funcoes.html  # termo:instrução%20de%20importação)

Uma instrução que lê um arquivo de módulo e cria um objeto de módulo.

---
Texto e imagens / text and images: CC BY-NC-SA 4.0; Código / code: GNU GPL v3.0 exceto onde explicitamente indicado por questões de compatibilidade.
