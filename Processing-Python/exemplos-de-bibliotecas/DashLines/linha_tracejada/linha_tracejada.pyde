add_library('dashedlines')

def setup():
    size(300, 300)
    global dash
    dash = DashedLines(this)
    dash.pattern(10, 5)
    
def draw():
    background(255)
    dash.line(10, 10, mouseX, mouseY)
