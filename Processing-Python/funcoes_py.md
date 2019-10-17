# Definindo e chamando funções

### Sintaxe da definição/declaração
```python
def nome_da_função(nome_parâmetro, nome_outro_parâmetro): # esta função precisa de dois parâmetros/argumentos
     Bloco_de_código_que_a_função_executa
```

### Sintaxe do uso/invocação da função
```python
nome_da_função(valor_parâmetro, valor_outro_parâmetro) # esta função precisa de dois parâmetros/argumentos

```

### Exemplo da função `olho()`

```python
def setup():
    size(400, 400)
    background(0)
    olho(300, 100, random(50, 100)) # x, y, tamanho sorteado
    olho(100, 200, random(10, 150)) 
    olho(200, 300, random(10, 150))

def olho(x, y, tamanho) :
    """Olho precisa de 3 parâmetros"""
    noStroke()
    fill(255)
    ellipse(x, y, tamanho, tamanho/2)
    fill(0)
    circle(x, y, tamanho*.40)
```

### Funções que devolvem valores

A função `olho()` desenha um olho mas não devolve nenhum valor, na verdade ela devolve o valor especial `None`(uma espécie de "dada"). Mas é comum termos funções que devolvem um valor. Aqui alguns exemplos:

```python
def cor_sorteada():
    """Sorteia uma cor RGB"""
    r = random(256)
    g = random(256)
    b = random(256)
    cor = color(r, g, b)
    return cor # devolve a cor e retorna o fluxo de execução
```

Uso:


---
Este material é baseado no material do curso https://arteprog.space/programacao-criativa/

---
Texto e imagens / text and images: CC BY-NC-SA 4.0; Código / code: GNU GPL v3.0 exceto onde explicitamente indicado por questões de compatibilidade.
