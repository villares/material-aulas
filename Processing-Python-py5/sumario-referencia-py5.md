# Sumário da Referência do py5

<h1 id="toc"></h1>

<!--
* [Desenhando formas](#desenhando-formas): [Elementos básicos](#elementos-básicos); [Formas 3D](#formas-3d); [Formas baseadas em vértices](#formas-baseadas-em-vértices); [Curvas independentes](#curvas-independentes); [Criando e exibindo objetos Py5Shape](#criando-e-exibindo-objetos-py5shape).
* [Cor e outros atributos gráficos](#cor-e-outros-atributos-gráficos): [Criando e atribuindo cores](#criando-e-atribuindo-cores); [Analisando cores](#analisando-cores); [Atributos de traço e controle de estilo](#atributos-de-traço-e-controle-de-estilo).
* [Entrada de dados (*Input*)](#entrada-de-dados-input): [Lendo arquivos](#lendo-arquivos); [Variáveis do teclado](#variáveis-do-teclado); [Funções de evento do teclado](#funções-de-evento-do-teclado); [Variáveis do mouse](#variáveis-do-mouse); [Funções de evento do mouse](#funções-de-evento-do-mouse); [Funções auxiliares de data e horário](#funções-auxiliares-de-data-e-horário).
* [Saída de dados (*Output*)](#saída-de-dados-output): [Escrevendo arquivos](#escrevendo-arquivos); [Saída de imagens](#saída-de-imagens); [Área de texto (console)](#área-de-texto-console).
* [Tipografia](#tipografia): [Desenhando texto](#desenhando-texto); [Carregando e selecionando fontes](#carregando-e-selecionando-fontes); [Métricas de texto](#métricas-de-texto).
* [Transformações do Sistema de Coordenadas](#transformações-do-sistema-de-coordenadas): [Operações Básicas](#operações-básicas); [Rotações 3D](#rotações-3d); [Operações com a matrix de transformações](#operações-com-a-matrix-de-transformações).
* [Ambiente do Sketch](#ambiente-do-sketch): [Configuração e variáveis](#configuração-e-variáveis); [Outros controles da janela do sketch](#outros-controles-da-janela-do-sketch).
* [Relacionadas à matemática](#relacionadas-à-matemática): [Cálculo](#cálculo); [Aleatoriedade (*Random*)](#aleatoriedade-random); [Trigonometria](#trigonometria).
* [Trabalhando com imagens](#trabalhando-com-imagens): [Carregando e exibindo](#carregando-e-exibindo); [Pixels](#pixels); [Texturas](#texturas); [Objetos de imagem](#objetos-de-imagem).
* [Cena 3D](#cena-3d): [Câmera](#câmera); [Coordenadas](#coordenadas); [Luzes](#luzes); [Propriedade dos materiais](#propriedade-dos-materiais)
* [Apresentação (*Rendering*)](#apresentação-rendering): [Contexto gráfico](#contexto-gráfico); [Shaders](#shaders).
* [Execução do sketch](#execução-do-sketch): [Controle do laço de repetição *draw*](#controle-do-laço-de-repetição-draw); [Controle avançado da execução](#controle-avançado-da-execução); [Análise da Performance (*Performance Profiling*)](#análise-da-performance-performance-profiling); [Linhas de execução (*Threading*)](#linhas-de-execução-threading); [Constantes da JVM](#constantes-da-jvm).
* [Classes e outras ferramentas do py5](#classes-e-outras-ferramentas-do-py5): [Classes](#classes); [Ferramentas](#ferramentas).
-->

### Desenhando formas

#### Elementos básicos

* [arc()](http://py5coding.org/reference/sketch_arc.html) - Desenha um arco na tela.
* [circle()](http://py5coding.org/reference/sketch_circle.html) - Desenha um círculo na tela.
* [ellipse()](http://py5coding.org/reference/sketch_ellipse.html) - Desenha uma elipse (oval) - na tela.
* [ellipse_mode()](http://py5coding.org/reference/sketch_ellipse_mode.html ) - Modifica o ponto a partir do qual elipses e círculos são desenhados alterando a maneira como os valores fornecidos são interpretados.
* [line()](http://py5coding.org/reference/sketch_line.html) - Desenha uma linha (um caminho direto entre dois pontos) - na tela.
* [lines()](http://py5coding.org/reference/sketch_lines.html) - Desenhe uma coleção de linhas na tela.
* [point()](http://py5coding.org/reference/sketch_point.html) - Desenha um ponto, uma coordenada no espaço na dimensão de um pixel.
* [points()](http://py5coding.org/reference/sketch_points.html) - Desenhe uma coleção de pontos, cada um uma coordenada no espaço na dimensão de um pixel.
* [quad()](http://py5coding.org/reference/sketch_quad.html) - Um quadrilátero é um quadrilátero, um polígono de quatro lados.
* [rect()](http://py5coding.org/reference/sketch_rect.html) - Desenha um retângulo na tela.
* [rect_mode()](http://py5coding.org/reference/sketch_rect_mode.html). Modifica o local a partir do qual os retângulos e quadrados são desenhados, alterando a maneira como os valores fornecidos são interpretados.
* [square()](http://py5coding.org/reference/sketch_square.html) - Desenha um quadrado na tela.
* [triangle()](http://py5coding.org/reference/sketch_triangle.html) - Desenha um triângulo na tela.

#### Formas 3D

* [box()](http://py5coding.org/reference/sketch_box.html) - Uma caixa é um retângulo com extrusão. Você precisará definir o renderizador `P3D` em `size()` para usá-la.
* [sphere()](http://py5coding.org/reference/sketch_sphere.html) - Uma esfera é uma bola oca feita de triângulos em malha (*mesh*). Você precisará do renderizador `P3D`.
* [sphere_detail()](http://py5coding.org/reference/sketch_sphere_detail.html) - Controla o grau de detalhes usado para criar uma esfera ajustando o número de vértices da malha.

#### Formas baseadas em vértices

* [begin_closed_shape()](http://py5coding.org/reference/sketch_begin_closed_shape.html) - Este método é usado para iniciar uma forma fechada personalizada.
* [begin_contour()](http://py5coding.org/reference/sketch_begin_contour.html) - Use os métodos `begin_contour()` e `end_contour()` para criar formas negativas dentro de formas como o centro da letra 'O'.
* [begin_shape()](http://py5coding.org/reference/sketch_begin_shape.html) - O uso das funções `begin_shape()` e `end_shape()` permite a criação de formas mais complexos.
* [bezier_vertex()](http://py5coding.org/reference/sketch_bezier_vertex.html) - Especifica coordenadas de vértice para curvas de Bezier.
* [bezier_vertices()](http://py5coding.org/reference/sketch_bezier_vertices.html) - Crie uma coleção de vértices bezier.
* [curve_vertex()](http://py5coding.org/reference/sketch_curve_vertex.html) - Especifica coordenadas de vértice para curvas.
* [curve_vertices()](http://py5coding.org/reference/sketch_curve_vertices.html) - Crie uma coleção de vértices de curva.
* [end_contour()](http://py5coding.org/reference/sketch_end_contour.html) - Use os métodos `begin_contour()` e `end_contour()` para criar formas negativas dentro de formas como o centro da letra 'O'.
* [end_shape()](http://py5coding.org/reference/sketch_end_shape.html) - A função `end_shape()` é a companheira de `begin_shape()` e só pode ser chamada depois de begin_shape().
* [quadratic_vertex()](http://py5coding.org/reference/sketch_quadratic_vertex.html) - Especifica as coordenadas do vértice para curvas quadráticas de Bezier.
* [quadratic_vertices()](http://py5coding.org/reference/sketch_quadratic_vertices.html) - Adicione uma coleção de vértices quadráticos.
* [vertex()](http://py5coding.org/reference/sketch_vertex.html) - Adicione um novo vértice a uma forma.
* [vertices()](http://py5coding.org/reference/sketch_vertices.html) - Adicione uma coleção de vértices a uma forma.

#### Curvas independentes

* [bezier()](http://py5coding.org/reference/sketch_bezier.html) - Desenha uma curva Bezier na tela.
* [bezier_detail()](http://py5coding.org/reference/sketch_bezier_detail.html) - Define a resolução na qual os Béziers são exibidos.
* [bezier_point()](http://py5coding.org/reference/sketch_bezier_point.html) - Avalia o Bezier no ponto t para os pontos a, b, c, d.
* [bezier_tangent()](http://py5coding.org/reference/sketch_bezier_tangent.html) - Calcula a tangente de um ponto em uma curva Bezier.
* [curve()](http://py5coding.org/reference/sketch_curve.html) - Desenha uma curva (*Catmull-Rom spline*) na tela.
* [curve_detail()](http://py5coding.org/reference/sketch_curve_detail.html) - Define a resolução na qual as curvas são exibidas.
* [curve_point()](http://py5coding.org/reference/sketch_curve_point.html) - Avalia a curva no ponto t para os pontos a, b, c, d.
* [curve_tangent()](http://py5coding.org/reference/sketch_curve_tangent.html) - Calcula a tangente de um ponto em uma curva.
* [curve_tightness()](http://py5coding.org/reference/sketch_curve_tightness.html) - Modifica as formas criados com `curve()` e `curve_vertex()`.

#### Criando e exibindo objetos Py5Shape

* [classe Py5Shape](http://py5coding.org/reference/py5shape.html) - Tipo de dados para armazenar formas.
* [create_shape()](http://py5coding.org/reference/sketch_create_shape.html) - A função `create_shape()` é usada para definir uma nova forma.
* [load_shape()](http://py5coding.org/reference/sketch_load_shape.html) - Carrega a geometria em uma variável do tipo `Py5Shape`.
* [shape()](http://py5coding.org/reference/sketch_shape.html) - Desenha formas na janela de exibição.
* [shape_mode()](http://py5coding.org/reference/sketch_shape_mode.html) - Modifica o local a partir do qual as formas são desenhadas.

[sobe](#top)

### Cor e outros atributos gráficos

#### Criando e atribuindo cores

* [background()](http://py5coding.org/reference/sketch_background.html) - O `background()` A função define a cor usada para o fundo da janela py5.
* [clear()](http://py5coding.org/reference/sketch_clear.html) - Limpe a superfície de desenho definindo cada pixel como preto.
* [color_mode()](http://py5coding.org/reference/sketch_color_mode.html) - Altera a maneira como o py5 interpreta os dados de cores.
* [fill()](http://py5coding.org/reference/sketch_fill.html) - Define a cor usada para preencher as formas.
* [no_fill()](http://py5coding.org/reference/sketch_no_fill.html) - Desativa a geometria de preenchimento.
* [no_stroke()](http://py5coding.org/reference/sketch_no_stroke.html) - Desativa o desenho do traço (contorno).
* [stroke()](http://py5coding.org/reference/sketch_stroke.html) - Define a cor usada para desenhar linhas e bordas ao redor das formas.
* [color()](http://py5coding.org/reference/sketch_color.html) - Cria cores para armazenar em variáveis do tipo de dados color (um inteiro de 32 bits).
* [lerp_color()](http://py5coding.org/reference/sketch_lerp_color.html) - Calcula uma cor entre duas cores em um incremento específico.

#### Analisando cores

* [hex_color()](http://py5coding.org/reference/sketch_hex_color.html) - Converte um valor de cor em uma string com a representação hexadecimal da cor.
* [alpha()](http://py5coding.org/reference/sketch_alpha.html) - Extrai o valor alfa (opacidade) de uma cor, escalado para corresponder ao `color_mode()` atual.
* [blue()](http://py5coding.org/reference/sketch_blue.html) - Extrai o valor azul de uma cor, escalado para corresponder ao `color_mode()` atual.
* [brightness()](http://py5coding.org/reference/sketch_brightness.html) - Extrai o valor de brilho de uma cor.
* [green()](http://py5coding.org/reference/sketch_green.html) - Extrai o valor verde de uma cor, escalado para corresponder ao `color_mode()` atual.
* [hue()](http://py5coding.org/reference/sketch_hue.html) - Extrai o valor de matiz de uma cor.
* [red()](http://py5coding.org/reference/sketch_red.html) - Extrai o valor vermelho de uma cor, escalado para corresponder ao `color_mode()` atual.
* [saturation()](http://py5coding.org/reference/sketch_saturation.html) - Extrai o valor de saturação de uma cor.

#### Atributos de traço e controle de estilo

* [stroke_weight()](http://py5coding.org/reference/sketch_stroke_weight.html) - Define a largura do traçado usado para linhas, pontos e a borda ao redor das formas.
* [stroke_cap()](http://py5coding.org/reference/sketch_stroke_cap.html) - Define o estilo de renderização de finais de linha.
* [stroke_join()](http://py5coding.org/reference/sketch_stroke_join.html) - Define o estilo das juntas que conectam os segmentos de linha.
* [pop_style()](http://py5coding.org/reference/sketch_pop_style.html) - A função `push_style()` salva as configurações de estilo atuais e `pop_style()` restaura as configurações anteriores; essas funções são sempre usadas juntas.
* [push_style()](http://py5coding.org/reference/sketch_push_style.html) - A função `push_style()` salva as configurações de estilo atuais e `pop_style()` restaura as configurações anteriores.
* [push()](http://py5coding.org/reference/sketch_push.html) - combina `push_style()` e `push_matrix()` A função `push()` salva as configurações e transformações do estilo de desenho atual, enquanto pop( ) - restaura essas configurações.
* [pop()](http://py5coding.org/reference/sketch_pop.html) - combina `pop_style()` e `pop_matrix()` A função `pop()` restaura as configurações de estilo de desenho anteriores e transformações após `push()` os mudou.

[sobe](#top)

### Entrada de dados (*Input*)

#### Lendo arquivos

* [load_bytes()](http://py5coding.org/reference/sketch_load_bytes.html) - Carrega dados de bytes de um arquivo ou URL.
* [load_json()](http://py5coding.org/reference/sketch_load_json.html) - Carregue um arquivo de dados JSON de um arquivo ou URL.
* [load_pickle()](http://py5coding.org/reference/sketch_load_pickle.html) - Carrega um objeto Python em conserva de um arquivo.
* [load_strings()](http://py5coding.org/reference/sketch_load_strings.html) - Carrega uma lista de strings de um arquivo ou URL.
* [parse_json()](http://py5coding.org/reference/sketch_parse_json.html) - Analisa dados JSON serializados de uma string.
* [select_folder()](http://py5coding.org/reference/sketch_select_folder.html) - Abre uma caixa de diálogo de seleção de arquivo para selecionar uma pasta.
* [select_input()](http://py5coding.org/reference/sketch_select_input.html) - Abre uma caixa de diálogo do seletor de arquivos para selecionar um arquivo para entrada.

#### Variáveis do teclado

* [is_key_pressed](http://py5coding.org/reference/sketch_is_key_pressed.html) - A variável `is_key_pressed` armazena se um botão do teclado está ou não sendo pressionado no momento.
* [key](http://py5coding.org/reference/sketch_key.html) - A variável de sistema `key` traz o valor da última tecla que foi usada no teclado (seja tendo sido pressionada ou liberada). No caso de teclas especiais, que podem ser identificadas com `key_code`, o valor será a constante `CODED`.
* [key_code](http://py5coding.org/reference/sketch_key_code.html) - A variável `key_code` é usada para detectar teclas especiais, como as teclas de setas (`UP`, `DOWN`, `LEFT` e `RIGHT`), bem como `ALT`, `CONTROL`, e `SHIFT`.

#### Funções de evento do teclado

* `key_pressed()` - Se definida, esta função será chamada uma vez quando uma tecla do teclado for pressionada.
* `key_released()` - Se definida, esta função será chamada uma vez quando uma tecla do teclado for liberada.
* `key_typed()` - Se definida, esta função será chamada uma vez quando uma tecla do teclado for pressionada e liberada.

#### Variáveis do mouse

* [is_mouse_pressed](http://py5coding.org/reference/sketch_is_mouse_pressed.html) - A variável `is_mouse_pressed` armazena se um botão do mouse está ou não sendo pressionado no momento.
* [mouse_button](http://py5coding.org/reference/sketch_mouse_button.html) - Quando um botão do mouse é pressionado, o valor da variável de sistema `mouse_button` é definido como `LEFT`, `RIGHT` ou `CENTER`, dependendo de qual botão é pressionado .
* [mouse_x](http://py5coding.org/reference/sketch_mouse_x.html) - A variável de sistema `mouse_x` sempre contém a coordenada horizontal atual do mouse.
* [mouse_y](http://py5coding.org/reference/sketch_mouse_y.html) - A variável de sistema `mouse_y` sempre contém a coordenada vertical atual do mouse.
* [pmouse_x](http://py5coding.org/reference/sketch_pmouse_x.html) - A variável de sistema `pmouse_x` sempre contém a posição horizontal do mouse no quadro anterior ao quadro atual.
* [pmouse_y](http://py5coding.org/reference/sketch_pmouse_y.html) - A variável de sistema `pmouse_y` sempre contém a posição vertical do mouse no quadro anterior ao quadro atual.
* [rmouse_x](http://py5coding.org/reference/sketch_rmouse_x.html) - A coordenada horizontal atual do mouse após ativar o desenho invariante de escala.
* [rmouse_y](http://py5coding.org/reference/sketch_rmouse_y.html) - A coordenada vertical atual do mouse após ativar o desenho invariante de escala.

#### Funções de evento do mouse

* `mouse_pressed()` - Se definida, esta função será chamada uma vez quando um botão do mouse for pressionado.
* `mouse_released()` - Se definida, esta função será chamada uma vez quando um botão do mouse for pressionado.
* `mouse_clicked()` - Se definida, esta função será chamada uma vez quando um botão do mouse for clicado.
* `mouse_draged()` - Se definida, esta função será chamada várias vezes conforme o mouse for movido enquanto pressionado.
* `mouse_wheel()` - Se definida, esta função será chamada quando a roda do mouse for girada.
* `mouse_moved()` - Se definida, esta função será chamada várias vezes conforme o mouse for movido.
* `mouse_entered()` - Se definida, esta função será chamada quando o mouse entrar na área do esboço.
* `mouse_exited()` - Se definida, esta função será chamada quando o mouse sair da área do esboço.

#### Funções auxiliares de data e horário

* [day()](http://py5coding.org/reference/sketch_day.html) - Informa o dia atual, um valor de 1 a 31, consultando o relógio do seu computador.
* [hour()](http://py5coding.org/reference/sketch_hour.html) - Informa a hora atual, um valor de 0 a 23, consultando o relógio do seu computador.
* [millis()](http://py5coding.org/reference/sketch_millis.html) - Retorna o número de milissegundos (milésimos de segundo) - desde o início do programa.
* [minuto()](http://py5coding.org/reference/sketch_minute.html) - Informa o minuto atual, um valor de 0 a 59, consultando o relógio do seu computador.
* [month()](http://py5coding.org/reference/sketch_month.html) - Informa o mês atual, um valor de 1 a 12, consultando o relógio do seu computador.
* [second()](http://py5coding.org/reference/sketch_second.html) - Informa o segundo atual, um valor de 0 a 59, consultando o relógio do seu computador.
* [year()](http://py5coding.org/reference/sketch_year.html) - Informa o a ano atual, um número inteiro com 4 dígitos, consultando o relógio do seu computador.

[sobe](#top)

### Saída de dados (*Output*)

#### Escrevendo arquivos

* [begin_raw()](http://py5coding.org/reference/sketch_begin_raw.html) - - Para gravar arquivos vetoriais a partir de elementos 3D, use o `begin_raw()` e comando `end_raw()`.
* [begin_record()](http://py5coding.org/reference/sketch_begin_record.html) - - Abre um novo arquivo e todas as funções de desenho subseqüentes são repetidas neste arquivo, bem como na janela de exibição.
* [end_raw()](http://py5coding.org/reference/sketch_end_raw.html) - Complemento para begin_raw(); eles sempre devem ser usados juntos.
* [end_record()](http://py5coding.org/reference/sketch_end_record.html) - Interrompe o processo de gravação iniciado por `begin_record()` e fecha o arquivo.
* [save_bytes()](http://py5coding.org/reference/sketch_save_bytes.html) - Salvar dados de byte em um arquivo.
* [save_json()](http://py5coding.org/reference/sketch_save_json.html) - Salvar dados JSON em um arquivo.
* [save_pickle()](http://py5coding.org/reference/sketch_save_pickle.html) - Pickle um objeto Python em um arquivo.
* [save_strings()](http://py5coding.org/reference/sketch_save_strings.html) - Salve uma lista de strings em um arquivo.
* [select_output()](http://py5coding.org/reference/sketch_select_output.html) - Abre uma caixa de diálogo de seleção de arquivo para selecionar um arquivo para saída.

#### Saída de imagens

* [save()](http://py5coding.org/reference/sketch_save.html) - Salve a superfície de desenho em um arquivo de imagem.
* [save_frame()](http://py5coding.org/reference/sketch_save_frame.html) - Salve o quadro atual como uma imagem.

#### Área de texto (console)

* [println()](http://py5coding.org/reference/sketch_println.html) - Imprima texto ou outros valores no console (não na área de desenho do esboço). Semelhante ao `print()` do Python.
* [set_println_stream()](http://py5coding.org/reference/sketch_set_println_stream.html) - Personalize para onde vai a saída de `println()`.

[sobe](#top)

### Tipografia

#### Desenhando texto

* [text()](http://py5coding.org/reference/sketch_text.html) - Desenha o texto na tela, ou seja, o área de desenho de esboço.
* [text_align()](http://py5coding.org/reference/sketch_text_align.html) - Define o alinhamento atual do texto de desenho.
* [text_leading()](http://py5coding.org/reference/sketch_text_leading.html) - Define o espaçamento entre linhas de texto em unidades de pixels.
* [text_mode()](http://py5coding.org/reference/sketch_text_mode.html) - Define a maneira como o texto é desenhado na tela, seja como mapas de textura ou como geometria vetorial.
* [text_size()](http://py5coding.org/reference/sketch_text_size.html) - Define o tamanho da fonte atual.

#### Carregando e selecionando fontes

* [create_font()](http://py5coding.org/reference/sketch_create_font.html) - Converte dinamicamente uma fonte para o formato usado por py5 de um arquivo .ttf ou .otf dentro do Sketch pasta “data” ou uma fonte instalada em outro local do computador.
* [load_font()](http://py5coding.org/reference/sketch_load_font.html) - Carrega uma fonte formatada em .vlw em um objeto `Py5Font`.
* [text_font()](http://py5coding.org/reference/sketch_text_font.html) - Define a fonte atual que será desenhada com a função `text()`.

#### Métricas de texto

* [text_width()](http://py5coding.org/reference/sketch_text_width.html) - Calcula e retorna a largura de qualquer caractere ou string de texto.
* [text_ascent()](http://py5coding.org/reference/sketch_text_ascent.html) - Retorna a subida da fonte atual em seu tamanho atual.
* [text_descent()](http://py5coding.org/reference/sketch_text_descent.html) - Retorna a descida da fonte atual em seu tamanho atual.

[sobe](#top)

### Transformações do Sistema de Coordenadas

#### Operações Básicas

* [push_matrix()](http://py5coding.org/reference/sketch_push_matrix.html) - Salva a matriz de transformação que descreve a atual sistema de coordenadas na pilha de matrizes para que possa ser restaurado posteriormente com `pop_matrix()`.
* [pop_matrix()](http://py5coding.org/reference/sketch_pop_matrix.html) - Recupera a última matriz de transformação armazenada na pilha de matrizes restaurando um estado anterior do sistema de coordenadas.
* [translate()](http://py5coding.org/reference/sketch_translate.html) - Especifica uma quantidade para deslocar a origem do sistema de coordenadas, deslocando objetos desenhados na janela de exibição. Pode ser usado em 2D, `translate(x, y)`, ou 3D, `traslate(x, y, z)`.
* [rotate()](http://py5coding.org/reference/sketch_rotate.html) - Gira o sistema de coordenadas na quantidade especificada pelo parâmetro de ângulo.
* [scale()](http://py5coding.org/reference/sketch_scale.html) - Aumenta ou diminui o tamanho das formas expandindo e contraindo o sistema de coordenadas conforme o fator passado como argumento.
* [shear_x()](http://py5coding.org/reference/sketch_shear_x.html) - Inclina formas em torno do eixo X de acordo com o ângulo indicado.
* [shear_y()](http://py5coding.org/reference/sketch_shear_y.html) - Inclina formas ao redor do eixo Y de acordo com o ângulo indicado.

#### Rotações 3D

* [rotate_x()](http://py5coding.org/reference/sketch_rotate_x.html) - Gira em torno do eixo X de acordo com o ângulo indicado.
* [rotate_y()](http://py5coding.org/reference/sketch_rotate_y.html) - Gira em torno do eixo Y de acordo com o ângulo indicado.
* [rotate_z()](http://py5coding.org/reference/sketch_rotate_z.html) - Gira em torno do eixo Z de acordo com o ângulo indicado.

#### Operações com a matrix de transformações

* [apply_matrix()](http://py5coding.org/reference/sketch_apply_matrix.html) - Multiplica a matriz atual pela especificada por meio dos argumentos passados.
* [get_matrix()](http://py5coding.org/reference/sketch_get_matrix.html) - Obtenha a matriz atual como um array numpy.
* [print_matrix()](http://py5coding.org/reference/sketch_print_matrix.html) - Imprime a matriz atual na saída padrão.
* [reset_matrix()](http://py5coding.org/reference/sketch_reset_matrix.html) - Substitui a matriz atual pela matriz de identidade.
* [set_matrix()](http://py5coding.org/reference/sketch_set_matrix.html) - Defina a matriz atual para aquela especificada como argumento.

[sobe](#top)

### Ambiente do Sketch

#### Configuração e variáveis

* [size()](http://py5coding.org/reference/sketch_size.html) - Função que pode ser chamada uma vez só par definir o tamanho do sketch, largura e altura, em pixels. Fora quando usada no modo estático (static mode), deve ser usada apenas dentro de `setup()` ou `settings()`.
* [full_screen()](http://py5coding.org/reference/sketch_full_screen.html) - Faz com que o sketch tenha o tamanho total da tela do computador. Substitui `size()`.
* [width](http://py5coding.org/reference/sketch_width.html) - Variável de sistema que armazena a largura da janela de exibição.
* [height](http://py5coding.org/reference/sketch_height.html) - Variável de sistema que armazena a altura da janela de exibição.
* [smooth()](http://py5coding.org/reference/sketch_smooth.html) - Desenha toda a geometria com bordas suaves (anti-aliased). Deve ser usado logo após `size()`.
* [no_smooth()](http://py5coding.org/reference/sketch_no_smooth.html) - Desenha toda a geometria e fontes com bordas serrilhadas (aliased) - e imagens com bordas rígidas entre os pixels quando ampliadas, em vez de interpolar pixels.
* [cursor()](http://py5coding.org/reference/sketch_cursor.html) - Define o cursor para um símbolo predefinido ou uma imagem ou o torna visível se estiver oculto.
* [no_cursor()](http://py5coding.org/reference/sketch_no_cursor.html) - Oculta o cursor da visualização.
* [frame_count](http://py5coding.org/reference/sketch_frame_count.html) - A variável de sistema `frame_count` contém o número de quadros que foram exibidos desde o início do programa.
* [frame_rate()](http://py5coding.org/reference/sketch_frame_rate.html) - Especifica o número alvo de quadros a serem exibidos a cada segundo. Se o desenho de um quadro ficar lento, o alvo não será alcançado!
* [get_frame_rate()](http://py5coding.org/reference/sketch_get_frame_rate.html) - Obtenha a atual taxa de quadros por segundo do Sketch em execução.
* [display_density()](http://py5coding.org/reference/sketch_display_density.html) - Esta função retorna o número “2” se a tela for uma tela de alta densidade (chamada tela Retina no OSX ou alta dpi no Windows e Linux) - e um “1” se não.
* [pixel_density()](http://py5coding.org/reference/sketch_pixel_density.html) - Esta função possibilita que o py5 renderize usando todos os pixels em telas de alta resolução, como telas Retina da Apple e telas de alto DPI do Windows.
* [display_height](http://py5coding.org/reference/sketch_display_height.html) - Variável de sistema que armazena a altura de exibição da tela inteira.
* [display_width](http://py5coding.org/reference/sketch_display_width.html) - Variável de sistema que armazena a largura de exibição da tela inteira.
* [focused](http://py5coding.org/reference/sketch_focused.html) - Confirma se um programa py5 está “focado”, o que significa que está ativo e aceitará entradas de mouse ou teclado.
* [sketch_path()](http://py5coding.org/reference/sketch_sketch_path.html) - O caminho atual do Sketch.

#### Outros controles da janela do sketch

* [get_surface()](http://py5coding.org/reference/sketch_get_surface.html) - Obtenha o objeto `Py5Surface` usado para a janela do Sketch.
* [pixel_height](http://py5coding.org/reference/sketch_pixel_height.html) - Altura da janela de exibição em pixels.
* [pixel_width](http://py5coding.org/reference/sketch_pixel_width.html) - Largura da janela de exibição em pixels.
* [ratio_left](http://py5coding.org/reference/sketch_ratio_left.html) - Largura da seção esquerda da janela que não se ajusta à proporção desejada de um esboço invariante em escala.
* [ratio_scale](http://py5coding.org/reference/sketch_ratio_scale.html) - Fator de escala usado para manter desenho invariante de escala.
* [ratio_top](http://py5coding.org/reference/sketch_ratio_top.html) - Altura da seção superior da janela que não se ajusta à proporção desejada de um esboço invariante em escala.
* [rheight](http://py5coding.org/reference/sketch_rheight.html) - A altura da janela de exibição de escala invariante.
* [rwidth](http://py5coding.org/reference/sketch_rwidth.html) - A largura da janela de exibição invariante de escala.
* [window_move()](http://py5coding.org/reference/sketch_window_move.html) - Defina a localização da janela do Sketch.
* [window_ratio()](http://py5coding.org/reference/sketch_window_ratio.html) - Defina uma proporção de janela para permitir o desenho invariante de escala.
* [window_resizable()](http://py5coding.org/reference/sketch_window_resizable.html) - Defina a janela Sketch como redimensionável pelo usuário.
* [window_resize()](http://py5coding.org/reference/sketch_window_resize.html) - Defina uma nova largura e altura para a janela Sketch.
* [window_title()](http://py5coding.org/reference/sketch_window_title.html) - Defina o título da janela Sketch.
* [window_x](http://py5coding.org/reference/sketch_window_x.html) - A coordenada x da localização atual da janela.
* [window_y](http://py5coding.org/reference/sketch_window_y.html) - A coordenada y do local da janela atual.

[sobe](#top)

### Relacionadas à matemática

#### Cálculo

* [ceil()](http://py5coding.org/reference/sketch_ceil.html) - Calcula o valor int mais próximo que é maior que ou igual ao valor do parâmetro.
* [constrain()](http://py5coding.org/reference/sketch_constrain.html) - Restringe um valor para não exceder um valor máximo e mínimo.
* [dist()](http://py5coding.org/reference/sketch_dist.html) - Calcula a distância entre dois pontos.
* [exp()](http://py5coding.org/reference/sketch_exp.html) - Retorna o número de Euler e (2,71828…) - elevado à potência do parâmetro n.
* [floor()](http://py5coding.org/reference/sketch_floor.html) - Calcula o valor int mais próximo que é menor ou igual ao valor do parâmetro.
* [lerp()](http://py5coding.org/reference/sketch_lerp.html) - Calcula um número entre dois números em um incremento específico.
* [log()](http://py5coding.org/reference/sketch_log.html) - Calcula o logaritmo natural (o logaritmo base-e) - de um número.
* [mag()](http://py5coding.org/reference/sketch_mag.html) - Calcula a magnitude (ou comprimento) - de um vetor.
* [norm()](http://py5coding.org/reference/sketch_norm.html) - Normaliza um número de outro intervalo em um valor entre 0 e 1.
* [remap()](http://py5coding.org/reference/sketch_remap.html) - Remapeia (transforma ou traduz) um número de um intervalo para outro.
* [sq()](http://py5coding.org/reference/sketch_sq.html) - Eleva um número ao quadrado (multiplica um número por si mesmo).
* [sqrt()](http://py5coding.org/reference/sketch_sqrt.html) - Calcula a raiz quadrada de um número.
* [Py5Vector class](http://py5coding.org/reference/py5vector.html) - Classe para descrever um vetor 2D, 3D ou 4D.

#### Aleatoriedade (*Random*)

* [noise()](http://py5coding.org/reference/sketch_noise.html) - Gere valores de ruído pseudoaleatórios para coordenadas específicas usando o algoritmo de ruído do Processing.
* [noise_detail()](http://py5coding.org/reference/sketch_noise_detail.html) - Ajusta o caráter e o nível de detalhe do algoritmo de ruído de Processing, produzido pela função `noise()`.
* [noise_seed()](http://py5coding.org/reference/sketch_noise_seed.html) - Define o valor inicial para `noise()`.
* [np_random](http://py5coding.org/reference/sketch_np_random.html) - Acesse o gerador de números aleatórios numpy que o py5 usa para fornecer a funcionalidade de números aleatórios.
* [os_noise()](http://py5coding.org/reference/sketch_os_noise.html) - Gere valores de ruído pseudo-aleatórios para coordenadas específicas usando o algoritmo OpenSimplex 2 (versão suave / SuperSimplex).
* [os_noise_seed()](http://py5coding.org/reference/sketch_os_noise_seed.html) - Define o valor de semente para `os_noise()`.
* [random()](http://py5coding.org/reference/sketch_random.html) - Gera números aleatórios.
* [random_choice()](http://py5coding.org/reference/sketch_random_choice.html) - Selecione itens aleatórios de uma lista.
* [random_gaussian()](http://py5coding.org/reference/sketch_random_gaussian.html) - Gera valores gaussianos aleatórios.
* [random_int()](http://py5coding.org/reference/sketch_random_int.html) - Gera inteiros aleatórios.
* [random_seed()](http://py5coding.org/reference/sketch_random_seed.html) - Define o valor de semente para as funções aleatórias de py5.

#### Trigonometria

* [acos()](http://py5coding.org/reference/sketch_acos.html) - O inverso de `cos()` retorna o arco cosseno de um valor.
* [asin()](http://py5coding.org/reference/sketch_asin.html) - O inverso de `sin()` retorna o arco seno de um valor.
* [atan()](http://py5coding.org/reference/sketch_atan.html) - O inverso de `tan()` retorna o arco tangente de um valor.
* [atan2()](http://py5coding.org/reference/sketch_atan2.html) - Calcula a inclinação (um ângulo em radianos) do segmento que liga um ponto à origem. Exemplo de uso: `ang = atan2(ya - yb, xa - xb)` (para um sengmento com extremidades em `xa, ya` e `xb, yb`).
* [cos()](http://py5coding.org/reference/sketch_cos.html) - Calcula o cosseno de um ângulo.
* [degrees()](http://py5coding.org/reference/sketch_degrees.html) - Converte uma medida em radianos em seu valor correspondente em graus.
* [radians()](http://py5coding.org/reference/sketch_radians.html) - Converte uma medida de grau em seu valor correspondente em radianos.
* [sin()](http://py5coding.org/reference/sketch_sin.html) - Calcula o seno de um ângulo.
* [tan()](http://py5coding.org/reference/sketch_tan.html) - Calculates the ratio of the sine and cosine of an angle.

[sobe](#top)

### Trabalhando com imagens

#### Carregando e exibindo

* [image()](http://py5coding.org/reference/sketch_image.html) - A função `image()` desenha uma imagem na janela de exibição.
* [image_mode()](http://py5coding.org/reference/sketch_image_mode.html) - Modifica o local de onde as imagens são desenhadas alterando a maneira como os parâmetros fornecidos a `image()` são interpretados.
* [load_image()](http://py5coding.org/reference/sketch_load_image.html) - Carrega uma imagem em uma variável do tipo `Py5Image`.
* [no_tint()](http://py5coding.org/reference/sketch_no_tint.html) - Remove o valor de preenchimento atual para exibir imagens e reverte para exibir imagens com seus matizes originais.
* [tint()](http://py5coding.org/reference/sketch_tint.html) - Define o valor de preenchimento para exibir imagens.

#### Pixels

* [apply_filter()](http://py5coding.org/reference/sketch_apply_filter.html) - Filtra a janela de exibição usando um filtro predefinido ou com um sombreador personalizado.
* [blend()](http://py5coding.org/reference/sketch_blend.html) - Combina uma região de pixels de uma imagem em outra (ou nela mesma novamente) - com suporte total ao canal alfa.
* [copy()](http://py5coding.org/reference/sketch_copy.html) - Copia uma região de pixels da janela de exibição para outra área da janela de exibição e copia uma região de pixels de uma imagem usada como src_img parâmetro na janela de exibição.
* [get()](http://py5coding.org/reference/sketch_get.html) - Lê a cor de qualquer pixel ou captura uma seção da superfície de desenho.
* [load_np_pixels()](http://py5coding.org/reference/sketch_load_np_pixels.html) - Carrega os dados de pixel da janela de exibição atual na matriz np_pixels[].
* [load_pixels()](http://py5coding.org/reference/sketch_load_pixels.html) - Carrega os dados de pixel da janela de exibição atual na matriz pixels[].
* [np_pixels[]](http://py5coding.org/reference/sketch_np_pixels.html) - A matriz np_pixels[] contém os valores para todos os pixels na janela de exibição.
* [pixels[]](http://py5coding.org/reference/sketch_pixels.html) - A matriz pixels[] contém os valores para todos os pixels na janela de exibição.
* [set_np_pixels()](http://py5coding.org/reference/sketch_set_np_pixels.html) - Defina todo o conteúdo de np_pixels[] para o conteúdo de outro array numpy dimensionado e digitado adequadamente.
* [update_np_pixels()](http://py5coding.org/reference/sketch_update_np_pixels.html) - Atualiza a janela de exibição com os dados na matriz np_pixels[].
* [update_pixels()](http://py5coding.org/reference/sketch_update_pixels.html) - Atualiza a janela de exibição com os dados na matriz pixels[].

#### Texturas

* [texture()](http://py5coding.org/reference/sketch_texture.html) - Define uma textura a ser aplicada aos pontos de vértice.
* [texture_mode()](http://py5coding.org/reference/sketch_texture_mode.html) - Define o espaço de coordenadas para mapeamento de textura.
* [texture_wrap()](http://py5coding.org/reference/sketch_texture_wrap.html) - Define se as texturas se repetem ou desenham uma vez dentro de um mapa de textura.

#### Objetos de imagem

* [classe Py5Image](https://py5coding.org/reference/py5image.html) - Tipo de dados para armazenar imagens.
* [create_image()](http://py5coding.org/reference/sketch_create_image.html) - Cria um novo `Py5Image` (o tipo de dados para armazenar imagens).
* [convert_image()](http://py5coding.org/reference/sketch_convert_image.html) - Converte objetos de imagem não-py5 em objetos `Py5Image`.
* [create_image_from_numpy()](http://py5coding.org/reference/sketch_create_image_from_numpy.html) - Converte um array numpy em um objeto `Py5Image`.
* [request_image()](http://py5coding.org/reference/sketch_request_image.html) - Use um objeto Py5Promise para carregar uma imagem em uma variável do tipo `Py5Image`.

[sobe](#top)

### Cena 3D

#### Câmera

* [begin_camera()](http://py5coding.org/reference/sketch_begin_camera.html) - As funções `begin_camera()` e `end_camera()` permitem personalização avançada do espaço da câmera.
* [camera()](http://py5coding.org/reference/sketch_camera.html) - Define a posição da câmera definindo a posição do olho, o centro da cena e qual eixo está voltado para cima.
* [end_camera()](http://py5coding.org/reference/sketch_end_camera.html) - Os métodos `begin_camera()` e `end_camera()` permitem personalização avançada do espaço da câmera.
* [frustum()](http://py5coding.org/reference/sketch_frustum.html) - Define uma matriz de perspectiva conforme definido pelos parâmetros.
* [ortho()](http://py5coding.org/reference/sketch_ortho.html) - Define uma projeção ortográfica e define um volume de recorte paralelo.
* [perspective()](http://py5coding.org/reference/sketch_perspective.html) - Define uma projeção em perspectiva aplicando o encurtamento, fazendo com que os objetos distantes pareçam menores do que os mais próximos.
* [print_camera()](http://py5coding.org/reference/sketch_print_camera.html) - Imprime a matriz da câmera atual na saída padrão.
* [print_projection()](http://py5coding.org/reference/sketch_print_projection.html) - Imprime a matriz de projeção atual na saída padrão.

#### Coordenadas

* [model_x()](http://py5coding.org/reference/sketch_model_x.html) - Retorna a posição tridimensional X, Y, Z no espaço do modelo.
* [model_y()](http://py5coding.org/reference/sketch_model_y.html) - Retorna a posição tridimensional X, Y, Z no espaço do modelo.
* [model_z()](http://py5coding.org/reference/sketch_model_z.html) - Retorna a posição tridimensional X, Y, Z no espaço do modelo.
* [screen_x()](http://py5coding.org/reference/sketch_screen_x.html) - Toma uma posição X, Y, Z tridimensional e retorna o valor X para onde ele aparecerá em uma tela (bidimensional) - .
* [screen_y()](http://py5coding.org/reference/sketch_screen_y.html) - Toma uma posição X, Y, Z tridimensional e retorna o valor Y para onde ele aparecerá em uma tela (bidimensional) - .
* [screen_z()](http://py5coding.org/reference/sketch_screen_z.html) - Toma uma posição X, Y, Z tridimensional e retorna o valor Z para onde ele aparecerá em uma tela (bidimensional) - .

#### Luzes

* [ambient_light()](http://py5coding.org/reference/sketch_ambient_light.html) - Adiciona uma luz ambiente.
* [directional_light()](http://py5coding.org/reference/sketch_directional_light.html) - Adiciona uma luz direcional.
* [light_falloff()](http://py5coding.org/reference/sketch_light_falloff.html) - Define as taxas de queda para luzes pontuais, pontuais e ambientes.
* [light_specular()](http://py5coding.org/reference/sketch_light_specular.html) - Define a cor especular das luzes.
* [lights()](http://py5coding.org/reference/sketch_lights.html) - Define a luz ambiente padrão, luz direcional, queda e valores especulares.
* [no_lights()](http://py5coding.org/reference/sketch_no_lights.html) - Desative toda a iluminação.
* [normal()](http://py5coding.org/reference/sketch_normal.html) - Define o vetor normal atual.
* [point_light()](http://py5coding.org/reference/sketch_point_light.html) - Adiciona um ponto de luz.
* [spot_light()](http://py5coding.org/reference/sketch_spot_light.html) - Adiciona uma luz pontual.

#### Propriedade dos materiais

* [ambient()](http://py5coding.org/reference/sketch_ambient.html) - Define a refletância do ambiente para formas desenhadas na tela.
* [emissive()](http://py5coding.org/reference/sketch_emissive.html) - Define a cor emissiva do material usado para desenhar formas desenhadas na tela.
* [shininess()](http://py5coding.org/reference/sketch_shininess.html) - Define a quantidade de brilho na superfície das formas.
* [specular()](http://py5coding.org/reference/sketch_specular.html) - Define a cor especular dos materiais usados para formas desenhadas na tela, que define a cor dos destaques.

[sobe](#top)

### Apresentação (*Rendering*)

#### `Contexto gráfico` 

* [blend_mode()](http://py5coding.org/reference/sketch_blend_mode.html) - Combina os pixels na janela de exibição de acordo com um modo definido.
* [clip()](http://py5coding.org/reference/sketch_clip.html) - Limita a renderização aos limites de um retângulo definido pelos parâmetros.
* [create_graphics()](http://py5coding.org/reference/sketch_create_graphics.html) - Cria e retorna um novo objeto `Py5Graphics`.
* [flush()](http://py5coding.org/reference/sketch_flush.html) - Flush comandos de desenho para o renderizador.
* [g](http://py5coding.org/reference/sketch_g.html) - O objeto `Py5Graphics` usado pelo Sketch.
* [get_graphics()](http://py5coding.org/reference/sketch_get_graphics.html) - Obtenha o objeto `Py5Graphics` usado pelo Sketch.
* [hint()](http://py5coding.org/reference/sketch_hint.html) - Esta função é usada para ativar ou desativar recursos especiais que controlam como os gráficos são desenhados.
* [no_clip()](http://py5coding.org/reference/sketch_no_clip.html) - Desativa o recorte iniciado anteriormente pela função `clip()`.

#### Shaders

* [load_shader()](http://py5coding.org/reference/sketch_load_shader.html) - Carrega um shader em um objeto `Py5Shader`.
* [reset_shader()](http://py5coding.org/reference/sketch_reset_shader.html) - Restaura os shaders padrão.
* [shader()](http://py5coding.org/reference/sketch_shader.html)Aplica o shader especificado pelos parâmetros.

[sobe](#top)

### Execução do sketch

#### Controle do laço de repetição *draw*

* [loop()](http://py5coding.org/reference/sketch_loop.html) - Por padrão, py5 percorre draw( ) - continuamente, executando o código dentro dele.
* [no_loop()](http://py5coding.org/reference/sketch_no_loop.html) - Impede que py5 execute continuamente o código dentro de `draw()`.
* [redraw()](http://py5coding.org/reference/sketch_redraw.html) - Executa o código dentro de `draw()` uma vez.
* [exit_sketch()](http://py5coding.org/reference/sketch_exit_sketch.html) - Sai/pára/sai do programa.
* `exiting()` - Se definida, esta função será executada depois que o sketch parar.

#### Controle avançado da execução

* [finished](http://py5coding.org/reference/sketch_finished.html) - Variável booleana que reflete se o Sketch parou permanentemente.
* [hot_reload_draw()](http://py5coding.org/reference/sketch_hot_reload_draw.html) - Execute um hot reload da função de desenho do Sketch.
* [is_dead](http://py5coding.org/reference/sketch_is_dead.html) - Valor booleano que reflete se o Sketch foi executado e agora parou.
* [is_dead_from_error](http://py5coding.org/reference/sketch_is_dead_from_error.html) - Valor booleano que reflete se o Sketch foi executado e agora parou devido a um erro.
* [is_ready](http://py5coding.org/reference/sketch_is_ready.html) - Valor booleano que reflete se o Sketch está no estado pronto.
* [is_running](http://py5coding.org/reference/sketch_is_running.html) - Valor booleano que reflete se o Sketch está no estado de execução.
* [pargs](http://py5coding.org/reference/sketch_pargs.html) - lista de valores passados para o Sketch quando é executado via `run_sketch()` 

#### Análise da Performance (*Performance Profiling*)

* [print_line_profiler_stats()](http://py5coding.org/reference/sketch_print_line_profiler_stats.html) - Imprima as estatísticas do analisador (*profiler*) criado com `profile_draw()` ou `profile_functions()`.
* [profile_draw()](http://py5coding.org/reference/sketch_profile_draw.html) - Cria uma estimativa dos tempos de execução da função `draw()` com um *profiler*.
* [profile_functions()](http://py5coding.org/reference/sketch_profile_functions.html) - Cria uma estatística dos tempos de execução das funções do Sketch com um *profiler*.

#### Linhas de execução (*Threading*)

* [has_thread()](http://py5coding.org/reference/sketch_has_thread.html) - Determina se um *thread* (linha de execução) de determinado nome existe e está em execução no momento.
* [join_thread()](http://py5coding.org/reference/sketch_join_thread.html) - Atrela trecho do código à um *thread* indicado, isto é, se essa linha de execução existir o comando aguarda até que ela termine.
* [launch_promise_thread()](http://py5coding.org/reference/sketch_launch_promise_thread.html) - Crie um objeto `Py5Promise` que armazenará o resultado retornado de uma função quando essa função for concluída.
* [launch_repeating_thread()](http://py5coding.org/reference/sketch_launch_repeating_thread.html) - Inicie um novo *thread* que executará repetidamente uma função em paralelo com seu código do Sketch.
* [launch_thread()](http://py5coding.org/reference/sketch_launch_thread.html) - Inicie um novo thread para executar uma função em paralelo com seu código do Sketch.
* [list_threads()](http://py5coding.org/reference/sketch_list_threads.html) - Liste os nomes de todos os *threads* em execução no momento.
* [stop_all_threads()](http://py5coding.org/reference/sketch_stop_all_threads.html) - Interrompa todos os *threads* em execução.
* [stop_thread()](http://py5coding.org/reference/sketch_stop_thread.html) - Pare um *thread* de um determinado nome.

#### Constantes da JVM

* [java_platform](http://py5coding.org/reference/sketch_java_platform.html) - Versão do Java atualmente usada pelo py5.
* [java_version_name](http://py5coding.org/reference/sketch_java_version_name.html) - Nome da versão do Java atualmente em uso pelo py5.

[sobe](#top)

### Classes e outras ferramentas do py5

#### Classes

* [Py5Graphics](http://py5coding.org/reference/py5graphics.html) - Gráficos principais e contexto de renderização, bem como a implementação básica da API para o "núcleo" do Processing.
* [Py5Image](http://py5coding.org/reference/py5image.html) - Um tipo de dados para armazenar imagens. Permite carregar, converter e exibir formatos de imagem externos, bem como manipulação eficiente de pixels como matrizes NumPy.
* [Py5Shape](http://py5coding.org/reference/py5shape.html) - Tipo de dados para armazenar formas. Permite carregar e exibir formas SVG (Scalable Vector Graphics) e OBJ.
* [Py5Shader](http://py5coding.org/reference/py5shader.html) - Esta classe encapsula um programa de shader GLSL, incluindo um vértice e um fragment shader.
* [Py5Surface](http://py5coding.org/reference/py5surface.html) - O objeto `Py5Surface` é a janela na qual o py5 desenha as animações. Use-o para interagir com a janela e alterar algumas de suas características, como o título ou a localização.
* [Py5Font](http://py5coding.org/reference/py5font.html) - `Py5Font` é a classe de fonte tipográfica para o py5. Para criar uma fonte para usar com py5, use `create_font_file()`. Isso criará uma fonte no formato que o py5 requer.
* [Py5MouseEvent](http://py5coding.org/reference/py5mouseevent.html) - Tipo de dados para fornecer informações sobre eventos de mouse. Uma instância dessa classe será passada para funções de evento de mouse definidas pelo usuário. Útil para capturar toda a atividade do mouse de um usuário.
* [Py5KeyEvent](http://py5coding.org/reference/py5keyevent.html) - Tipo de dados para fornecer informações sobre a chave. Útil para capturar toda a atividade de teclado de um usuário.
* [Py5Vector](http://py5coding.org/reference/py5vector.html) - Classe para descrever um vetor 2D, 3D ou 4D. Um vetor é uma entidade que tem uma magnitude e uma direção. Este tipo de dados armazena os componentes do vetor como um conjunto de coordenadas.

#### Ferramentas

* [Py5 Magics](http://py5coding.org/reference/py5vector.html) - Os py5 Magics são "meta-comandos" do Jupyter Notebook que podem estar dentro dos Jupyter Notebooks para aprimorar a capacidade do py5 de funcionar no notebook. As mágicas do py5 permitirão que os usuários criem Sketches e incorporem os resultados no Notebook sem definir nenhuma função ou chamar a função `size()`.
* [Py5 Tools](http://py5coding.org/reference/py5tools.html) - As ferramentas py5 são funções utilitárias extras não diretamente relacionadas à criação de esboços que ajudam a facilitar o uso de py5. Por exemplo, você pode usá-los para adicionar arquivos jar ao caminho de classe Java antes de importar py5.
* [Py5 Functions](http://py5coding.org/reference/py5functions.html) - As funções py5 são funções utilitárias extras que tornam o py5 mais fácil de usar. Por exemplo, você pode usá-los para os arquivos de fontes tipográficas `.vlw` do Processing sem precisar usar o IDE do Processing.

[sobe](#top)
