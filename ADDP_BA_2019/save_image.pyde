add_library('pdf')
salvar_pdf = False

def setup():
    global seed
    seed = int(random(1000))
    print(seed)
    size(500, 500)
    
def draw():
    if salvar_pdf:
        beginRecord(PDF, "####.pdf")
    
    randomSeed(seed)
    background(240, 240, 200)
    translate(250, 300)
    galho(60)
    
    if salvar_pdf:
        endRecord()
        global salvar_pdf
        salvar_pdf = False
    
def galho(tamanho):
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
          
def keyPressed():
    global seed, salvar_pdf
    if keyCode == LEFT:
         seed = seed - 1
    if keyCode == RIGHT:
         seed = seed + 1
    if key == " ":
        seed = int(random(100000))
        print(seed)
    if key == "p":
        salvar_pdf = True
        print("Salvando PDF")
    if key == "s":
        saveFrame('imagem.png')
        print("Salvando PNG")
