# Animação inspirada na obra de Kazimir Malevich, “Composição suprematista: avião voando” (1914-1915). [Acervo Museu de Arte Moderna de Nova York]

# Interpretação > "Malevitando"

def setup():
    size(700, 700, P3D)

def draw():
    background (211, 209, 197)
    
    rotateX(radians(frameCount * .2))
    noStroke() #quadamarelo
    fill (218, 150, 23)
    rect(50, 50, 55, 55)
    
    rotateY(radians(frameCount * .05))
    noStroke() #retamarelo
    fill (218, 150, 23)
    rect(300, 600, 80, 60)
    
    rotateY(QUARTER_PI + radians(frameCount * 1)) 
    noStroke() #retamarelo
    fill (218, 150, 23)
    rect(620, 600, 40, 50)
    
    noStroke() #retamarelo
    fill (218, 150, 23)
    rect(620, 100, 20, 30)
    
    rotateY(QUARTER_PI + radians(frameCount * - 1)) 
    noStroke() #retamarelo
    fill (218, 150, 23)
    rect(100, 150, 200, 80)
    
    rotateX(radians(frameCount * 3))
    noStroke() #retamarelo
    fill (218, 150, 23)
    rect(500, 150, 70, 35)

    rotateX(radians(frameCount * -1))
    noStroke() #quadpreto
    fill (0)
    rect(400, 300, 55, 55)
    
    rotateY(radians(frameCount * .02))
    noStroke() #retpreto
    fill (0)
    rect(500, 400, 100, 200)
       
    noStroke() #retpreto
    fill (0)
    rect(100, 400, 90, 150)

    rotateX(radians(frameCount * .02))
    noStroke() #retazul
    fill (45, 58, 100)
    rect(300, 400, 30, 150)
   
    rotateX(radians(frameCount * -.1))
    noStroke() #retazul
    fill (45, 58, 100)
    rect(650, 400, 20, 80)
    
    noStroke() #retlaranja
    fill (191, 65, 53)
    rect(50, 300, 270, 20)
    
    rotateX(radians(frameCount * -1))
    noStroke() #retlaranja
    fill (191, 65, 53)
    rect(100, 250, 100, 10)
