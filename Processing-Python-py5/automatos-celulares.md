# Autômatos Celulares (*Celular Automata*)

# O que são os autômatos celulares, de onde veio essa ideia?

Criados inicalmente como ferramentas de exploração teórica/matemática, robôs auto-replicantes imaginados por von Neuman ou crescimento de cristais, mas também uma atividade lúdica, tornada relativamente popular pela coluna do Martin Gardner de recreações matemáticas na revista Scientific America, que apresentou o jogo da vida do Conway. Pesquisados em profundidade por Wolfram.

Foram adotados por artista visuais que se interessam por computação por conta dos padrões interessantes que geram e o impacto da sua evolução(isso de lembrarem elemento vivos). Neste material didático os olhamos deste ponto de vista, assim como do ponto de vista didático(para quem quer aprender/ensinar programação), exploratório, lúdico e estético. Talvez um pouco histórico-cultural também...

Mais recentemente pesquisadores de urbanismo os estudam como uma ferramenta de simulação, aplicando-os na análise da evolução de trechos de cidade.

# Alguns exemplos
- "Autômato Celular Elementar" de Wolfram(1D)
- Jogo da vida de Conway(*Conway's game of life*)
  - Exemplo do Jogo da vida de Conway com tabuleiro de lista de listas
  - Exemplo do Jogo da vida de Conway com tabuleiro infinito em um conjunto(set) e a biblioteca py5

# Um trecho do capítulo sobre autômatos celulares do *Nature of Code* de
# Daniel Shiffman

Um autômato celular(CA) é um modelo de um sistema de objetos "celulares" com as seguintes características:

- As células vivem em uma grade. (Os exemplos a seguir serão em uma e duas dimensões neste capítulo, embora um autômato celular possa existir em qualquer número finito de dimensões.)

- Cada célula tem um estado. O número de possibilidades de Estado é tipicamente finito. O exemplo mais simples tem as duas possibilidades de 1 e 0 (também referidas como "on" e "off" ou "viva" e "morta").

- Cada célula tem um bairro. Isso pode ser definido de várias maneiras, mas é tipicamente uma lista de células adjacentes.


![image](https://user-images.githubusercontent.com/88688270/138708935-cc5a1244-28c7-4fe8-ba6c-c263d78b0d14.png)


# Autômato Celular Elementar

Os exemplos neste capítulo começarão com uma simulação do trabalho de Wolfram. Para entender o CA elementar de Wolfram, devemos nos perguntar: "Qual é o autômato celular mais simples que podemos imaginar?" O que é emocionante sobre essa pergunta e sua resposta é que, mesmo com o CA mais simples imaginável, veremos as propriedades de sistemas complexos em ação.
Quais são os três elementos-chave de um CA?

**_1) Grade._** A grade mais simples seria unidimensional: uma linha de células.

![image](https://user-images.githubusercontent.com/88688270/138709430-77179e96-0537-4f5b-894a-8beec76e16a6.png)


** _2) Estados._** O conjunto mais simples de estados(além de ter apenas um estado) seriam dois estados: 0 ou 1.

![image](https://user-images.githubusercontent.com/88688270/138709446-6c68a081-dc9d-4be6-add5-b83b5f46b13a.png)


** _3) Bairro._** O bairro mais simples em uma dimensão para qualquer célula seria a própria célula e seus dois vizinhos adjacentes: um para a esquerda e outro para a direita.

![image](https://user-images.githubusercontent.com/88688270/138709466-fa61542f-a6b5-4634-afba-2f5a1e057d74.png)


Então começamos com uma linha de células, cada uma com um estado inicial(digamos que é aleatório), e cada uma com dois vizinhos. Teremos que descobrir o que queremos fazer com as células nas bordas(já que elas têm apenas um vizinho cada), mas isso é algo que podemos resolver mais tarde.

![image](https://user-images.githubusercontent.com/88688270/138709799-f3c06fe5-99da-4a90-bf79-63eacb849b27.png)


Ainda não discutimos, no entanto, qual é talvez o detalhe mais importante de como os autômatos celulares funcionam: o tempo. Não estamos realmente falando sobre o tempo real aqui, mas sobre o CA viver durante um período de tempo, que também poderia ser chamado de geração e, no nosso caso, provavelmente se referirá à contagem de quadros de uma animação. Os números acima nos mostram que o CA no momento é igual a 0 ou geração 0. As perguntas que temos que nos fazer são: Como calcular os estados para todas as células da geração 1? E geração 2? E assim por diante.


![image](https://user-images.githubusercontent.com/88688270/138709822-828b47bd-4436-41f7-806e-34f84b82a27a.png)


Digamos que temos uma célula individual no AC, e vamos chamá-la de CELL. A fórmula para calcular o estado do CELL a qualquer momento t é a seguinte:

**_Estado celular no tempo t=f(bairro cell no tempo t - 1)_**

Em outras palavras, o novo estado de uma célula é uma função de todos os estados do bairro da célula no momento anterior(ou durante a geração anterior). Calculamos um novo valor estatal olhando para todos os estados vizinhos anteriores.

![image](https://user-images.githubusercontent.com/88688270/138710778-647e9cbd-c37d-428e-bc5b-d326edc1d80c.png)

Agora, no mundo dos autômatos celulares, há muitas maneiras de calcular o estado de uma célula a partir de um grupo de células. O novo estado de um pixel(ou seja, sua cor) é a média de todas as cores de seus vizinhos. Com o CA elementar de Wolfram, no entanto, podemos realmente fazer algo um pouco mais simples e aparentemente absurdo: Podemos olhar para todas as configurações possíveis de uma célula e seu vizinho e definir o resultado do estado para cada configuração possível.

Temos três células, cada uma com um estado de 0 ou 1. De quantas maneiras possíveis podemos configurar os estados? Se você ama binário, você notará que três células definem um número de 3 bits, e quão alto você pode contar com 3 bits? Até 8.

![image](https://user-images.githubusercontent.com/88688270/138711227-9505cca9-ce72-4dbc-9b47-b75b99f8ad10.png)

Uma vez definidos todos os bairros possíveis, precisamos definir um resultado(novo valor estadual: 0 ou 1) para cada configuração do bairro.

![image](https://user-images.githubusercontent.com/88688270/138711341-e748849e-9206-4136-92bb-da7f328a4a5a.png)

O modelo wolfram padrão é começar a geração 0 com todas as células tendo um estado de 0, exceto para a célula média, que deve ter um estado de 1.

![image](https://user-images.githubusercontent.com/88688270/138711395-c795b03f-dc2b-43c1-b86e-0d23ac293d38.png)

Referindo-se ao ruleset acima, vamos ver como uma determinada célula(vamos escolher a central) mudaria de geração 0 para geração 1.

![image](https://user-images.githubusercontent.com/88688270/138711439-b8964ed4-8d19-4bc3-8932-82c11a9db0bf.png)

Tente aplicar a mesma lógica em todas as células acima e preencha as células vazias.
Agora, vamos passar de apenas uma geração e colorir as células — 0 significa branco, 1 significa preto — e empilhar as gerações, com cada nova geração aparecendo abaixo da anterior.

![image](https://user-images.githubusercontent.com/88688270/138711566-64d90b32-eecd-43a6-a7fe-83c7fb1b60a4.png)

A forma de baixa resolução que estamos vendo acima é o "triângulo Sierpiński". Nomeado em homenagem ao matemático polonês Wacław Sierpiński, é um padrão fractal que examinaremos no próximo capítulo. Isso mesmo: este sistema incrivelmente simples de 0s e 1s, com pequenos bairros de três células, pode gerar uma forma tão sofisticada e detalhada quanto o triângulo Sierpiński. Vamos olhar para ele novamente, apenas com cada célula um único pixel de largura para que a resolução seja muito maior.

![image](https://user-images.githubusercontent.com/88688270/138711649-d4ccbfdf-1650-46a7-89c7-40d64498ab8e.png)

Este resultado em particular não aconteceu por acidente. Eu escolhi este conjunto de regras por causa do padrão que ele gera. Dê uma olhada na Figura 7.8 mais uma vez. Observe como existem oito configurações possíveis de bairro; por isso, definimos um "ruleset" como uma lista de 8 bits.

Assim, esta regra em particular pode ser ilustrada da seguinte forma:

![image](https://user-images.githubusercontent.com/88688270/138711696-aaa167c3-e9ca-47d7-b800-585e25a62908.png)

Oito 0s e 1s significa um número de 8 bits. Quantas combinações de oito 0s e 1 existem? 256. É assim como definimos os componentes de uma cor RGB. Temos 8 bits para vermelho, verde e azul, o que significa que fazemos cores com valores de 0 a 255 (256 possibilidades).


# O Jogo da Vida

Tendo como base o conceito de autômatos celulares, vamos compor o Jogo da Vida, que é o princípio do Campo Minado e de simulações de crescimento de bactérias.

Primeiro, é necessário criar um "tabuleiro", ou um campo. Esse campo vai atender dois valores: 0 e 1, ou "vivo" e "morto"

```python
tam=20
board=[]

def setup():
    global n_colunas, n_linhas
    size(500, 500)
    stroke(255, 0, 0)
    n_colunas=int(width / tam)  # calcula numeto de colunas
    n_linhas=int(height / tam)  # calcula numero de linhas
    # ivnentando o tabuleiro
    for _ in range(n_colunas):
        board.append([0] * n_linhas)  # jogando uma coluna para dentro
    # sorteando algumas celulas vivas (posição com valor 1)
    for c in range(n_colunas):  # 0, 1, 2, ... n_colunas - 1
        for l in range(n_linhas):  # 0, 1, 3, ... n_colunas - 1
            if random(100) < 15:
                board[c][l]=1

def draw():
    background(0, 0, 100)
    for c in range(n_colunas):  # sequência de números para colunas
        for l in range(n_linhas):
            if board[c][l] == 1:
                fill(255)
                rect(c * tam, l * tam, tam, tam)
            fill(255, 0, 0)
            text(vizinhos_vivos(c, l), c * tam + tam / 2, l * tam + tam / 2)
            # é uma grade que começamos a desenhar

def vizinhos_vivos(i, j):
    viz=((-1, -1), (-1, 0), (-1, -1), (0, -1),
           (0, 1), (1, -1), (1, 0), (1, 1))
    vivos=0
    for oi, oj in viz:
        estado_vizinha=board[(i + oi) % n_colunas][(j + oj) % n_linhas]
        vivos=vivos + estado_vizinha
    return vivos
```

![image](https://user-images.githubusercontent.com/88688270/138721627-4f69781c-9cd3-4f7a-9f2e-16b466fce1d1.png)

Para entender melhor, basta analisar a imagem a seguir. O zero central(com fundo branco) é uma célula 'viva', mas que não possui células vivas ao seu redor(por isso o valor zero). As células ao seu redor são células 'mortas' que sinalizam que tem uma ou duas células vivas.

![image](https://user-images.githubusercontent.com/88688270/138721737-544c50e6-27a4-47db-b334-d2ad2d8bfc72.png)


Agora, para entender melhor como funcionam as gerações anteriormente citadas, no código a seguir, têm-se uma geração 0, que consecutivamente forma uma nova geração(geração 1), que formará uma outra, e assim por diante.

```python
tam=5    # cria variavel global tam (tamanho das celulas)
board=[]  # lista vazia que vai ser o tabuleiro

def setup():
    global n_colunas, n_linhas
    size(600, 600)
    # stroke(255, 0, 0)  # cor de traço
    n_colunas=int(width / tam)  # calcula numero de colunas
    n_linhas=int(height / tam)  # calcula numero de linhas
    # inventando o tabuleiro
    for _ in range(n_colunas):
        board.append([0] * n_linhas)  # jogando uma coluna pra dentro
    # sorteando algumas celulas vivas (posição com valor 1)
    for c in range(n_colunas):  # 0, 1, 2, ... n_colunas - 1
        for l in range(n_linhas):  # 0, 1, 3, ... n_linhas - 1
            if random(100) < 15:
                board[c][l]=1

def draw():
    background(0, 0, 100)
    for c in range(n_colunas):
        for l in range(n_linhas):
            if board[c][l] == 1:
                fill(255)
                rect(c * tam, l * tam, tam, tam)
            # fill(255, 0, 0)
            # text(vizinhos_vivos(c, l),
            #      c * tam + tam / 2, l * tam + tam / 2)
    if frameCount % 5 == 0:  # 1, 2, 3, 4, 5, 6, 7,
        atualizar_tabuleiro()

def atualizar_tabuleiro():
    global board
    next_board=[]
    for _ in range(n_colunas):
        next_board.append([0] * n_linhas)
    for c in range(n_colunas):
        for l in range(n_linhas):
           vivos=vizinhos_vivos(c, l)
           if vivos == 3:
               next_board[c][l]=1
           elif vivos < 2 or vivos > 3:
               next_board[c][l]=0
           else:
               next_board[c][l]=board[c][l]
    board=next_board

def vizinhos_vivos(i, j):
    viz=((-1, -1), (-1, 0), (-1, 1), (0, -1),
                  (0, 1), (1, -1), (1, 0), (1, 1))
    vivos=0
    for oi, oj in viz:
        estado_vizinha=board[(i + oi) % n_colunas][(j + oj) % n_linhas]
        vivos=vivos + estado_vizinha
    return vivos
```

** BIBLIOGRAFIA **
SHIFFMAN, Daniel. _Cellular Automata_. In: < https://natureofcode.com/book/chapter-7-cellular-automata/>.
