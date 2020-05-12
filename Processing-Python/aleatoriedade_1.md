# Números 'aleatórios'

## Mais precisamente números pseudo-aleatórios

Computadores são máquinas determinísticas e não conseguem realmente 'sortear' um número, por isso usam algorítmos (receitas) que produzem sequências de números praticamente indistinguíveis, para a maioria dos usos[＊](#footnote1), de sequências verdadeiramente aleatórias. Por conta disso ganham este nome tecnicamente mais preciso de *pseudo-aleatórios* (falsos aleatórios). 

### Função `random()` no Processing

Podemos pedir ao Processing para nos entregar um número entre 0 e *n*  chamando `random(n)` ou entre *a* e *b* chamando `random(a, b)`. O número devolvido não é um número inteiro (*int*), mas podemos jogar fora a parte decimal fazendo a conversão com a função `int()`,  assim: `int(random(n))`.

Um exemplo tradicional, e divertido, é fazer um pincel de círculos com o tamanho e a cor 'sorteados'. Note que o `fill()` aceita números *float*  e os converte em *int* para nós. O quarto argumento de `fill(r, g, b, alpha)` indica uma cor translúcida.

![pincel com random](assets/pincel_aleatorio.gif)

```python
def setup():
    size(400, 400)
    noStroke()

def draw():
    r = random(256)
    g = random(256)
    b = random(256)
    tamanho = random(20, 60)
    fill(r, g, b, 100)  # cor 'sorteada' translúcida
    if mousePressed:
        ellipse(mouseX, mouseY, tamanho, tamanho)
        
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

- [Mais sobre pseudo-aleatoriedade, módulo `random` do Python e sementes](aleatoriedade_2.md)

---

> <a name="footnote1" href="#mais-precisamente-números-pseudo-aleatórios">＊</a> Para aplicações de segurança da informação, como por exemplo gerar certos tipos de chaves criptográficas, é possível incluir 'fontes externas de entropia', de forma a garantir resultados mais imprevisíveis.

---

Texto e imagens / text and images: CC BY-NC-SA 4.0; Código / code: GNU GPL v3.0 exceto onde explicitamente indicado por questões de compatibilidade.
