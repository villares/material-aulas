# Lendo e escrevendo dados em arquivos CSV

# *Comma Separated Values*, um formato de intercâmbio primitivo, porém ainda útil

Vamos agora falar sobre como ler e escrever dados simples em um arquivo CSV, o nome vem de *Comma Separated Values*, isto é, um arquivo texto com valores separados por vígula (mas às vezes se usam outros separadores como tabulções, no que teoricamente deveriam ser um TSV...).  Tanto o Processing como o a biblioteca padrão do Python tem ferramentas para ajudar a lidar com este formato.

```
sketch_csv(pasta/folder do sketch)
  L  sketch_csv.py (o arquivo do seu programa)
  L  data (uma pasta/folder)
       L  dados.csv (o arquivo CSV)
```

Conteúdo do aquivo [`dados.csv`](assets/dados.csv):

```
nome, valor, area, largura, comprimento, x, y
A1, 800, 32, 2, 16, 0, 19
A3, 2520, 252, 14, 18, 2, 17
...
```
Exemplo que lê o arquivo

```python
import csv

with open('dados.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['nome'], row['valor'])

print(row)
```

# Assuntos relacionados

* [Textos no programa, no console e na tela(*strings*)](strings_py.md)
* Se quiser ler mais sobre CSV na documentação do Python: [`csv` — CSV File Reading and Writing](https://docs.python.org/3/library/csv.html)
