
# Lendo todas as imagens de uma pasta

![exemplo de grade de imagens](https://raw.githubusercontent.com/villares/material-aulas/master/Processing-Python/assets/muitas_imagens.png)

> Exemplo de execução carregando 110 imagens medievais coletadas pelo artista e educador[Daniel Seda](https://www.danielseda.com/).

Tendo visto previamente como [ler e usar imagens de arquivos externos](imagens_externas.md) com `load_image()`, e a estrutura de dados lista(`list`) neste exemplo mais avançado vamos permitir que a pessoa escolha uma pasta e o *sketch* vai carregar todas as imagens nela encontradas.

A seleção da pasta começa com uma chamada da função `select_folder()`, quando pressioanada a tecla 'o' (na função de evento `key_pressed()`).

```python
def setup():
    size(880, 550)

def draw():
    background(0)
    # aqui vai ter o código que põe as imagens na tela

def key_pressed():
    if key == 'o':
        select_folder("Selecione uma pasta", adicionar_imagens)

```

Note que o primeiro argumento de `select_folder()` é `"Selecione uma pasta"` o texto(*string*) que vai como título da janela de seleção. O segundo argumento `adicionar_imagens` é mais curioso, trata-se do nome de uma função que será chamada quando a pessoa terminar de interagir com a janela de seleção de pasta(diretório / *folder*). Isso é uma estratégia conhecida em programação como designar uma "função de retorno" ou, em inglês, *callback*.

Na estratégia com *callback* uma função definida é chamada para nós quando algum evento acontece. Neste nosso caso, a função `adicionar_imagens()` é chamada no encerramento da janela de selecionar pastas (esta parte de abrir a janela para selecionar pastas é iniciada com a execução de `select_folder()`, mas o momento do encerramento depende da pessoa usando o programa).

É preciso criar uma variável global para guardar as informações dos arquivos encontrados, fazemos isso com esta linha antes do `setup()` que cria uma lista vazia e aponta o nome `imagens` para ela:

```python

imagens = []

def setup():
    size(880, 550)

def draw():
    background(0)
    ...
```

A função `adicionar_imagens()` é executada só quando a pessoa terminou de escolher uma pasta ou se tiver cancelado o processo, ela tem um parâmetro `dir_path` que recebe a pasta selecionada ou o valor especial `None` (se a pessoa fechou a janela sem selecionar uma pasta):

```python
def adicionar_imagens(dir_path):
    if dir_path == None:
        print("Seleção cancelada.")
    else:
        print(f'Pasta selecionada: {dir_path}')
        for file_path in lista_imagens(dir_path):
            img = load_image(file_path)
            print(f'imagem {file_path.name} carregada.')
            imagens.append((file_path.name, img))
        print(f'Número de imagens: {len(imagens)}')
```

Saiba que o código que cuida da janela do sistema operacional para escolhermos a pasta, e também o código da função `adicionar_imagens()`, chamada em seguida, são executados em linhas de execução(*threads*) separadas do *sketch* principal, isto é correm em separado, e por conta disso não interrompem execução do `draw()`, o chamado 'laço principal de repetição' do Processing.

O carregamento das imagens é um procedimento razoavelmente lento e por isso é possível vê-las aparecendo aos poucos na tela, conforme são acrescentadas na lista `imagens` pela execução do laço `for` em `adicionar_imagens()`.

Uma boa parte da solução da nossa tarefa, na verdade, está encapsulada em `lista_imagens()`, função que usamos em `adicionar_imagens()`. Ela recebe o caminho da pasta selecionada (*path*) e devolve uma lista com tuplas dos nomes dos arquivos das imagens e o caminho (*path*) delas para ser usado no `load_image()`:

```python
def lista_imagens(data_path):
    data_path = Path(data_path) # Garante um objeto pathlib.Path
    img_ext = ('jpg', 'png', 'jpeg', 'gif', 'tif', 'tga')
    try:
        f_list = [item for item in data_path.iterdir()
                  if item.is_file() and item.suffix.lower()[1:] in img_ext]
    except Exception as e:
        print(e)
        return []
    return f_list
```

Não vamos entrar em detalhes aqui, mas você pode querer ler mais sobre [compreensão de listas](https://panda.ime.usp.br/pensepy/static/pensepy/09-Listas/listas.html#list-comprehensions) (a maneira compacta de produzir uma lista usada para criar a `f_list`) e [tratamento de exceções](http://turing.com.br/pydoc/3.8/tutorial/errors.html#excecoes) (o trecho dentro dentro de `try:` e  `except... :`) para entender melhor a função `lista_imagens()`.

Por fim, aqui vai o código completo do sketch, contendo a parte que desenha uma grade de imagens no `draw()` com os itens da lista `imagens`:

```python

imagens = []
w, h = 80, 55  # largura e altura do espaço para cada imagem

def setup():
    global colunas, linhas
    size(880, 550)
    colunas, linhas = width // w, height // h
    print(f'Posições na grade: {colunas * linhas}')

def draw():
    background(0)
    # Desenha grade com `imagens` com colunas fixas de largura `w`,
    # imagens mais largas são sobrepostas pela pr
    contador = 0
    for c in range(colunas):
        x=c * w
        for l in range(linhas):
            y=l * h
            if contador < len(imagens):
                nome, img = imagens[contador]
                fator = h / img.height
                image(img, x, y, img.width * fator, img.height * fator)
                contador += 1
                
    if not imagens:   # if len(imagens) == 0:
        text_size(20)
        text("aperte 'o' para selecionar uma pasta\n"  # note ausência da vírgula aqui
             "aperte a barra de espaço para limpar a grade",
             100, 100)

def key_pressed():
    if key == 'o':
        select_folder("Selecione uma pasta", adicionar_imagens)
    if key == ' ':
        imagens[:] = []  # esvazia a lista de imagens
    if key == 'p':
        save_frame('####.png')

def adicionar_imagens(dir_path):
    if dir_path == None:
        print("Seleção cancelada.")
    else:
        print("Pasta selecionada: " + dir_path)
        for file_path in lista_imagens(dir_path):
            img = load_image(file_path)
            print(f'imagem {file_path.name} carregada.')
            imagens.append((file_path.name, img))
        print(f'Número de imagens: {len(imagens)}')

def lista_imagens(data_path):
    """
    Devolve uma a lista dos caminhos (objetos pathlib.Path) dos arquivos
    de imagem contidos na pasta `data_path` (ou na pasta /data/ próxima ao sketch).
    """
    data_path = Path(data_path) # Garante um objeto pathlib.Path
    img_ext = ('jpg', 'png', 'jpeg', 'gif', 'tif', 'tga')
    try:
        f_list = [item for item in data_path.iterdir()
                  if item.is_file() and item.suffix.lower()[1:] in img_ext]
    except Exception as e:
        print(e)
        return []
    return f_list
```

Uma variante do `draw()` que permite largura variável das imagens, fixando a altura, como no exemplo anterior, mas:

```python
def draw():
    background(0)
    # Desenha `imagens` em filas de altura 'h', deslocando na horizontal com
    # largura de cada imagem.
    x = y = 0
    for nome, img in imagens:
        print(img)
        fator = h / img.height
        if x + img.width * fator > width:
            x=0
            y += h
        image(img, x, y, img.width * fator, img.height * fator)
        x += img.width * fator
```

# Assuntos relacionados

- Estrutura de pixels das imagens em [Pixels e imagens](pixels.md)
- [Lendo e escrevendo texto em arquivos (*file IO*)](file_IO.md)
