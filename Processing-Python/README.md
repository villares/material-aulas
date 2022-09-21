## Material para Processing modo Python

- [O que é e como instalar o Processing modo Python](https://abav.lugaralgum.com/como-instalar-o-processing-modo-python/)

### Elementos fundamentais

- 0.0.0. [Primeiros passos e desenho básico](desenho-basico_py.md)
  - 0.0.1. [Variáveis](variaveis.md)
  - 0.0.2. [O que é indentação?](indentacao.md)
  - 0.0.3. [Mais sobre cores(RGB e HSB)](mais_sobre_cores.md)
  - 0.0.4. [Desenhando polígonos](poligonos_1.md)

- 0.1.0. [Condicionais(`if` e `else`)](condicionais_py.md)
  - 0.1.1. [Qual a diferença entre `=` (atribuição) e `==` (comparação)?](atribuicao-e-comparacao.md)
  - 0.1.2. [Condições aninhadas e outras estruturas condicionais](condicionais_2.md)
  - 0.1.3. [Divisão com inteiros, divisão por zero e o resto da divisão](divisao.md)

- 0.2.0 [Movimento: uma animação simples usando `setup()` e `draw()`](movimento_py.md)
  - 0.2.1 [Escopo de variáveis(local e global)](escopo_py.md)

- 0.3.0 [Declarando novas funções](funcoes_py.md)
  - 0.3.1 [Modificando as coordenadas com `translate()`, `rotate()` e mais!](transformacoes_coordenadas.md)
  - 0.3.2 [Funções recursivas](recursao_py.md)
  - 0.3.3 [Funções com argumentos padrão(ou opcionais)](funcoes_2.md)

- 0.4.0 [Sequências e laços de repetição(iteração com `for`)](lacos_py.md)
  - 0.4.1 [Mais sobre sequências e fatias](mais_sequencias.md)
  - 0.4.2 [Grades retangulares: filas e colunas de elementos](grades.md)
  - 0.4.3 [Mais sobre polígonos](poligonos_2.md)
  - 0.4.4 [Desenhando formas curvas](curvas.md)
  - 0.4.5 [Laço de repetição com `while`](while.md)

- 0.5.0 [Tipos de valores(inteiros, números de ponto flutuante, texto(*strings*))](tipagem_py.md)
  - 0.5.1 [Textos no programa, no console e na tela(*strings*)](strings_py.md)
  - 0.5.2 [Trabalhando com fontes e outros ajustes do texto](tipografia.md) 
  - 0.5.3 [Métodos dos objetos *string*](string_methods.md)
  - 0.5.4 [O valor especial `None`](None.md)

- 0.6.0 [Interação: input com teclado e mouse](input_py.md)

- 0.7.0[Aleatoriedade: `random` e números 'sorteados'](aleatoriedade_1.md)
  - 0.7.1 [Mais sobre aleatoriedade e as diferenças ente o `random` de Processing e de Python](aleatoriedade_2.md)
  - 0.7.2 [*Perlin Noise* (ruído de Perlin) um tipo especial de número pseudo-aleatório](noise.md)
  - 0.7.3 [Como usar seno `sin()`, cosseno `cos()` e arco tangente `atan2()`](seno_cosseno_atan2.md)
  - 0.7.4 [Manipulando números com `remap()` e `lerp()`](map_lerp.md) - e fazendo cores intermediárias!
  - 0.7.5 [O que é *easing*?](easing.md) - transições de movimento

- 0.8.0 [Funções como argumentos de outras funções](funcoes-como-argumentos.md) - `sort()` e funções `lambda`

### Mais sobre estruturas de dados

- 1.1.1 [Métodos das listas](list_methods.md)
- 1.2.1 [Mais estruturas de dados: dicionário (_dict_)](dicionarios.md)
- 1.3.1 [Mais estruturas de dados: conjunto (_set_)](conjuntos.md)
- 1.4.1 [Compreensão de listas e outras *comprehensions*](comprehension.md)

### Desenhando em 3D

- 2.1.0 [Primeiros passos com `size(…, …, P3D)`](desenho-3D.md)

### Mais sobre interação com o teclado e mouse

- 3.1.1 [Escutando teclas simultâneas](teclas_simultaneas.md)
- 3.1.2 [Um botão simples](botao_simples.md)
- 3.1.3 [Arrastando círculos](arrastando_circulos.md)
- 3.1.4 [Rodinha do mouse(*mouse wheel*)](rodinha_mouse.md)
- 3.1.5 [Parando o `draw()`](no_loop.md)
- 3.1.6 [Uma janela de diálogo com um campo de texto](input_janela.md)

#### Exportação de imagens e outras saídas

- 4.1.1 [Exportando imagens(bitmap/raster)](exportando_imagem.md)
- 4.1.2 [Exportando PDF(saída vetorial)](exportando_pdf.md)
- 4.1.3 [Exportando SVG(saída vetorial)](exportando_svg.md)
- 4.1.4 [Exportando animações(vídeos ou GIF)](exportar_animacoes.md)
- 4.1.5 [Exportando um aplicativo independente](export_application.md)

### Arquivos externos

- 5.1.1 [Lendo um arquivo vetorial(SVG)](recursos_vetoriais_externos.md)
- 5.2.0 [Lendo arquivos de imagem(*bitmap/raster*)](imagens_externas.md)
  - 5.2.1 [Lendo todas as imagens da pasta `data`](imagens_externas_pasta2.md) e sorteando uma
  - 5.2.1 [Lendo todas as imagens de uma pasta selecionada pela pessoa usuária](imagens_externas_pasta.md) (avançado)
- 5.3.1 [Lendo e escrevendo texto em arquivos(*file IO*)](file_io.md)

### Orientação a Objetos

- 6.1.1 [Primeiros passos de orientação a objetos: usando a classe Slider](slider_com_oo.md)
- 6.2.1 [Um botão com orientação a objetos](botao_com_oo.md)
- 6.3.1 [Uma classe de partículas simples](particulas.md)
- 6.4.1 [Operações com vetores e a classe `Py5Vector` do Processing](vetores.md) [REVIsAR] 
- 6.5.1 [Introdução a orientação a objetos com bandeirinhas](bandeirinhas/README.md)

### Questões mais avançadas da ferramenta

- 7.1.1 [Usando várias abas no IDE](modulos.md)
- 7.1.2 [Sobre o Python 2 e alguns recursos do Python 3](futuro.md)
- 7.2.1 [Dicas para portar exemplos do Processing modo Java para o modo Python](java_para_python.md)
- 7.2.2 [Mais sobre Python, Jython e Java](http://arteprog.space/Processando-Processing/tutoriais-PT/python-Python_Jython_e_Java) (página externa)
- 7.3.1  [Mais sobre atributos gráficos](mais_atributos_graficos.md)
- 7.4.1  [Desenhando em um espaço fora da tela (offscreen buffer)](offscreen_buffer.md) e recortando imagens
- 7.5.1  [Manipulando a janela](mais_que_size.md) (tela cheia, redimensionamento e múltiplas janelas)

### Pequenos projetos e outros exemplos

- 8.1.1 [Módulos ou mosaicos de Truchet](truchet.md)
- 8.2.1 [Jogo PONG](pong/) - Estudos para o fazer um jogo
- 8.3.1 [`caneta_automatica_py`](caneta_automatica/) - Módulo para desenhar inspirado na tartaruga de Logo
- 8.4.1 [Lousa mágica](https://abav.lugaralgum.com/lousa-magica) - Desenho com Arduino e potenciômetros


