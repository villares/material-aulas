# Laço de repetição `while`
Este é um laço de repetição indeterminado, vejamos alguns exemplos:

## Sumário

- [A estrutura/sintaxe dos laços while](#a-estrutura/sintaxe-dos-laços-while)
- [While e else](#while-e-else)
- [Primeiro exemplo](#primeiro-exemplo)
- [Exemplo derivado do primeiro](#exemplo-derivado-do-primeiro)
- [Segundo exemplo com um conjunto](#segundo-exemplo-com-um-conjunto)
- [Terceiro exemplo](#terceiro-exemplo)


Um laço de repetição com `while` pode ser conveniente quando:

- Você precisa de contadores, ou uma sequênica de números, não-inteiros, e a forma `for i in range(inicio, parada, passo)` só funciona com inteiros. Isso pode ser resolvido implementando um [`frange()`](java_para_python.md#implementando-um-range-com-passos-não-inteiros) mas também pode ser feito com `while`

- O número de de iterações (voltas do laço) é indeterminado, isto é, não é conhecido com antecedência, você só descobre a hora de parar no meio do processo de repetições.

### A estrutura/sintaxe dos laços `while`

De forma geral os laços de repetição baseados no `while` tem a seguinte estrutura: 

```python 
while «condição»: #  enquanto a condição for verdadeira, execute:
    «corpo» 
```
No caso da estrutura if, a condição é avaliada como True (verdadeiro) ou False (falso) e o bloco de códigos é executado uma única vez. No caso do while, o bloco de códigos será executado enquanto a condição for verdadeira, resultando em um loop infinito. Para evitar essa repetição infinita é necessário modificar o código do corpo de modo que:

No código do corpo é necessário que seja modificada de alguma forma a condição avaliada pelo laço, para que ela se torne `False` (falsa) em determinado momento, ou então invocar `break`. Uma dessas duas coisas é necessária para evitar uma repetição infinita.

Vejamos uma descrição em abstrato de algumas dessas estratégias (que podem inclusive ser combinadas):

```python
«é criada uma variável-contador» 
while «condição que depende do contador»:
    «corpo do laço, deve incluir 
    atualização ou incremento do contador»     
```

```python
«é criada uma estrutura de dados» 
while «condição que envolve a estrutura de dados»:
    «corpo do laço, deve incluir
    modificação da estrutura de dados»      
```

```python
while True: # um laço inicialmente infinito
    «corpo do laço, deve incluir
    efeito que afeta a condição de saída»
    if «condição de saída»:
        break # saída do laço    
```
### While e else: 

```python
x = 0
while(x < 10):
    print(x) # quando a condição for verdadeira
    x += 1;
else: # quando a condição for falsa
    print ("False")

x = 0
while (x < 10):
    print (x) # quando a condição for verdadeira
    x+=1;
    break # saída do laço
else: # quando a condição for falsa
    print ("False") # não será executado
```

O break interrompe a execução de todo o ciclo e, nesse caso, o bloco do condicionante else, isto é, o bloco de códigos executado quando a condição não é verdadeira, não será executado.


#### Primeiro exemplo

No exemplo abaixo usaremos o laço `while` testando se o valor de um ângulo `ang` é menor que 360 graus (em radianos, a constante Pi vezes dois, ou, no Processing `TWO_PI`). 

O corpo do laço produz os vértices, que são pontos de um polígono em forma de estrela, a cada ciclo, e `ang` vai tendo o seu valor aumentado (`ang += passo`), até deixar de ser menor que `TWO_PI`, dessa forma encerrando o laço.

```python
def setup():
    size(400, 400)
    background(0)
    estrela(width / 2, height / 2, 190, 100, 10)

def estrela(x, y, raio_a, raio_b, num_pontas):
    passo = TWO_PI / num_pontas
    beginShape()
    ang = 0
    while ang < TWO_PI:  # enquanto o ângulo for menor que 2 * PI:
        sx = cos(ang) * raio_a
        sy = sin(ang) * raio_a
        vertex(x + sx, y + sy)
        sx = cos(ang + passo / 2.) * raio_b
        sy = sin(ang + passo / 2.) * raio_b
        vertex(x + sx, y + sy)
        ang += passo  # aumente o ângulo um passo
    endShape(CLOSE)
```

![estrela](assets/estrela.png)

#### Exemplo derivado do primeiro

```python
def setup ():
    size(600, 600)
    background(0)
    mandala(width/2, height/2, 100, 10)
    
def mandala( x, y, raio, num_petalas): 
    passo = TWO_PI/num_petalas
    ang = 0
        
    while ang < TWO_PI:
        sx = cos(ang) * raio
        sy = sin(ang) * raio
        fill(255, 255, 255 , 50)
        circle((x + sx), (y + sy), raio*2)
        
        ang = ang + passo
```
![estrela](assets/while_set.png)

#### Segundo exemplo com um conjunto

Imagine uma grade com 6400 posições, vocẽ quer sortear exatamente 3200 quadrados, mas não quer sobreposições.

```python
squares = set()  # conjunto, coleção que não preserva a ordem

def setup():
    size(400, 400)
    background(0, 0, 100)
    while len(squares) < 5000:
        x = int(random(width) / 5)
        y = int(random(height) / 5)
        if (x, y) not in squares:   # esta operação é rápida em conjuntos
             squares.add((x, y))    # note .add() e não .append()
             rect(x * 10, y * 10, 10, 10)
    print(len(squares))    
```

![estrela](assets/while_set.png)

#### Terceiro exemplo

Neste terceiro exemplo queremos acumular retângulos de larguras aleatórias até uma determinada largura total máxima. No corpo do `while()`
há um mecanismo que checa se a adição da largura da vez passa do limite, e ajusta apropriadamente a última largura.

```python
def setup():
    size(400, 400)
    background(0)
    colorMode(HSB)
    total = 0
    while total < 400:
        largura = int(random(1, 32))
        if total + largura > 400:
            largura = 400 - total
        fill(largura * 8, 200, 200)
        rect(total, 0, largura, height)
        total += largura
        print(total)
```

![estrela](assets/while_add.png)
