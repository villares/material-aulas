## Lendo e escrevendo dados em arquivos CSV

### *Comma Separated Values*, um formato de intercâmbio primitivo, porém ainda útil

Vamos agora falar sobre como ler e escrever dados simples em um arquivo CSV, um arquivo texto com valores separados por vígula. Tanto o Processing como o a biblioteca padrão do Python tem ferramentas para ajudar a lidar com este formato.

*AVISO:*  Infelizmente o módulo `csv` da biblioteca padrão do Jython, o Python 2 que estamos usando, não entende de Unicode então vamos usar uma biblioteca chamada [`unicodecsv`](https://raw.githubusercontent.com/villares/material-aulas/main/Processing-Python/assets/unicodecsv.py) que resolve isso para nós.

Em preparação para o nosso primeiro exemplo, note que precisaremos de um arquivo `dados.csv` que deve ficar dentro da pasta `/data/` dentro  do seu sketch, e de uma cópia de `unicodecsv.py` que você pode copiar do no parágrafo anteror:

```
sketch_2020_05a                (pasta/folder do sketch)
  L  sketch_2020_05a.pyde      (arquivo com o código)
  L  unicodecsv.py             (biblioteca de ajuda)
  L  data                      (pasta/folder)
       L  dados.csv            (arquivo CSV)
```

Conteúdo do aquivo:

```
maçã
abacaxi
pêra
banana
jaca
maracujá
```
Exemplo que escreve e depois lê do mesmo arquivo

```python
from __future__ import unicode_literals, print_function
import unicodecsv as csv
import os

# Define dados
data = [
    (1, "maçã,", 1.0),
    (42, "manga, uva", 2.0),
    (1337, "jaca", -1),
    (0, "kiwi", 123),
    (-2, "Nada.", 3),
    #(float("NaN"), None, ""),
    #(float("infinity"), True, False),
]

def setup():
    size(600, 600)
    background(0, 100, 0)
    # textSize(24)
    textFont(createFont('Source Code Pro', 24))
    # Write CSV file
    caminho_pasta_data = sketchPath('data')
    if not os.path.exists(caminho_pasta_data):
        os.mkdir(caminho_pasta_data) # cria pasta se não existir
    caminho_arquivo = os.path.join("data", "test.csv")
    with open(caminho_arquivo, "w") as fp:
        writer = csv.writer(fp)
        # writer.writerow(["your", "header", "foo"])  # write header
        writer.writerows(data)
    
    # Read CSV file
    with open(caminho_arquivo) as fp:
        reader = csv.reader(fp)
        # next(reader, None)  # skip the headers
        data_read = [row for row in reader]
        x, y = 20, 20
        for row in data_read:
            for item in row:
                print(item.ljust(12), end='')
                textSize(24)
                text(item.ljust(12), x, y)
                pushStyle()
                textSize(12)
                text(str(type(item)), x, y + 32)
                popStyle()
                x += textWidth(item.ljust(12))
            y += 64
            x = 20
            print()
```

### Assuntos relacionados

* [Textos no programa, no console e na tela (*strings*)](strings_py.md)
* Se quiser ler mais sobre *Filie IO* na documentação do Python: [Python 2.7 Tutorial: Reading and Writing Files](https://docs.python.org/2/tutorial/inputoutput.html#reading-and-writing-files)


