# Como exportar uma imagem

um * frame * é o resultado visual produzido na área de desenho do * sketch * no processing em um determinado momento. para salvar um * frame * em um arquivo bitmap/raster, como por exemplo PNG, TIF ou JPG, usamos a função `save_frame()`.

passamos como argumento o nome do arquivo que deve ser salvo, e a extensão de três letras após o ponto no nome do arquivo indica o formato que deve ser salvo. por exemplo `save_frame("imagem.jpg")` salva um arquivo JPG na pasta do * sketch*. se utilizarmos alguns caracteres "#" no nome do arquivo eles serão substituídos pelo número do * frame*.

O código abaixo exemplifica como salvar uma imagem PNG de um frame. quando uma tecla é pressionada, é executada a função `key_pressed()` e se for identificada a tecla "s" (`key == 's'`) é execuatada a função save_frame(), que grava uma imagem na pasta do sketch.

# Um exemplo bem simples

O código abaixo exemplifica como salvar uma imagem PNG de um frame. quando uma tecla é pressionada, é executada a função `key_pressed()` e se for identificada a tecla "s" (`key == 's'`) é executada a função `save_frame()`, que grava uma imagem na pasta do * sketch*.

```python


def setup():
    size(500, 500)


def draw():
    background(0, 0, 200)
    x, y = random(width), random(height)
    circle(x, y, 100)


def key_pressed():
    if key == 's':
        save_frame("frame.png")
        print("PNG salvo")


```
reulta no aquivo "frame421.png" na pasta do * sketch*:

![frame421.png](assets/frame.png)

# `saveFrame()` dentro do `draw()`

# `` no nome do arquivo a ser salvo,  um número grande de quadros pode ser salvo em alguns segundos, o que deve ser feito com cuidado (pode entupir o disco do seu computador).
usar `save_frame()`dentro do laço principal `draw()` torna o * sketch * muito mais lento, pois salva uma imagem a cada * frame * do draw. acrescentando carateres ``

normalmente é criada uma condição que interrompe o sketch com `exit()` ou que só permite salvar um certo número de imagens(no exemplo abaixo, um quadro a cada 5 com `frame_count % 5 == 0`).

```python


def draw():
    # desenho
    ...
    # salva só a cada 5 frames até o frame 100
    if frame_count % 5 == 0 and frame_count <= 100:
        save_frame("imagem###.png")


```

neste outro exemplo, data e horário no nome do arquivo e interrupção do sketch.

```python
nome_output = '{}-{}-{}-{}-{}-{}-frame###.png'.format(
    year(), month(), day(), hour(), minute(), second())


def draw():
    # desenho
    ...
    save_frame(nome_output)
    if frame_count > 100:
        exit()  # interrompe a execução do sketch


```

# Exportando em resolução maior do que a da tela

um objeto * Py5Graphics * é uma espécie de tela virtual que pode gravar o resultado do desenho em paralelo à área de desenho normal, podendo também receber ajustes especiais aplicados apenas a esse objeto-tela, como `.scale()` no exemplo abaixo, o que permite exportar uma imagem 10 vezes maior do que a mostrada na tela.

```python


def setup():
    size(50, 50)
    # preparo da gravação
    scale = 10
    f = create_graphics(width * scale, height * scale)
    begin_record(f)  # início da gravação
    # ajustes que só afetam o arquivo sendo gravado
    f.scale(scale)
    f.stroke_weight(.5)

    # instruções que afentam a tela e o arquivo
    # sem background após o beginRecord o arquivo fica com fundo transparente!
    background(0, 200, 0)
    circle(6, 6, 10)

    # fim da gravação
    end_record()
    f.save("exportando_imagem_ampliada.png")


```
repare que a espessura de linha está sendo ajustada para um valor diferente com `f.stroke_weight()`. sem o ajuste ela ficaria 10 vezes maior no arquivo do que na área de desenho normal(acompanhando e resto da imagem) e desta maneira ela fica apenas 5 vezes maior no arquivo.

![](assets/exportando_imagem_ampliada.png)

# Exportando apenas parte da tela (e em um local selecionado!)

no exemplo a seguir, vamos usar a estratégia de desenhar em um objeto `Py5Graphics` como no exemplo anterior, e demonstrar também as seguintes possibilidades:

* salvar um frame de um skeetch interativo(com `draw()`)

- salvar apenas parte da imagem na tela(útil para remover elementos de interface/controle)
- acrescentar ajustes ou elementos apenas na imagem salva
- escolher onde salvar a imagem(fora da pasta do sketch).

![](assets/exportando_parcial_0.png)

ambos os textos da imagem acima, em preto e em branco, não estarão presentes no arquivo salvo, assim como toda a àrea cinza em volta ou qualquer elemento nela desenhado.

```python
salvar = False


def setup():
    size(500, 500)
    global w, h, offset, f
    # dimensões da imagem e um deslocamento / margem
    w, h, margem = 400, 400, 50
    f = create_graphics(w, h)


def draw():
    global salvar
    translate(margem, margem)  # 0, 0 no canto da imagem a ser salva
    # instruções antes do beginRecord só aparecem na tela
    # Se não for criado fundo depois de beginRecord, no arquivo fundo
    # transparente
    background(100)  # fundo geral na tela apenas
    fill(0)
    text(u'Só na tela', 0, -20)
    # início da gravação
    if salvar:
        begin_record(f)  # início da gravação
    # As instruções aqui aparecem na tela e no arquivo
    no_stroke()
    fill(0, 0, 200)
    rect(0, 0, w, h)  # fundo no arquivo usando um retângulo
    fill(0, 200, 0)
    circle(100, 100, 100)
    # fim da gravação
    if salvar:
        # instruções com 'f.' aparecem só na gravação
        f.fill(255, 0, 0)
        f.text(u'Só na gravação', 20, 300)
        end_record()
        salvar = False
        # em vez de f.save("arquivo_na_pasta_do_sketch.png")
        # vamos usar esta função selectOtuput que chama por nós salva_arquivo()
        select_output("Escolha onde Salvar", "salva_arquivo")
    # instruções depois do endRecord também aparecem só na tela
    fill(255)
    text(u'Também só na tela', 10, 20)


def key_pressed():
    global salvar
    if key == 's':
        salvar = True


def salva_arquivo(selection):
    """
    um alerta: cuidado! possíveis 'falhas' nesta função,
    como erros de gravação (por disco cheio, ou falta de
    permissão para gravar em um diretório), mas também
    qualquer outros bugs que você introduzir ampliando
    este código, vão interromper esta linha de execução
    silencionamente, sem mostrar nenhum aviso de erro :(
    """
    if selection is not None:
        # importante usar unicode() em vez de str() aqui!
        nome = unicode(selection)
        if not nome.lower().endswith('.png'):
            nome += '.png'
        f.save(nome)
        print("Imagem, salva em: " + nome)
    else:
        print("operação de salvar cancelada")


```

![](assets/exportando_parcial_1.png)

note o texto em vermelho que só aparece no arquivo salvo.

# Assuntos relacionados

- [desenhando fora da vista com * Py5Graphics * (*offscreen buffer*)](offscreen_buffer.md)
- [exportando PDF](exportando_pdf.md)
- [exportando SVG](exportando__svg.md)
