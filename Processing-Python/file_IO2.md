## Lendo e escrevendo dados em arquivos CSV

### *Comma Separated Values*, um formato de intercâmbio primitivo, porém ainda útil

Vamos agora falar sobre como ler e escrever dados simples em um arquivo CSV, um arquivo texto com valores separados por vígula. Tanto o Processing como o a biblioteca padrão do Python tem ferramentas para ajudar a lidar com este formato.

*AVISO:*  Infelizmente o módulo **`csv`** da biblioteca padrão do Jython, o Python 2 que estamos usando, não entende de Unicode então vamos usar uma biblioteca chamada **`unicodecsv`** que resolve isso para nós.

Em preparação para o nosso primeiro exemplo, note que precisaremos de um arquivo [`dados.csv`](https://raw.githubusercontent.com/villares/material-aulas/main/Processing-Python/assets/dados.csv) que deve ficar dentro da pasta `/data/` dentro  do seu sketch, e de uma cópia de [`unicodecsv.py`](https://raw.githubusercontent.com/villares/material-aulas/main/Processing-Python/assets/unicodecsv.py) (clique com o botão da direita do mouse para salvar no seu computador)

```
sketch_2020_05a                (pasta/folder do sketch)
  L  sketch_2020_05a.pyde      (arquivo com o código)
  L  unicodecsv.py             (biblioteca de ajuda)
  L  data                      (pasta/folder)
       L  dados.csv            (arquivo CSV)
```

Conteúdo do aquivo:

```
nome,valor,area,largura,comprimento,x,y
A1,800,32,2,16,0,19
A3,2520,252,14,18,2,17
...
```
Exemplo que lê o arquivo

```python
from __future__ import unicode_literals, print_function
import unicodecsv as csv


```

### Assuntos relacionados

* [Textos no programa, no console e na tela (*strings*)](strings_py.md)
* Se quiser ler mais sobre *Filie IO* na documentação do Python: [Python 2.7 Tutorial: Reading and Writing Files](https://docs.python.org/2/tutorial/inputoutput.html#reading-and-writing-files)


