## Material para cursos e oficinas ([repositório](https://github.com/villares/material-aulas/))

### Como colaborar e contribuir?

Este material didático pode ser modificado e usado para dar aulas. Leia as [instruções para colaborar com este repositório](https://github.com/villares/material-aulas/blob/master/sobre/como-contribuir.md) e abra [*issues*](https://github.com/villares/material-aulas/issues) apontando problemas, sugerindo assuntos e melhorias, ou contribua com *Pull Requests* para o repositório.

 Você pode também [fazer pequenas doações](https://gumroad.com/villares)! 

### Combinações de Processing com Python

> O material deste repositório foi criado inicialmente para que se pudesse aprender a programar usando **Processing modo Python**, uma ferramenta livre de programação com a sintaxe de Python e que inclui o vocabulário, os recursos de desenho e manipulação de imagens do Processing. Existem hoje diversas possibilidades de combinar essas duas linguagens, veja abaixo com obter algumas delas:

- [O que é e como instalar o Processing modo Python](https://abav.lugaralgum.com/como-instalar-o-processing-modo-python/)
- [pyp5js](https://github.com/berinhard/pyp5js) com [**editor experimental online**](https://berinhard.github.io/pyp5js/pyodide/) do projeto</sub>
- Biblioteca [py5](https://py5.ixora.io) ([instruções de instalação usando **Thonny IDE + plugin**](https://github.com/villares/thonny-py5mode/tree/pt-br))</sub>
- Veja mais outras opções descritas neste quadro: [Processing + Python tools table](https://github.com/villares/Resources-for-teaching-programming#processing--python-tools-table)

<details>

<summary> ### Processing modo Python </summary>

#### Elementos fundamentais

- [Primeiros passos e desenho básico](Processing-Python/desenho-basico_py.md)
  - [Variáveis](Processing-Python/variaveis.md)
  - [Desenhando polígonos](Processing-Python/poligonos_1.md) 
  - [O que é indentação?](Processing-Python/indentacao.md) 
  - [Mais sobre cores (RGB e HSB)](Processing-Python/mais_sobre_cores.md)
- [Condicionais (`if` e `else`)](Processing-Python/condicionais_py.md)
  - [Qual a diferença entre `=` (atribuição) e `==` (comparação)?](Processing-Python/atribuicao-e-comparacao.md)
  - [Condições aninhadas e outras estruturas condicionais](Processing-Python/condicionais_2.md)
  - [Divisão com inteiros, obtendo resultados `float`, divisão por zero e o resto da divisão](Processing-Python/divisao.md) 
- [Movimento: uma animação simples usando `setup()` e `draw()`](Processing-Python/movimento_py.md)
  - [Escopo de variáveis (local e global)](Processing-Python/escopo_py.md)
- [Declarando novas funções](Processing-Python/funcoes_py.md)
  - [Modificando as coordenadas com `translate()`, `rotate()` e mais!](Processing-Python/transformacoes_coordenadas.md)
  - [Funções recursivas](Processing-Python/recursao_py.md)
  - [Funções com argumentos padrão (ou opcionais)](Processing-Python/funcoes_2.md)
- [Sequências e laços de repetição (iteração com `for`)](Processing-Python/lacos_py.md)
  - [Mais sobre sequências e fatias](Processing-Python/mais_sequencias.md)
  - [Grades retangulares: filas e colunas de elementos](Processing-Python/grades.md)
  - [Mais sobre polígonos](Processing-Python/poligonos_2.md)
  - [Desenhando formas curvas](Processing-Python/curvas.md) 
  - [Laço de repetição com `while`](Processing-Python/while.md)
- [Tipos de valores (inteiros, números de ponto flutuante, texto (*strings*))](Processing-Python/tipagem_py.md)
  - [Textos no programa, no console e na tela (*strings*)](Processing-Python/strings_py.md)
  - [Trabalhando com fontes e outros ajustes do texto](Processing-Python/tipografia.md)
  - [Métodos dos objetos *string*](Processing-Python/string_methods.md)
- [Interação: input com teclado e mouse](Processing-Python/input_py.md)
- [Aleatoriedade: `random` e números 'sorteados'](Processing-Python/aleatoriedade_1.md)
  - [Mais sobre aleatoriedade e as diferenças ente o `random` de Processing e de Python](Processing-Python/aleatoriedade_2.md)
  - [*Perlin Noise* (ruído de Perlin) um tipo especial de número pseudo-aleatório](Processing-Python/noise.md)
- [Como usar seno `sin()`, cosseno `cos()` e arco tangente `atan2()`](Processing-Python/seno_cosseno_atan2.md)
- [Manipulando números com `map()` e `lerp()`](Processing-Python/map_lerp.md) - e fazendo cores intermediárias!
  - [O que é *easing*?](Processing-Python/easing.md) - transições de movimento
- [Funções como argumentos de outras funções](Processing-Python/funcoes-como-argumentos.md) - `sort()` e funções `lambda`

#### Mais sobre estruturas de dados

- [Métodos das listas](Processing-Python/list_methods.md)
- [Mais estruturas de dados: dicionário (_dict_)](Processing-Python/dicionarios.md)
- [Mais estruturas de dados: conjunto (_set_)](Processing-Python/conjuntos.md)
- [Compreensão de listas e outras *comprehensions*](Processing-Python/comprehension.md)

#### Desenhando em 3D

- [Primeiros passos com `size(…, …, P3D)`](Processing-Python/desenho-3D.md)

#### Mais sobre interação com o teclado e mouse

- [Escutando teclas simultâneas](Processing-Python/teclas_simultaneas.md)
- [Um botão simples](Processing-Python/botao_simples.md)
- [Arrastando círculos](Processing-Python/arrastando_circulos.md)
- [Rodinha do mouse (*mouse wheel*)](Processing-Python/rodinha_mouse.md)
- [Parando o `draw()`](Processing-Python/no_loop.md)
- [Uma janela de diálogo com um campo de texto](Processing-Python/input_janela.md)

#### Exportação de imagens e outras saídas

- [Exportando imagens (bitmap/raster)](Processing-Python/exportando_imagem.md)
- [Exportando PDF (saída vetorial)](Processing-Python/exportando_pdf.md)
- [Exportando SVG (saída vetorial)](Processing-Python/exportando_svg.md)
- [Exportando animações (vídeos ou GIF)](Processing-Python/exportar_animacoes.md) 
- [Exportando um aplicativo independente](Processing-Python/export_application.md)

#### Arquivos externos

- [Lendo um arquivo vetorial (SVG)](Processing-Python/recursos_vetoriais_externos.md)
- [Lendo arquivos de imagem (*bitmap/raster*)](Processing-Python/imagens_externas.md)
  - [Lendo todas as imagens da pasta `data`](Processing-Python/imagens_externas_pasta2.md) e sorteando uma
  - [Lendo todas as imagens de uma pasta selecionada pela pessoa usuária](Processing-Python/imagens_externas_pasta.md) (avançado)
- [Lendo e escrevendo texto em arquivos (*file IO*)](Processing-Python/file_IO.md)

#### Orientação a Objetos

- [Primeiros passos de orientação a objetos: usando a classe Slider](Processing-Python/slider_com_OO.md)
- [Um botão com orientação a objetos](Processing-Python/botao_com_OO.md)
- [Uma classe de partículas simples](Processing-Python/particulas.md)
- [Operações com vetores e a classe `PVector` do Processing](Processing-Python/vetores.md)
- [Introdução a orientação a objetos com bandeirinhas](https://abav.lugaralgum.com/mestrado/bandeirinhas/) (página externa)

#### Questões mais avançadas da ferramenta

- [Usando várias abas no IDE](Processing-Python/modulos.md)
- [Sobre o Python 2 e alguns recursos do Python 3](Processing-Python/futuro.md)
- [Dicas para portar exemplos do Processing modo Java para o modo Python](Processing-Python/java_para_python.md)
- [Mais sobre Python, Jython e Java](http://arteprog.space/Processando-Processing/tutoriais-PT/python-Python_Jython_e_Java) (página externa)
- [Mais sobre atributos gráficos](Processing-Python/mais_atributos_graficos.md)
- [Desenhando em um espaço fora da tela (offscreen buffer)](Processing-Python/offscreen_buffer.md) e recortando imagens
- [Manipulando a janela](Processing-Python/mais_que_size.md) (tela cheia, redimensionamento e múltiplas janelas)

#### Pequenos projetos e outros exemplos

- [Módulos ou mosaicos de Truchet](Processing-Python/truchet.md)
- [Jogo PONG](https://github.com/villares/material-aulas/tree/master/pong) - Estudos para o fazer um jogo
- [`caneta_automatica_py`](caneta_automatica) - Módulo para desenhar inspirado na tartaruga de Logo
- [Lousa mágica](https://abav.lugaralgum.com/lousa-magica) - Desenho com Arduino e potenciômetros

</details>

#### Recursos externos

##### Processing modo Python

- [py.processing.org/reference](http://py.processing.org/reference) - Referência do Processing modo Python
- [Processing.py in Ten Lessons](https://tabreturn.github.io/#processing-reverse) (em Inglês) de [Tristan B. @tabreturn](http://portfolio.tabreturn.com/)
- Livro [Getting Started with Processing.py](http://www.worldcat.org/oclc/1001947294) (em Inglês) Allison Parrish et al.

##### Processing modo Java

- [processing.org/reference](http://processing.org/reference) - Tem algumas páginas à mais e coisas que funcionam no Python
- Livro [O código transcendente](https://codigotranscendente.github.io/livro/about.html) de Mateus Berruezo
- [Programação Criativa](http://arteprog.space/programacao-criativa) de Monica Rizzolli e Alexandre Villares
- [Guia de programação em Processing](https://www.ranoya.com/aulas/designgenerativo/playgroundDocs/introProcessing.php?theme=dgen&elementos=processing), Prof. Guilherme Ranoya (UFPE).
- [Tradução da referência da linguagem - versão 1.0 (2005)](http://www.dainf.ct.utfpr.edu.br/~merkle/processing/reference/ptBR/index.html), Prof. Luiz Merkle (UFTPR)

### Outros recursos introdutórios abertos

#### Livros de Python

- DOWNEY, Allen. [Pense em Python 2e](https://penseallen.github.io/PensePython2e/)
- BORGES, Luiz Eduardo. [Python para desenvolvedores 3e](https://ricardoduarte.github.io/python-para-desenvolvedores/#conteudo)
- SWEIGART, Al. Automatize tarefas maçantes com Python (traduzido pela Novatec)<br> ou [automatetheboringstuff.com](https://automatetheboringstuff.com) (site do autor em Inglês)

#### Processando-Processing

- [Ajude a traduzir mais coisas!](https://github.com/arteprog/processando-processing)

---
### Licenças

**Texto e imagens:** Alexandre B A Villares - [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.pt_BR), exceto onde indicado, confira atribuições em cada página para materiais adaptados/remixados de outras fontes. Agradeço aos colaboradores do repositório que doam suas contribuições nestes termos!

**Código:** GNU GPL v3.0, exceto onde for indicado, por alguma razão.
