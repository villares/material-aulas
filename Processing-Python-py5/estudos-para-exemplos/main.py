from outro_arquivo import f

def setup():
    size(400, 400)
    
def draw():
    background(200)
    f()
    
def key_pressed():
    if key == ' ':
        save_frame('###.png')