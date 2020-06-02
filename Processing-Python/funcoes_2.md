
## Parâmetros padrão e outras malandragens

Você já reparou que a função `rect()` aceita 4, 5 ou 8 argumentos? [Confira na referência](https://py.processing.org/reference/rect.html).

Você chama `rect(x, y, largura, altura)`, ou `rect(x, y, largura, altura, raio_cantos)` ou ainda `rect(x, y, largura, altura, raio_sup_esq, raio_sup_dir, raio_inf_dir, raio_inf_esq)`.

Outro caso é a função para pedir a cor de preenchimento, podemos chamar `fill(cinza)`, `fill(cinza, alpha_opacidade)`, `fill(r, g, b)`, `fill(r, g, b, alpha_opacidade)`.

Em Python é possível obter esse mesmo tipo de comportamento, em uma função que nós estamos definindo, de algumas maneiras. Vamos explorar aqui uma das mais simples.

Neste exemplo vamos estudar uma função que devolve cores geradas com random. A primeira versão era assim:

```python
def cor_sorteada():
    """Sorteia uma cor RGB"""
    r = random(256)
    g = random(256)
    b = random(256)
    return color(r, g, b)
```

Vamos imaginar que gostaríamos de especificar às vezes um valor de opacidade (*alpha *)
    
