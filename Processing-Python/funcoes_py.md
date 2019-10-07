# Definindo e chamando funções

### Sintaxe da definição/declaração
```python
def nome_da_função(parâmetro, outro_parâmetro): # esta função precisa de dois parâmetros/argumentos
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

---
Este material é baseado no material do curso https://arteprog.space/programacao-criativa/

---
Texto e imagens / text and images: CC BY-NC-SA 4.0; Código / code: GNU GPL v3.0 exceto onde explicitamente indicado por questões de compatibilidade.
