# eye

## How to creat an eye
    
``` python
 
 
def setup():
    size(500, 500) # tamanho da área de desenho
    olho(200, 200, 50, color(255, 0, 0))
    olho(100, 100, 200, color(0, 200, 0))
    
def draw():
    olho(mouseX, mouseY, 100, color(random(255),
                                    random(255),
                                    random(255)))
    
def olho(x, y, largura, cor):
    noStroke()
    fill(255)
    ellipse(x, y, largura, largura / 2)
    fill(cor)
    circle(x, y, largura / 2)
    fill(0)
    circle(x, y, largura / 6)
    
     ``` 


