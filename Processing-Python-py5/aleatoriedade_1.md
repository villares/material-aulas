# Números "aleatórios"

## Mais precisamente números pseudoaleatórios

Computadores são máquinas determinísticas e não conseguem realmente 'sortear' um número, por isso usam algorítmos (receitas) que produzem sequências de números praticamente indistinguíveis, para a maioria dos usos[<sup>＊</sup>](#footnote1), de sequências verdadeiramente aleatórias. Por conta disso ganham este nome tecnicamente mais preciso de *pseudoaleatórios* (falsos aleatórios). 

### Função `random()` no py5

Podemos pedir ao py5 para nos entregar um número entre 0 e *n*  chamando `random(n)` ou entre *a* e *b* chamando `random(a, b)`. O número devolvido não é um número inteiro (*int*), mas podemos jogar fora a parte decimal fazendo a conversão com a função `int()`,  assim: `int(random(n))`.

Um exemplo tradicional, e divertido, é fazer um pincel de círculos com o tamanho e a cor 'sorteados'. Note que o `fill()` aceita números *float*  e os converte em *int* para nós. O quarto argumento de `fill(r, g, b, alpha)` indica uma cor translúcida.

![pincel com random](assets/pincel_aleatorio.gif)

<!-- editor-pyp5js -->
```python
def setup():
    size(400, 400)
    noStroke()

def draw():
    r = random(256)
    g = random(256)
    b = random(256)
    tamanho = random(20, 60)
    fill(r, g, b, 128)  # cor 'sorteada' 50% translúcida
    if is_mouse_pressed:
        ellipse(mouse_x, mouse_y, tamanho, tamanho)
        
def keyPressed():
    if key == ' ':  # tecle espaço para limpar a tela
        background(200)
    if key == 's':
        saveFrame('####.png')
```

#### Outros exemplos

```python
# Produz um valor entre 0 e 10 (10 não incluso)
sorteio = random(10) 

# Produz um valor entre 0 e 20 (não incluso) convertido em inteiro 
d20 = int(random(20)) # 0, 1, 2, 4, 5, 6, 7, 8, 9, 10, 11, … 19.

# Produz números entre -5 e 5 
faixa = random(-5, 5)  # exemplos: 3.91, -2.23, -1.2, 4.25 
```

## Assuntos relacionados

- [Mais sobre pseudoaleatoriedade, módulo `random` do Python e sementes](aleatoriedade_2.md)

---

> <a name="footnote1" href="#mais-precisamente-números-pseudoaleatórios">＊</a> Para aplicações de segurança da informação, como por exemplo gerar certos tipos de chaves criptográficas, é possível incluir 'fontes externas de entropia', de forma a garantir resultados mais imprevisíveis.