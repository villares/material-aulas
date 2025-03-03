# Experimentos com retículas e imagens

### Criando uma grade de elementos

```python!
num_colunas = num_filas = 10

def setup():
    size(800, 800)
    background(255) # fundo branco
    no_stroke() # sem contorno nos elementos
    fill(0)     # preenchimento preto
    esp = width / num_colunas  # calcula o espaçamento
    for fila in range(num_filas):
        y = esp / 2 + esp * fila
        for coluna in range(num_colunas):
            x = esp / 2 + esp * coluna
            diametro = esp * 0.75
            circle(x, y, diametro)  
```
![image](assets/Sy82uILaT.png "image")


```python=


def setup():
    size(800, 800)
    img = load_image("https://upload.wikimedia.org/wikipedia/commons/d/dd/Adalovelace.jpg")
    #image(img, 0, 0, width, height)
    
    num_colunas = num_filas = 100
    esp = width / num_colunas
    background(0)  # fundo preto
    for m in range(num_filas):
        y = m * esp + esp / 2
        for n in range(num_colunas):  # 0, 1, 2, 3, 4, 5
            x = n * esp + esp / 2
            # remap(v, inicial_origem, final_origem, inicaial_algo, final_alvo)
            xi = int(remap(x, 0, width, 0, img.width))
            yi = int(remap(y, 0, height, 0, img.height))
            cor = img.get_pixels(xi, yi)
            #fill(cor)
            circle(x, y, esp)


```
---

Retícula PB - Lendo uma imagem na mesma proporção

```python!
num_colunas = num_filas = 80

def setup():
    size(800, 800)
    background(0) # fundo preto
    img = load_image("https://upload.wikimedia.org/wikipedia/commons/d/dd/Adalovelace.jpg")
    #image(img, 0, 0, 800, 800)
    no_stroke() # sem contorno nos elementos
    esp = width / num_colunas  # calcula o espaçamento
    for fila in range(num_filas):
        y = esp / 2 + esp * fila
        for coluna in range(num_colunas):
            x = esp / 2 + esp * coluna
            xi = remap(x, 0, width, 0, img.width)
            yi = remap(y, 0, height, 0, img.height)
            cor = img.get_pixels(int(xi), int(yi))
            #fill(cor)
            fill(255)
            diametro = brightness(cor) / 255 * esp
            circle(x, y, diametro)    
```


![ada](assets/rkIKi8I6a.png)

---
Exemplo retícula pontos pretos

```python=
num_colunas = num_filas = 100

def setup():
    size(800, 800)
    img = load_image("https://upload.wikimedia.org/wikipedia/commons/d/dd/Adalovelace.jpg")
    # img = load_image("Adalovelace.jpg")
    esp = width / num_colunas
    background(255)  # fundo branco
    for m in range(num_filas):
        y = m * esp + esp / 2
        for n in range(num_colunas):  # 0, 1, 2, 3, 4, 5
            x = n * esp + esp / 2
            # remap(v, inicial_origem, final_origem, inicaial_algo, final_alvo)
            xi = int(remap(x, 0, width, 0, img.width))
            yi = int(remap(y, 0, height, 0, img.height))
            cor = img.get_pixels(xi, yi)
            b = brightness(cor)
            fill(0)
            #fill(cor)
            d = remap(b, 0, 255, esp + 5, 0) 
            no_stroke()
            circle(x, y, d)
```
![image](assets/HkAZBFOaa.png)


---
cores saturadas 1

```python=


def setup():
    size(800, 800)
    img = load_image("Adalovelace.jpg")    
    num_colunas = num_filas = 100
    esp = width / num_colunas
    background(0)  # fundo
    for m in range(num_filas):
        y = m * esp + esp / 2
        for n in range(num_colunas):  # 0, 1, 2, 3, 4, 5
            x = n * esp + esp / 2
            # remap(v, inicial_origem, final_origem, inicaial_algo, final_alvo)
            xi = int(remap(x, 0, width, 0, img.width))
            yi = int(remap(y, 0, height, 0, img.height))
            cor = img.get_pixels(xi, yi)
            b = brightness(cor)
            h = hue(cor)
            color_mode(HSB) # Matiz, Sat, Bri
            nova_cor = color(h, 255, 255)
            fill(nova_cor)
            d = remap(b, 0, 255, 0, esp) 
            no_stroke()
            circle(x, y, d)
```
![image](assets/B1gT4t_pT.png)

---

Cores saturadas escuras com quadradinhos

```python=
num_colunas = num_filas = 100

def setup():
    size(800, 800)
    background(255)  # fundo branco
    img = load_image("https://upload.wikimedia.org/wikipedia/commons/d/dd/Adalovelace.jpg")
    # img = load_image("Adalovelace.jpg") # se tiver uma cópia local   
    esp = width / num_colunas
    for m in range(num_filas):
        y = m * esp + esp / 2
        for n in range(num_colunas):  # 0, 1, 2, 3, 4, 5
            x = n * esp + esp / 2
            # remap(v, inicial_origem, final_origem, inicaial_algo, final_alvo)
            xi = int(remap(x, 0, width, 0, img.width))
            yi = int(remap(y, 0, height, 0, img.height))
            cor = img.get_pixels(xi, yi)
            b = brightness(cor)
            h = hue(cor)
            color_mode(HSB) # Matiz, Sat, Bri
            nova_cor = color(h, 255, 128)
            fill(nova_cor)
            d = 0 + remap(b, 0, 255, esp, 0) 
            no_stroke()
            rect_mode(CENTER)
            #circle(X, Y, D)
            square(x, y, d)
    save("out.png")

```
![out](assets/H1Wb09vT6.png)




---

Sebastian Notes

```python=
# aula com Alexandre de 7 marco 2024        
def setup():
    size(800, 800)
    img = load_image("Adalovelace.jpg")
    #image(img, 0, 0, width, height) #just shows the image
    
    num_colunas = num_filas = 100
    esp = width / num_colunas
    background(255)  # fundo branco, fundo preto sera 0 in vez de 255
    for m in range(num_filas):
        y = m * esp + esp / 2
        for n in range(num_colunas):  # 0, 1, 2, 3, 4, 5
            x = n * esp + esp / 2
            # remap(v, inicial_origem, final_origem, inicaial_algo, final_alvo)
            xi = int(remap(x, 0, width, 0, img.width))
            yi = int(remap(y, 0, height, 0, img.height))
            cor = img.get_pixels(xi, yi)
            b = brightness(cor)
            h = hue(cor)
            color_mode(HSB) # matiz, sat, bri
            nova_cor = color(h, 255, 128)
            fill(nova_cor)
            d = 3 + remap(b, 0, 255, esp, 0) 
            no_stroke()
            circle(x, y, d)

    save("out.png")

```