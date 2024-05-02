
# Lendo todas as imagens de uma pasta

![exemplo de grade de imagens](https://raw.githubusercontent.com/villares/material-aulas/master/Processing-Python/assets/muitas_imagens.png)

> Exemplo de execução carregando 110 imagens medievais coletadas pelo artista e educador[Daniel Seda](https://www.danielseda.com/).

Tendo visto previamente como [ler e usar imagens de arquivos externos](imagens_externas.md) com `load_image()`, e a estrutura de dados lista (`list`), neste exemplo mais avançado vamos permitir que a pessoa escolha um diretório (pasta/*folder*) e o *sketch* vai carregar todas as imagens nela encontradas e mostrá-las em uma grade. Vamos usar uma função do py5 que pede ao sistema operacional que abra uma janela na interface gŕafica para a seleção de uma pasta no sistema de armazenagem de arquivos.

**Cuidado!** Carregar na memória um grande número de imagens pesadas pode fazer o seu programa quebrar... neste caso pode ser interessante gerar e armazernar apenas *thumbnails*, versões reduzidas das imagens, um assunto que não é abordado aqui.


## A função `select_folder()` do py5

A seleção da pasta começa com uma chamada da função `select_folder()`, quando pressioanada a tecla 'o' (na função de evento `key_pressed()`).

```python
def setup():
    size(880, 550)

def draw():
    background(0)
    # aqui vai ter o código que põe as imagens na tela

def key_pressed():
    if key == 'o':
        select_folder('Selecione uma pasta', adicionar_imagens)

```

Note que o primeiro argumento de `select_folder()` é `'Selecione uma pasta'` o texto (*string*) que vai como título da janela de seleção. O segundo argumento `adicionar_imagens` é mais curioso, trata-se de uma referência a uma função que será chamada quando a pessoa terminar de interagir com a janela de seleção de pastas apresentada pelo sistema operacional. 

Estamos passando uma função como argumento de outra, em  uma estratégia conhecida como "função de retorno" ou, em inglês, *callback*. Repare que a referência ao "objeto função" que é passado como argumento da função `select_folder()` é o nome da função, sem aspas, mas sem os parenteses `()`, os parenteses fariam disso uma chamada da função (ela seria executada imediatamente neste ponto do código).

Na estratégia com *callback* uma função definida é chamada para nós quando algum evento acontece. Neste nosso exemplo, a função `adicionar_imagens()` é chamada no envento do encerramento da janela de selecionar pastas. Note que a abertura da janela para selecionar pastas é iniciada com a execução de `select_folder()`, mas o momento do encerramento depende da pessoa usando o programa e não sabemos quanto tempo vai levar para acontecer.

## A função `adicionar_imagens()`

Então, é preciso definir uma função `adicionar_imagens()` que será executada só quando a pessoa terminou de escolher uma pasta ou se tiver cancelado o processo, ela precisa ter um parâmetro, `caminho_pasta`, que recebe o caminho da pasta selecionada ou o valor especial `None` (se a pessoa fechou a janela sem selecionar uma pasta).

Nossa função vai acrescentar numa lista global chamada `imagens` tuplas com dois elementos, o nome do arquivo e a imagem carregada com `load_image()`, um string e um objeto do tipo `Py5Image` com os dados da imagem, respectivamente.

```python
def adicionar_imagens(caminho_pasta):
    if caminho_pasta == None:
        print('Seleção cancelada.')
    else:
        print(f'Pasta selecionada: {caminho_pasta.name}')
        for caminho_imagem in lista_imagens(caminho_pasta):
            img = load_image(caminho_imagem)  # carrega a imagem na memória
            print(f'imagem {caminho_imagem.name} carregada.')
            imagens.append((caminho_imagem.name, img))  # acrescenta uma tupla à lista imagens
        print(f'Número de imagens: {len(imagens)}')
```

Saiba que o código que cuida da janela do sistema operacional para escolhermos a pasta, e também o código da função `adicionar_imagens()`, chamada em seguida, são executados em linhas de execução (*threads*) separadas do *sketch* principal, isto é correm em separado, e por conta disso não interrompem execução do `draw()`, o chamado 'laço principal de repetição' do Processing.

O carregamento das imagens é um procedimento razoavelmente lento e por isso é possível vê-las aparecendo aos poucos na tela, conforme são acrescentadas na lista `imagens` pela execução do laço `for` em `adicionar_imagens()`.

## Uma estrutura de dados para receber as imagens

Atenção, note que dentro de `adicionar_imagens()` usamos `imagens.append(...)`, por isso precisamos criar essa lista `ìmagens` para guardar os dados dos arquivos encontrados, fazemos isso antes do `setup()` que criando uma lista vazia e apontando uma variável global chamada `imagens` para ela:

```python

imagens = []  # esta lista vai receber tuplas assim: (nome_da_imagem, objeto_py5image) 

def setup():
    size(880, 550)

def draw():
    background(0)
    ...
```

## A função auxiliar `lista_imagens()`

Uma boa parte da solução da nossa tarefa, na verdade, está encapsulada em `lista_imagens()`, função que usamos em `adicionar_imagens()` e que recebe o caminho da pasta selecionada no parâmetro `caminho_pasta`. 

Nessa função usamos uma tupla chamada `extensoes_validas`, contendo as extensões que vamos considerar para tratar os arquivos como arquivos de imagem, e criamos a lista `lista_caminhos`, que começa vazia e será devolvida no final da função (contendo caminhos para imagens, se tudo der certo). 

Em seguida, checamos com um `if` se o caminho obtido é um caminho de diretório válido (`caminho_pasta.is_dir()` devolve `True`) e a função deve então percorrer o gerador `caminho_pasta.iterdir()`, verificando quais terminam com extensão de imagem e nesse caso, adicionando o caminho do arquivo à lista `lista_caminhos`.

No final devolvemos com `return lista_caminhos` a lista, que estará vazia caso o diretório não seja válido ou não contenha nenhuma imagem, ou então `lista_caminhos` vai conter os caminhos dos arquivos de imagem, que vamos usar depois com `load_image()`:

```python
def lista_imagens(caminho_pasta):
    extensoes_validas = ('.jpg', '.png', '.jpeg', '.gif', '.tif', '.tga')
    lista_caminhos = []  # esta lista vai receber caminhos de arquivos com extensão de imagem
    if caminho_pasta.is_dir():
        for caminho_imagem in caminho_pasta.iterdir():
            if caminho_imagem.is_file() and caminho_imagem.suffix.lower() in extensoes_validas:
                lista_caminhos.append(caminho_imagem)
    else:
        print('Devolvendo uma lista vazia pois não foi fornecida uma pasta válida!')
    return lista_caminhos
```

## O código de um exemplo completo

Aqui vai então uma versão funcional do sketch, contendo a parte que desenha uma grade de imagens no `draw()` com os itens da lista `imagens`:

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

def adicionar_imagens(caminho_pasta):
    """Callback que será chamado pela função select_folder() do py5"""
    if caminho_pasta == None:
        print('Seleção cancelada.')
    else:
        print(f'Pasta selecionada: {caminho_pasta.name}')
        for caminho_imagem in lista_imagens(caminho_pasta):
            img = load_image(caminho_imagem)
            print(f'imagem {caminho_imagem.name} carregada.')
            imagens.append((caminho_imagem.name, img))
        print(f'Número de imagens: {len(imagens)}')

def lista_imagens(caminho_pasta):
    """
    Devolve uma a lista dos caminhos (objetos pathlib.Path) dos arquivos com 
    extensões de imagem no nome, encontrados iterando itens de `caminho_pasta`.
    """
    caminho_pasta = Path(caminho_pasta) # Garante um objeto pathlib.Path
    extensoes_validas = ('.jpg', '.png', '.jpeg', '.gif', '.tif', '.tga')
    lista_caminhos = []
    if caminho_pasta.is_dir():
        for caminho_imagem in caminho_pasta.iterdir():
            if caminho_imagem.is_file() and caminho_imagem.suffix.lower() in extensoes_validas:
                lista_caminhos.append(caminho_imagem)
    else:
        print('Devolvendo uma lista vazia pois não foi fornecida uma pasta válida!')
    return lista_caminhos
```

### Uma versão mais robusta de `adicionar_imagens()`

Se por acaso na pasta com imagens que estamos examinando houver algum arquivo que não é uma imagem mas tem extensão de imagem, ou se houver uma imagem "corrompida", a operação da funçao `load_image()` vai falhar, e pode *levantar uma exceção*. Podemos *tratar essa exceção*, usando uma estrutura com um bloco `try:` e outro `except ... :` como na função modificada a seguir:

```python
def adicionar_imagens(caminho_pasta):
    """Callback que será chamado pela função select_folder() do py5"""
    if caminho_pasta == None:
        print('Seleção cancelada.')
    else:
        print(f'Pasta selecionada: {caminho_pasta.name}')
        for caminho_imagem in lista_imagens(caminho_pasta):
            try:
                img = load_image(caminho_imagem)
                print(f'imagem {caminho_imagem.name} carregada.')
                imagens.append((caminho_imagem.name, img))
            except Exception as erro:
                print(erro)
                break # mais seguro, interrompe mais carregamentos
        print(f'Número de imagens: {len(imagens)}')
```

Para entender melhor o funcionamento de `try:` e  `except ... :` na função `adicionar_imagens()`, você pode ler:
- [Allen Downey explicando as exceções em Python no contexto de leitura e escrita de arquivos](https://penseallen.github.io/PensePython2e/14-arquivos.html#145---captura-de-exceções)
- [O problema da divisão por zero (e um pouco sobre tratamento de exceções)](https://abav.lugaralgum.com/material-aulas/Processing-Python-py5/divisao.html)
- [Tratamento de exceções na documentação oficial do Python](https://docs.python.org/pt-br/3/tutorial/errors.html#exceptions) 

### Uma variação para o desenho da grade

Uma variante do `draw()` que permite largura variável das imagens, fixando a altura, como no exemplo anterior, mas deslocando na horizontal:

```python
def draw():
    background(0)
    # Desenha `imagens` em filas de altura `h`,
    #  deslocando na horizontal a largura de cada imagem.
    x = y = 0
    for nome, img in imagens:
        fator = h / img.height
        if x + img.width * fator > width:
            x=0
            y += h
        image(img, x, y, img.width * fator, img.height * fator)
        x += img.width * fator
```

### Uma versão recursiva da função `lista_imagens()`

Esta versão procura imagens em uma pasta fornecida como argumento, mas também em sub-pastas da pasta!

```python
def lista_imagens(caminho):
    """
    Devolve uma a lista dos caminhos (objetos pathlib.Path) dos arquivos com 
    extensões de imagem no nome, encontrados iterando itens do diretório
    passado como argumento para o parâmetro `caminho`, incluindo itens dos
    sub-diretórios.
    """
    extensoes_validas = ('.jpg', '.png', '.jpeg', '.gif', '.tif', '.tga')
    if caminho.is_dir():
        lista_caminhos = []
        for item in caminho.iterdir():
            lista_caminhos.extend(lista_imagens(item))
        return lista_caminhos
    elif caminho.is_file() and caminho.suffix.lower() in extensoes_validas:
        return [caminho]
    else:
        return []
```

## Outros assuntos relacionados

- Estrutura de pixels das imagens em [Pixels e imagens](pixels.md)
- [Lendo e escrevendo texto em arquivos (*file IO*)](file_IO.md)
