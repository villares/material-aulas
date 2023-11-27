# Uma janela de diálogo com um campo de texto como *input*

## Contexto histórico

Em quase todas as implementações de Python existe uma função chamada `input()` que 'pergunta' a quem estiver executando o programa um valor por meio da digitação no console, o texto digitado é devolvido então para o programa como *string*.

```python
while True:
    nome = input('Qual o seu nome?\n')
    if nome.strip():
        print(f'Olá, {nome}!\n')
    else:
        print('Olá, você deixou a resposta vazia, vou encerrar!')
        exit()  # Melhor exit_sketch() se estiver usando o py5
```

Resultados possíveis no console

```
Qual o seu nome?   
Alexandre
Olá, Alexandre!

Qual o seu nome?   
Olá, você deixou a resposta vazia, vou encerrar!

```

O Processing modo Python não tinha essa função, e a solução a seguir era um contorno possível. Com py5 agora é possível usar `input()` e interagir no console, mas ainda pode ser legal  disparar uma janela de diálogo, com um campo de texto. Especialmente se você estiver usando a tela toda (*fullscreen*) e não for muito prático ver o console.

## *showInputDialog* do Java swing

```python
def gui_input(question='', suggestion=''):
    from javax.swing import JOptionPane
    return JOptionPane.showInputDialog(None, question, suggestion)

```

Vejamos então um exemplo de uso, em que um clique do mouse dispara a janela para o input textual.

![](assets/input_janela.gif)

```python
texto = "clique na janela para mudar o texto"


def setup():
    size(400, 400)
    text_align(CENTER, CENTER)


def draw():
    background(0, 0, 200)
    text(texto, width / 2, height / 2)


def mouse_pressed():
    global texto
    resposta = gui_input('escreva um novo texto')
    if resposta:
        texto = resposta
    elif resposta == "":
        print("[resposta vazia]")
    else:
        print(resposta)  # se cancelada a janela exibe `None` no console


def gui_input(question='', suggestion=''):
    from javax.swing import JOptionPane
    return JOptionPane.showInputDialog(None, question, suggestion)
```
