# Como exportar uma imagem

Um quadro (*frame*) é o resultado visual produzido na área de desenho do *sketch* no Processing em um determinado momento. Para salvar um quadro em um arquivo bitmap/raster, como por exemplo PNG, TIF ou JPG, usamos a função `save_frame()`.

Passamos como argumento o nome do arquivo que deve ser salvo, e a extensão de três letras após o ponto no nome do arquivo indica o formato que deve ser salvo. Por exemplo `save_frame("imagem.jpg")` salva um arquivo JPG na pasta do *sketch*. Se utilizarmos alguns caracteres "#" no nome do arquivo eles serão substituídos pelo número do *frame*.

## Um exemplo simples

O código abaixo exemplifica como salvar uma imagem PNG de um quadro. Quando uma tecla é pressionada, é executada a função `key_pressed()` e se for identificada a tecla "s" (`key == 's'`) é execuatada a função `save_frame()`, que grava uma imagem.


```python
def setup():
    size(500, 500)

def draw():
    background(0, 0, 200)
    x, y = random(width), random(height)
    circle(x, y, 100)


def keyPressed():
    if key == 's':
        save_frame("frame###.png")
        print("PNG salvo")
```

Resulta em arquivo semelhante a este "frame421.png" na pasta do *sketch*:

![frame421.png](assets/frame.png)

## `save_frame()` dentro do `draw()`

Usar `save_frame()`dentro do laço principal `draw()` torna o *sketch* muito mais lento, pois salva uma imagem a cada *frame* do draw. Acrescentando alguns carateres `#` no nome do arquivo a ser salvo, um número grande de quadros pode ser salvo em alguns segundos, o que deve ser feito com cuidado (pode entupir o disco do seu computador). Normalmente é criada uma condição que interrompe o sketch com `exit()` ou que só permite salvar um certo número de imagens(no exemplo abaixo, um quadro a cada 5 com `frame_count % 5 == 0 and frame_count <= 100`).

```python


def draw():
    # desenho
    ...
    # salva só a cada 5 frames até o frame 100
    if frame_Count % 5 == 0 and frame_count <= 100:
        save_frame("imagem###.png")
```

Neste outro exemplo, data e horário no nome do arquivo e interrupção do sketch.

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

## Exportando em resolução maior do que a da tela

Um objeto * Py5Graphics * é uma espécie de tela virtual que pode gravar o resultado do desenho em paralelo à área de desenho normal, podendo também receber ajustes especiais aplicados apenas a esse objeto-tela, como `.scale()` no exemplo abaixo, o que permite exportar uma imagem 10 vezes maior do que a mostrada na tela.

### Exportando um sketch estático

```python
def setup():
    size(50, 50)
    # preparo da gravação
    fator_escala = 10
    f = create_graphics(width * fator_escala, height * fator_escala)
    begin_record(f)  # início da gravação
    # ajustes que só afetam o arquivo sendo gravado
    f.scale(fator_escala)
    f.stroke_weight(0.5)
    # instruções que afetam a tela e o arquivo
    background(0, 200, 0)
    circle(6, 6, 10)
    # fim da gravação
    end_record()
    f.save("exportando_imagem_ampliada.png")
```
Repare que a espessura de linha está sendo ajustada para um valor diferente com `f.strokeWeight()`. Sem o ajuste ela ficaria 10 vezes maior no arquivo do que na área de desenho normal(acompanhando e resto da imagem) e desta maneira ela fica apenas 5 vezes maior no arquivo.

![](assets/exportando_imagem_ampliada.png)

### Exportando um único frame de um sketch interativo

```python
fator_escala = 10
salvar_png = False

def setup():
    size(200, 200)  # com fator 10, vira 2000px x 2000px

def draw():
    global salvar_png
    if salvar_png:
        output_buffer = create_graphics(width * fator_escala,
                                        height * fator_escala)
        begin_record(output_buffer)
        output_buffer.scale(fator_escala)   
        file_name = f'{frame_count}.png'
    # seu desenho vai aqui
    background(0, 100, 0) 
    circle(mouse_x, mouse_y, width / 2)
    if salvar_png:
        salvar_png = False
        end_record()
        output_buffer.save(file_name)
        print(f'{file_name} salvo.')

def key_pressed():
    global salvar_png
    if key == 'h':
        salvar_png = True
```
![3069](https://user-images.githubusercontent.com/3694604/233481566-b1757f01-f477-4663-b02e-8b60f5471a5d.png)

## Exportando apenas parte da tela (e em um local selecionado!)

No exemplo a seguir, vamos usar a estratégia de desenhar em um objeto `Py5Graphics` como no exemplo anterior, e demonstrar também as seguintes possibilidades:

- Salvar um frame de um sketch interativo(com `draw()`)
- Salvar apenas parte da imagem na tela(útil para remover elementos de interface/controle)
- Acrescentar ajustes ou elementos apenas na imagem salva
- Escolher onde salvar a imagem(fora da pasta do sketch).

![image](https://user-images.githubusercontent.com/3694604/233478591-07162252-2e31-492a-9342-7abf025be26c.png)

Ambos os textos da imagem acima, em preto e em branco, não estarão presentes no arquivo salvo, assim como toda a àrea cinza em volta ou qualquer elemento nela desenhado.

```python
salvar = False

def setup():
    size(500, 500)
    global w, h, margem, f
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
    text('Só na tela', 0, -20)
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
        f.text('Só na gravação', 20, 300)
        end_record()
        salvar = False
        # em vez de f.save("arquivo_na_pasta_do_sketch.png")
        # vamos usar esta função selectOtuput que chama por nós salva_arquivo()
        select_output("Escolha onde Salvar", salva_arquivo)
    # instruções depois do end_record também aparecem só na tela
    fill(255)
    text('Também só na tela', 10, 20)
```

![](assets/exportando_parcial_1.png)

Note o texto em vermelho que só aparece no arquivo salvo.

# Assuntos relacionados

- [Desenhando fora da vista com *Py5Graphics* (*offscreen buffer*)](offscreen_buffer.md)
- [Exportando PDF](exportando_pdf.md)
- [Exportando SVG](exportando_Svg.md)
