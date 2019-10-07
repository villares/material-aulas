# Movimento

## Círculo rebatendo nas bordas

```python
raio = 50  # tamanho do raio do círculo
vx = random(-4, 4) # sorteia velocidade horizontal inicial
vy = random(-4, 4) # sorteia velocidade vertical inicial

def setup():
    global px, py
    size(600, 400)
    # Definir posição inicial
    px, py = width / 2, height / 2

def draw():
    global px, py, vx, vy
    background(255)
    # Atualizar a posição do círculo
    px = px + vx
    py = py + vy
    # Testa se o círculo está fora da tela,
    # se estiver, inverte a velocidade (vira -velocidade).
    if px > width - raio or px < raio:
        vx = -vx
    if py > height - raio or py < raio:
        vy = -vy
    # Desenhar o círculo
    fill(0)  # preenchimento preto
    noStroke()  # sem traço de contorno
    circle(px, py, raio * 2)

```

![](https://github.com/arteprog/programacao-criativa/blob/master/assets/imagens/bounce.gif?raw=true)

---
Este material é baseado no material do curso https://arteprog.space/programacao-criativa/

---
Texto e imagens / text and images: CC BY-NC-SA 4.0; Código / code: GNU GPL v3.0 exceto onde explicitamente indicado por questões de compatibilidade.
