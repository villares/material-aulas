## material para cursos e oficinas ([repositório](https://github.com/villares/material-aulas/))

### Como colaborar e contribuir?

Este material didático pode ser modificado e usado para dar aulas. Leia as [instruções para colaborar com este repositório](https://github.com/villares/material-aulas/blob/master/sobre/como-contribuir.md) e abra [*issues*](https://github.com/villares/material-aulas/issues) apontando problemas, sugerindo assuntos e melhorias, ou contribua com *Pull Requests* para o repositório.

 Você pode também [fazer pequenas doações](https://gumroad.com/villares)! 

### Processing modo Python

> Para aprender a programar usando **Processing modo Python**, uma ferramenta livre de programação com a sintaxe de Python e que inclui o vocabulário, os recursos de desenho e manipulação de imagens, de Processing.

- [O que é e como instalar o Processing modo Python](https://abav.lugaralgum.com/como-instalar-o-processing-modo-python/)
  <br><sub>**ferramentas alternativas:**</sub>
     - <sub>[pyp5js](https://github.com/berinhard/pyp5js) com [**editor experimental online**](https://berinhard.github.io/pyp5js/pyodide/) do projeto</sub>
     - <sub>Biblioteca [p5py](https://github.com/p5py/p5/) ([instruções de instalação](p5py/instalacao_p5py.md))</sub>
     - <sub>Editor online [Triket.io](https://trinket.io/python/cfaf743794)</sub>
     - <sub>Editores online [SkulptIDE](http://tiny.cc/processing_python) e [BrythonIDE](https://esperanc.github.io/brythonide/) do prof. Claudio Esperança</sub>

#### Elementos fundamentais

- [Primeiros passos e desenho básico](Processing-Python/desenho-basico_py.md)
  - [Variáveis](Processing-Python/variaveis.md)
  - [Desenhando polígonos](Processing-Python/poligonos_1.md) 
  - [O que é indentação?](Processing-Python/indentacao.md) 
  - [Divisão com números inteiros](Processing-Python/divisao.md)
  - [Mais sobre cores (RGB e HSB)](Processing-Python/mais_sobre_cores.md)
- [Condicionais (`if` e `else`)](Processing-Python/condicionais_py.md)
  - [Qual a diferença entre `=` (atribuição) e `==` (comparação)?](Processing-Python/atribuicao-e-comparacao.md)
  - [Condições aninhadas e outras estruturas condicionais](Processing-Python/condicionais_2.md)
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
  - [Laço de repetição com `while`](Processing-Python/while.md)
- [Tipos de valores (inteiros, números de ponto flutuante, texto (*strings*))](Processing-Python/tipagem_py.md)
  - [Textos no programa, no console e na tela (*strings*)](Processing-Python/strings_py.md)
  - [Trabalhando com fontes e outros ajustes do texto](Processing-Python/tipografia.md)
- [Interação: input com teclado e mouse](Processing-Python/input_py.md)
- [Aleatoriedade: `random` e números 'sorteados'](Processing-Python/aleatoriedade_1.md)
  - [Mais sobre aleatoriedade](Processing-Python/aleatoriedade_2.md)
  - [*Perlin Noise* (ruído de Perlin) um tipo especial de número pseudo-aleatório](Processing-Python/noise.md)
- [Como usar seno `sin()`, cosseno `cos()` e arco tangente `atan2()`](Processing-Python/seno_cosseno_atan2.md)
- [Manipulando números com `map()` e `lerp()`](Processing-Python/map_lerp.md) - e fazendo cores intermediárias!
  - [O que é *easing*?](Processing-Python/easing.md) - transições de movimento

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
  - [Lendo todas as imagens de uma pasta](Processing-Python/imagens_externas_pasta.md)
- [Lendo e escrevendo texto em arquivos (*file IO*)](Processing-Python/file_IO.md)

#### Orientação a Objetos
- [Um botão com orientação a objetos](Processing-Python/botao_com_OO.md)
- [Um *slider* com orientação a objetos](Processing-Python/slider_com_OO.md)
- [Uma classe de partículas simples](Processing-Python/particulas.md)
- [Introdução a orientação a objetos com bandeirinhas](https://abav.lugaralgum.com/mestrado/bandeirinhas/) (página externa)

<!-- 
#### Funções como objetos e algumas ideias de Programação Funcional
- [Usando`map()`,`reduce()`e outras funções que recebem funções como argumentos](funcoes_como_objetos_1.md)
- [Listas e dicionários de funções](funcoes_como_objetos_2.md)
- [*Decorators*: O que são? Onde vivem? Do que se alimentam?](funcoes_decoradores.md)
-->
#### Questões mais avançadas da ferramenta

- [Usando várias abas no IDE](Processing-Python/modulos.md)
- [Sobre o Python 2 e alguns recursos do Python 3](Processing-Python/futuro.md)
- [Dicas para portar exemplos do Processing modo Java para o modo Python](Processing-Python/java_para_python.md)
- Mais sobre [Python, Jython e Java](http://arteprog.space/Processando-Processing/tutoriais-PT/python-Python_Jython_e_Java) (página externa)
- Manipulando a janela ([tela cheia, redimensionamento e múltiplas janelas](Processing-Python/mais_que_size.md))

#### Pequenos projetos

- [Jogo PONG](https://github.com/villares/material-aulas/tree/master/pong) - Estudos para o fazer um jogo
- [`caneta_automatica_py`](caneta_automatica) - Módulo para desenhar inspirado na tartaruga de Logo
- [Lousa mágica](https://abav.lugaralgum.com/lousa-magica) - Desenho com Arduino e potenciômetros

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

**Código:** GNU GPL v3.0, exceto onde indicado por questões de compatibilidade (MIT/Apache e etc.)

