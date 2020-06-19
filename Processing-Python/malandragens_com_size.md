## Manipulações avançadas da janela

### Tela cheia, janela com o tamanho calculado, e redimensionando a janela no meio do caminho



#### Variáveis no `size()`, usando `settings()`

Por questões de implementação do Processing, não é possível usar variáveis nos argumentos do size, quando este está, como de costume, no `setup()`. A solução é usar uma função chamada `settings()` que se for definida, o Processing chama, antes do `setup()`.

```python
def settings():
    img = loadImage('arquivo.jpg')
    size(img.width, img.height)
 
def draw():
    background(img) 
```

#### Mudando o tamnho da janela 

