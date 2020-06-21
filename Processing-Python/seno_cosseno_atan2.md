## Um pouco de ângulos, com seno, cosseno e arco tangente

### `sin()`, `cos()` e `atan2()`

As funções trigonométricas não são nenhum bicho de sete cabeças, `TWO_PI / 3` no máximo...

Para começar é preciso saber que quando elas pedem um ângulo como argumento. elas esperam que você informe esse ângulo em *radianos*, se você pensa em graus, é só usar `radians(angulo_em_graus)` para converter. Algumas como `atan2()` devolvem um ângulo em radianos, que pode ser convertido em graus com `degrees(angulo_em_radianos)`se você precisar.

### Seno e cosseno

Para além da origem dessas funções nas relações matemáticas dos ângulos de um triângulo e de um círculo de raio unitário, das coisas mais úteis que você pode entender facilmente é que essas funções devolvem valores entre **-1** e **1** de maneira cíclica, periódica.

Vamos visualizar aqui em dois exemplos o que isso significa.

#### `sin()` e `cos()` no espaço



#### `sin()` e `cos()` no tempo



### `atan2()`

#### Descobrindo o ângulo de um segmento de reta





#### Desenhando uma seta

```python
def setup():
    size(500, 500)
    
def draw():
    background(255)
    cx, cy = width / 2, height / 2
    seta(cx, cy, mouseX, mouseY)
    seta(100, 200, 300, 400)    

def seta(xa, ya, xb, yb):
    d = dist(xa, ya, xb, yb)
    a = atan2(ya - yb, xa - xb)
    line(xa, ya, xb, yb)
    pushMatrix() 
    translate(xb, yb)
    rotate(a)
    tc = d / 10
    line(0, 0, tc, tc)
    line(0, 0, tc, -tc)
    popMatrix()
```

