## Material para py5 com Thonny IDE

- 0.0.0 [O que é e como instalar o py5 e o Thonny IDE](https://abav.lugaralgum.com/como-instalar-py5/)
   - 0.0.1 [Sumário traduzido da referência do py5](sumario-referencia-py5.md)

### Elementos fundamentais

- 1.0.0 [Primeiros passos e desenho básico](desenho-basico_py.md)
  - 1.0.1 [Variáveis](variaveis.md)
  - 1.0.2 [O que é indentação?](indentacao.md)
  - 1.0.3 [Mais sobre cores(RGB e HSB)](mais_sobre_cores.md)
  - 1.0.4 [Desenhando polígonos](poligonos_1.md)

- 1.1.0 [Movimento e interatividade](setup_draw.md) a estrutura `setup()` e `draw()`	
  - 1.1.1 [Execução condicional (`if`/`else`), operadores de comparação e lógicos](condicionais_py.md)
  - 1.1.2 [Qual a diferença entre `=` (atribuição) e `==` (comparação)?](atribuicao-e-comparacao.md)
  - 1.1.3 [Criando uma animação simples](movimento_py.md)	
  - 1.1.4 [Escopo de variáveis(local e global)](escopo_py.md)
  - 1.1.5 [Divisão por zero e o resto da divisão](divisao.md) 

- 1.3.0 [Declarando novas funções](funcoes_py.md)
  - 1.3.1 [Modificando as coordenadas](transformacoes_coordenadas.md) com `translate()`, `rotate()` e mais!
  - 1.3.2 [Funções recursivas](recursao_py.md)
  - 1.3.3 [Funções com argumentos padrão(ou opcionais)](funcoes_2.md)
  - 1.3.4 [Condições aninhadas e outras estruturas condicionais](condicionais_2.md)

- 1.4.0 [Sequências e laços de repetição (iteração com `for`)](lacos_py.md)
  - 1.4.1 [Mais sobre sequências e fatias](mais_sequencias.md)
  - 1.4.2 [Grades retangulares: filas e colunas de elementos](grades.md)
  - 1.4.3 [Mais sobre polígonos](poligonos_2.md)
  - 1.4.4 [Desenhando formas curvas](curvas.md)
  - 1.4.5 [Laço de repetição com `while`](while.md)

- 1.5.0 [Tipos de valores](tipagem_py.md) como texto (*strings*) e números inteiros (*int*) ou de ponto flutuante (*float*) 
  - 1.5.1 [Textos no programa, no console e na tela (*strings*)](strings_py.md)
  - 1.5.2 [Trabalhando com fontes e outros ajustes do texto](tipografia.md) 
  - 1.5.3 [Métodos dos objetos *string*](string_methods.md)
  - 1.5.4 [O valor especial `None`](None.md)
  - 1.5.5 [Números inteiros (*int*) e números de ponto flutuante (*float*)](numeros.md)


- 1.6.0 [Interação: input com teclado e mouse](input_py.md)

- 1.7.0[Aleatoriedade: `random` e números "sorteados"](aleatoriedade_1.md)
  - 1.7.1 [Mais sobre aleatoriedade](aleatoriedade_2.md) e as diferenças ente o `random` do py5 e o do Python
  - 1.7.2 [*Perlin Noise* (ruído de Perlin)](noise.md) um tipo especial de número pseudo-aleatório
  - 1.7.3 [Como usar seno `sin()`, cosseno `cos()` e arco tangente `atan2()`](seno_cosseno_atan2.md) 
  - 1.7.4 [Manipulando números com `remap()` e `lerp()`](map_lerp.md) e também interpolando cores
  - 1.7.5 [O que é *easing*?](easing.md) - transições de movimento

- 1.8.0 [Funções como argumentos de outras funções](funcoes-como-argumentos.md) - `sort()` e funções `lambda`

### Mais sobre estruturas de dados

- 2.1.1 [Métodos das listas](list_methods.md)
- 2.2.1 [Mais estruturas de dados: dicionário (_dict_)](dicionarios.md)
- 2.3.1 [Mais estruturas de dados: conjunto (_set_)](conjuntos.md)
- 2.4.1 [Compreensão de listas e outras *comprehensions*](comprehension.md)

### Desenhando em 3D

- 3.1.0 [Primeiros passos com `size(…, …, P3D)`](desenho-3D.md)

### Mais sobre interação com o teclado e mouse

- 4.1.1 [Escutando teclas simultâneas](teclas_simultaneas.md)
- 4.2.1 [Um botão simples](botao_simples.md)
- 4.3.1 [Arrastando círculos](arrastando_circulos.md)
- 4.4.1 [Rodinha do mouse(*mouse wheel*)](rodinha_mouse.md)
- 4.5.1 [Parando o `draw()`](no_loop.md)
- 4.6.1 [Uma janela de diálogo com um campo de texto](input_janela.md)

### Exportação de imagens e outras saídas

- 5.1.1 [Exportando imagens (bitmap/raster)](exportando_imagem.md)
- 5.2.1 [Exportando PDF (saída vetorial)](exportando_pdf.md)
- 5.3.1 [Exportando SVG (saída vetorial)](exportando_svg.md)
- 5.4.1 [Exportando animações (vídeos ou GIF)](exportar_animacoes.md)
<!-- 5.5.1 [Exportando um aplicativo independente](export_application.md) [REVISAR] -->

### Arquivos externos

- 6.1.1 [Lendo um arquivo vetorial(SVG)](recursos_vetoriais_externos.md)
- 6.2.0 [Lendo arquivos de imagem(*bitmap/raster*)](imagens_externas.md)
  - 6.2.1 [Lendo todas as imagens da pasta `data`](imagens_externas_pasta2.md) e sorteando uma
  - 6.2.1 [Lendo todas as imagens de uma pasta selecionada pela pessoa usuária](imagens_externas_pasta.md) (avançado)
- 6.3.1 [Lendo e escrevendo texto em arquivos(*file IO*)](file_IO.md)

### Orientação a Objetos

- 7.1.1 [Primeiros passos de orientação a objetos: usando a classe Slider](slider_com_OO.md)
- 7.2.1 [Um botão com orientação a objetos](botao_com_OO.md)
- 7.3.1 [Uma classe de partículas simples](particulas.md)
- 7.4.1 [Operações com vetores e a classe `Py5Vector` do Processing](vetores.md) 
- 7.5.1 [Introdução a orientação a objetos com bandeirinhas](bandeirinhas)

### Questões mais avançadas das ferramentas

- 8.1.1 [Usando várias abas no IDE](modulos.md)
- 8.2.1 [Dicas para portar exemplos do Processing modo Java para o modo Python](java_para_python.md)
<!-- - 8.2.2 REVISAR [Mais sobre Python, Jython e Java](http://arteprog.space/Processando-Processing/tutoriais-PT/python-Python_Jython_e_Java) (página externa) -->
- 8.3.1 [Mais sobre atributos gráficos](mais_atributos_graficos.md)
- 8.4.1 [Desenhando em um espaço fora da tela](offscreen_buffer.md) (offscreen buffer) e recortando imagens
- 8.5.1 [Manipulando a janela](mais_que_size.md) (Tela cheia, redimensionamento e múltiplas janelas) 

### Pequenos projetos e outros exemplos

#### Neste repositório

- 9.1.1 [Módulos ou mosaicos de Truchet](truchet.md)
- 9.1.2 [Jogo PONG](pong/) - Estudos para o fazer um jogo
<!-- 9.1.3 [`caneta_automatica_py`](caneta_automatica/) - Módulo para desenhar inspirado na tartaruga de Logo -->
- 9.1.4 [L-System](LSystem.md) - Sistema de Lindenmayer

#### Externos

- 9.2.1 [Lousa mágica](https://abav.lugaralgum.com/lousa-magica) - Desenho com Arduino e potenciômetros
- 9.2.2 [Paper Objects with Processing and Python](https://abav.lugaralgum.com/Paper-objects-with-Processing-and-Python)
- 9.2.3 [Arc, tangents & Bezier studies](https://github.com/villares/arc_tangents_and_bezier_studies)
- 9.2.4 [Simulações física 2D com PyMunk - Pinball](https://github.com/villares/pymunk-pinball-paulista)
