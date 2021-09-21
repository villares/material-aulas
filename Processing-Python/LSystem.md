# L-System - Sistema de Lindenmayer

L-Systems são as estruturas e procedimentos criados por Aristide Lindenmayer para estudar o crescimento de algas e plantas, por meio da manipulação de sequências de símbolos. As sequências são geradas por sucessivas iterações da aplicação de regras de substituição. A tradução computacional dessas estruturas foi discutida pela primeira vez em *Lecture Notes in Biomathematics* por Przemyslaw Prusinkiewcz e James Hanan.

Referências externas:
- [The Algorithmic Beauty of Plants](http://algorithmicbotany.org/papers/#abop) (+ diversos livros e artigos)
- https://www.cgjennings.ca/articles/l-systems/
- http://www.paulbourke.net/fractals/lsys/ 

### Um exemplo completo

```python
axioma = "X"
regras = {"X": "F+[[X]-X]-F[-FX]+X",
          "F": "FF"
          }          
tamanho = 10
angulo = 25
iteracoes = 4  # repeticoes (voltas na aplicação das regras)
xo, yo = 300, 500

def setup():
    global frase
    size(600, 600)
    frase = gerar_sistema(iteracoes, aximoa, regras)
    print(len(frase))

def draw():
    background(240, 240, 200)
    translate(xo, yo)
    desenha_sistema(frase)
            
def gerar_sistema(num, axioma, regras):
    """
    Produz um sistema-L a partir da  frase `axioma`,
    repetindo `num` iterações, as substituições descritas
    nas pelo dicionário `regras`
    """
    frase_inicial = axioma
    for i in range(num):
        frase_nova = ""
        for simbolo in frase_inicial:
            substituicao = regras.get(simbolo, simbolo)  
            frase_nova = frase_nova + substituicao
        frase_inicial = frase_nova
    return frase_nova
            
def desenha_sistema(simbolos):
    """
    Recebe uma frase e desenha de acordo com
    as "regras de desenho".
    """
    for simbolo in simbolos:
        if simbolo == "F":
            line(0, 0, 0, -tamanho)
            translate(0, -tamanho)
        if simbolo == "+":
            rotate(radians(angulo))
        if simbolo == "-":
            rotate(radians(-angulo))
        if simbolo == "[":
            pushMatrix()
        if simbolo == "]":
            popMatrix()

def keyPressed():
    global tamanho, angulo, iteracoes, frase
    if key == 'z':
        tamanho -= 1 # tamanho = tamanho - 1
    if key == 'x':
        tamanho += 1
    if key == 'a':
        angulo -= 1
    if key == 's':
        angulo += 1       
    if key == 'q':
        iteracoes -= 1
        frase = gerar_sistema(iteracoes, axioma, regras)
        print(len(frase))
    if key == 'w':
        iteracoes += 1   
        frase = gerar_sistema(iteracoes, axioma, regras)
        print(len(frase))
```
