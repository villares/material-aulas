add_library('sound') # aviso de que vai usar o microfone

x, y = 400, 300

def setup():
    global loudness
    size(800, 600)
    # fullScreen()  # testar se 1 vai para segundo monitor
    background(0)
    # Burocracia para receber o som e analisar o volume
    source = AudioIn(this, 0)
    source.start()
    loudness = Amplitude(this)
    loudness.input(source)

                
def draw():
    fill(0, 10)
    noStroke()
    rect(0, 0, width, height)
    volume = loudness.analyze()
    tamanho = int(map(volume, 0, 0.5, 30, 350))
    stroke(255)
    circle(x, y, tamanho)
    
