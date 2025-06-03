# Material didático para usar com Thonny IDE e py5

## Elementos fundamentais

- 0.0.0 [O que é e como instalar o py5 e o Thonny IDE](https://abav.lugaralgum.com/como-instalar-py5/)
  - 0.0.1 [Sumário traduzido da referência do py5](sumario-referencia-py5.md)

### Primeiros passos
- 1.0.0 [Primeiros passos e desenho básico](desenho-basico_py.md)
- 1.0.1 [Variáveis](variaveis.md)
- 1.0.2 [Desenhando polígonos](poligonos_1.md)
- 1.0.3 [O que é indentação?](indentacao.md) - primeiro contato com `setup()` e `draw()`
- 1.0.4 [Mais sobre cores(RGB e HSB)](mais_sobre_cores.md)

### Execução condicional, aleatoriedade e movimento
- 1.1.0 [Execução condicional (`if`/`else`)](condicionais_py.md), operadores relacionais e operadores lógicos
- 1.1.1 [Mais movimento e interatividade com `setup()` e `draw()`](setup_draw.md)
- 1.1.2 [Qual a diferença entre `=` (atribuição) e `==` (comparação)?](atribuicao-e-comparacao.md)
- 1.1.3 [Criando uma animação](movimento_py.md)
- 1.1.4 [Escopo de variáveis(local e global)](escopo_py.md)
- 1.1.5 [Aleatoriedade: `random` e números "sorteados"](aleatoriedade_1.md)
- 1.1.6 [Divisão por zero e o resto da divisão](divisao.md) 

### Definindo novas funções
- 1.2.0 [Definindo novas funções](funcoes_py.md)
- 1.2.1 [Funções com argumentos padrão(ou opcionais)](funcoes_2.md)
- 1.2.2 [Condições aninhadas e outras estruturas condicionais](condicionais_2.md)
- 1.2.3 [Modificando o sistema de coordenadas](transformacoes_coordenadas.md) com `translate()`, `rotate()`, `scale()` e mais!
- 1.2.4 [Funções recursivas](recursao_py.md) e a recursividade no seu desenho 
- 1.2.5 [Primeiros passos de desenho em 3D](desenho-3D.md) - `size(…, …, P3D)`

### Laços de repetição
- 1.3.0 [Repetição com laços `for`](lacos_py.md)
- 1.3.1 [Grades retangulares: filas e colunas de elementos](grades.md)
- 1.3.2 [Mais sobre sequências de elementos e fatias](mais_sequencias.md)
- 1.3.3 [Mais sobre polígonos](poligonos_2.md)
- 1.3.4 [Desenhando formas curvas](curvas.md)
- 1.3.5 [Laço de repetição com `while`](while.md)

### Tipos de valores
- 1.4.0 [Tipos de valores](tipagem_py.md) como texto (*strings*) e números inteiros (*int*) ou de ponto flutuante (*float*)
- 1.4.1 [Textos no programa, no console e na tela: *strings*](strings_py.md)
- 1.4.2 [Trabalhando com fontes e outros ajustes do texto](tipografia.md) 
- 1.4.3 [Métodos dos objetos *string* e *f-strings*](string_methods.md) 
- 1.4.4 [O valor especial `None`](None.md)
- 1.4.5 [Números inteiros (*int*) e números de ponto flutuante (*float*)](numeros.md)

### Mais interação com teclado e mouse
- 1.5.0 [Input com teclado e mouse](input_py.md)
- 1.5.1 [Detectando teclas simultâneas](teclas_simultaneas.md)
- 1.5.2 [Um botão simples](botao_simples.md)
- 1.5.3 [Arrastando círculos](arrastando_circulos.md)
- 1.5.4 [Usando a rodinha do mouse(*mouse wheel*)](rodinha_mouse.md)
- 1.5.5 [Parando o `draw()`](no_loop.md)

## Orientação a objetos
- 2.1.1 [Primeiros passos de orientação a objetos: usando a classe Slider](slider_com_OO.md)
- 2.2.1 [Um botão com orientação a objetos](botao_com_OO.md)
- 2.3.1 [Uma classe de partículas simples](particulas.md)
- 2.4.1 [Operações com vetores e a classe `Py5Vector`](vetores.md)
- 2.5.1 [Introdução a orientação a objetos com bandeirinhas](bandeirinhas/README.md)

## Mais sobre estruturas de dados
- 3.1.1 [Métodos das listas](list_methods.md)
- 3.2.1 [Mais estruturas de dados: dicionário (_dict_)](dicionarios.md)
- 3.3.1 [Mais estruturas de dados: conjunto (_set_)](conjuntos.md)
- 3.4.1 [Compreensão de listas e outras *comprehensions*](comprehension.md)
- 3.5.1 [Removendo itens de coleções](removendo_itens.md)

## Aprofundando ideias anteriores
- 4.1.0 [Mais sobre aleatoriedade](aleatoriedade_2.md) e as diferenças ente o `random` do py5 e o do Python
- 4.1.1 [*Perlin Noise* (ruído de Perlin)](noise.md) um tipo especial de número pseudoaleatório
- 4.2.1 [Mais sobre atributos gráficos](mais_atributos_graficos.md)
- 4.4.1 [Como usar seno `sin()`, cosseno `cos()` e arco tangente `atan2()`](seno_cosseno_atan2.md) 
- 4.5.1 [Manipulando números com `remap()` e `lerp()`](map_lerp.md) e também interpolando cores
- 4.6.1 [O que é *easing*?](easing.md) - transições de movimento
- 4.7.1 [Funções como argumentos de outras funções](funcoes-como-argumentos.md) - `sort()` e funções `lambda`
- 4.7.2 [Detectando a sobreposição de elementos geométricos](colisoes.md) - o problema das "colisões"
- 4.7.3 [Desenhando em um espaço fora da tela (*offscreen buffer*)](offscreen_buffer.md)  
- 4.7.4 [Recortando e mascarando imagens](recortando_imagens.md)

## Exportação de imagens e outras saídas
- 5.1.1 [Exportando imagens (bitmap/raster)](exportando_imagem.md)
- 5.2.1 [Exportando PDF (saída vetorial)](exportando_pdf.md)
- 5.3.1 [Exportando SVG (saída vetorial)](exportando_svg.md)
- 5.4.1 [Exportando animações (vídeos ou GIF)](exportar_animacoes.md)

## Lendo e escrevendo arquivos externos
- 6.1.0 [Carregado formas de um arquivo vetorial (SVG)](recursos_vetoriais_externos.md)
- 6.2.0 [Lendo arquivos de imagem(*bitmap/raster*)](imagens_externas.md)
  - 6.2.1 [Criando retículas a partir de amostras de pixels de image](reticulas.md)
  - 6.2.2 [Lendo todas as imagens da pasta `data`](imagens_externas_pasta2.md) e sorteando uma
  - 6.2.3 [Lendo todas as imagens de uma pasta selecionada pela pessoa usuária](imagens_externas_pasta.md) (avançado)
- 6.3.0 [Lendo e escrevendo texto em arquivos (*file IO*)](file_IO.md)
  - 6.3.1 [Lendo e escrevendo dados "tabulados" em CSV](file_IO2.md)

## Questões mais avançadas das ferramentas
- 7.1.0 [Os "modos de uso" da biblioteca py5](os_modos_de_py5.md)
- 7.1.1 [Usando várias abas no IDE e importando código de outros módulos](modulos.md) 
- 7.2.1 [Dicas para portar exemplos de Processing para Python com py5](java_para_python.md)
- 7.3.1 [Manipulando a janela](mais_que_size.md) - Tela cheia, redimensionamento e múltiplas janelas
- 7.4.1 [Uma janela de diálogo com um campo de texto](input_janela.md)
  <!-- - 7.5.1 usando bibliotecas externas Python e Java) -->

## Pequenos projetos e outros exemplos
- Neste repositório
    - [Módulos de Truchet](truchet.md) - Azulejos e rotações
    - [Jogo PONG](pong/README.md) - Estudos para o fazer um jogo
    - [L-System](LSystem.md) - Sistema de Lindenmayer
    - [Autômatos Celulares](automatos-celulares.md) - Jogo da vida de Conway (*Conway's Game of Life*)
- Externos
    - [Lousa mágica](https://abav.lugaralgum.com/lousa-magica) - Desenho com Arduino e potenciômetros
    - [Paper Objects with Processing and Python](https://abav.lugaralgum.com/Paper-objects-with-Processing-and-Python) - Volumes para cortar e montar
    - [Arc, tangents & Bezier studies](https://abav.lugaralgum.com/arc_tangents_and_bezier_studies) - Como desenhar linhas tangentes entre arcos e polígonos com arredondamentos
    - [Simulações física 2D com PyMunk](https://github.com/villares/pymunk-pinball-paulista) - Pinball
