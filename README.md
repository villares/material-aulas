
---

## material para cursos e oficinas ([repositório](https://github.com/villares/material-aulas/))

Para aprender a programar usando **Processing modo Python**, uma ferramenta livre de programação com a sintaxe de Python e que inclui o vocabulário, os recursos de desenho e manipulação de imagens, de Processing.

### Como colaborar e contribuir?

Este material didático é aberto. Leia as [instruções para colaborar com este repositório](/como-contribuir.md) e abra [*issues*](https://github.com/villares/material-aulas/issues) apontando problemas, sugerindo assuntos e melhorias, ou contribua com *Pull Requests* para o repositório.

 Você pode também [fazer pequenas doações](https://gumroad.com/villares)! 

### Sumário

- [O que é e como instalar o Processing modo Python](https://abav.lugaralgum.com/como-instalar-o-processing-modo-python/)
   - <sub>Caso não possa instalar, experimente no navegador: [Triket.io](https://trinket.io/python/cfaf743794) ou [SkulptIDE](http://tiny.cc/processing_python) do prof. Claudio Esperança.</sub>
  - <sub>Conheça também o projeto [pyp5js](https://github.com/berinhard/pyp5js) que converte Python em JavaScript+P5js</sub>
- [Primeiros passos e desenho básico](Processing-Python/desenho-basico_py.md)
  - [Variáveis](Processing-Python/variaveis.md)
  - [Desenhando polígonos](Processing-Python/poligonos_1.md)  
  - [O que é indentação?](Processing-Python/indentacao.md)  
  - [Divisão com números inteiros](divisao.md)
- [Condicionais (`if` e `else`)](Processing-Python/condicionais_py.md)
  - [Qual a diferença entre `=` (atribuição) e `==` (comparação)?](Processing-Python/atribuicao-e-comparacao.md)
  - [Condições aninhadas e outras estruturas condicionais](Processing-Python/condicionais_2.md)
- [Movimento: uma animação simples usando `setup()` e `draw()`](Processing-Python/movimento_py.md)
  - [Escopo de variáveis (local e global)](Processing-Python/escopo_py.md)
- [Declarando novas funções](Processing-Python/funcoes_py.md)
  - [Alterando o sistema de coordenadas (`translate()`, `rotate()` e outras)](Processing-Python/transformacoes_coordenadas.md)
  - [Funções recursivas](Processing-Python/recursao_py.md)
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
- [Manipulando números com `map()` e `lerp()`](Processing-Python/map_lerp.md) - e fazendo cores intermediárias!
  - [O que é *easing*?](Processing-Python/easing.md) - transições de movimento
- [Desenhando em 3D](Processing-Python/desenho-3D.md)

#### Mais sobre interação com o teclado e mouse

- [Escutando teclas simultâneas](Processing-Python/teclas_simultaneas.md)
- [Um botão simples](Processing-Python/botao_simples.md)
- [Arrastando círculos](Processing-Python/arrastando_circulos.md)
- [Rodinha do mouse (*mouse wheel*)](Processing-Python/rodinha_mouse.md)
- [Parando o `draw()`](Processing-Python/no_loop.md)

#### Exportação de imagens e outras saídas

- [Exportando imagens (bitmap/raster)](Processing-Python/exportando_imagem.md)
- [Exportando PDF (saída vetorial)](Processing-Python/exportando_pdf.md)
- [Exportando SVG (saída vetorial)](Processing-Python/exportando_svg.md)
- [Exportando animações (vídeos ou GIF)](Processing-Python/exportar_animacoes.md) 
- [Exportando um aplicativo independente](Processing-Python/export_application.md)

#### Arquivos externos
- [Lendo um arquivo vetorial (SVG)](Processing-Python/recursos_vetoriais_externos.md)
- [Lendo arquivos de imagem (*bitmap/raster*)](Processing-Python/imagens_externas.md)
  - [Lendo todas as imagem de uma pasta](Processing-Python/imagens_externas_pasta.md)
- [Lendo e escrevendo texto em arquivos (*file IO*)](Processing-Python/file_IO.md)

#### Orientação a Objetos
- [Um botão com orientação a objetos](Processing-Python/botao_com_OO.md)
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
- Mais sobre [Python, Jython e Java](http://arteprog.space/Processando-Processing/tutoriais-PT/python-Python_Jython_e_Java) (página externa)

#### Pequenos projetos

- [Jogo PONG](https://github.com/villares/material-aulas/tree/master/pong) - Estudos para o fazer um jogo
- [`caneta_automatica_py`](caneta_automatica) - Módulo para desenhar inspirado na tartaruga de Logo
- [Lousa mágica](https://abav.lugaralgum.com/lousa-magica) - Desenho com Arduino e potenciômetros

### Referências

- [py.processing.org/reference](http://py.processing.org/reference)

#### Outros recursos introdutórios abertos

##### Livros de Python

- DOWNEY, Allen. [Pense em Python 2e](https://penseallen.github.io/PensePython2e/)
- BORGES, Luiz Eduardo. [Python para desenvolvedores 3e](https://ricardoduarte.github.io/python-para-desenvolvedores/#conteudo)
- SWEIGART, Al. Automatize tarefas maçantes com Python (traduzido pela Novatec)<br> ou [automatetheboringstuff.com](https://automatetheboringstuff.com) (site do autor em Inglês)

##### Processing modo Python

- [Processing.py in Ten Lessons](https://tabreturn.github.io/#processing-reverse) (em Inglês) de [Tristan B. @tabreturn](http://portfolio.tabreturn.com/)

##### Processing modo Java

- [Programação Criativa](http://arteprog.space/programacao-criativa) de Monica Rizzolli e Alexandre Villares
- [Guia de programação em Processing](https://www.ranoya.com/aulas/designgenerativo/playgroundDocs/introProcessing.php?theme=dgen&elementos=processing), Prof. Guilherme Ranoya (UFPE).
- [Tradução da referência da linguagem - versão 1.0 (2005)](http://www.dainf.ct.utfpr.edu.br/~merkle/processing/reference/ptBR/index.html), Prof. Luiz Merkle (UFTPR)

---
Texto e imagens: CC BY-NC-SA 4.0; Código: GNU GPL v3.0 exceto onde explicitamente indicado por questões de compatibilidade.
