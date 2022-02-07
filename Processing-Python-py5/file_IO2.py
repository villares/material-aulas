# Lendo e escrevendo dados em arquivos CSV

# *Comma Separated Values*, um formato de intercâmbio primitivo, porém ainda útil

from __future__ import unicode_literals, print_function
import unicodecsv as csv
vamos agora falar sobre como ler e escrever dados simples em um arquivo CSV, um arquivo texto com valores separados por vígula. tanto o processing como o a biblioteca padrão do python tem ferramentas para ajudar a lidar com este formato.

*AVISO: * infelizmente o módulo **`csv`** da biblioteca padrão do jython, o python 2 que estamos usando, não entende de unicode então vamos usar uma biblioteca chamada **`unicodecsv`** que resolve isso para nós.

em preparação para o nosso primeiro exemplo, note que precisaremos de um arquivo[`dados.csv`](https: // raw.githubusercontent.com/villares/material-aulas/main/processing-python/assets/dados.csv) que deve ficar dentro da pasta `/ data /` dentro  do seu sketch, e de uma cópia de[`unicodecsv.py`](https: // raw.githubusercontent.com/villares/material-aulas/main/processing-python/assets/unicodecsv.py)(clique com o botão da direita do mouse para salvar no seu computador)

```
sketch_2020_05a(pasta/folder do sketch)
  L  sketch_2020_05a.pyde(arquivo com o código)
  L  unicodecsv.py(biblioteca de ajuda)
  L  data(pasta/folder)
       L  dados.csv(arquivo CSV)
```

conteúdo do aquivo:

```
nome, valor, area, largura, comprimento, x, y
A1, 800, 32, 2, 16, 0, 19
A3, 2520, 252, 14, 18, 2, 17
...
```
exemplo que lê o arquivo

```python


```

# Assuntos relacionados

* [textos no programa, no console e na tela(*strings*)](strings_py.md)
* se quiser ler mais sobre * filie IO * na documentação do python: [python 2.7 tutorial: reading and writing files](https: // docs.python.org/2/tutorial/inputoutput.html  # reading-and-writing-files)
