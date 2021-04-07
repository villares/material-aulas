## Lendo e escrevendo dados em arquivos (*file IO*)

### Entrada (*input*) e saída (*output*) de dados em arquivos

Nosso primeiro exemplo vai ser sobre como ler e escrever dados simples em um arquivo CSV (*comma separated values*, um arquivo texto com valores separados por vígula).

O arquivo `dados.csv` vai ficar dentro da pasta `/data/` dentro  do seu sketch:

```
sketch_2020_05a                (pasta/folder do sketch)
  L  sketch_2020_05a.pyde      (arquivo com o código)
  L  data                      (pasta/folder)
       L  dados.csv           (arquivo texto)
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

A leitura dos dos dados pode ser feita no Python de maneira mais 'universal', o que é útil saber para poder fazer em outros contextos de uso de Python:

```python
# No Python - exemplo mais universal
from io import open as io_open # melhor para ler unicode no Python 2 
with io_open("data/dados.txt",'r') as file:
    linhas = file.readlines()
```

Ou usando uma função bem simples do Processing chamada `loadStrings()`:

```python
# No Processing - mais específico - não use antes do setup()!
linhas = loadStrings("nomes.txt")  # dados.txt na pasta /data/
```

Note que em ambos os casos, ler dados de um arquivo no computador é considerada uma operação relativamente lenta e não deve ser feita repetidas vezes dentro do `draw()` pois vai ser um disperdício e deixa o seu desenho ou animação lentos.

```python
def setup():
    size(400, 400)
    background(0)
    # dados.txt na pasta /data/
    linhas = loadStrings("fdadostxt")  

    fill(100, 100, 255)
    textAlign(CENTER, CENTER)
    textSize(24)
    for linha in linhas:
        x, y = random(40, 360), random(20, 380)             
        text(linha, x, y)    
```

![resultado](assets/read_lines.png)

#### Escrevendo em arquivos no Python sem a ajuda do Processing

A maneira mais 'universal' em Python de se escrever em um arquivo texto é usando `open(caminho_arquivo, modo)`, que fornece um objeto com o método `.write()`.

O mais recomendado é usar um chamado 'gerenciador de contexto', fazendo um bloco indentado que começa com `with open(caminho_arquivo, modo) as objeto_arquivo:`. Se não usar o `with open(... :` você precisa cuidar de 'fechar' o aquivo com `.close()` depois de ler ou escrever, e ainda corre o risco do arquivo ficar aberto se o seu programa encerrar no meio do caminho.

Veja o caso de gravar os dados dos círculos no exemplo anterior como ficaria:

```
with open(caminho_arquivo, 'w') as file:
    for circulo in circulos:
        x, y, tamanho = circulo
        file.write(u'{} {} {}'.format(x, y, tamanho))
```

### Assuntos relacionados

* [Textos no programa, no console e na tela (*strings*)](strings_py.md)
* Se quiser ler mais sobre *Filie IO* na documentação do Python: [Python 2.7 Tutorial: Reading and Writing Files](https://docs.python.org/2/tutorial/inputoutput.html#reading-and-writing-files)        
