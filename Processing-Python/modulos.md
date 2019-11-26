# Usando as abas no IDE do Processing

Multiplas abas são utilizadas para organizar melhor um *sketch*  mais longo. É comum separar definições de classes e outras funções em abas "secundárias". 

As funções `setup()`,  `draw()` assim como as que são acionadas por eventos (por exemplo, `mouseDragged()` ou `keyPressed()`) precisam ficar na primeira aba.

## Abas secundárias no modo Python 

Diferente das abas no IDE de Processing no modo tradicional, Java (que são tratadas como uma continuidade do código na primeira aba) as abas no modo Python são arquivos `.py` e se comportam como "módulos" Python,  por isso precisam ser "importadas", sendo referenciadas com a instrução `import`.

Ao criar uma nova aba, por exemplo, com o nome `segunda_aba`, ela se torna o arquivo `segunda_aba.py`. Note que a primeira aba do *sketch* é um arquivo com a extensão `.pyde`, extensão que fica oculta.

Na primeira aba, ou em qualquer aba que precise do código de outro módulo/aba, é preciso usar algo como:
```Python
from nome_aba import * 
```
Ou ainda, preferível e mais elegante:
```python
from nome_aba import uma_funcao, UmaClasse
```
Note que o nome do módulo é escrito **sem a extensão `.py`.**

#### Atenção 1: Não esqueça de salvar sempre quando usar abas!

*Sketches* com mais de uma aba, quando modificados não executam corretamente a menos que sejam salvos!

####  Atenção 2: Se as abas secundárias tiverem caracteres não-ASCII 

Acrescente `# -*- coding: utf-8 -*-` na primeira linha do arquivo. 

Veja também:  [`from __future__ import unicode_literals`](futuro.md)

#### Glossário

[módulo](https://penseallen.github.io/PensePython2e/03-funcoes.html#termo:m%C3%B3dulo)

Um arquivo que contém uma coleção de funções relacionadas e outras definições.

[instrução de importação](https://penseallen.github.io/PensePython2e/03-funcoes.html#termo:instrução%20de%20importação)

Uma instrução que lê um arquivo de módulo e cria um objeto de módulo.

---
Texto e imagens / text and images: CC BY-NC-SA 4.0; Código / code: GNU GPL v3.0 exceto onde explicitamente indicado por questões de compatibilidade.
