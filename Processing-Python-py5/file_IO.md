# Lendo e escrevendo texto em arquivos (*file IO*) [REVISAR]

## Entrada (*input*) e saída (*output*) de dados em arquivos texto

Nosso primeiro exemplo vai ser sobre como ler linhas de texto(*strings*) de um arquivo texto(*text file*).

O arquivo `frutas.txt` vai ficar dentro da pasta `/ data /` dentro  do seu sketch:
```
sketch_2020_05a(pasta/folder do sketch)
  L  sketch_2020_05a.py  (arquivo com o código)
  L  data                (pasta/folder)
       L  frutas.txt     (arquivo texto)
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
A leitura dos dos dados pode ser feita no Python com o gerenciador de contexto `with open(____) as ____:`  que cuida de fechar o arquivo depois de encerrada a leitura.

```python
# No Python - exemplo mais universal
path_arquivo = sketch_path() / 'data' / 'frutas.txt'
with open(path_arquivo, 'r') as arquivo:
    linhas = arquivo.readlines()
```

Note que ler dados de um arquivo no computador é considerada uma operação relativamente lenta e não deve ser feita repetidas vezes dentro do `draw()` pois vai ser um disperdício e deixa o seu desenho ou animação lentos.

```python
def setup():
    size(400, 400)
    background(0)
    path_arquivo = sketch_path() / 'data' / 'frutas.txt'
    # precisa existir este arquivo senão vai acontecer um erro
    with open(path_arquivo, 'r') as arquivo:
        linhas = arquivo.readlines()
    fill(100, 100, 255)
    text_align(CENTER, CENTER)
    text_size(24)
    for linha in linhas:
        x, y=random(40, 360), random(20, 380)
        text(linha, x, y)
```

![resultado](assets/read_lines.png)

# [REVISAR REMOVER load_strings()]

## Escolhendo um arquivo para abrir

Usando o a função `select_input()`,  você permite que a pessoa escolha um arquivo para subsequente leitura, como no exemplo anterior, com `load_strings()`. É preciso passar dois argumentos: um texto para o título da janela de seleção, e o nome de uma função que será executada quano a pessoa terminar de selecionar o arquivo(ou cancelar a seleção).

```python
linhas = [
    "tecle 'o' para abrir um arquivo",
    "tecle 'a' para apagar a lista",
         ]

def setup():
    size(400, 400)

def draw():
    background(0)
    fill(100, 100, 255)
    text_align(LEFT, TOP)
    text_size(20)
    for i, linha in enumerate(linhas):
        x=10 + 120 * (i // 20)
        y=i * 19 - 380 * (i // 20)
        text(linha, x, y)

def key_pressed():
    if key == 'o':
        select_input("escolha um arquivo:", "select_file")
    if key == 'a':
        linhas[:]=[]
    if key == 's':
        save_frame("select_input.png")

def select_file(selection):
    if selection == None:
        print(u"Seleção cancelada.")
    else:
        path=selection.get_absolute_path()
        print("Arquivo selecionado: " + path)
        linhas.extend(load_strings(path))
```

![resultado](assets/select_input.png)

## Escrevendo texto em arquivos (e escolhendo onde salvar um arquivo)

De maneira análoga, podemos usar `save_strings()` para salvar em um arquivo do disco uma lista de * strings*. No exemplo abaixo usamos `select_output()` para disparar uma janela que pergunta o nome e local para salvar um arquivo.

```python
circulos=[]

def setup():
    size(400, 400)
    fill(100, 100, 255)
    print(u"Tecle 'W' para gravar e 'L' para carregar dados de um arquivo texto")

def draw():
    background(0)
    for circulo in circulos:
        x, y, tamanho=circulo
        ellipse(x, y, tamanho, tamanho)

def mouse_dragged():
    circulo=(mouse_x, mouse_y, random(20, 40))
    circulos.append(circulo)

def key_pressed():
    if key == 'w' or key == 'W':
        # Argumentos: título, função chamada na conclusão
        select_output("Salvar como:", "salvar_circulos")
    if key == 'l' or key == 'L':
        select_input("Escolha um arquivo:", "carregar_circulos")
    if key == ' ':
        circulos[:]=[]

def salvar_circulos(arquivo):
    if arquivo == None:
        print("Gravação cancelada.")
    else:
        caminho_arquivo=arquivo.get_absolute_path()
        if not caminho_arquivo.endswith('.txt'):
            caminho_arquivo += '.txt'
        linhas=[]
        for circulo in circulos:
                x, y, tamanho=circulo
                linhas.append(u'{} {} {}'.format(x, y, tamanho))
        save_strings(caminho_arquivo, linhas)

def carregar_circulos(arquivo):
    if arquivo == None:
        print(u"Seleção cancelada.")
    else:
        caminho_arquivo=arquivo.get_absolute_path()
        print("Arquivo selecionado: " + caminho_arquivo)
        linhas=load_strings(caminho_arquivo)
        for linha in linhas:
            str_x, str_y, str_tamanho=linha.split()
            circulo=float(str_x), float(str_y), float(str_tamanho)
            circulos.append(circulo)
```
![circulos](assets/output.png)

Veja um trecho do arquivo gerado pelo exemplo[`output.txt`](assets/output.txt)
```
68 120 37.5507659912
71 98 32.7605819702
78 83 26.2493400574
84 71 36.1811676025
87 63 35.6623039246
89 59 37.2014465332
90 56 37.5425949097
91 56 23.1710891724
93 55 34.2703857422
98 50 31.6832389832
103 47 33.4321708679
...
```
# Escrevendo em arquivos no Python sem a ajuda do Processing

A maneira mais 'universal' em Python de se escrever em um arquivo texto é usando `open(caminho_arquivo, modo)`, que fornece um objeto com o método `.write()`.

O mais recomendado é usar um chamado 'gerenciador de contexto', fazendo um bloco indentado que começa com `with open(caminho_arquivo, modo) as objeto_arquivo: `. Se não usar o `with open(...: ` você precisa cuidar de 'fechar' o aquivo com `.close()` depois de ler ou escrever, e ainda corre o risco do arquivo ficar aberto se o seu programa encerrar no meio do caminho.

Veja o caso de gravar os dados dos círculos no exemplo anterior como ficaria:

```python
from codecs import open  # para poder usar unicode="utf-8" no Python 2
with open(caminho_arquivo, "w", encoding="utf-8") as file:
    for circulo in circulos:
        x, y, tamanho=circulo
        file.write(u'{} {} {}'.format(x, y, tamanho))
 ```


## Assuntos relacionados

* [Textos no programa, no console e na tela(*strings*)](strings_py.md)
* Se quiser ler mais sobre * Filie IO * na documentação do Python: [Python 2.7 Tutorial: Reading and Writing Files](https://docs.python.org/2/tutorial/inputoutput.html  # reading-and-writing-files)
