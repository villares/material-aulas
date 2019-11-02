# Recursão

Allen Downey [no livro Pense em Python 2e](https://penseallen.github.io/PensePython2e/05-cond-recur.html#termo:recursividade) definie *recursão* ou *recursividade* como o processo de chamar uma função que está sendo atualmente executada.

A ideia central é de que uma função pode chamar outras funções, e no caso de uma função recursiva, uma função pode também chamar ela mesma!

Para que isso funcione (e não caia em uma cilada conhecida como "recursão infinita") é preciso que a função em certas condições chegue em uma opção de execução que não requer chamar ela mesma, é o chamado "caso base".

### Exemplo 01

![imagem1](https://github.com/arteprog/programacao-criativa/blob/master/assets/imagens/recursao/01recursao.jpg?raw=true)

```python
vdef setup():
    size(500, 500)
    desenharRetangulo(0, 0, 500, 10)

def desenharRetangulo(x, y, tam,level):
    rect(x, y, tam, tam)
    if level > 1:
        level = level - 1
        desenharRetangulo(x, y, tam / 2, level)
        desenharRetangulo(x + tam, y, tam / 2, level)
```

### Árvore recursiva

<iframe src="https://abav.lugaralgum.com/sketch-a-day/2019/sketch_191025pybr2019/index.html" style="width: 500px; height: 500px; border: 0px"></iframe>

```python
def setup():
    size(500, 500)
 
def draw():
    background(240, 240, 200)
    translate(250, 300)
    galho(60)
    
def galho(tamanho):
    ang = radians(mouseX)
    encurtar = .8
    line(0, 0, 0, -tamanho)  
    if tamanho > 5:
        translate(0, -tamanho)
        rotate(ang)
        galho(tamanho * encurtar)  
        rotate(2 * -ang)
        galho(tamanho * encurtar) 
        rotate(ang)
        translate(0, tamanho)
```

---
Este material é baseado no material do curso https://arteprog.space/programacao-criativa/

---
Texto e imagens / text and images: CC BY-NC-SA 4.0; Código / code: GNU GPL v3.0 exceto onde explicitamente indicado por questões de compatibilidade.

