# Input com teclado e mouse - entradas de dados

No py5, o teclado e o mouse são duas as principais formas de entrada de dados. Em outra ocasião trataremos da leitura de arquivos e outras fontes de dados. Vejamos aqui maneiras de se obter informações sobre o movimento e cliques do mouse, assim como saber sobre as teclas sendo pressionadas no teclado.

## Variáveis de sistema

As variáveis de sistema como `mouse_x`, `mouse_y` e `is_mouse_pressed` oferecem a todo instante informações sobre o estado do mouse. Podem ser consultadas em qualquer lugar do programa e são vistas frequentemente em condicionais dentro do bloco de `draw()`.

De maneira análoga, `is_key_pressed`, `key` e `key_code` tratam do estado do teclado. A variável `is_key_pressed` indica se há uma tecla pressionada naquele instante, `key` indica qual foi a última tecla 'comum' pressionada, se for igual à constante `CODED` então é possível consultar `key_code` para saber qual foi a última tecla 'codificada', a comparando, por exemplo, com as constantes `SHIFT`, `ALT` e `CONTROL`, ou as constantes das setas do teclado (`UP`, `DOWN`, `LEFT`, `RIGHT`), entre [algumas outras constantes listadas no final da página](#contantes-para-usar-com-keycode-e-o-correspondente-valor-numérico).

### Exemplo

![](assets/keyPressed_keyCode.gif)

<!-- editor-pyp5js -->
```python
def setup():
    size(400, 400)
    background(100, 100, 200)

def draw():
    if is_key_pressed and key_code == SHIFT:     # se a tecla SHIFT estiver pressonada
        stroke_weight(5)                     # # usa linha mais grossa
        stroke(255)  # com traço branco
    else:           # senão, quando tecla SHIFT não estiver pressonada
        stroke_weight(3)                     # usa linha m
        stroke(0)   # com traço preto

    if is_mouse_pressed:                        # Se o mouse estiver pressionado
         # Então desenha uma linha da posição anterior do mouse até a atual
         line(pmouse_x, pmouse_y, mouse_x, mouse_y)
                # termina o bloco (repare que no faz nada se o mouse estiver
                # solto)
```

### Quadro das variáveis de sistema

| tipo | nome | descrição |
| --- | --- | --- |
| int | mouse_button | indica qual botão do mouse foi clicado `LEFT`, `RIGHT` ou `CENTER`
| boolean | is_mouse_pressed | estado do mouse(`True` indica pressionado)
| int | mouse_x | informa a posição X do mouse na tela
| int | mouse_y | informa a posição Y do mouse na tela
| int | pmouse_x | informa a posição X anterior do mouse na tela
| int | pmouse_y | informa a posição Y anterior do mouse na tela
| string | key | caractere da última tecla 'comum' pressionada, ou a constante `CODED`
| int | key_code | código da última tecla 'codificada', como `SHIFT`, `UP` e etc.
| boolean | is_key_pressed | indica se alguma tecla está pressionada com(`True`)


## Funções acionadas por eventos

Quando definimos funções com certos nomes especiais 'encomendados', como `key_pressed()`, `mouse_pressed()`, ou alguma outra listada no quadro mais abaixo, elas serão executadas pelopela biblioteca py5 quando certos eventos do mouse ou do teclado acontecerem.

No jargão do desenvolvimento de interfaces isso é chamado de *tratamento de eventos*. Repare que não chamamos essas funções no nosso código, py5 chama por nós as funções nos 'eventos' apropriados, caso elas tenham sido definidas.

As funções precisam ser definidas fora do bloco de `draw()`. Ao contrário do Processing Java (e o antigo Modo Python), não é necessário definir uma função `draw()` para que exista um laço principal que redesenha a tela.

### Exemplo com as funções `mouse_dragged()` e `key_pressed()`

![](assets/mouseDragged.gif)

<!-- editor-pyp5js -->
```python
def setup():
    size(400, 400)
    background(100, 200, 100)

def draw():  # opcional
    pass

def mouse_dragged():
    stroke_weight(5)
    # Desenha uma linha da posição anterior do mouse até a atual
    line(pmouse_x, pmouse_y, mouse_x, mouse_y)

def key_pressed():         # Esta função executa uma vez quando uma tecla é pressionada
    if key == 'a':         # Se a tecla do caractere 'a' foi a última pressionada
        # Apague a tela com um fundo verde (só executa sob as condições acima)
        background(100, 200, 100)

    if key_code == DOWN:                         # Se a seta para baixo foi precionada
        # salve a imagem da tela de pintura em um arquivo PNG
        save_frame("imagem-####.png")
        # mostre no console o número do frame
        println("salvo o frame {}.".format(frameCount))
```
### O uso da função `key_typed()` 

A função `key_typed()`, quando definida, náo é acionada por teclas pelas teclas 'codificadas' (`CODED`), como as teclas modificadoras como `SHIFT`, `CONTROL`, `ALT`, ou as setas `UP`,`DOWN`,`LEFT`, `RIGHT`, mas tem a vantagem de permitir a captura, na variável `key`, de glifos que dependem de combinações de teclas, por exemplo, letras acentuadas como `àéîõü`, entre muitas outras.

### Quadro das funções acionadas por eventos

| nome da função | descrição do evento |
| --- | --- |
| mouse_released() | executada quando o botão do mouse é solto depois de pressionado
| mouse_wheel(event) | executada quando a rodinha do mouse é girada (deslocamento obtido com `event.get_count()`)
| mouse_clicked() | executada quando o mouse é clicado(já solto o botão)
| mouse_dragged() | executada quando o mouse é movido pressionado
| mouse_moved() | executada quando o mouse é movido
| mouse_pressed() | executada quando o botão do mouse é pressionado
| key_pressed() | executada quando uma tecla é pressionada
| key_released() | executada quando uma tecla é solta
| key_typed() | executada quando uma tecla alfa-numérica é digitada

## Algumas constantes úteis

### Contantes para usar com `key_code` (e o correspondente valor numérico)
```
UP      38
DOWN    40
LEFT    37
RIGHT   39
ALT     18
CONTROL 17
SHIFT   16
```

### Constantes para usar com `key` (e o *string*  equivalente)
```
BACKSPACE '\b'
TAB       '\t'
ENTER     '\n'
RETURN    '\r'
ESC       '\x1b'
DELETE    '\x7f'
```

## Assuntos relacionados

- [Escutando teclas simultâneas](teclas_simultaneas.md)
- [Um botão simples](botao_simples.md)
- [Arrastando círculos](arrastando_circulos.md)
- [Como ler a rodinha do mouse (*mouse wheel* ou *scroll wheel*)](rodinha_mouse.md)
