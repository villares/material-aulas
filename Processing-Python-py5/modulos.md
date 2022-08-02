# Usando `import` e vários arquivos no Thonny IDE
# TL:DR; Você pode separar o seu código em outro arquivos .py e tratá-los como *módulos*

Múltiplos arquivos podem ser utilizados para organizar melhor um * sketch * mais longo. é comum separar as definições de classes e outras funções em arquivos "secundários".

**as funções `setup()`,  `draw()` assim como as que são acionadas por eventos, por exemplo, `mouse_dragged()` ou `key_pressed()` devem ficar no arquivo principal**

# Usando vários arquivos .py

Se você puser parte do seu código em diferentes arquivos `.py`, eles então se comportam como "módulos" Python, precisam ter o seu conteúdo "importado", sendo referenciados com a instrução `import`.

Por exemplo, um aarquivo com o nome `segundo_arquivo.py` na primeiro arquivo, ou em qualquer arquivo que precise do código de outro módulo/arquivo, é preciso usar algo como:

```python
from nome_arquivo import *
``` 

ou ainda, considerado preferível e mais elegante em projetos grandes na comunidade python:

```python
from nome_arquivo import uma_funcao, outra_funcao, uma_classe, outra_classe
```

**Note que o nome do módulo é escrito ** sem a extensão `.py`.**

# Atenção: Não esqueça de salvar sempre quando usar arquivos!

*Sketches* com mais de um arquivo, quando modificados não executam corretamente a menos que sejam salvos!

# Exemplo de importação da biblioteca padrão do Python

A instrução `import` e suas variantes são usadas para importar ferramentas da biblioteca padrão do python, módulos que vem junto com o interpretador python contendo diversas funções e classes, mas que só ficam disponíveis quando requisitados.

Vamos usar como exemplo aqui o módulo `random` de python que tem uma função chamada `choice()`, que 'sorteia um item' (leia mais sobre [pseudo-aleatoriedade](aleatoriedade_1.md) e o [módulo `random`](aleatoriedade_2.md)) de uma coleção, que pode ser uma tupla, lista, conjunto..., e isso pode ser bastante útil na programação criativa.

Se fizermos `import random`, temos dois problemas, matamos a função `random()` do processing e temos que usar a forma `sorteio = random.choice(colecao)` que é muito longa. A forma `from random import *` também mata o `random()` do processing. uma opção melhor pode ser fazer assim:

```python
from random import choice

colecao = ("A", "B", "C", "D")
sorteio = choice(colecao)
```

Um estilo muito comum, se você precisa de todos os métodos de `random`, mas não quer 'poluir' os nomes globais do processing, é fazer assim:

```python
import random as rnd

colecao = ("A", "B", "C", "D")
sorteio = rnd.choice(colecao)
```

# Glossário

[módulo](https: // penseallen.github.io/pense_python2e/03-funcoes.html  # termo:m%C3%B3dulo) um arquivo que contém uma coleção de funções relacionadas e outras definições.

[instrução de importação](https: // penseallen.github.io/pense_python2e/03-funcoes.html  # termo:instrução%20de%20importação) uma instrução que lê um arquivo de módulo e cria um objeto de módulo.
