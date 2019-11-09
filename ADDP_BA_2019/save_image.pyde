def setup(): #cria o setup do desenho, inclusive a área da imagem
    global seed
    seed = int(random(1000))
    print(seed)
    size(500, 500)
    
def draw(): #define o plano de fundo e o desenho
    randomSeed(seed)
    background(240, 240, 200)
    translate(250, 300)
    galho(60)
          
def galho(tamanho): #definição do galho
    ang = radians(mouseX)
    reducao = .8
    strokeWeight(tamanho / 10)
    line(0, 0, 0, -tamanho)
    if tamanho > 5:
        pushMatrix()
        translate(0, -tamanho)
        rotate(ang)
        # stroke(255, 0, 0)
        galho(tamanho * reducao - random(0, 2))
        # rotate(-ang * 2)
        rotate(-ang)
        rotate(-ang)
        # stroke(0, 0, 255)
        galho(tamanho * reducao - random(0, 2))
        popMatrix()
          
def keyPressed(): #o que acontece se você pressionar a tecla s, salva o PNG
    if keyCode == LEFT:
         seed = seed - 1
    if keyCode == RIGHT:
         seed = seed + 1
    if key == " ":
        seed = int(random(100000))
        print(seed)
    if key == "s":
        saveFrame('imagem.png')
        print("Salvando PNG")
